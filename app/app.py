import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("../models/churn_model.pkl")

st.title("📞 Customer Churn Prediction App")
st.write("Enter customer details to predict whether they are likely to churn.")

# Input fields for key features
gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", ["No", "Yes"])
Partner = st.selectbox("Has Partner", ["No", "Yes"])
Dependents = st.selectbox("Has Dependents", ["No", "Yes"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
PhoneService = st.selectbox("Phone Service", ["No", "Yes"])
Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["No", "Yes"])
PaymentMethod = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, step=1.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0, step=10.0)

# Prepare input for prediction
input_data = pd.DataFrame({
    'gender': [gender],
    'SeniorCitizen': [1 if SeniorCitizen == "Yes" else 0],
    'Partner': [1 if Partner == "Yes" else 0],
    'Dependents': [1 if Dependents == "Yes" else 0],
    'tenure': [tenure],
    'PhoneService': [1 if PhoneService == "Yes" else 0],
    'Contract': [Contract],
    'PaperlessBilling': [1 if PaperlessBilling == "Yes" else 0],
    'PaymentMethod': [PaymentMethod],
    'MonthlyCharges': [MonthlyCharges],
    'TotalCharges': [TotalCharges]
})

# Encode categorical columns like before
input_data = pd.get_dummies(input_data)
for col in model.feature_names_in_:
    if col not in input_data.columns:
        input_data[col] = 0
input_data = input_data[model.feature_names_in_]

# Predict churn
if st.button("🔍 Predict Churn"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ This customer is likely to churn!")
    else:
        st.success("✅ This customer is not likely to churn.")
