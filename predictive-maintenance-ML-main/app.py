import streamlit as st
import pandas as pd
import joblib

rfc = joblib.load('best_model.joblib')

st.title("Machine Predictive Maintenance Classification")

# Collecting user inputs
col1, col2 = st.columns(2)

with col1:
    selected_type = st.selectbox('Select a Type', ['Low', 'Medium', 'High'])
    type_mapping = {'Low': 0, 'Medium': 1, 'High': 2}
    selected_type = type_mapping[selected_type]

with col2:
    air_temperature = st.text_input('Air temperature [K]')

with col1:
    process_temperature = st.text_input('Process temperature [K]')

with col2:
    rotational_speed = st.text_input('Rotational speed [rpm]')

with col1:
    torque = st.text_input('Torque [Nm]')

with col2:
    tool_wear = st.text_input('Tool wear [min]')

# Prediction logic
failure_pred = ''

if st.button('Predict Failure'):
    try:
        # Convert inputs to numeric types
        air_temperature = float(air_temperature)
        process_temperature = float(process_temperature)
        rotational_speed = float(rotational_speed)
        torque = float(torque)
        tool_wear = float(tool_wear)

        # Create input DataFrame
        input_data = pd.DataFrame([[selected_type, air_temperature, process_temperature,
                                    rotational_speed, torque, tool_wear]],
                                  columns=['Type', 'Air temperature [K]', 'Process temperature [K]',
                                           'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]'])

        # Predict and interpret result
        failure_pred = rfc.predict(input_data)
        if failure_pred[0] == 1:
            failure_pred = 'Failure'
        else:
            failure_pred = 'No Failure'

    except ValueError as e:
        failure_pred = f"Error: {str(e)}"

    st.success(failure_pred)
