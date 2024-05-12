# -*- coding: utf-8 -*-
"""
Created on Sun May 12 22:53:32 2024

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt

# Define paths for convenience
input_file_path = r"E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\Run1_Data\Run1_CleanedData.csv"
output_directory = r"E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\Run1_Data\Plots\script2_run1_1st\newplots"

# Load the data
tesla_data = pd.read_csv(input_file_path)
tesla_data_cleaned = tesla_data.drop(index=0)
tesla_data_cleaned = tesla_data_cleaned.apply(pd.to_numeric, errors='coerce')

# Identify extreme changes in vehicle speed
extreme_changes_indices = tesla_data_cleaned['DI_vehicleSpeed'].diff().abs() > 25
extreme_events_times = tesla_data_cleaned['Time'][extreme_changes_indices]

# Plotting Vehicle Speed over Time with marks for extreme speed changes
plt.figure(figsize=(12, 7))
plt.plot(tesla_data_cleaned['Time'], tesla_data_cleaned['DI_vehicleSpeed'], label='Vehicle Speed')
plt.scatter(tesla_data_cleaned['Time'][extreme_changes_indices], tesla_data_cleaned['DI_vehicleSpeed'][extreme_changes_indices], color='red', label='Extreme Speed Changes (>25 km/h)')
plt.title('Vehicle Speed Over Time with Extreme Changes Marked')
plt.xlabel('Time (seconds)')
plt.ylabel('Speed (km/h)')
plt.legend()
plt.grid(True)
plt.savefig(output_directory + 'vehicle_speed_over_time.png')

# Detailed visualization around an example extreme event time
example_event_time = extreme_events_times.iloc[0]
time_window = 5  # seconds before and after the event
event_data = tesla_data_cleaned[(tesla_data_cleaned['Time'] >= example_event_time - time_window) &
                                (tesla_data_cleaned['Time'] <= example_event_time + time_window)]

# Plotting ESP Vehicle Speed around the extreme event
plt.figure(figsize=(12, 7))
plt.plot(event_data['Time'], event_data['ESP_vehicleSpeed'], label='ESP Vehicle Speed', color='purple')
plt.title('ESP Vehicle Speed Around Extreme Event')
plt.xlabel('Time (seconds)')
plt.ylabel('Speed (km/h)')
plt.legend()
plt.grid(True)
plt.savefig(output_directory + 'esp_vehicle_speed_around_event.png')

# Plotting ESP Front Left Brake Torque around the extreme event
plt.figure(figsize=(12, 7))
plt.plot(event_data['Time'], event_data['ESP_brakeTorqueFrL'], label='ESP Brake Torque Front Left', color='orange')
plt.title('ESP Front Left Brake Torque Around Extreme Event')
plt.xlabel('Time (seconds)')
plt.ylabel('Torque (Nm)')
plt.legend()
plt.grid(True)
plt.savefig(output_directory + 'esp_brake_torque_around_event.png')

# Plotting Regenerative Braking Data around the extreme event
fig, ax1 = plt.subplots(figsize=(12, 7))
ax1.set_xlabel('Time (seconds)')
ax1.set_ylabel('Battery Current (A)', color='tab:blue')
ax1.plot(event_data['Time'], event_data['RawBattCurrent132'], label='Raw Battery Current', color='tab:blue')
ax1.plot(event_data['Time'], event_data['SmoothBattCurrent132'], label='Smooth Battery Current', color='tab:green', linestyle='--')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.legend(loc='upper left')
ax1.grid(True)

# Assuming 'BMS_maxRegenPower' exists and is relevant
ax2 = ax1.twinx()
ax2.set_ylabel('Regenerative Power (kW)', color='tab:red')  # Adjust units if necessary
ax2.plot(event_data['Time'], event_data['BMS_maxRegenPower'], label='Max Regenerative Power', color='tab:red', linestyle='-.')
ax2.tick_params(axis='y', labelcolor='tab:red')
ax2.legend(loc='upper right')

plt.title('Regenerative Braking Data Around Extreme Event')
plt.savefig(output_directory + 'regenerative_braking_data.png')

