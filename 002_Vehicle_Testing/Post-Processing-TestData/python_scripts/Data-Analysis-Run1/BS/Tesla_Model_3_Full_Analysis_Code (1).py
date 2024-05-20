
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
