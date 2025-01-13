import streamlit as st
import pandas as pd
import joblib
from pymongo import MongoClient
from datetime import datetime
import time
import webbrowser

# Page configuration with dark theme
st.set_page_config(
    page_title="Live Analysis",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark theme
st.markdown("""
    <style>
    /* Dark theme colors */
    :root {
        --bg-color: #0E1117;
        --text-color: #FFFFFF;
        --accent-color: #262730;
        --border-color: #333333;
    }
    
    /* Overall page styling */
    .stApp {
        background-color: var(--bg-color);
        color: var(--text-color);
    }
    
    .status-box {
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
        background-color: var(--accent-color);
    }
    
    .green-status {
        color: #00FF00;
        border-left: 4px solid #00FF00;
    }
    
    .red-status {
        color: #FF0000;
        border-left: 4px solid #FF0000;
    }
    
    .sensor-table {
        background-color: var(--accent-color);
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
        width: 100%;
    }
    
    .sensor-row {
        display: flex;
        justify-content: space-between;
        padding: 8px 0;
        border-bottom: 1px solid var(--border-color);
    }
    
    .sensor-value {
        color: var(--text-color);
        font-family: monospace;
    }
    
    .header-style {
        color: var(--text-color);
        margin: 10px 0;
    }
    
    .stButton>button {
        width: 100%;
        background-color: var(--accent-color) !important;
        color: var(--text-color) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 5px;
    }

    .stselectbox{
    color: var(--text-color) !important;
}
    
    /* Analysis section */
    .analysis-box {
        background-color: var(--accent-color);
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
        border-left: 4px solid #FF7A00;
    }
    </style>
""", unsafe_allow_html=True)

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

# App title
st.title("Machine Predictive Maintenance")

def open_link(url):
    webbrowser.open_new_tab(url)

# Navigation buttons
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button('Home'):
        open_link("http://localhost:3000/dashboard")
with col2:
    clicked = st.button('Start Monitoring')
with col3:
    if st.button('View Details'):
        open_link("http://localhost:3000/reports")

# Type selection
selected_type = st.selectbox('Select Machine Type', ['Low', 'Medium', 'High'])
type_mapping = {'Low': 0, 'Medium': 1, 'High': 2}
selected_type = type_mapping[selected_type]

def display_sensor_readings(reading_time, sensors_data):
    st.markdown(f"### Sensor Readings at {reading_time}:")
    
    st.markdown(f"""
        <div class='sensor-table'>
            <div class='sensor-row'>
                <span>Air Temperature [K]: {sensors_data['Air Temperature [K]']}</span>
                <span>Process Temperature [K]: {sensors_data['Process Temperature [K]']}</span>
                <span>Rotational Speed [rpm]: {sensors_data['Rotational Speed [rpm]']}</span>
                <span>Torque [Nm]: {sensors_data['Torque [Nm]']}</span>
                <span>Tool Wear [min]: {sensors_data['Tool Wear [min]']}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

def display_status(predicted_type, confidence_score=None):
    status_class = 'green-status' if predicted_type == 'No Failure' else 'red-status'
    status_icon = '🟢' if predicted_type == 'No Failure' else '🔴'
    
    if predicted_type == 'No Failure':
        st.markdown(f"""
            <div class='status-box {status_class}'>
                <h3>Status: {status_icon} No Failure</h3>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class='status-box {status_class}'>
                <h3>Status: {status_icon} {predicted_type}</h3>
                <p>Confidence Score: {confidence_score:.2f}%</p>
            </div>
        """, unsafe_allow_html=True)

def display_analysis(predicted_type):
    if predicted_type != 'No Failure':
        analysis_data = {
            'Heat Dissipation Failure': {
                'component': 'Cooling System',
                'detail': 'The process temperature has exceeded safe thresholds intermittently, indicating potential overheating of transistors.'
            },
            'Power Failure': {
                'component': 'Electrical Supply',
                'detail': 'A sudden drop in power levels suggests an issue with the electrical supply.'
            },
            'Overstrain Failure': {
                'component': 'Mechanical System',
                'detail': 'Torque levels have exceeded safe limits, suggesting mechanical stress.'
            },
            'Tool Wear Failure': {
                'component': 'Tool',
                'detail': 'Tool wear has reached critical levels, indicating maintenance or replacement is required.'
            },
            'Random Failures': {
                'component': 'Unspecified',
                'detail': 'Random anomalies detected. Perform a thorough diagnostic.'
            }
        }
        
        analysis = analysis_data.get(predicted_type, {})
        st.markdown(f"""
            <div class='analysis-box'>
                <h3>Analysis:</h3>
                <p><strong>Status:</strong> Failure Detected</p>
                <p><strong>Fault Component:</strong> {analysis['component']}</p>
                <p><strong>Detail:</strong> {analysis['detail']}</p>
                <p><strong>Recommended Action:</strong> Schedule immediate maintenance inspection</p>
            </div>
        """, unsafe_allow_html=True)
if clicked:
    try:
        all_readings = collection.find().sort("timestamp", 1)
        
        for reading in all_readings:
            sensors_data = {
                'Air Temperature [K]': reading.get("air_temperature"),
                'Process Temperature [K]': reading.get("process_temperature"),
                'Rotational Speed [rpm]': reading.get("rotational_speed"),
                'Torque [Nm]': reading.get("torque"),
                'Tool Wear [min]': reading.get("tool_wear")
            }
            
            if None in sensors_data.values():
                st.warning("⚠️ Incomplete sensor data detected")
                continue
                
            input_data = pd.DataFrame([[
                selected_type,
                sensors_data['Air Temperature [K]'],
                sensors_data['Process Temperature [K]'],
                sensors_data['Rotational Speed [rpm]'],
                sensors_data['Torque [Nm]'],
                sensors_data['Tool Wear [min]']
            ]], columns=['Type', 'Air temperature [K]', 'Process temperature [K]',
                        'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]'])
            
            prediction = rfc.predict(input_data)
            prediction_prob = rfc.predict_proba(input_data)
            predicted_type = categories[prediction[0]]
            confidence_score = prediction_prob[0][prediction[0]] * 100
            
            display_sensor_readings(datetime.now(), sensors_data)
            display_status(predicted_type, confidence_score if predicted_type != 'No Failure' else None)
            display_analysis(predicted_type)
            
            if predicted_type != 'No Failure':
                break
                
            time.sleep(3)
            
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")