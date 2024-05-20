# -*- coding: utf-8 -*-
"""
Created on Sat May 17 07:14:48 2024

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file, assuming correct header handling
file_path = r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run1\Run1_CleanFilterData.xlsx'
data = pd.read_excel(file_path, header=0, skiprows=[1])

# Convert 'DI_vehicleSpeed' to numeric in case of non-numeric entries
data['DI_vehicleSpeed'] = pd.to_numeric(data['DI_vehicleSpeed'], errors='coerce')

# Calculate the change in speed over a 3-second window
window_size = 3  # seconds
speed_changes_window = data['DI_vehicleSpeed'].diff(periods=window_size).abs()

# Define a threshold for significant changes
threshold_window = 50  # kmph change over 3 seconds

# Identify critical points with the new windowed threshold
critical_points_window = speed_changes_window[speed_changes_window >= threshold_window].index

# Plotting vehicle speed over time with updated critical events using the windowed approach
plt.figure(figsize=(14, 7))
plt.plot(data['DI_vehicleSpeed'], label='Vehicle Speed (kph)', color='blue')
plt.title(f'Vehicle Speed Over Time with {window_size}-Second Window Threshold')
plt.xlabel('Time (Index)')
plt.ylabel('Speed (kph)')
plt.grid(True)

# Mark updated critical events with crosses for the new threshold
for point in critical_points_window:
    plt.scatter(point, data.loc[point, 'DI_vehicleSpeed'], color='red', marker='x', s=100)

plt.legend()

# Save the figure to a file
save_path = r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run1\Plots\RUN-1_1-180524\vehicle_speed_plot.png'
plt.savefig(save_path, format='png')
plt.show()

