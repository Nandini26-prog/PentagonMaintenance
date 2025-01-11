import streamlit as st
import pandas as pd
import joblib
from pymongo import MongoClient
from datetime import datetime
import time

# Load the machine learning model
rfc = joblib.load('best_model.joblib')

# Connect to MongoDB
client = MongoClient("mongodb+srv://nandininj26:C9eCrZZQ5G4l9ISm@cluster0.aadz9.mongodb.net/")
db = client["PredictiveMaintenance"]
collection = db["sensor_readings"]

# Streamlit App Title
st.title("Machine Predictive Maintenance")

# Add the new buttons: View Details and Home
col1, col2 = st.columns(2)

with col1:
    if st.button('View Details'):
        # Placeholder for action when View Details is clicked
        st.write("Here you can display the details of your model or any additional info.")
        
with col2:
    if st.button('Home'):
        # Placeholder for action when Home is clicked
        st.write("This will redirect to the home page or main menu.")

# Collecting user inputs for type
selected_type = st.selectbox('Select a Type', ['Low', 'Medium', 'High'])
type_mapping = {'Low': 0, 'Medium': 1, 'High': 2}
selected_type = type_mapping[selected_type]

# Prediction logic
st.write("Monitoring sensor readings and predicting failures in real-time...")

# Start monitoring and predicting
if st.button('Start Monitoring'):
    try:
        # Fetch all sensor readings from MongoDB
        all_readings = collection.find().sort("timestamp", 1)

        for reading in all_readings:
            # Extract the necessary fields
            air_temperature = reading.get("air_temperature")
            process_temperature = reading.get("process_temperature")
            rotational_speed = reading.get("rotational_speed")
            torque = reading.get("torque")
            tool_wear = reading.get("tool_wear")

            # Ensure all necessary fields are present
            if None in [air_temperature, process_temperature, rotational_speed, torque, tool_wear]:
                st.warning(f"Incomplete data: {reading}")
                continue

            # Create input DataFrame for prediction
            input_data = pd.DataFrame([[selected_type, air_temperature, process_temperature,
                                        rotational_speed, torque, tool_wear]],
                                      columns=['Type', 'Air temperature [K]', 'Process temperature [K]',
                                               'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]'])

            # Predict failure
            prediction = rfc.predict(input_data)
            if prediction[0] == 1:
                failure_pred = '**❌ FAILURE DETECTED!**'
            else:
                failure_pred = '**✅ No Failure**'

            # Compact display of sensor readings
            st.markdown(f"### Sensor Readings at {datetime.now()}:")
            st.write(f"**Air Temperature [K]:** {air_temperature}, **Process Temperature [K]:** {process_temperature}")
            st.write(f"**Rotational Speed [rpm]:** {rotational_speed}, **Torque [Nm]:** {torque}")
            st.write(f"**Tool Wear [min]:** {tool_wear}")
            st.markdown(f"#### Prediction: {failure_pred}")

            # If failure is detected, display an alert and stop monitoring
            if prediction[0] == 1:
                st.error("⚠️ **ALERT: Machine Failure Detected! **")
                break

            # Wait for 3 seconds before processing the next reading
            time.sleep(3)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
