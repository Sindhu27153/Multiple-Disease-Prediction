# Multiple-Disease-Prediction
The Multiple Disease Prediction System is an AI-powered web application that predicts the diseases using patients Lab Reports.
<h3>Overview</h3>

The Multiple Disease Prediction System is an AI-powered web application that predicts the likelihood of diseases like Parkinson’s, Kidney Disease, and Liver Disease using patient health parameters. The system leverages Machine Learning and Streamlit to provide fast and accurate disease risk assessments.

<h3>Features</h3>

📊 User Input: Collects patient health data such as blood pressure, glucose levels, and other medical parameters.

🧠 Machine Learning Models: Trained on medical datasets to predict disease risk.

📈 Visualization: Interactive charts and graphs for better insights.

🌍 Web-Based: Built using Streamlit for easy access and usability.

<h3>Dataset and Features</h3>

The model is trained using medical datasets that contain various health parameters:

Demographics: Age, Gender

Vital Signs: Blood Pressure, Heart Rate

Blood Tests: Glucose, Urea, Creatinine, Hemoglobin

Liver Function Tests: Bilirubin, Albumin, Enzymes

Kidney Function Tests: Sodium, Potassium, Specific Gravity

Other Factors: Hypertension, Diabetes, Smoking History

<h3>Installation</h3>

Prerequisites

Ensure you have Python installed on your system.

python --version

<h3>Clone the Repository</h3>

git clone https://github.com/sindhu27153/multiple-disease-prediction.git
cd multiple-disease-prediction

<h3>Install Dependencies</h3>

pip install -r requirements.txt

Run the Streamlit App

streamlit run app.py

<h3>Model Training</h3>

The machine learning models are trained using scikit-learn and stored as pickle (.pkl) files.
To retrain the models:

python train_model.py

<h3>Deployment</h3>

The application can be deployed on platforms like Heroku, AWS, or Streamlit Sharing.

<h3>Future Enhancements</h3>

🔍 Expand predictions to more diseases.

📱 Mobile app integration.

📡 API-based access for hospitals and telehealth platforms.

<h3>Contributors</h3>

👨‍💻 Sindhu27153 – GitHub

<h3>Acknowledgments</h3>

Special thanks to the medical research community for open-source datasets.

🚀 Ready to Predict? Run the app and get started!
