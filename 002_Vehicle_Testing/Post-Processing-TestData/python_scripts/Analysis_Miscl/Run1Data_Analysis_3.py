# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:28:36 2024

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = r"E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\Run1_Data\Run1_CleanedData.csv"
output_directory= r"E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\Run1_Data\Plots\script2_run3_1st"

data = pd.read_csv(file_path)

# Remove non-numeric rows (assuming the first row contains units or descriptions)
data_cleaned = data.drop(index=0)

# Convert all columns to numeric, non-convertible values will be NaN
data_cleaned = data_cleaned.apply(pd.to_numeric, errors='coerce')

# Calculate descriptive statistics for DI_vehicleSpeed
vehicle_speed_stats = data_cleaned['DI_vehicleSpeed'].describe()
print("Descriptive Statistics for DI_vehicleSpeed:")
print(vehicle_speed_stats)

# Plotting the distribution of DI_vehicleSpeed
plt.figure(figsize=(20, 20))
plt.hist(data_cleaned['DI_vehicleSpeed'], bins=30, color='blue', alpha=0.7)
plt.title('Distribution of Vehicle Speed (DI_vehicleSpeed)')
plt.xlabel('Speed (km/h)')
plt.ylabel('Frequency')
plt.grid(True)
plt.legend()
plt.savefig(output_directory + r"\regenerative_braking_data.png")
plt.show()

# Assuming 'ESP_signal1' is a placeholder for actual ESP data column names
# Check for ESP columns, if they exist in the dataset
esp_columns = [col for col in data_cleaned.columns if 'ESP' in col and col != 'ESP_vehicleSpeed']
if esp_columns:
    # Calculate correlations between vehicle speed and ESP signals
    correlation_matrix = data_cleaned[['DI_vehicleSpeed'] + esp_columns].corr()

    # Visualizing the correlation with a heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix for Vehicle Speed and ESP Signals')
    plt.show()

    # Plotting Vehicle Speed and ESP Signal Over Time
    plt.figure(figsize=(10, 5))
    plt.plot(data_cleaned['Time'], data_cleaned['DI_vehicleSpeed'], label='Vehicle Speed')
    for esp in esp_columns:
        plt.plot(data_cleaned['Time'], data_cleaned[esp], label=f'{esp}', alpha=0.7)
    plt.legend()
    plt.title('Vehicle Speed and ESP Signals Over Time')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.show()
else:
    print("No ESP columns found in the dataset.")
