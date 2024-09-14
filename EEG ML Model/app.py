from flask import Flask, request, jsonify, render_template
from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_fscore_support
import pandas as pd
import pickle
import json

app = Flask(__name__)

# Load the Random Forest model
rf_model = pickle.load(open(r'EEG ML Model/RF_model.pkl', 'rb'))
lr_model = pickle.load(open(r'EEG ML Model/LR_model.pkl', 'rb'))
cnn_model = pickle.load(open(r'EEG ML Model/CNN_model.pkl', 'rb'))

# Serve the main HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Handle the prediction route
@app.route('/check-model', methods=['POST'])
def checkModel():
    file = request.files['file'] # Uploaded file (.csv)
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    try:
        # Read the uploaded CSV file
        eeg_data = pd.read_csv(file)
        
        # Assuming your model expects the same feature columns as training
        X = eeg_data.drop(['label', 'file_name'], axis=1)
        Y = eeg_data['label']

        using_cnn = False
        if request.form['submit_btn'] == 'LR':
            prediction = lr_model.predict(X)
        elif request.form['submit_btn'] == 'RF':
            prediction = rf_model.predict(X)
        elif request.form['submit_btn'] == 'CNN':
            prediction = cnn_model.predict(X)

            using_cnn = True

            accuracy = accuracy_score(Y, prediction.round())
            conf_matrix = confusion_matrix(Y, prediction.round())
            # class_report = classification_report(Y, prediction)
            metrics = precision_recall_fscore_support(Y, prediction.round(), average='macro')

        if not using_cnn:
            accuracy = accuracy_score(Y, prediction)
            conf_matrix = confusion_matrix(Y, prediction)
            # class_report = classification_report(Y, prediction)
            metrics = precision_recall_fscore_support(Y, prediction, average='macro')
        

        precision = metrics[0]
        recall = metrics[1]
        f1 = metrics[2]

        return render_template('result.html', accuracy=accuracy, confusion_matrix=conf_matrix, precision=precision, recall=recall, f1_score=f1)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file'] # Uploaded file (.csv)

    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    try:
        # Read the uploaded CSV file
        eeg_data = pd.read_csv(file)

        # Assuming your model expects the same feature columns as training
        if request.form['submit_btn'] == 'RF':
            prediction = rf_model.predict(eeg_data)
        elif request.form['submit_btn'] == 'LR':
            prediction = lr_model.predict(eeg_data)
        elif request.form['submit_btn'] == 'CNN':
            prediction = cnn_model.predict(eeg_data)

        temp = 0
        for i in prediction.tolist():
            if i == 0:
                temp += 1

        chanceHealthy = temp/len(prediction)
        chanceUnhealthy = (len(prediction)-temp)/len(prediction)
        if chanceHealthy >= 0.7:
            return jsonify({'result': 'Healthy', 'chance': str(round(chanceHealthy*100, 2))+'%'})
        else:
            return jsonify({'result': 'Schizophrenic', 'chance': str(round(chanceUnhealthy*100, 2))+'%'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
