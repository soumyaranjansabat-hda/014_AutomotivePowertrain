
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

# Dynamic Response Analysis
# Plotting lateral, longitudinal, and vertical accelerations during sudden braking events
fig, axs = plt.subplots(3, 1, figsize=(14, 12), sharex=True)

# Lateral Acceleration
axs[0].plot(stability_data.index, stability_data['RCM_lateralAccel'], label='Lateral Acceleration (m/s²)', color='blue')
axs[0].set_title('Lateral Acceleration During Sudden Braking Events')
axs[0].set_ylabel('Acceleration (m/s²)')
axs[0].legend()
axs[0].grid(True)

# Longitudinal Acceleration
axs[1].plot(stability_data.index, stability_data['RCM_longitudinalAccel'], label='Longitudinal Acceleration (m/s²)', color='green')
axs[1].set_title('Longitudinal Acceleration During Sudden Braking Events')
axs[1].set_ylabel('Acceleration (m/s²)')
axs[1].legend()
axs[1].grid(True)

# Vertical Acceleration
axs[2].plot(stability_data.index, stability_data['RCM_verticalAccel'], label='Vertical Acceleration (m/s²)', color='red')
axs[2].set_title('Vertical Acceleration During Sudden Braking Events')
axs[2].set_ylabel('Acceleration (m/s²)')
axs[2].set_xlabel('Time Index')
axs[2].legend()
axs[2].grid(True)

# Highlight the braking event points
for ax in axs:
    for index in sudden_braking_indices:
        ax.axvline(x=index, color='gray', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# Rotational Rates Analysis
# Plotting yaw, pitch, and roll rates during sudden braking events
fig, axs = plt.subplots(3, 1, figsize=(14, 12), sharex=True)

# Yaw Rate
axs[0].plot(stability_data.index, stability_data['RCM_yawRate'], label='Yaw Rate (rad/s)', color='blue')
axs[0].set_title('Yaw Rate During Sudden Braking Events')
axs[0].set_ylabel('Rate (rad/s)')
axs[0].legend()
axs[0].grid(True)

# Pitch Rate
axs[1].plot(stability_data.index, stability_data['RCM_pitchRate'], label='Pitch Rate (rad/s)', color='green')
axs[1].set_title('Pitch Rate During Sudden Braking Events')
axs[1].set_ylabel('Rate (rad/s)')
axs[1].legend()
axs[1].grid(True)

# Roll Rate
axs[2].plot(stability_data.index, stability_data['RCM_rollRate'], label='Roll Rate (rad/s)', color='red')
axs[2].set_title('Roll Rate During Sudden Braking Events')
axs[2].set_ylabel('Rate (rad/s)')
axs[2].set_xlabel('Time Index')
axs[2].legend()
axs[2].grid(True)

# Highlight the braking event points
for ax in axs:
    for index in sudden_braking_indices:
        ax.axvline(x=index, color='gray', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# Correlation Analysis
# Prepare data by combining dynamic responses with vehicle speed and brake torque data
correlation_data = stability_data.loc[sudden_braking_indices.min() - narrow_window : sudden_braking_indices.max() + narrow_window, 
                                      ['DI_vehicleSpeed', 'ESP_brakeTorqueFrL', 'ESP_brakeTorqueFrR', 'ESP_brakeTorqueReL', 'ESP_brakeTorqueReR',
                                       'RCM_lateralAccel', 'RCM_longitudinalAccel', 'RCM_verticalAccel', 'RCM_yawRate', 'RCM_pitchRate', 'RCM_rollRate']]

# Calculate correlation matrix
correlation_matrix = correlation_data.corr()

# Plot correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.2f')
plt.title('Correlation Matrix of Dynamic Responses, Vehicle Speed, and Brake Torques')
plt.show()

# Grouped Correlation Matrices
# Group 1: Vehicle Speed and Brake Torques
group1_columns = ['DI_vehicleSpeed', 'ESP_brakeTorqueFrL', 'ESP_brakeTorqueFrR', 'ESP_brakeTorqueReL', 'ESP_brakeTorqueReR']
group1_corr_matrix = correlation_data[group1_columns].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(group1_corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.2f')
plt.title('Correlation Matrix: Vehicle Speed and Brake Torques')
plt.show()

# Group 2: Accelerations
group2_columns = ['RCM_lateralAccel', 'RCM_longitudinalAccel', 'RCM_verticalAccel']
group2_corr_matrix = correlation_data[group2_columns].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(group2_corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.2f')
plt.title('Correlation Matrix: Accelerations')
plt.show()

# Group 3: Rotational Rates
group3_columns = ['RCM_yawRate', 'RCM_pitchRate', 'RCM_rollRate']
group3_corr_matrix = correlation_data[group3_columns].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(group3_corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.2f')
plt.title('Correlation Matrix: Rotational Rates')
plt.show()

# Group 4: Combined Dynamic Responses with Vehicle Speed and Brake Torques
group4_columns = group1_columns + group2_columns + group3_columns
group4_corr_matrix = correlation_data[group4_columns].corr()

plt.figure(figsize=(12, 10))
sns.heatmap(group4_corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.2f')
plt.title('Correlation Matrix: Combined Dynamic Responses with Vehicle Speed and Brake Torques')
plt.show()

# Energy Distribution Analysis
# Constants
vehicle_mass = 1850  # Approximate mass of Tesla Model 3 in kg
g = 9.81  # Acceleration due to gravity in m/s²
wheel_radius = 0.33  # Approximate wheel radius in meters for Tesla Model 3

# Calculate deceleration force from longitudinal acceleration
deceleration_force = vehicle_mass * stability_data['RCM_longitudinalAccel']

# Estimate regenerative braking energy (assuming a fraction of deceleration is due to regenerative braking)
# For simplification, assume 30% of deceleration energy is captured by regenerative braking
regenerative_braking_fraction = 0.30
aligned_deceleration_force = deceleration_force.loc[braking_event_indices]
aligned_vehicle_speed = stability_data.loc[braking_event_indices, 'DI_vehicleSpeed']
regenerative_braking_energy_estimate = (aligned_deceleration_force * aligned_vehicle_speed * regenerative_braking_fraction * time_intervals).sum() / 3600  # Convert to kWh

# Estimate mechanical braking energy using brake torque data (simplified model)
aligned_brake_torque_data = brake_torque_data.loc[braking_event_indices]
mechanical_braking_power = aligned_brake_torque_data.sum(axis=1) * aligned_vehicle_speed * (1000/3600) / wheel_radius  # Convert speed to m/s
mechanical_braking_energy_estimate = (mechanical_braking_power * time_intervals).sum() / 3600  # Convert to kWh

# Visualize energy contributions
energy_data_estimate = {
    'Estimated Regenerative Braking Energy (kWh)': regenerative_braking_energy_estimate,
    'Estimated Mechanical Braking Energy (kWh)': mechanical_braking_energy_estimate
}

plt.figure(figsize=(8, 6))
plt.bar(energy_data_estimate.keys(), energy_data_estimate.values(), color=['blue', 'red'])
plt.ylabel('Energy (kWh)')
plt.title('Estimated Energy Distribution During Sudden Braking Events')
plt.show()
