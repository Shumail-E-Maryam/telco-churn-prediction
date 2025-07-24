# Telco Customer Churn Prediction 🧠📉

An end-to-end machine learning pipeline to predict telecom customer churn using `scikit-learn` and `Streamlit`. This project was completed as **Task 1** of my internship at **DevelopersHubCo**.

## 📌 Project Overview

Churn refers to customers leaving a service or company — in the telecom industry, predicting churn helps retain customers and reduce revenue loss. This project leverages the **Telco Customer Churn Dataset** to build a full ML workflow from **data preprocessing** to **model training**, and finally to **deployment using Streamlit**.

## 🛠️ Features

- 📊 Cleaned and preprocessed raw data using `Pipeline` and `ColumnTransformer`
- 🤖 Trained Logistic Regression and Random Forest models
- 🔍 Performed hyperparameter tuning using `GridSearchCV`
- 🧪 Evaluated models using accuracy, precision, recall
- 💾 Exported the trained pipeline using `joblib`
- 🌐 Built a user-friendly **Streamlit app** for live churn predictions

## 🔍 Dataset

- Dataset: [Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn)
- Features include:
  - Demographics (gender, senior citizen, etc.)
  - Services used (internet, phone, etc.)
  - Tenure, monthly charges, contract type
  - Target: `Churn` (Yes/No)

## 🧰 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn (Pipeline, GridSearchCV)
- Streamlit
- Joblib

