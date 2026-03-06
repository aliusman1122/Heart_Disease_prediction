from pathlib import Path
import streamlit as st
import numpy as np
import joblib

# Get project root folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Load model and scaler using absolute path
model = joblib.load(BASE_DIR / "model" / "svm_model.pkl")
scaler = joblib.load(BASE_DIR / "model" / "scaler.pkl")

st.title("❤️ Heart Disease Prediction System")

st.write("Enter patient medical information")

age = st.number_input("Age", 1, 120)
sex = st.selectbox("Sex", [0, 1])
cp = st.number_input("Chest Pain Type (0-3)", 0, 3)
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol")
fbs = st.selectbox("Fasting Blood Sugar >120", [0, 1])
restecg = st.number_input("Rest ECG (0-2)", 0, 2)
thalach = st.number_input("Max Heart Rate")
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("Oldpeak")
slope = st.number_input("Slope (0-2)", 0, 2)
ca = st.number_input("Number of Major Vessels (0-4)", 0, 4)
thal = st.number_input("Thal (0-3)", 0, 3)

if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak,
                            slope, ca, thal]])
    
    input_data = scaler.transform(input_data)
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("⚠️ Patient has Heart Disease")
    else:
        st.success("✅ Patient does NOT have Heart Disease")