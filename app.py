import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("food_demand_model.pkl")

st.title("Food Demand Forecasting System")

st.write("Predict Food Order Demand")

# Inputs
week = st.number_input("Week", min_value=1)

checkout_price = st.number_input(
    "Checkout Price"
)

base_price = st.number_input(
    "Base Price"
)

emailer_for_promotion = st.selectbox(
    "Email Promotion",
    [0, 1]
)

homepage_featured = st.selectbox(
    "Homepage Featured",
    [0, 1]
)

# Prediction Button
if st.button("Predict Orders"):

    features = np.array([
        [
            week,
            checkout_price,
            base_price,
            emailer_for_promotion,
            homepage_featured
        ]
    ])

    prediction = model.predict(features)

    st.success(
        f"Predicted Food Orders: {int(prediction[0])}"
    )