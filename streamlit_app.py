import streamlit as st
import pandas as pd
from joblib import load

# Load the trained pipeline
model = load('../models/telco_churn_pipeline.joblib')

st.title("📞 Telco Customer Churn Predictor")

st.markdown("Fill in the customer information:")

gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Has Partner?", ["Yes", "No"])
dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, step=1.0)
total_charges = st.number_input("Total Charges", min_value=0.0, step=10.0)

# Create input row
input_df = pd.DataFrame([{
    'gender': gender,
    'SeniorCitizen': senior,
    'Partner': partner,
    'Dependents': dependents,
    'tenure': tenure,
    'PhoneService': phone_service,
    'InternetService': internet_service,
    'Contract': contract,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges,
    'customerID': 'dummy123'
}])

if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    label = "Churn ❌" if prediction == 1 else "No Churn ✅"
    st.success(f"Prediction: **{label}**")

