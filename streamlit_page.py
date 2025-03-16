import streamlit as st
import numpy as np
import pickle

# Load models
def load_model(path):
    with open(path, "rb") as file:
        return pickle.load(file)

parkinson_model = load_model('parkinson_model.pkl')
liver_model = load_model('liver_model.pkl')
kidney_model = load_model('kidney_model.pkl')

# Function for prediction
def predict_disease(model, input_data):
    data = np.array(input_data).reshape(1, -1)
    return model.predict(data)[0]



# Streamlit 
st.title("Multiple Disease Prediction APP")
st.write("Enter the required parameters to predict Parkinson's disease.")

# Sidebar for disease selection
disease = st.sidebar.selectbox("Select Disease", ["Parkinson’s disease", "Liver disease", "Kidney disease"])

if disease == "Parkinson’s disease":
    st.subheader("Parkinson's Disease Prediction")
    fo = st.number_input("Fo (Hz)")
    fhi = st.number_input("Fhi (Hz)")
    flo = st.number_input("Flo (Hz)")
    jitter = st.number_input("Jitter(%)")
    jitter_abs = st.number_input("Jitter(Abs")
    RAP = st.number_input("RAP")
    PPQ = st.number_input("PPQ")
    jitter_DDP = st.number_input("Jitter(DDP)")
    shimmer = st.number_input("Shimmer")
    shimmer_db = st.number_input("Shimmer:dB")
    shimmer_APQ3 = st.number_input("Shimmer:APQ3")
    shimmer_APQ5 = st.number_input("Shimmer:APQ5")
    APQ = st.number_input("APQ")
    shimmer_DDA = st.number_input("Shimmer:DDA")
    NHR = st.number_input("NHR")
    HNR = st.number_input("HNR")
    RPDE = st.number_input("RPDE")
    DFA =  st.number_input("DFA")
    spread1 = st.number_input("spread1")
    spread2 = st.number_input("spread2")
    D2 = st.number_input("D2")
    PPE = st.number_input("PPE")



    input_data = [fo, fhi, flo,jitter,jitter_abs,RAP,PPQ,jitter_DDP,shimmer,shimmer_db,shimmer_APQ3,shimmer_APQ5,APQ,shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]

    
    if st.button("Predict"):
        result = predict_disease(parkinson_model, input_data)
        result_text = "Parkinson Disease is Present,Please Take Necessary Treatment" if result == 1 else "You are a healthy person"
        st.success(result_text)
        

elif disease == "Liver disease":
    st.subheader("Liver Disease Prediction")
    age = st.number_input("Age")
    total_bilirubin = st.number_input("Total Bilirubin")
    direct_bilirubin = st.number_input("Direct Bilirubin")
    alk_phos = st.number_input("Alkaline Phosphotase")
    alamine_aminotransferase = st.number_input("Alamine Aminotransferase")
    aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase")
    total_proteins= st.number_input("Total Proteins")
    albumin = st.number_input("Albumin")
    albumin_and_globulin_ratio = st.number_input("Albumin_and_globulin_ratio")
    gender_Male = st.number_input("Gender_Male")

    input_data = [age, total_bilirubin,direct_bilirubin,alk_phos,alamine_aminotransferase,aspartate_aminotransferase,total_proteins,albumin,albumin_and_globulin_ratio,gender_Male]

    
    if st.button("Predict",key="Liver_predict"):
        result = predict_disease(liver_model, input_data)
        result_text = "Liver is affected,Need Liver diagnosis" if result == 1 else "you have Healthy liver"
        st.success(result_text)
        

elif disease == "Kidney disease":

    st.subheader("Kidney Disease Prediction")
    
    age = st.number_input("Age")
    bp = st.number_input("Blood Pressure (mmHg)")
    sg = st.number_input("Specific Gravity")
    al = st.number_input("Albumin")
    su = st.number_input("Sugar")
    bgr = st.number_input("Blood Glucose Random")
    bu = st.number_input("Blood Urea")
    sc = st.number_input("Serum Creatinine")
    sod = st.number_input("Sodium")
    pot = st.number_input("Potassium")
    hemo = st.number_input("Hemoglobin")
    pcv = st.number_input("Packed Cell Volume")
    wc = st.number_input("White Blood Cell Count")
    rc = st.number_input("Red Blood Cell Count")

    # Selectboxes for Categorical Features
    rbc = st.selectbox("Red Blood Cells", ["normal", "abnormal"])
    pc = st.selectbox("Pus Cell", ["normal", "abnormal"])
    pcc = st.selectbox("Pus Cell Clumps", ["present", "notpresent"])
    ba = st.selectbox("Bacteria", ["present", "notpresent"])
    htn = st.selectbox("Hypertension", ["yes", "no"])
    dm = st.selectbox("Diabetes Mellitus", ["yes", "no"])
    cad = st.selectbox("Coronary Artery Disease", ["yes", "no"])
    appet = st.selectbox("Appetite", ["good", "poor"])
    pe = st.selectbox("Pedal Edema", ["yes", "no"])
    ane = st.selectbox("Anemia", ["yes", "no"])

    # Convert categorical values to numbers
    categorical_mapping = {
        "normal": 0, "abnormal": 1,
        "present": 1, "notpresent": 0,
        "yes": 1, "no": 0,
        "good": 1, "poor": 0
    }

    input_data = [
        age, bp, sg, al, su, 
        categorical_mapping[rbc], categorical_mapping[pc], 
        categorical_mapping[pcc], categorical_mapping[ba], 
        bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, 
        categorical_mapping[htn], categorical_mapping[dm], 
        categorical_mapping[cad], categorical_mapping[appet], 
        categorical_mapping[pe], categorical_mapping[ane]
    ]

    if st.button("Predict", key="kidney_predict"):
        result = predict_disease(kidney_model, input_data)
        result_text = "Kidney Disease Positive" if result == 1 else "Your Kidney seems to be healthy"
        st.success(result_text)
        

