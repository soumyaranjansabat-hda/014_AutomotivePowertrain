
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'path_to_your_data.xlsx'
data_df = pd.read_excel(file_path, sheet_name='Data', skiprows=[1])

# Select relevant columns for analysis
motor_columns = ['FrontHighVoltage1A5', 'FrontMotorCurrent1A5', 'FrontPower2E5', 'FrontTorque1D5',
                 'RearHighVoltage126', 'RearMotorCurrent126', 'RearPower266', 'RearTorque1D8', 'DI_vehicleSpeed']
motor_data_df = data_df[motor_columns]

# Visualization: Scatter Plots
sns.scatterplot(data=motor_data_df, x='FrontMotorCurrent1A5', y='FrontTorque1D5').set_title('Front Motor Current vs. Torque')
sns.scatterplot(data=motor_data_df, x='RearMotorCurrent126', y='RearTorque1D8').set_title('Rear Motor Current vs. Torque')
plt.show()

# Visualization: Line Graphs
sns.lineplot(data=motor_data_df, x='DI_vehicleSpeed', y='FrontTorque1D5').set_title('Vehicle Speed vs. Front Motor Torque')
sns.lineplot(data=motor_data_df, x='DI_vehicleSpeed', y='RearTorque1D8').set_title('Vehicle Speed vs. Rear Motor Torque')
plt.show()

# Calculate the correlation matrix
correlation_matrix = motor_data_df.corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
plt.title('Correlation Matrix Heatmap')
plt.show()

# Time Series Analysis: Plotting Front Motor Torque over Time
plt.figure(figsize=(12, 6))
plt.plot(time_series_df['FrontTorque1D5'], label='Front Motor Torque')
plt.title('Front Motor Torque Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Torque (Nm)')
plt.legend()
plt.show()

# Correlation and Visualization Code for Regenerative Braking Analysis

# Correlation Matrix for Motor Performance and Energy Recovery
motor_performance_data = regen_braking_data[['FrontMotorCurrent1A5', 'RearMotorCurrent126', 'FrontTorque1D5', 'RearTorque1D8']]
motor_performance_corr_matrix = motor_performance_data.corr()
energy_recovery_data = regen_braking_data[['ESP_vehicleSpeed', 'RegenEnergyChange', 'SmoothBattCurrent132']]
energy_recovery_corr_matrix = energy_recovery_data.corr()

# Plotting Correlation Matrices
plt.figure(figsize=(10, 5))
sns.heatmap(motor_performance_corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Motor Performance Correlation Matrix')
plt.figure(figsize=(10, 5))
sns.heatmap(energy_recovery_corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Energy Recovery Correlation Matrix')

# Line Graph for Regenerative Braking Analysis
fig, ax1 = plt.subplots(figsize=(14, 8))
ax1.plot(regen_braking_data['Time (relative)'], regen_braking_data['ESP_vehicleSpeed'], 'b-', label='Vehicle Speed')
ax2 = ax1.twinx()
ax2.plot(regen_braking_data['Time (relative)'], regen_braking_data['FrontMotorCurrent1A5'], 'r-', label='Front Motor Current')
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(regen_braking_data['Time (relative)'], regen_braking_data['RegenEnergyChange'], 'g-', label='Regen Energy Change')
ax1.set_xlabel('Time (seconds)')
ax1.set_ylabel('Speed (kph)')
ax2.set_ylabel('Motor Current (A)')
ax3.set_ylabel('Energy Change (kWh)')
fig.tight_layout()
fig.legend(loc='upper right', bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
plt.show()

# Additional Python code for Regression Analysis and Visualization

# Regression Model for Efficiency
import statsmodels.api as sm
predictors = sm.add_constant(regen_braking_events[['SOCave', 'FrontMotorCurrent1A5', 'RearMotorCurrent126', 'FrontTorque1D5', 'RearTorque1D8', 'ESP_vehicleSpeed']])
target = regen_braking_events['Efficiency'].fillna(0)
model = sm.OLS(target, predictors, missing='drop')
results = model.fit()
print(results.summary())

# Heatmap and Line Graph Visualization Code
# (The plotting code used in the analysis steps is included here as needed.)

# Python code for Visualizing Regenerative Braking Dynamics with Split Graphs

# Graph 1: Regenerative Energy Change and Vehicle Speed
fig, ax1 = plt.subplots(figsize=(14, 6))
ax1.plot(regen_braking_events.index, regen_braking_events['EnergyRecovered'], 'r-', label='Regen Energy Change')
ax1.set_xlabel('Time (relative)')
ax1.set_ylabel('Regen Energy Change (kWh)', color='r')
ax2 = ax1.twinx()
ax2.plot(regen_braking_events.index, regen_braking_events['ESP_vehicleSpeed'], 'b-', label='Vehicle Speed (ESP)')
ax2.set_ylabel('Vehicle Speed (km/h)', color='b')
plt.title('Regenerative Energy Change and Vehicle Speed Over Time')
plt.legend()
plt.show()

# Graph 2: Rear Motor Current and Smooth Battery Current
fig, ax1 = plt.subplots(figsize=(14, 6))
ax1.plot(regen_braking_events.index, regen_braking_events['RearMotorCurrent126'], 'g-', label='Rear Motor Current')
ax1.set_xlabel('Time (relative)')
ax1.set_ylabel('Rear Motor Current (A)', color='g')
ax2 = ax1.twinx()
ax2.plot(regen_braking_events.index, regen_braking_events['SmoothBattCurrent132'], 'p-', label='Smooth Battery Current')
ax2.set_ylabel('Smooth Battery Current (A)', color='p')
plt.title('Rear Motor Current and Smooth Battery Current Over Time')
plt.legend()
plt.show()

# Identify specific events: Locate periods with significant drops in vehicle speed to indicate sudden braking
event_threshold = 10  # Example threshold for significant speed drop
sudden_braking_events = stability_data[stability_data['DI_vehicleSpeed'].diff().abs() > event_threshold].index

# Choose one or two specific events for detailed analysis
selected_event_index = sudden_braking_events[0]  # Choosing the first identified event for detailed analysis

# Define a narrower window around the selected event for detailed analysis
detailed_event_window = 10  # Number of rows before and after the event to consider
event_data = stability_data.loc[selected_event_index - detailed_event_window : selected_event_index + detailed_event_window]

# Plot detailed data around the selected event
fig, axs = plt.subplots(6, 1, figsize=(14, 20), sharex=True)

# Vehicle Speed
axs[0].plot(event_data.index, event_data['DI_vehicleSpeed'], label='Vehicle Speed (KPH)', color='black')
axs[0].set_title('Vehicle Speed During Specific Event')
axs[0].set_ylabel('Speed (KPH)')
axs[0].legend()
axs[0].grid(True)

# Brake Torques
axs[1].plot(event_data.index, event_data['ESP_brakeTorqueFrL'], label='Front Left Brake Torque (Nm)', color='blue')
axs[1].plot(event_data.index, event_data['ESP_brakeTorqueFrR'], label='Front Right Brake Torque (Nm)', color='green')
axs[1].plot(event_data.index, event_data['ESP_brakeTorqueReL'], label='Rear Left Brake Torque (Nm)', color='red')
axs[1].plot(event_data.index, event_data['ESP_brakeTorqueReR'], label='Rear Right Brake Torque (Nm)', color='purple')
axs[1].set_title('Brake Torques During Specific Event')
axs[1].set_ylabel('Brake Torque (Nm)')
axs[1].legend()
axs[1].grid(True)

# Wheel Speeds
axs[2].plot(event_data.index, event_data['WheelSpeedFL175'], label='Front Left Wheel Speed (KPH)', color='blue')
axs[2].plot(event_data.index, event_data['WheelSpeedFR175'], label='Front Right Wheel Speed (KPH)', color='green')
axs[2].plot(event_data.index, event_data['WheelSpeedRL175'], label='Rear Left Wheel Speed (KPH)', color='red')
axs[2].plot(event_data.index, event_data['WheelSpeedRR175'], label='Rear Right Wheel Speed (KPH)', color='purple')
axs[2].set_title('Wheel Speeds During Specific Event')
axs[2].set_ylabel('Speed (KPH)')
axs[2].legend()
axs[2].grid(True)

# Lateral, Longitudinal, and Vertical Accelerations
axs[3].plot(event_data.index, event_data['RCM_lateralAccel'], label='Lateral Acceleration (m/s²)', color='blue')
axs[3].plot(event_data.index, event_data['RCM_longitudinalAccel'], label='Longitudinal Acceleration (m/s²)', color='green')
axs[3].plot(event_data.index, event_data['RCM_verticalAccel'], label='Vertical Acceleration (m/s²)', color='red')
axs[3].set_title('Accelerations During Specific Event')
axs[3].set_ylabel('Acceleration (m/s²)')
axs[3].legend()
axs[3].grid(True)

# Yaw, Pitch, and Roll Rates
axs[4].plot(event_data.index, event_data['RCM_yawRate'], label='Yaw Rate (rad/s)', color='blue')
axs[4].plot(event_data.index, event_data['RCM_pitchRate'], label='Pitch Rate (rad/s)', color='green')
axs[4].plot(event_data.index, event_data['RCM_rollRate'], label='Roll Rate (rad/s)', color='red')
axs[4].set_title('Rotational Rates During Specific Event')
axs[4].set_ylabel('Rate (rad/s)')
axs[4].legend()
axs[4].grid(True)

# Highlight the event point
for ax in axs:
    ax.axvline(x=selected_event_index, color='gray', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# Display detailed event data for inspection
import ace_tools as tools; tools.display_dataframe_to_user(name="Detailed Event Data", dataframe=event_data)

event_data.describe()
