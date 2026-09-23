import streamlit as st
import pandas as pd
import pickle


# -----------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------

st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)


# -----------------------------------------
# LOAD TRAINED MODEL
# -----------------------------------------

try:

    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

except FileNotFoundError:

    st.error(
        "model.pkl not found. "
        "Please upload model.pkl to the GitHub repository."
    )

    st.stop()


# -----------------------------------------
# TITLE
# -----------------------------------------

st.title("🚗 Car Price Prediction App")

st.write(
    "Enter the car details below to predict "
    "the estimated selling price."
)


# -----------------------------------------
# USER INPUTS
# -----------------------------------------

st.subheader("Enter Car Details")


year = st.number_input(
    "Year",
    min_value=1990,
    max_value=2026,
    value=2018,
    step=1
)


present_price = st.number_input(
    "Present Price (Lakhs)",
    min_value=0.0,
    value=5.0,
    step=0.1
)


kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=30000,
    step=1000
)


fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG"]
)


seller_type = st.selectbox(
    "Seller Type",
    ["Dealer", "Individual"]
)


transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)


owner = st.number_input(
    "Previous Owners",
    min_value=0,
    max_value=3,
    value=0,
    step=1
)


# -----------------------------------------
# ENCODING
# -----------------------------------------

fuel_value = {
    "Petrol": 0,
    "Diesel": 1,
    "CNG": 2
}[fuel_type]


seller_value = {
    "Dealer": 0,
    "Individual": 1
}[seller_type]


transmission_value = {
    "Manual": 0,
    "Automatic": 1
}[transmission]


# -----------------------------------------
# PREDICTION
# -----------------------------------------

if st.button("🔮 Predict Selling Price"):

    input_data = pd.DataFrame({
        "Year": [year],
        "Present_Price": [present_price],
        "Kms_Driven": [kms_driven],
        "Fuel_Type": [fuel_value],
        "Seller_Type": [seller_value],
        "Transmission": [transmission_value],
        "Owner": [owner]
    })

    prediction = model.predict(input_data)

    predicted_price = prediction[0]

    st.success(
        f"🚗 Predicted Selling Price: "
        f"₹ {predicted_price:.2f} Lakhs"
    )
