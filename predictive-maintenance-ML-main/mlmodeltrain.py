#!/usr/bin/env python
# coding: utf-8

# Install required libraries
#get_ipython().system('pip install scikit-learn==1.3.0')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle
import joblib

# Load dataset
df = pd.read_csv('predictive_maintenance.csv')

# Basic information
print(df.head())
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Ordinal encoding for 'Type' column
oe = OrdinalEncoder(categories=[['L', 'M', 'H']])
df['Type'] = oe.fit_transform(df[['Type']]).astype(int)

# Ensure the target variable is processed correctly
categories = [
    'No Failure', 'Heat Dissipation Failure', 'Power Failure', 
    'Overstrain Failure', 'Tool Wear Failure', 'Random Failures'
]
custom_encoder = {cat: i for i, cat in enumerate(categories)}
df['Failure Type'] = df['Failure Type'].map(custom_encoder)

# Split features and target
X = df.iloc[:, 2:8]  # Selecting relevant features
y = df['Failure Type']  # Target: 'Failure Type'

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model: Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

rf_train_acc = round(rf_model.score(X_train, y_train) * 100, 2)
rf_test_acc = round(accuracy_score(y_pred_rf, y_test) * 100, 2)

print("Random Forest Training Accuracy:", rf_train_acc, "%")
print("Random Forest Test Accuracy:", rf_test_acc, "%")
print("Classification Report:\n", classification_report(y_test, y_pred_rf))

# Save the best model
joblib.dump(rf_model, 'best_model.joblib')

# Save column names for future use
feature_columns = X.columns.tolist()
with open('feature_columns.pkl', 'wb') as f:
    pickle.dump(feature_columns, f)

# Confidence scores
if hasattr(rf_model, "predict_proba"):
    y_pred_proba = rf_model.predict_proba(X_test)  # Get class probabilities
    confidence_scores = np.max(y_pred_proba, axis=1)  # Use the highest probability for confidence
    for i, (pred, conf) in enumerate(zip(y_pred_rf, confidence_scores)):
        print(f"Sample {i}: Predicted Class = {pred}, Confidence Score = {conf:.2f}")
else:
    print("Confidence scores not available for this model.")

# Visualization of confidence scores
plt.hist(confidence_scores, bins=10, color='skyblue', edgecolor='black')
plt.title('Confidence Score Distribution')
plt.xlabel('Confidence Score')
plt.ylabel('Frequency')
plt.show()
