# 📊 Customer Churn Prediction using Machine Learning

## 🔍 Project Overview
Customer churn prediction is a crucial task for subscription-based businesses.
This project aims to predict whether a customer is likely to leave (churn) based on
their demographic information, account details, and service usage patterns.

The project follows a complete **end-to-end machine learning workflow**, from data
analysis to model deployment using Streamlit.

---

## 🎯 Objectives
- Analyze customer behavior data
- Perform exploratory data analysis (EDA)
- Preprocess and prepare data for modeling
- Train and evaluate multiple machine learning models
- Select the best-performing model
- Deploy the model using a Streamlit web application

---

## 🗂️ Dataset
- Dataset: **WA_Fn-UseC_-Telco-Customer-Churn.csv**
- Each row represents a customer
- Target variable: **Churn** (Yes / No)

Key features include:
- Demographics (gender, senior citizen)
- Account information (tenure, contract type, payment method)
- Service usage (internet service, online security, tech support)
- Billing details (monthly charges, total charges)

---

## 🛠️ Project Structure
customer-churn-prediction/
│
├── app/
│ └── app.py # Streamlit application
├── data/
│ └── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── models/
│ └── churn_model.pkl # Saved Random Forest model
├── notebooks/
│ └── churn_eda.ipynb # Complete ML workflow notebook
├── requirements.txt
└── README.md

---

## 📈 Steps Performed

### Step 1: Data Loading & Dataset Description
- Loaded dataset using pandas
- Reviewed structure, columns, and target variable

### Step 2: Exploratory Data Analysis (EDA)
- Analyzed churn distribution
- Visualized relationships between features and churn
- Checked correlations and trends

### Step 3: Data Preprocessing
- Handled missing values
- Encoded categorical variables
- Converted target variable to numeric format

### Step 4: Feature Engineering & Train-Test Split
- Selected relevant features
- Split data into training and testing sets

### Step 5: Model Training
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

### Step 6: Model Comparison
- Compared models using accuracy and classification metrics
- Analyzed feature importance using Random Forest

### Step 7: Best Model Selection & Saving
- Random Forest selected as the best model
- Model saved using `joblib` for deployment

---

## 🚀 Streamlit Web Application
A Streamlit app was developed to allow users to input customer details and receive
real-time churn predictions.

### Run the app locally:
```bash
streamlit run app/app.py
