# Classification of Schizophrenia using EEG Signals

## Overview
This project focuses on classifying EEG signals to detect schizophrenia using various machine learning models. The dataset comprises EEG data from 84 individuals (39 healthy, 45 schizophrenic), recorded for 1 minute across 16 channels. The goal is to accurately classify the data into healthy or schizophrenic categories.

## Project Workflow
1. **Data Preprocessing:**
   - The EEG data was provided in `.eea` format, which was reorganized into CSV files.
   - Two methodologies were tested to compile a final dataset, resulting in a dataset of 7680x16x82 rows (with data from two individuals removed for testing).
   - The 1st method code is available in the `create_final_database_method1.py` file. But it takes a LOT of time to run even with multithreading in 16 threads.
   - The 2nd method code is available in the `create_combined_eeg_data.py` file.

2. **Model Training and Testing:**
   - Several machine learning models were implemented and tested:
     - Logistic Regression
     - Convolutional Neural Network (CNN)
     - Random Forest
     - All the jupyter notebooks are available

3. **Model Evaluation:**
   - Models were evaluated using precision, recall, and F1 score metrics. The best F1 score obtained was 0.75 for Random Forest.

4. **Web Deployment:**
   - The trained models were deployed on a web application using Flask for the backend, allowing users to interact with the models.
   - This code is provided in the `EEG ML Model` folder.

## Results
- Logistic Regression and CNN models predicted schizophrenia with a high probability but exhibited signs of overfitting.
- Random Forest provided more balanced predictions with an F1 score of 0.75.
  
## Conclusion
- The accuracy shown on the website for the classifiers is very high due to use of same data set for testing, some level of overfitting is observed. The provided dataset was very small, so it was not possible to use a different dataset for testing.
- While testing samples, lot of error is observed, but if see the values of Recall, F1 Score and Precision, it is 0.75 which is not bad. So, to explain it, there are two possible reasons:
    - This happened with only a few files
    - The use of dataset created using the first methodology could have a significant impact on the metrics of the model.

## Authors
- Aditya Mehta
- [Ayush Singh](https://github.com/Ayush181005)
- [Nisarg Adhwaryu](https://github.com/Nisarg-Adhvaryu)