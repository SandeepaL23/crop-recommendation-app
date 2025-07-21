import streamlit as st
import numpy as np
import joblib

# Custom CSS for styling
st.markdown("""
    <style>
    .main-title {
        font-size: 40px;
        color: #228B22;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 18px;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton>button {
        background-color: #228B22;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        height: 3em;
        width: 100%;
    }
    .stSuccess {
        font-size: 22px;
        color: #228B22;
        text-align: center;
    }
    </style>
    <div class="main-title">🌾 Crop Recommendation System</div>
    <div class="subtitle">Enter soil and environmental details to get the best crop suggestion.</div>
""", unsafe_allow_html=True)

# Load the trained model
model = joblib.load('crop_recommendation_model.pkl')

# Input fields in columns for better layout
col1, col2, col3 = st.columns(3)
with col1:
    N = st.slider("Nitrogen", min_value=0.0, max_value=140.0, value=50.0)
    K = st.slider("Potassium", min_value=0.0, max_value=200.0, value=50.0)
    ph = st.slider("pH", min_value=0.0, max_value=14.0, value=6.5)
with col2:
    P = st.slider("Phosphorous", min_value=0.0, max_value=140.0, value=50.0)
    temperature = st.slider("Temperature (°C)", min_value=0.0, max_value=60.0, value=25.0)
with col3:
    humidity = st.slider("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
    rainfall = st.slider("Rainfall (mm)", min_value=0.0, max_value=300.0, value=100.0)

st.markdown("---")

# Predict button
if st.button("Predict Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    st.success(f"🌱 Recommended Crop: **{prediction[0].capitalize()}**")