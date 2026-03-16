import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("customer_churn_model.pkl")
scaler = joblib.load("customer_churn_scaler.pkl")

st.title("Customer Churn Prediction")

st.write("Enter Customer Details to Predict Churn.")

# Sidebar inputs
st.sidebar.header("Customer Information")

tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)

monthly_charges = st.sidebar.slider(
    "Monthly Charges",
    0.0,
    150.0,
    70.0
)

total_charges = st.sidebar.slider(
    "Total Charges",
    0.0,
    10000.0,
    2000.0
)

contract = st.sidebar.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

internet_service = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

payment_method = st.sidebar.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer", "Credit card"]
)

# Encoding inputs
contract_map = {
    "Month-to-month": 0,
    "One year": 1,
    "Two year": 2
}

internet_map = {
    "DSL": 0,
    "Fiber optic": 1,
    "No": 2
}

payment_map = {
    "Electronic check": 0,
    "Mailed check": 1,
    "Bank transfer": 2,
    "Credit card": 3
}

# Create dataframe
input_data = pd.DataFrame({
    "tenure": [tenure],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges],
    "Contract": [contract_map[contract]],
    "InternetService": [internet_map[internet_service]],
    "PaymentMethod": [payment_map[payment_method]]
})

# Match features with training data
input_data = input_data.reindex(columns=scaler.feature_names_in_, fill_value=0)

# Scale data
input_scaled = scaler.transform(input_data)

# Prediction button
if st.button("Predict Churn"):

    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)

    if prediction[0] == 1:
        st.error("Customer is likely to Churn")
    else:
        st.success("Customer will Stay")

    st.subheader("Prediction Probability")

    st.write(f"Stay Probability: {probability[0][0]:.2f}")
    st.write(f"Churn Probability: {probability[0][1]:.2f}")
