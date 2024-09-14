from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import os

app = Flask(__name__)

# Load the Random Forest model
rf_model = pickle.load(open('C:\\Users\\nisar\\one drive\\Desktop\\IEEE\\EEG ML Model\\model.pkl', 'rb'))

# Serve the main HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Handle the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Read the uploaded CSV file
        eeg_data = pd.read_csv(file)
        
        # Assuming your model expects the same feature columns as training
        X = eeg_data.drop(['label', 'file_name'], axis=1)

        # Make prediction
        prediction = rf_model.predict(X)

        # Return the first prediction
        result = int(prediction[0])

        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
