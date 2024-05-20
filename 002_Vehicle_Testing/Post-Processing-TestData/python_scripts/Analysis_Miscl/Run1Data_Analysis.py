# -*- coding: utf-8 -*-
"""
Created on Sun May 12 19:06:52 2024

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
excel_path = 'E:/HDA_Lectures/001_Repository/014_AutomotivePowertrain/002_Vehicle_Testing/Post-Processing-TestData/Run1_Data/Run1_CleanedData.xlsx'
data = pd.read_excel(excel_path)

# Convert all relevant columns to numeric, setting errors='coerce' to handle any non-numeric values gracefully
columns_of_interest = [
    'Time', 'SmoothBattCurrent132', 'FrontMotorCurrent1A5', 'RearMotorCurrent126', 
    'BMS_maxRegenPower'
]
for column in columns_of_interest:
    data[column] = pd.to_numeric(data[column], errors='coerce')

# Plotting key metrics over time
fig, axs = plt.subplots(4, 1, figsize=(14, 18), sharex=True)

# Smooth HV Battery Current
axs[0].plot(data['Time'], data['SmoothBattCurrent132'], label='SmoothBattCurrent132', color='blue')
axs[0].set_title('Smooth HV Battery Current Over Time')
axs[0].set_ylabel('Current (A)')
axs[0].legend()
plt.savefig('Smooth_HV_Battery_Current_Over_Time.png')  # Save the plot

# Front Motor Current
axs[1].plot(data['Time'], data['FrontMotorCurrent1A5'], label='FrontMotorCurrent1A5', color='green')
axs[1].set_title('Front Motor Current Over Time')
axs[1].set_ylabel('Current (A)')
axs[1].legend()
plt.savefig('Front_Motor_Current_Over_Time.png')  # Save the plot

# Rear Motor Current
axs[2].plot(data['Time'], data['RearMotorCurrent126'], label='RearMotorCurrent126', color='red')
axs[2].set_title('Rear Motor Current Over Time')
axs[2].set_ylabel('Current (A)')
axs[2].legend()
plt.savefig('Rear_Motor_Current_Over_Time.png')  # Save the plot

# Max Regenerative Braking Power
axs[3].plot(data['Time'], data['BMS_maxRegenPower'], label='BMS_maxRegenPower', color='purple')
axs[3].set_title('Max Regenerative Braking Power Over Time')
axs[3].set_ylabel('Power (kW)')
axs[3].set_xlabel('Time (sec)')
axs[3].legend()
plt.tight_layout()
plt.savefig('Max_Regenerative_Braking_Power_Over_Time.png')  # Save the plot

# Calculating and plotting the correlation matrix
correlation_data = data[['SmoothBattCurrent132', 'FrontMotorCurrent1A5', 'RearMotorCurrent126', 'BMS_maxRegenPower']].dropna()
correlation_matrix = correlation_data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix of Key Metrics')
plt.savefig('Correlation_Matrix.png')  # Save the plot
