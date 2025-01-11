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
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
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

# Model 1: Logistic Regression
log_model = LogisticRegression(solver='lbfgs', max_iter=10000)
log_model.fit(X_train, y_train)
y_pred_log = log_model.predict(X_test)

log_train_acc = round(log_model.score(X_train, y_train) * 100, 2)
log_test_acc = round(accuracy_score(y_pred_log, y_test) * 100, 2)

print("Logistic Regression Training Accuracy:", log_train_acc, "%")
print("Logistic Regression Test Accuracy:", log_test_acc, "%")
print("Classification Report:\n", classification_report(y_test, y_pred_log))

# Model 2: Decision Tree
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
y_pred_dt = dt_model.predict(X_test)

dt_train_acc = round(dt_model.score(X_train, y_train) * 100, 2)
dt_test_acc = round(accuracy_score(y_pred_dt, y_test) * 100, 2)

print("Decision Tree Training Accuracy:", dt_train_acc, "%")
print("Decision Tree Test Accuracy:", dt_test_acc, "%")
print("Classification Report:\n", classification_report(y_test, y_pred_dt))

# Model 3: Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

rf_train_acc = round(rf_model.score(X_train, y_train) * 100, 2)
rf_test_acc = round(accuracy_score(y_pred_rf, y_test) * 100, 2)

print("Random Forest Training Accuracy:", rf_train_acc, "%")
print("Random Forest Test Accuracy:", rf_test_acc, "%")
print("Classification Report:\n", classification_report(y_test, y_pred_rf))

# Model 4: Support Vector Machines
svc_model = SVC(random_state=42)
svc_model.fit(X_train, y_train)
y_pred_svc = svc_model.predict(X_test)

svc_train_acc = round(svc_model.score(X_train, y_train) * 100, 2)
svc_test_acc = round(accuracy_score(y_pred_svc, y_test) * 100, 2)

print("SVC Training Accuracy:", svc_train_acc, "%")
print("SVC Test Accuracy:", svc_test_acc, "%")
print("Classification Report:\n", classification_report(y_test, y_pred_svc))

# Save the best model (Random Forest in this case)
joblib.dump(rf_model, 'best_model.joblib')

# Save column names for future use
feature_columns = X.columns.tolist()
with open('feature_columns.pkl', 'wb') as f:
    pickle.dump(feature_columns, f)