# -*- coding: utf-8 -*-
"""
Created on Sat May 18 07:38:16 2024

@author: HP
"""
# file_path = r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run1\Run1_CleanFilterData.xlsx'
# plt.savefig(r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run1\Plots\RUN-1_2-180524\vehicle_speed_distribution.png')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the Excel file
file_path = file_path = r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run1\Run1_CleanFilterData.xlsx'

data = pd.read_excel(file_path)

# Remove the first data row containing unit labels
cleaned_data = data.drop(index=0)

# Remove the 'Time (absolute)' column
cleaned_data = cleaned_data.drop(columns=['Time (absolute)'])

# Convert all remaining columns to numeric if possible
cleaned_data = cleaned_data.apply(pd.to_numeric, errors='coerce')

# Fill missing values with the median for each column
cleaned_data = cleaned_data.fillna(cleaned_data.median())

# Descriptive statistics for 'DI_vehicleSpeed'
vehicle_speed_stats = cleaned_data['DI_vehicleSpeed'].describe()
print(vehicle_speed_stats)

# Plotting the histogram for 'DI_vehicleSpeed' and saving the plot
plt.figure(figsize=(10, 6))
cleaned_data['DI_vehicleSpeed'].hist(bins=20)
plt.title('Distribution of Vehicle Speed')
plt.xlabel('Speed (km/h)')
plt.ylabel('Frequency')
plt.grid(False)
plt.savefig(r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run1\Plots\RUN-1_2-180524\vehicle_speed_distribution.png')
plt.show()

# Plotting the line graph for 'DI_vehicleSpeed' over time
plt.figure(figsize=(14, 7))
plt.plot(cleaned_data['Time (relative)'], cleaned_data['DI_vehicleSpeed'], label='Vehicle Speed')
plt.title('Vehicle Speed Over Time')
plt.xlabel('Time (relative) (seconds)')
plt.ylabel('Speed (km/h)')
plt.legend()
plt.grid(True)
plt.savefig(r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run1\Plots\RUN-1_2-180524\vehicle_speed_timeseries.png')
plt.show()

# Part 1: Regenerative Braking and Motor Current
columns_part1 = ['BMS_kwhRegenChargeTotal', 'FrontMotorCurrent1A5', 'RearMotorCurrent126']

# Calculate the correlation matrix for the relevant columns
correlation_matrix_part1 = cleaned_data[columns_part1].corr()

# Visualize the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix_part1, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix: Regenerative Braking and Motor Current')
plt.show()

# Generate scatter plots for pairs of variables to visualize correlations
sns.pairplot(cleaned_data[columns_part1])
plt.suptitle('Scatter Plots: Regenerative Braking and Motor Current', y=1.02)
plt.show()

columns_part2 = ['BMS_kwhRegenChargeTotal', 'SmoothBattCurrent132', 'RawBattCurrent132']

# Calculate the correlation matrix for the relevant columns
correlation_matrix_part2 = cleaned_data[columns_part2].corr()

# Visualize the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix_part2, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix: Regenerative Braking and Battery Current')
plt.show()

# Generate scatter plots for pairs of variables to visualize correlations
sns.pairplot(cleaned_data[columns_part2])
plt.suptitle('Scatter Plots: Regenerative Braking and Battery Current', y=1.02)
plt.show()

# Part 3: Motor Current and Battery Current
columns_part3 = ['FrontMotorCurrent1A5', 'RearMotorCurrent126', 'SmoothBattCurrent132', 'RawBattCurrent132']

# Calculate the correlation matrix for the relevant columns
correlation_matrix_part3 = cleaned_data[columns_part3].corr()

# Visualize the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix_part3, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix: Motor Current and Battery Current')
plt.show()

# Generate scatter plots for pairs of variables to visualize correlations
sns.pairplot(cleaned_data[columns_part3])
plt.suptitle('Scatter Plots: Motor Current and Battery Current', y=1.02)
plt.show()
