# Telecom Customer Churn Prediction

## Live Demo

Deployed Web Application :
https://customer-churn-prediction-2-f6dy.onrender.com/

---

## Project Overview

Customer Churn Prediction is a critical problem for Telecom Companies. Identifying Customers who are likely to leave enables Businesses to take Proactive Measures to Retain them.

This project develops a **Machine Learning based System that Predicts whether a Telecom Customer is likely to Churn** based on their Account Information, Billing Details and Service Usage.

The project includes a **Complete end-to-end Machine Learning Workflow**, starting from Data Preprocessing and Model Training to Deploying an Interactive Web Application.

A user-friendly dashboard was built using **Streamlit**, allowing users to input customer information and receive real-time churn predictions.

---

## Dataset

Dataset Used : **Telco Customer Churn Dataset**

The Dataset contains Customer-Level information including :

• Customer tenure
• Monthly charges
• Total charges
• Contract type
• Internet service type
• Payment method
• Additional services (Online Security, Backup, Device Protection, etc.)

Target Variable :

**Churn (Yes / No)**

---

## Machine Learning Pipeline

The project follows a Standard Machine Learning Workflow :

1. Data Cleaning and Handling Missing Values
2. Exploratory Data Analysis (EDA)
3. Feature Encoding and Transformation
4. Feature Scaling
5. Model Training
6. Model Evaluation
7. Model Deployment

---

## Models Used

The following Machine Learning Models were Evaluated :

• Logistic Regression
• Random Forest Classifier

The Best-Performing Model was Selected and Saved using **Joblib** for deployment in the web application.

---

## Model Evaluation Metrics

The Model Performance was Evaluated using :

• Accuracy
• Precision
• Recall
• F1 Score
• Confusion Matrix

---

## Web Application

An interactive web application was developed using **Streamlit** that allows users to:

• Enter Customer Details through an Intuitive Interface
• Predict Churn likelihood in Real-Time
• View Prediction Probabilities

The Application is Deployed Online using **Render** for Public Access.

---

## Tech Stack

Python
Pandas
NumPy
Scikit-learn
Streamlit
Joblib

Deployment Platform : Render

---

## Project Structure

Customer-Churn-Prediction

app.py — Streamlit application for Churn Prediction
requirements.txt — Project Dependencies
customer_churn_model.pkl — Trained Machine Learning Model
customer_churn_scaler.pkl — Feature Scaling Object
TelcoChurn.csv — Dataset used for Analysis
Customer_Churn_Analysis.ipynb — Notebook containing EDA and Model Training

---

## Future Improvements

• Implement advanced models such as Gradient Boosting or XGBoost
• Add more customer behavior features
• Build a full analytics dashboard with churn insights
• Deploy the application using Docker for scalability

---

## Author

Aasmeet Kaur
