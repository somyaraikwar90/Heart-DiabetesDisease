import streamlit as st
import numpy as np
import pickle

# Load trained model (save using joblib or pickle)
model = pickle.load(open('best_model.pkl', 'rb'))

st.title("🩺 Diabetes Prediction App")
st.write("Enter your health parameters:")

# Input fields
pregnancies = st.number_input("Pregnancies", 0, 20)
glucose = st.number_input("Glucose", 0, 200)
bp = st.number_input("Blood Pressure", 0, 150)
skin = st.number_input("Skin Thickness", 0, 100)
insulin = st.number_input("Insulin", 0, 900)
bmi = st.number_input("BMI", 0.0, 70.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0)
age = st.number_input("Age", 1, 120)

# Prediction
if st.button("Predict"):
    data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    result = model.predict(data)
    st.success("🔴 Diabetic" if result[0] == 1 else "🟢 Not Diabetic")