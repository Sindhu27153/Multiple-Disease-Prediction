# Multiple-Disease-Prediction
The Multiple Disease Prediction System is an AI-powered web application that predicts the diseases using patients Lab Reports.
Overview

The Multiple Disease Prediction System is an AI-powered web application that predicts the likelihood of diseases like Parkinson’s, Kidney Disease, and Liver Disease using patient health parameters. The system leverages Machine Learning and Streamlit to provide fast and accurate disease risk assessments.

Features

📊 User Input: Collects patient health data such as blood pressure, glucose levels, and other medical parameters.

🧠 Machine Learning Models: Trained on medical datasets to predict disease risk.

📈 Visualization: Interactive charts and graphs for better insights.

🌍 Web-Based: Built using Streamlit for easy access and usability.

Dataset and Features

The model is trained using medical datasets that contain various health parameters:

Demographics: Age, Gender

Vital Signs: Blood Pressure, Heart Rate

Blood Tests: Glucose, Urea, Creatinine, Hemoglobin

Liver Function Tests: Bilirubin, Albumin, Enzymes

Kidney Function Tests: Sodium, Potassium, Specific Gravity

Other Factors: Hypertension, Diabetes, Smoking History

Installation

Prerequisites

Ensure you have Python installed on your system.

python --version

Clone the Repository

git clone https://github.com/sindhu27153/multiple-disease-prediction.git
cd multiple-disease-prediction

Install Dependencies

pip install -r requirements.txt

Run the Streamlit App

streamlit run app.py

Model Training

The machine learning models are trained using scikit-learn and stored as pickle (.pkl) files.
To retrain the models:

python train_model.py

Deployment

The application can be deployed on platforms like Heroku, AWS, or Streamlit Sharing.

Future Enhancements

🔍 Expand predictions to more diseases.

📱 Mobile app integration.

📡 API-based access for hospitals and telehealth platforms.

Contributors

👨‍💻 Sindhu27153 – GitHub

Acknowledgments

Special thanks to the medical research community for open-source datasets.

🚀 Ready to Predict? Run the app and get started!
