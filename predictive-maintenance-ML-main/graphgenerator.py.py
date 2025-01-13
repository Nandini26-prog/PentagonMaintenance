#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


# pip install "numpy<2"


# In[2]:


# pip install --upgrade matplotlib seaborn


# In[3]:


# pip install "pybind11>=2.12"


# In[4]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr


# In[5]:


# Manually input the dataset
data = pd.DataFrame([
    [4423, 4422, "M19282", "M", 302.6, 310.2, 2157, 17.2, 94, 0, "No Failure"],
    [4424, 4423, "M19283", "M", 302.6, 310.2, 1563, 39.0, 97, 0, "No Failure"],
    [4425, 4424, "M19284", "M", 302.6, 310.2, 1631, 31.0, 100, 0, "No Failure"],
    [4426, 4425, "L51605", "L", 302.5, 310.2, 1547, 36.9, 103, 0, "No Failure"],
    [4427, 4426, "L51606", "L", 302.6, 310.3, 1479, 40.4, 105, 0, "No Failure"],
    [4428, 4427, "M19287", "M", 302.4, 310.1, 1379, 48.9, 107, 1, "Heat Dissipation Failure"],
    [4429, 4428, "L51608", "L", 302.4, 310.1, 1906, 21.2, 110, 0, "No Failure"]
], columns=['ID', 'Previous_ID', 'Tool_ID', 'Type', 'Air_Temp', 'Process_Temp', 
            'Rotational_Speed', 'Torque', 'Tool_Wear', 'Failure', 'Failure_Type'])

# Display the first few rows of the DataFrame
data.head()


# In[11]:


# Select numeric columns
numeric_columns = ['Air_Temp', 'Process_Temp', 'Rotational_Speed', 'Torque', 'Tool_Wear']

# Normalize the data for heatmap visualization
severity_data = data[numeric_columns].copy()
for column in severity_data.columns:
    severity_data[column] = (severity_data[column] - severity_data[column].min()) / \
                            (severity_data[column].max() - severity_data[column].min())

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(severity_data.T, cmap='YlOrRd', xticklabels=range(1, len(data) + 1),
            yticklabels=numeric_columns, annot=True, fmt='.2f')
plt.title('Component-Wise Fault Severity Heatmap')
plt.xlabel('Time Step')
plt.ylabel('Component')
plt.tight_layout()
plt.show()


# In[13]:


# Define the maximum tool wear (assumed limit for RUL calculation)
max_tool_wear = 250

# Calculate RUL
rul = max_tool_wear - data['Tool_Wear']

# Plot RUL
plt.figure(figsize=(12, 6))
plt.plot(range(1, len(data) + 1), rul, marker='o', linewidth=2)
plt.axhline(y=50, color='r', linestyle='--', label='Critical RUL Threshold')
plt.title('Remaining Useful Life (RUL) Estimation')
plt.xlabel('Time Step')
plt.ylabel('Estimated RUL')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


# In[15]:


# Define thresholds for each component
thresholds = {
    'Air_Temp': 302.6,
    'Process_Temp': 310.2,
    'Rotational_Speed': 1600,
    'Torque': 40.0,
    'Tool_Wear': 105
}

# Plot threshold exceedance for each component
fig, axes = plt.subplots(len(numeric_columns), 1, figsize=(12, 15))
fig.suptitle('Threshold Exceedance Visualization')

for i, (column, ax) in enumerate(zip(numeric_columns, axes)):
    values = data[column]
    threshold = thresholds[column]
    
    ax.plot(range(1, len(data) + 1), values, marker='o', label='Actual Value')
    ax.axhline(y=threshold, color='r', linestyle='--', label='Threshold')
    
    # Highlight exceedances
    exceedances = values > threshold
    if any(exceedances):
        ax.scatter(np.where(exceedances)[0] + 1, values[exceedances], 
                   color='red', s=100, label='Exceedance')
    
    ax.set_title(f'{column} Threshold Analysis')
    ax.set_xlabel('Time Step')
    ax.set_ylabel('Value')
    ax.grid(True)
    ax.legend()

plt.tight_layout()
plt.show()


# In[17]:


import matplotlib.pyplot as plt
import numpy as np

# Define thresholds for each component
thresholds = {
    'Air_Temp': 302.6,
    'Process_Temp': 310.2,
    'Rotational_Speed': 1600,
    'Torque': 40.0,
    'Tool_Wear': 105
}

# Define colors for each component
colors = {
    'Air_Temp': 'blue',
    'Process_Temp': 'orange',
    'Rotational_Speed': 'green',
    'Torque': 'purple',
    'Tool_Wear': 'brown'
}

# Plot all components on a single graph
plt.figure(figsize=(15, 8))
plt.title('Threshold Exceedance Visualization')

for column in thresholds:
    values = data[column]
    threshold = thresholds[column]
    
    # Plot actual values
    plt.plot(range(1, len(data) + 1), values, label=f'{column} (Actual)', color=colors[column])
    
    # Plot threshold line
    plt.axhline(y=threshold, color=colors[column], linestyle='--', label=f'{column} (Threshold)')
    
    # Highlight exceedances
    exceedances = values > threshold
    if any(exceedances):
        plt.scatter(np.where(exceedances)[0] + 1, values[exceedances], color='red', s=100, label=f'{column} Exceedance')

plt.xlabel('Time Step')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()


# In[19]:


# Compute the correlation matrix
corr_matrix = data[numeric_columns].corr()

# Plot the heatmap for correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, 
            square=True, fmt='.2f')
plt.title('Component Correlation Heatmap')
plt.tight_layout()
plt.show()


# In[21]:


def generate_all_visualizations():
    print("Generating Fault Severity Heatmap...")
    plot_fault_severity_heatmap()
    
    print("\nGenerating RUL Plot...")
    plot_rul()
    
    print("\nGenerating Threshold Exceedance Visualization...")
    plot_threshold_exceedance()
    
    print("\nGenerating Correlation Heatmap...")
    plot_correlation_heatmap()
    
# Call the function to generate all visualizations
generate_all_visualizations()


# In[ ]:




