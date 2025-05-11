# crop_app.py

import streamlit as st
import pickle
import numpy as np
import pickle


# Load model and label encoder
with open("random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

st.title("🌾 Crop Recommendation System")

st.write("Enter the soil and weather parameters to get a suitable crop suggestion:")

# Input fields
N = st.number_input("Nitrogen (N)", min_value=0, max_value=140)
P = st.number_input("Phosphorus (P)", min_value=0, max_value=140)
K = st.number_input("Potassium (K)", min_value=0, max_value=200)
temperature = st.number_input("Temperature (°C)", format="%.2f")
humidity = st.number_input("Humidity (%)", format="%.2f")
ph = st.number_input("pH value", format="%.2f")
rainfall = st.number_input("Rainfall (mm)", format="%.2f")

if st.button("Suggest Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    predicted_crop = le[prediction[0]]
    st.success(f"✅ Recommended Crop: **{predicted_crop}**")
