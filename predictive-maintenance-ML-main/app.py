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

# Failure type categories
categories = [
    'No Failure', 
    'Heat Dissipation Failure', 
    'Power Failure', 
    'Overstrain Failure', 
    'Tool Wear Failure', 
    'Random Failures'
]

# Streamlit App Title
st.title("Machine Predictive Maintenance")

# Add buttons for navigation
col1, col2 = st.columns(2)

with col1:
    if st.button('View Details'):
        st.write("Here you can display the details of your model or any additional info.")
        
with col2:
    if st.button('Home'):
        st.write("This will redirect to the home page or main menu.")

# Collect user input for type
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
            predicted_type = categories[prediction[0]]  # Map the integer to the failure type

            # Display sensor readings
            st.markdown(f"### Sensor Readings at {datetime.now()}:")
            st.write(f"**Air Temperature [K]:** {air_temperature}, **Process Temperature [K]:** {process_temperature}")
            st.write(f"**Rotational Speed [rpm]:** {rotational_speed}, **Torque [Nm]:** {torque}")
            st.write(f"**Tool Wear [min]:** {tool_wear}")
            st.markdown(f"#### Prediction: **{predicted_type}**")

            # If failure is detected, display an alert and detailed analysis
            if predicted_type != 'No Failure':
                st.error(f"⚠️ **ALERT: {predicted_type} Detected!**")
                
                # Wait for 2 seconds before showing analysis
                time.sleep(2)
                
                # Display detailed analysis in required format
                st.markdown("### Analysis:")

                if predicted_type == 'Heat Dissipation Failure':
                    st.write("**Status:** Failure Detected")
                    st.write("**Fault Component:** Cooling System")
                    st.write("**Detail:** The process temperature has exceeded safe thresholds intermittently, indicating potential overheating of transistors. Immediate cooling system inspection is recommended.")
                elif predicted_type == 'Power Failure':
                    st.write("**Status:** Failure Detected")
                    st.write("**Fault Component:** Electrical Supply")
                    st.write("**Detail:** A sudden drop in power levels suggests an issue with the electrical supply. Check for circuit interruptions.")
                elif predicted_type == 'Overstrain Failure':
                    st.write("**Status:** Failure Detected")
                    st.write("**Fault Component:** Mechanical System")
                    st.write("**Detail:** Torque levels have exceeded safe limits, suggesting mechanical stress. Inspect for potential overloading.")
                elif predicted_type == 'Tool Wear Failure':
                    st.write("**Status:** Failure Detected")
                    st.write("**Fault Component:** Tool")
                    st.write("**Detail:** Tool wear has reached critical levels, indicating that maintenance or replacement is required.")
                else:
                    st.write("**Status:** Failure Detected")
                    st.write("**Fault Component:** Unspecified")
                    st.write("**Detail:** Random anomalies detected. Perform a thorough diagnostic.")

                break

            # Wait for 3 seconds before processing the next reading
            time.sleep(3)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
