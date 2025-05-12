import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model (choose your best model here)
# Example: Random Forest model saved with joblib
# joblib.dump(model, 'random_forest_model.pkl')  <-- Save your model after training
model = joblib.load(r"C:\Users\Lenovo\Desktop\gradient_boosting_m.pkl")

st.title("🚚 Delivery Time Prediction App")

st.header("Input Order Details:")

# Create input fields
Weather = st.selectbox('Weather', ['clear', 'cloudy', 'rainy', 'stormy', 'fog'])
Traffic = st.selectbox('Traffic', ['low', 'medium', 'high', 'jam'])
Vehicle=st.selectbox("Vehicle",['scooter','van'])
Area =st.selectbox("Area",["urban","other","semi_urban","metropollitan"])
distance_km = st.number_input('Distance between Store and Customer (km)', min_value=0.0, format="%.2f")
Order_Hour = st.slider('Order Hour (24h format)', 0, 23, 12)
Order_DayOfWeek = st.selectbox('Day of the Week', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
Time_of_Day=st.selectbox("Time_of_Day",['Morning','Afternoon','Evening','Night'])



# Encode inputs (you must match your training encodings!)
weather_mapping = {'clear': 0, 'cloudy': 1, 'fog': 2, 'rainy': 3, 'stormy': 4}
traffic_mapping = {'low': 0, 'medium': 1, 'high': 2, 'jam': 3}
Vehicle_mapping={"scooter":1,"van":2}
Area_mapping = {'urban': 0, 'other': 1, 'semi_urban': 2, 'metropollitan': 3}
day_mapping = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
Time_of_Day_mapping = {"Morning": 0, 'Afternoon': 1, 'Evening': 2, 'Night': 3}

# Prepare input DataFrame
input_data = pd.DataFrame({
    'Weather': [weather_mapping[Weather]],
    'Traffic': [traffic_mapping[Traffic]],
    "Vehicle":Vehicle_mapping[Vehicle],
    "Area":Area_mapping[Area],
    'distance_km': [distance_km],
    'Order_Hour': [Order_Hour],
    'Order_DayOfWeek': [day_mapping[Order_DayOfWeek]],
    'Time_of_Day':Time_of_Day_mapping[Time_of_Day]   
})

# Predict button
if st.button('Predict Delivery Time'):
    prediction = model.predict(input_data)
    st.success(f"Estimated Delivery Time: {prediction[0]:.2f} minutes")
