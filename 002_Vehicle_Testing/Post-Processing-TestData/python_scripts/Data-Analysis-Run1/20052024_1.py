# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:18:09 2024

@author: Soumya Ranjan Sabat
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the Excel file
file_path = r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run1\Run1_FilterData.xlsx'

# Save Directory for plots
save_dir = r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run1\Plots\20052024_1'

# Read the 'Data' sheet
data_sheet = pd.read_excel(file_path, sheet_name='Data')

# Cleaning the data: remove the row with units and convert all data to numeric types
data_cleaned = data_sheet.iloc[1:].copy()
data_cleaned = data_cleaned.apply(pd.to_numeric, errors='coerce')

## Statistical Summary & Visualisation - Overall

# Extracting key parameters for statistical summary and visualization
key_parameters = [
    'BattBeginningOfLifeEnergy292', 'BattBrickVoltageMax332', 'BattBrickVoltageMin332', 
    'BattVoltage132', 'BMS_kwhDriveDischargeTotal', 'WheelSpeedFL175', 'WheelSpeedFR175', 
    'WheelSpeedRL175', 'WheelSpeedRR175', 'UI_SOC', 'UI_idealRange', 'UI_Range'
]

# Statistical summary of key parameters
statistical_summary = data_cleaned[key_parameters].describe()
# print(statistical_summary)

# Creating time-series plots for battery voltages, state of charge, and wheel speeds
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 18))
fig.tight_layout(pad=5.0)

# Plot 1: Battery Voltage Over Time
axes[0].plot(data_cleaned['Time (relative)'], data_cleaned['BattBrickVoltageMax332'], label='Max Brick Voltage', color='blue')
axes[0].plot(data_cleaned['Time (relative)'], data_cleaned['BattBrickVoltageMin332'], label='Min Brick Voltage', color='red')
axes[0].set_title('Battery Brick Voltages Over Time')
axes[0].set_xlabel('Time (sec)')
axes[0].set_ylabel('Voltage (V)')
axes[0].legend()

# Plot 2: State of Charge Over Time
axes[1].plot(data_cleaned['Time (relative)'], data_cleaned['UI_SOC'], color='green')
axes[1].set_title('State of Charge Over Time')
axes[1].set_xlabel('Time (sec)')
axes[1].set_ylabel('State of Charge (%)')

# Plot 3: Wheel Speeds Over Time
axes[2].plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedFL175'], label='Front Left', color='purple')
axes[2].plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedFR175'], label='Front Right', color='magenta')
axes[2].plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedRL175'], label='Rear Left', color='orange')
axes[2].plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedRR175'], label='Rear Right', color='brown')
axes[2].set_title('Wheel Speeds Over Time')
axes[2].set_xlabel('Time (sec)')
axes[2].set_ylabel('Speed (km/h)')
axes[2].legend()

plt.savefig(save_dir + r'\StatisticalTimeSeriesSummary.png')
# Show the plots
plt.show()


## Setting up the figure for three individual plots & no subplots

# Plotting Battery Voltage Over Time
plt.figure(figsize=(10, 6))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['BattBrickVoltageMax332'], label='Max Brick Voltage', color='blue')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['BattBrickVoltageMin332'], label='Min Brick Voltage', color='red')
plt.title('Battery Brick Voltages Over Time')
plt.xlabel('Time (sec)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.savefig(save_dir + r'\BatteryBrickVoltagesOverTime.png')
plt.show()

# Plotting State of Charge Over Time
plt.figure(figsize=(10, 6))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['UI_SOC'], color='green')
plt.title('State of Charge Over Time')
plt.xlabel('Time (sec)')
plt.ylabel('State of Charge (%)')
plt.savefig(save_dir + r'\StateofChargeOverTime.png')
plt.show()

# Plotting Wheel Speeds Over Time
plt.figure(figsize=(10, 6))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedFL175'], label='Front Left', color='purple')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedFR175'], label='Front Right', color='magenta')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedRL175'], label='Rear Left', color='orange')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedRR175'], label='Rear Right', color='brown')
plt.title('Wheel Speeds Over Time')
plt.xlabel('Time (sec)')
plt.ylabel('Speed (km/h)')
plt.legend()
plt.savefig(save_dir + r'\WheelSpeedsOverTime_2.png')
plt.show()

# Vehicle Testing Data Analysis

# Calculate average wheel speed for further analysis
data_cleaned['WheelSpeedAverage'] = data_cleaned[['WheelSpeedFL175', 'WheelSpeedFR175', 'WheelSpeedRL175', 'WheelSpeedRR175']].mean(axis=1)

## 1. Battery Voltage Stability vs. Wheel Speed
plt.figure(figsize=(10, 6))
sns.scatterplot(x='WheelSpeedAverage', y='BattVoltage132', data=data_cleaned, hue='BattVoltage132', palette='viridis')
plt.title('Battery Voltage Stability vs. Wheel Speed')
plt.xlabel('Average Wheel Speed (km/h)')
plt.ylabel('Battery Voltage (V)')
plt.savefig(save_dir + r'\BatteryVoltageStabilityVsWheelSpeed.png')
plt.show()

## 2. Energy Efficiency Analysis
# Calculate distance traveled assuming each entry is 1 second apart
data_cleaned['DistanceTraveled'] = data_cleaned['WheelSpeedAverage'] * (data_cleaned['Time (relative)'].diff().fillna(1) / 3600)  # in km
data_cleaned['CumulativeDistance'] = data_cleaned['DistanceTraveled'].cumsum()
data_cleaned['EnergyEfficiency'] = data_cleaned['BMS_kwhDriveDischargeTotal'] / data_cleaned['CumulativeDistance']  # kWh per km

plt.figure(figsize=(10, 6))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['EnergyEfficiency'])
plt.title('Energy Efficiency Over Time')
plt.xlabel('Time (sec)')
plt.ylabel('Energy Efficiency (kWh/km)')
plt.savefig(save_dir + r'\EnergyEfficiencyOverTime.png')
plt.show()

## 3. Battery Discharge Rate Analysis
data_cleaned['DischargeRate'] = data_cleaned['BMS_kwhDriveDischargeTotal'].diff().fillna(0) / data_cleaned['Time (relative)'].diff().fillna(1)

plt.figure(figsize=(10, 6))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['DischargeRate'])
plt.title('Battery Discharge Rate Over Time')
plt.xlabel('Time (sec)')
plt.ylabel('Discharge Rate (kWh/sec)')
plt.savefig(save_dir + r'\BatteryDischargeRateOverTime.png')
plt.show()

## 4. Correlation Between State of Charge and Battery Voltage
plt.figure(figsize=(10, 6))
sns.scatterplot(x='BattVoltage132', y='UI_SOC', data=data_cleaned)
plt.title('Correlation Between State of Charge and Battery Voltage')
plt.xlabel('Battery Voltage (V)')
plt.ylabel('State of Charge (%)')
plt.savefig(save_dir + r'\CorrelationBetweenStateofChargeandBatteryVoltage.png')
plt.show()

## 5. Anomaly Detection in Wheel Speeds
plt.figure(figsize=(10, 6))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedFL175'], label='Front Left')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedFR175'], label='Front Right')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedRL175'], label='Rear Left')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedRR175'], label='Rear Right')
plt.title('Wheel Speeds Over Time')
plt.xlabel('Time (sec)')
plt.ylabel('Speed (km/h)')
plt.legend()
plt.savefig(save_dir + r'\WheelSpeedsOverTime_Anomaly.png')
plt.show()

# Motor Performance During Braking Analysis

# Identifying braking events
braking_events = data_cleaned[(data_cleaned['IBST_driverBrakeApply'] > 0) & (data_cleaned['DI_accelPedalPos'] <= 0.1)]

# Extract relevant motor performance parameters
motor_performance = braking_events[['Time (relative)', 'FrontMotorCurrent1A5', 'RearMotorCurrent126', 
                                    'FrontTorque1D5', 'RearTorque1D8', 'FrontPower2E5', 'RearPower266']]

# Calculate the difference to highlight changes
motor_performance_diff = motor_performance.diff().fillna(0)

## 1. Motor Currents During Braking
# Plotting Motor Currents During Braking
plt.figure(figsize=(14, 8))
plt.plot(motor_performance['Time (relative)'], motor_performance['FrontMotorCurrent1A5'], label='Front Motor Current')
plt.plot(motor_performance['Time (relative)'], motor_performance['RearMotorCurrent126'], label='Rear Motor Current')
plt.title('Motor Currents During Braking Events')
plt.xlabel('Time (relative)')
plt.ylabel('Current (A)')
plt.legend()
plt.savefig(save_dir + r'\MotorCurrentsDuringBrakingEvents.png')
plt.show()

## 2. Motor Torques During Braking
# Plotting Motor Torques During Braking
plt.figure(figsize=(14, 8))
plt.plot(motor_performance['Time (relative)'], motor_performance['FrontTorque1D5'], label='Front Torque')
plt.plot(motor_performance['Time (relative)'], motor_performance['RearTorque1D8'], label='Rear Torque')
plt.title('Motor Torques During Braking Events')
plt.xlabel('Time (relative)')
plt.ylabel('Torque (Nm)')
plt.legend()
plt.savefig(save_dir + r'\MotorTorquesDuringBrakingEvents.png')
plt.show()

## 3. Motor Power During Braking
# Plotting Motor Power During Braking
plt.figure(figsize=(14, 8))
plt.plot(motor_performance['Time (relative)'], motor_performance['FrontPower2E5'], label='Front Power')
plt.plot(motor_performance['Time (relative)'], motor_performance['RearPower266'], label='Rear Power')
plt.title('Motor Power During Braking Events')
plt.xlabel('Time (relative)')
plt.ylabel('Power (kW)')
plt.legend()
plt.savefig(save_dir + r'\MotorPowerDuringBrakingEvents.png')
plt.show()

## 4. Motor Efficiencies Over Time
# Calculate Input Power for Front and Rear Motors
data_cleaned['FrontInputPower'] = data_cleaned['FrontHighVoltage1A5'] * data_cleaned['FrontMotorCurrent1A5']
data_cleaned['RearInputPower'] = data_cleaned['RearHighVoltage126'] * data_cleaned['RearMotorCurrent126']

# Calculate Efficiency for Front and Rear Motors
data_cleaned['FrontEfficiency'] = (data_cleaned['FrontPower2E5'] / data_cleaned['FrontInputPower']) * 100
data_cleaned['RearEfficiency'] = (data_cleaned['RearPower266'] / data_cleaned['RearInputPower']) * 100

# Clean up potential infinite values (e.g., divide by zero cases)
data_cleaned.replace([np.inf, -np.inf], np.nan, inplace=True)
data_cleaned.dropna(subset=['FrontEfficiency', 'RearEfficiency'], inplace=True)

# Plotting Motor Efficiencies
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['FrontEfficiency'], label='Front Motor Efficiency', color='blue')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RearEfficiency'], label='Rear Motor Efficiency', color='red')
plt.title('Motor Efficiencies Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Efficiency (%)')
plt.legend()
plt.savefig(save_dir + r'\MotorEfficienciesOverTime.png')
plt.show()

# Statistical Summary
front_eff_summary = data_cleaned['FrontEfficiency'].describe()
rear_eff_summary = data_cleaned['RearEfficiency'].describe()

print(front_eff_summary, rear_eff_summary)


## 5. Front and Rear Motor Efficiency & Mechanical Output Over Time
# Extract relevant columns for motor efficiency analysis
motor_efficiency_data = data_cleaned[
    [
        'Time (relative)', 'FrontTorque1D5', 'RearTorque1D8', 'FrontPower2E5',
        'RearPower266', 'FrontMotorCurrent1A5', 'RearMotorCurrent126', 
        'FrontHighVoltage1A5', 'RearHighVoltage126', 'DIF_torqueActual', 
        'DIR_torqueActual', 'DIF_axleSpeed', 'DIR_axleSpeed'
    ]
].copy()

# Calculate mechanical power output for front and rear motors
motor_efficiency_data['FrontMechanicalPower'] = motor_efficiency_data['FrontTorque1D5'] * motor_efficiency_data['DIF_axleSpeed'] * (2 * 3.14159 / 60) / 1000  # kW
motor_efficiency_data['RearMechanicalPower'] = motor_efficiency_data['RearTorque1D8'] * motor_efficiency_data['DIR_axleSpeed'] * (2 * 3.14159 / 60) / 1000  # kW

# Calculate motor efficiency for front and rear motors
motor_efficiency_data['FrontMotorEfficiency'] = motor_efficiency_data['FrontMechanicalPower'] / motor_efficiency_data['FrontPower2E5']
motor_efficiency_data['RearMotorEfficiency'] = motor_efficiency_data['RearMechanicalPower'] / motor_efficiency_data['RearPower266']

# Plotting the data for motor efficiency, mechanical output, and electrical input
plt.figure(figsize=(14, 12))

# Front Motor Efficiency
plt.subplot(3, 1, 1)
plt.plot(motor_efficiency_data['Time (relative)'], motor_efficiency_data['FrontMotorEfficiency'], label='Front Motor Efficiency', color='blue')
plt.ylabel('Efficiency')
plt.title('Front Motor Efficiency Over Time')
plt.grid(True)

# Rear Motor Efficiency
plt.subplot(3, 1, 2)
plt.plot(motor_efficiency_data['Time (relative)'], motor_efficiency_data['RearMotorEfficiency'], label='Rear Motor Efficiency', color='red')
plt.ylabel('Efficiency')
plt.title('Rear Motor Efficiency Over Time')
plt.grid(True)

# Mechanical Power Output
plt.subplot(3, 1, 3)
plt.plot(motor_efficiency_data['Time (relative)'], motor_efficiency_data['FrontMechanicalPower'], label='Front Mechanical Power', color='blue')
plt.plot(motor_efficiency_data['Time (relative)'], motor_efficiency_data['RearMechanicalPower'], label='Rear Mechanical Power', color='red')
plt.ylabel('Mechanical Power (kW)')
plt.xlabel('Time (s)')
plt.title('Mechanical Power Output Over Time')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig(save_dir + r'\FMeff_RMeff_MechPowOp.png')
plt.show()


# Regenerative Braking Analysis

# Calculate Regenerated Energy and Total Energy Used
data_cleaned['RegeneratedEnergy'] = data_cleaned['BMS_kwhRegenChargeTotal'].diff().fillna(0)
data_cleaned['TotalEnergyUsed'] = data_cleaned['BMS_kwhDriveDischargeTotal'].diff().fillna(0)

# Avoid division by zero by filtering out zero or near-zero total energy used values
valid_energy_used = data_cleaned['TotalEnergyUsed'] > 0

# Calculate Regenerative Efficiency for valid values only
data_cleaned['RegenerativeEfficiency'] = np.where(
    valid_energy_used,
    (data_cleaned['RegeneratedEnergy'] / data_cleaned['TotalEnergyUsed']) * 100,
    np.nan)

# Clean up potential infinite values and drop NaNs for visualization
data_cleaned.replace([np.inf, -np.inf], np.nan, inplace=True)
data_cleaned.dropna(subset=['RegenerativeEfficiency'], inplace=True)

## 1. Regenerative Efficiency Calculation
# Plotting Regenerative Efficiency
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RegenerativeEfficiency'], label='Regenerative Efficiency', color='green')
plt.title('Regenerative Efficiency Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Efficiency (%)')
plt.legend()
plt.savefig(save_dir + r'\RegenerativeEfficiencyOverTime.png')
plt.show()

## 2. Impact on Battery State of Charge (SOC)
# Plotting SOC Over Time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['UI_SOC'], label='State of Charge (SOC)', color='blue')
plt.title('Impact of Regenerative Braking on Battery SOC')
plt.xlabel('Time (relative)')
plt.ylabel('SOC (%)')
plt.legend()
plt.savefig(save_dir + r'\ImpactofRegenerativeBrakingonBatterySOC.png')
plt.show()

## 3. Dynamic Braking Strategy
# Plotting Front and Rear Braking Power During Braking Events
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['FrontPower2E5'], label='Front Power During Braking', color='blue')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RearPower266'], label='Rear Power During Braking', color='red')
plt.title('Dynamic Braking Strategy: Front and Rear Power Distribution')
plt.xlabel('Time (relative)')
plt.ylabel('Power (kW)')
plt.legend()
plt.savefig(save_dir + r'\DynamicBrakingStrategyFrontRearPowerDistribution.png')
plt.show()

## 4. Energy Recovered During Braking Events
# Total Energy Recovered During Braking Events
total_energy_recovered = data_cleaned['RegeneratedEnergy'].sum()

# Plotting Energy Recovered During Braking Events
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RegeneratedEnergy'].cumsum(), label='Cumulative Energy Recovered', color='purple')
plt.title('Cumulative Energy Recovered During Braking Events')
plt.xlabel('Time (relative)')
plt.ylabel('Energy Recovered (kWh)')
plt.legend()
plt.savefig(save_dir + r'\CumulativeEnergyRecoveredDuringBrakingEvents.png')
plt.show()

print(total_energy_recovered)


# Energy Related Study

# Threshold for considering acceleration (adjust based on data characteristics)
acceleration_threshold = 0.1

# Identify acceleration events
acceleration_events = data_cleaned[data_cleaned['DI_accelPedalPos'] > acceleration_threshold]

# Calculate Energy Consumption During Acceleration
acceleration_events['EnergyConsumed'] = acceleration_events['BMS_kwhDriveDischargeTotal'].diff().fillna(0)

## 1. Energy Consumption During Acceleration
# Plotting Energy Consumption During Acceleration
plt.figure(figsize=(14, 8))
plt.plot(acceleration_events['Time (relative)'], acceleration_events['EnergyConsumed'], label='Energy Consumed During Acceleration', color='orange')
plt.title('Energy Consumption During Acceleration')
plt.xlabel('Time (relative)')
plt.ylabel('Energy Consumed (kWh)')
plt.legend()
plt.savefig(save_dir + r'\EnergyConsumptionDuringAcceleration.png')
plt.show()

## 2. Energy Efficiency During Acceleration
# Assume a constant vehicle mass (kg) for kinetic energy calculation
vehicle_mass = 1610  # Example mass for Tesla Model 3

# Identify acceleration events
acceleration_events = data_cleaned[data_cleaned['DI_accelPedalPos'] > 0.1]

# Calculate Energy Input During Acceleration
acceleration_events['EnergyInput'] = acceleration_events['BMS_kwhDriveDischargeTotal'].diff().fillna(0) * 3600  # Convert kWh to Wh

# Calculate Kinetic Energy Gain
acceleration_events['Velocity'] = acceleration_events['DI_vehicleSpeed'] / 3.6  # Convert km/h to m/s
acceleration_events['KineticEnergy'] = 0.5 * vehicle_mass * acceleration_events['Velocity'] ** 2
acceleration_events['KineticEnergyGain'] = acceleration_events['KineticEnergy'].diff().fillna(0)

# Calculate Energy Efficiency During Acceleration
acceleration_events['EnergyEfficiency'] = (acceleration_events['KineticEnergyGain'] / acceleration_events['EnergyInput']) * 100

# Clean up potential infinite values and drop NaNs for visualization
acceleration_events.replace([np.inf, -np.inf], np.nan, inplace=True)
acceleration_events.dropna(subset=['EnergyEfficiency'], inplace=True)

## 2. Energy Efficiency During Acceleration
# Plotting Energy Efficiency During Acceleration
plt.figure(figsize=(14, 8))
plt.plot(acceleration_events['Time (relative)'], acceleration_events['EnergyEfficiency'], label='Energy Efficiency During Acceleration', color='orange')
plt.title('Energy Efficiency During Acceleration')
plt.xlabel('Time (relative)')
plt.ylabel('Efficiency (%)')
plt.legend()
plt.savefig(save_dir + r'\EnergyEfficiencyDuringAcceleration.png')
plt.show()

## 3. Correlation Between Energy Consumption and Speed
# Calculate the change in energy consumed
data_cleaned['EnergyConsumed'] = data_cleaned['BMS_kwhDriveDischargeTotal'].diff().fillna(0) * 3600  # Convert kWh to Wh

# Convert speed from km/h to m/s for a more accurate analysis
data_cleaned['Speed_mps'] = data_cleaned['DI_vehicleSpeed'] / 3.6

# Calculate the correlation between energy consumed and speed
correlation = data_cleaned[['EnergyConsumed', 'Speed_mps']].corr().iloc[0, 1]

## 3. Correlation Between Energy Consumption and Speed
# Scatter Plot of Energy Consumption vs. Speed
plt.figure(figsize=(14, 8))
plt.scatter(data_cleaned['Speed_mps'], data_cleaned['EnergyConsumed'], alpha=0.5, label='Energy vs. Speed', color='purple')
plt.title('Energy Consumption vs. Speed')
plt.xlabel('Speed (m/s)')
plt.ylabel('Energy Consumed (Wh)')
plt.legend()
plt.savefig(save_dir + r'\EnergyConsumptionVsSpeed.png')
plt.show()

## 3. Correlation Between Energy Consumption and Speed
# Line Plot of Energy Consumption and Speed over Time
fig, ax1 = plt.subplots(figsize=(14, 8))

color = 'tab:red'
ax1.set_xlabel('Time (relative)')
ax1.set_ylabel('Energy Consumed (Wh)', color=color)
ax1.plot(data_cleaned['Time (relative)'], data_cleaned['EnergyConsumed'], color=color, label='Energy Consumed')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Speed (m/s)', color=color)
ax2.plot(data_cleaned['Time (relative)'], data_cleaned['Speed_mps'], color=color, label='Speed')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Energy Consumption and Speed over Time')
fig.legend(loc='upper right', bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
plt.savefig(save_dir + r'\EnergyConsumptionAndSpeedOverTime.png')
plt.show()


# Powertrain Performance During Acceleration

# Threshold for considering acceleration (adjust based on data characteristics)
acceleration_threshold = 0.1

# Identify acceleration events
acceleration_events = data_cleaned[data_cleaned['DI_accelPedalPos'] > acceleration_threshold]

# Extract relevant parameters during acceleration events
powertrain_performance = acceleration_events[['Time (relative)', 'FrontMotorCurrent1A5', 'RearMotorCurrent126',
                                              'FrontTorque1D5', 'RearTorque1D8', 'FrontPower2E5', 'RearPower266']]

## 1. Motor Currents During Acceleration

# Plotting Front and Rear Motor Currents During Acceleration
plt.figure(figsize=(14, 8))
plt.plot(powertrain_performance['Time (relative)'], powertrain_performance['FrontMotorCurrent1A5'], label='Front Motor Current', color='blue')
plt.plot(powertrain_performance['Time (relative)'], powertrain_performance['RearMotorCurrent126'], label='Rear Motor Current', color='red')
plt.title('Motor Currents During Acceleration')
plt.xlabel('Time (relative)')
plt.ylabel('Current (A)')
plt.legend()
plt.savefig(save_dir + r'\MotorCurrentsDuringAcceleration.png')
plt.show()

## 2. Motor Torques During Acceleration
# Plotting Front and Rear Motor Torques During Acceleration
plt.figure(figsize=(14, 8))
plt.plot(powertrain_performance['Time (relative)'], powertrain_performance['FrontTorque1D5'], label='Front Torque', color='blue')
plt.plot(powertrain_performance['Time (relative)'], powertrain_performance['RearTorque1D8'], label='Rear Torque', color='red')
plt.title('Motor Torques During Acceleration')
plt.xlabel('Time (relative)')
plt.ylabel('Torque (Nm)')
plt.legend()
plt.savefig(save_dir + r'\MotorTorquesDuringAcceleration.png')
plt.show()

## 3. Motor Power Outputs During Acceleration
# Plotting Front and Rear Motor Power Outputs During Acceleration
plt.figure(figsize=(14, 8))
plt.plot(powertrain_performance['Time (relative)'], powertrain_performance['FrontPower2E5'], label='Front Power', color='blue')
plt.plot(powertrain_performance['Time (relative)'], powertrain_performance['RearPower266'], label='Rear Power', color='red')
plt.title('Motor Power Outputs During Acceleration')
plt.xlabel('Time (relative)')
plt.ylabel('Power (kW)')
plt.legend()
plt.savefig(save_dir + r'\MotorPowerOutputsDuringAcceleration.png')
plt.show()

## 4. Average Energy Efficiency at Various Speeds
# Calculate the change in energy consumed
data_cleaned['EnergyConsumed'] = data_cleaned['BMS_kwhDriveDischargeTotal'].diff().fillna(0) * 3600  # Convert kWh to Wh

# Convert speed from km/h to m/s for a more accurate analysis
data_cleaned['Speed_mps'] = data_cleaned['DI_vehicleSpeed'] / 3.6

# Calculate distance traveled during each time step assuming 1-second intervals
data_cleaned['DistanceTraveled'] = data_cleaned['Speed_mps']

# Calculate energy efficiency as distance traveled per unit energy consumed
data_cleaned['EnergyEfficiency'] = (data_cleaned['DistanceTraveled'] / data_cleaned['EnergyConsumed']) * 100

# Define speed bins (e.g., 0-10 m/s, 10-20 m/s, etc.)
speed_bins = np.arange(0, data_cleaned['Speed_mps'].max() + 5, 5)
data_cleaned['SpeedBin'] = pd.cut(data_cleaned['Speed_mps'], bins=speed_bins)

# Calculate average energy efficiency for each speed bin
average_efficiency_per_bin = data_cleaned.groupby('SpeedBin')['EnergyEfficiency'].mean().reset_index()

## 4. Average Energy Efficiency at Various Speeds
# Plotting Average Energy Efficiency for Each Speed Bin
plt.figure(figsize=(14, 8))
plt.bar(average_efficiency_per_bin['SpeedBin'].astype(str), average_efficiency_per_bin['EnergyEfficiency'], color='blue')
plt.title('Average Energy Efficiency at Various Speeds')
plt.xlabel('Speed Bin (m/s)')
plt.ylabel('Energy Efficiency (%)')
plt.xticks(rotation=45)
plt.savefig(save_dir + r'\AverageEnergyEfficiencyatVariousSpeeds.png')
plt.show()


# Dynamic Braking Across Different Speeds and Its Efficiency

# Identify braking events
braking_events = data_cleaned[(data_cleaned['IBST_driverBrakeApply'] > 0) & (data_cleaned['DI_accelPedalPos'] <= 0.1)]

# Extract relevant parameters during braking events
braking_performance = braking_events[['Time (relative)', 'Speed_mps', 'FrontMotorCurrent1A5', 'RearMotorCurrent126',
                                      'FrontTorque1D5', 'RearTorque1D8', 'FrontPower2E5', 'RearPower266', 'BMS_kwhDriveDischargeTotal', 'BMS_kwhRegenChargeTotal' ]]

# Calculate Regenerated Energy and Total Energy Used during braking events
braking_performance['RegeneratedEnergy'] = braking_performance['BMS_kwhRegenChargeTotal'].diff().fillna(0)
braking_performance['TotalEnergyUsed'] = braking_performance['BMS_kwhDriveDischargeTotal'].diff().fillna(0)

# Avoid division by zero by filtering out zero or near-zero total energy used values
valid_energy_used = braking_performance['TotalEnergyUsed'] > 0

# Calculate Regenerative Efficiency for valid values only
braking_performance['RegenerativeEfficiency'] = np.where(
    valid_energy_used,
    (braking_performance['RegeneratedEnergy'] / braking_performance['TotalEnergyUsed']) * 100,
    np.nan)

# Clean up potential infinite values and drop NaNs for visualization
braking_performance.replace([np.inf, -np.inf], np.nan, inplace=True)
braking_performance.dropna(subset=['RegenerativeEfficiency'], inplace=True)

# Define speed bins (e.g., 0-10 m/s, 10-20 m/s, etc.)
speed_bins = np.arange(0, braking_performance['Speed_mps'].max() + 5, 5)
braking_performance['SpeedBin'] = pd.cut(braking_performance['Speed_mps'], bins=speed_bins)

# Calculate average regenerative efficiency for each speed bin
average_efficiency_per_bin = braking_performance.groupby('SpeedBin')['RegenerativeEfficiency'].mean().reset_index()

## 1. Average Regenerative Efficiency at Various Speeds
# Plotting Average Regenerative Efficiency for Each Speed Bin
plt.figure(figsize=(14, 8))
plt.bar(average_efficiency_per_bin['SpeedBin'].astype(str), average_efficiency_per_bin['RegenerativeEfficiency'], color='blue')
plt.title('Average Regenerative Efficiency at Various Speeds')
plt.xlabel('Speed Bin (m/s)')
plt.ylabel('Regenerative Efficiency (%)')
plt.xticks(rotation=45)
plt.savefig(save_dir + r'\AverageRegenerativeEfficiencyatVariousSpeeds.png')
plt.show()


# # Plotting Dynamic Braking Behavior: Front and Rear Motor Currents During Braking Events
# plt.figure(figsize=(14, 8))
# plt.plot(braking_performance['Time (relative)'], braking_performance['FrontMotorCurrent1A5'], label='Front Motor Current', color='blue')
# plt.plot(braking_performance['Time (relative)'], braking_performance['RearMotorCurrent126'], label='Rear Motor Current', color='red')
# plt.title('Motor Currents During Braking')
# plt.xlabel('Time (relative)')
# plt.ylabel('Current (A)')
# plt.legend()
# plt.show()

# # Plotting Dynamic Braking Behavior: Front and Rear Motor Torques During Braking Events
# plt.figure(figsize=(14, 8))
# plt.plot(braking_performance['Time (relative)'], braking_performance['FrontTorque1D5'], label='Front Torque', color='blue')
# plt.plot(braking_performance['Time (relative)'], braking_performance['RearTorque1D8'], label='Rear Torque', color='red')
# plt.title('Motor Torques During Braking')
# plt.xlabel('Time (relative)')
# plt.ylabel('Torque (Nm)')
# plt.legend()
# plt.show()

# # Plotting Dynamic Braking Behavior: Front and Rear Motor Power Outputs During Braking Events
# plt.figure(figsize=(14, 8))
# plt.plot(braking_performance['Time (relative)'], braking_performance['FrontPower2E5'], label='Front Power', color='blue')
# plt.plot(braking_performance['Time (relative)'], braking_performance['RearPower266'], label='Rear Power', color='red')
# plt.title('Motor Power Outputs During Braking')
# plt.xlabel('Time (relative)')
# plt.ylabel('Power (kW)')
# plt.legend()
# plt.show()



# Regenerative Braking
## 1. Correlation Analysis of Relevant Parameters for Regen. Braking

# Select relevant parameters for regenerative braking
relevant_parameters = [
    'IBST_driverBrakeApply', 'DI_accelPedalPos', 'FrontMotorCurrent1A5', 'RearMotorCurrent126',
    'FrontTorque1D5', 'RearTorque1D8', 'FrontPower2E5', 'RearPower266',
    'BMS_kwhRegenChargeTotal', 'BMS_kwhDriveDischargeTotal', 'UI_SOC', 'DI_vehicleSpeed'
]

# Extract the relevant parameters
regenerative_braking_data = data_cleaned[relevant_parameters]

# Calculate the correlation matrix
correlation_matrix = regenerative_braking_data.corr()

# Plotting the correlation heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Relevant Parameters for Regenerative Braking')
plt.savefig(save_dir + r'\CorrelationRegenerativeBraking.png')
plt.show()


## 2. Correlation Analysis of Relevant Parameters for Regen. Braking [Split-Up Graphs]

# Select parameters for Driver Inputs and Vehicle Dynamics
driver_vehicle_params = [
    'IBST_driverBrakeApply', 'DI_accelPedalPos', 'DI_vehicleSpeed'
]

# Extract the relevant parameters
driver_vehicle_data = data_cleaned[driver_vehicle_params]

# Calculate the correlation matrix
correlation_matrix_driver_vehicle = driver_vehicle_data.corr()

### Part 1: Driver Inputs and Vehicle Dynamics
# Plotting the correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix_driver_vehicle, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap: Driver Inputs and Vehicle Dynamics')
plt.savefig(save_dir + r'\CorrelationDriverInputsVehicleDynamics.png')
plt.show()

# Select parameters for Motor and Powertrain
motor_powertrain_params = [
    'FrontMotorCurrent1A5', 'RearMotorCurrent126',
    'FrontTorque1D5', 'RearTorque1D8', 'FrontPower2E5', 'RearPower266'
]

# Extract the relevant parameters
motor_powertrain_data = data_cleaned[motor_powertrain_params]

# Calculate the correlation matrix
correlation_matrix_motor_powertrain = motor_powertrain_data.corr()

### Part 2: Motor and Powertrain Parameters
# Plotting the correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix_motor_powertrain, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap: Motor and Powertrain Parameters')
plt.savefig(save_dir + r'\CorrelationMotorPowertrainParameters.png')
plt.show()

# Select parameters for Battery and Energy
battery_energy_params = [
    'BMS_kwhRegenChargeTotal', 'BMS_kwhDriveDischargeTotal', 'UI_SOC'
]

# Extract the relevant parameters
battery_energy_data = data_cleaned[battery_energy_params]

# Calculate the correlation matrix
correlation_matrix_battery_energy = battery_energy_data.corr()

### Part 3: Battery and Energy Parameters
# Plotting the correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix_battery_energy, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap: Battery and Energy Parameters')
plt.savefig(save_dir + r'\CorrelationBatteryEnergyParameters.png')
plt.show()


## 3. Front vs Rear Motor - Who generates more regen power?
# Plotting the front and rear motor torques, focusing on regenerative braking phases
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['FrontTorque1D5'], label='Front Motor Torque', color='blue', alpha=0.8)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RearTorque1D8'], label='Rear Motor Torque', color='red', alpha=0.8)

plt.xlabel('Time (s)')
plt.ylabel('Torque (Nm)')
plt.title('Front and Rear Motor Torque During Regenerative Braking')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.savefig(save_dir + r'\FrontRearMotorTorqueDuringRegenerativeBraking.png')
plt.show()

front_regen_torque = data_cleaned['FrontTorque1D5'][data_cleaned['FrontTorque1D5'] < 0].sum()
rear_regen_torque = data_cleaned['RearTorque1D8'][data_cleaned['RearTorque1D8'] < 0].sum()
#print(front_regen_torque, rear_regen_torque)

## 4. Booster Brake Pedal Force and Regenerative Charge Over Time
# Extract relevant columns for analysis
relevant_data_braking = data_cleaned[
    [
        'Time (relative)', 'ESP_brakeTorqueFrL', 'ESP_brakeTorqueFrR',
        'ESP_brakeTorqueReL', 'ESP_brakeTorqueReR', 'FrontTorque1D5',
        'RearTorque1D8', 'WheelSpeedFL175', 'WheelSpeedFR175',
        'WheelSpeedRL175', 'WheelSpeedRR175', 'BMS_kwhRegenChargeTotal'
    ]
].copy()

# Detect sudden braking events by finding high brake torque values
brake_threshold = 100  # Example threshold for detecting sudden braking
sudden_braking_events = (relevant_data_braking[['ESP_brakeTorqueFrL', 'ESP_brakeTorqueFrR', 'ESP_brakeTorqueReL', 'ESP_brakeTorqueReR']] > brake_threshold).any(axis=1)

# Detect vehicle instability by finding rapid changes in wheel speeds
speed_diff_threshold = 5  # Example threshold for detecting rapid speed changes
wheel_speed_diff = relevant_data_braking[['WheelSpeedFL175', 'WheelSpeedFR175', 'WheelSpeedRL175', 'WheelSpeedRR175']].diff().abs()
vehicle_instability_events = (wheel_speed_diff > speed_diff_threshold).any(axis=1)

# Combine both events
sudden_events = sudden_braking_events | vehicle_instability_events

# Filter data for these events
event_data = relevant_data_braking[sudden_events]

# Plotting the data during these events
plt.figure(figsize=(14, 8))
plt.plot(event_data['Time (relative)'], event_data['FrontTorque1D5'], label='Front Motor Torque', color='blue', alpha=0.8)
plt.plot(event_data['Time (relative)'], event_data['RearTorque1D8'], label='Rear Motor Torque', color='red', alpha=0.8)
plt.plot(event_data['Time (relative)'], event_data['BMS_kwhRegenChargeTotal'], label='Total Regen Charge (kWh)', color='black', alpha=0.8)

plt.xlabel('Time (s)')
plt.ylabel('Torque (Nm) / Energy (kWh)')
plt.title('Motor Torque and Regenerative Energy During Sudden Braking and Instability Events')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.savefig(save_dir + r'\MotorTorqueRegenerativeInstabilityEvents.png')
plt.show()

## 5. Acclerator Pedal Vs Brake Pedal for Regeneration
# Extract relevant columns for visualization
relevant_data_visualization = data_cleaned[
    [
        'Time (relative)', 'DI_accelPedalPos', 'IBST_driverBrakeApply',
        'DI_vehicleSpeed', 'BMS_kwhRegenChargeTotal'
    ]
].copy()

# Plotting the data for accelerator pedal position, booster brake, speed, and regeneration
plt.figure(figsize=(14, 8))

# Accelerator Pedal Position
plt.subplot(4, 1, 1)
plt.plot(relevant_data_visualization['Time (relative)'], relevant_data_visualization['DI_accelPedalPos'], label='Accelerator Pedal Position', color='blue')
plt.ylabel('Pedal Position (%)')
plt.title('Accelerator Pedal Position Over Time')
plt.grid(True)

# Booster Brake Pedal Force
plt.subplot(4, 1, 2)
plt.plot(relevant_data_visualization['Time (relative)'], relevant_data_visualization['IBST_driverBrakeApply'], label='Booster Brake Pedal Force', color='red')
plt.ylabel('Brake Pedal Force (N)')
plt.title('Booster Brake Pedal Force Over Time')
plt.grid(True)

# Vehicle Speed
plt.subplot(4, 1, 3)
plt.plot(relevant_data_visualization['Time (relative)'], relevant_data_visualization['DI_vehicleSpeed'], label='Vehicle Speed', color='green')
plt.ylabel('Speed (km/h)')
plt.title('Vehicle Speed Over Time')
plt.grid(True)

# Regenerative Charge
plt.subplot(4, 1, 4)
plt.plot(relevant_data_visualization['Time (relative)'], relevant_data_visualization['BMS_kwhRegenChargeTotal'], label='Regenerative Charge', color='purple')
plt.xlabel('Time (s)')
plt.ylabel('Regen Charge (kWh)')
plt.title('Regenerative Charge Over Time')
plt.grid(True)

plt.tight_layout()
plt.savefig(save_dir + r'\CombinedPlot_1.png')
plt.show()


## 6. Motor Torque and Regenerative Energy During Sudden Braking and Instability Events
# Extract relevant columns for comparison
comparison_data = data_cleaned[
    [
        'Time (relative)', 'IBST_driverBrakeApply', 'BMS_kwhRegenChargeTotal'
    ]
].copy()

# Plotting the data for booster brake pedal force and regenerative charge
plt.figure(figsize=(14, 8))

# Booster Brake Pedal Force
plt.subplot(2, 1, 1)
plt.plot(comparison_data['Time (relative)'], comparison_data['IBST_driverBrakeApply'], label='Booster Brake Pedal', color='red')
plt.ylabel('Brake Pedal Force (N)')
plt.title('Booster Brake Pedal Force Over Time')
plt.grid(True)

# Regenerative Charge
plt.subplot(2, 1, 2)
plt.plot(comparison_data['Time (relative)'], comparison_data['BMS_kwhRegenChargeTotal'], label='Regenerative Charge', color='purple')
plt.xlabel('Time (s)')
plt.ylabel('Regen Charge (kWh)')
plt.title('Regenerative Charge Over Time')
plt.grid(True)

plt.tight_layout()
plt.savefig(save_dir + r'\CombinedPlot_2.png')
plt.show()

# Battery Parameters Analysis

# Calculate cumulative energy recovered
data_cleaned['CumulativeRegenEnergy'] = data_cleaned['BMS_kwhRegenChargeTotal'].cumsum()

## 1. Energy Recovered Over Time
# Plotting cumulative energy recovered over time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['CumulativeRegenEnergy'], label='Cumulative Energy Recovered', color='green')
plt.title('Cumulative Energy Recovered Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Cumulative Energy Recovered (kWh)')
plt.legend()
plt.savefig(save_dir + r'\CumulativeEnergyRecoveredOverTime.png')
plt.show()

## 2. State of Charge (SoC) Over Time
# Plotting SoC over time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['UI_SOC'], label='State of Charge (SoC)', color='blue')
plt.title('State of Charge (SoC) Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('SoC (%)')
plt.legend()
plt.savefig(save_dir + r'\SOCoverTime.png')
plt.show()

# Correlation between SoC and other parameters
soc_correlation = data_cleaned[['UI_SOC', 'FrontMotorCurrent1A5', 'RearMotorCurrent126',
                                    'FrontTorque1D5', 'RearTorque1D8', 'FrontPower2E5', 'RearPower266']].corr()

## 3. Battery Degradation Over Time
# Plotting SoC and Energy Discharged over time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['UI_SOC'], label='State of Charge (SoC)', color='blue')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['BMS_kwhDriveDischargeTotal'], label='Energy Discharged', color='red')
plt.title('State of Charge (SoC) and Energy Discharged Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Value')
plt.legend()
plt.savefig(save_dir + r'\SOC_EnergyDisspOverTime.png')
plt.show()

## 4. Correlation Between SoC and Motor Parameters
# Plotting SoC vs Motor Parameters
fig, ax = plt.subplots(3, 2, figsize=(14, 18))

ax[0, 0].scatter(data_cleaned['UI_SOC'], data_cleaned['FrontMotorCurrent1A5'], alpha=0.5, color='blue')
ax[0, 0].set_title('SoC vs Front Motor Current')
ax[0, 0].set_xlabel('State of Charge (SoC)')
ax[0, 0].set_ylabel('Front Motor Current (A)')

ax[0, 1].scatter(data_cleaned['UI_SOC'], data_cleaned['RearMotorCurrent126'], alpha=0.5, color='red')
ax[0, 1].set_title('SoC vs Rear Motor Current')
ax[0, 1].set_xlabel('State of Charge (SoC)')
ax[0, 1].set_ylabel('Rear Motor Current (A)')

ax[1, 0].scatter(data_cleaned['UI_SOC'], data_cleaned['FrontTorque1D5'], alpha=0.5, color='blue')
ax[1, 0].set_title('SoC vs Front Torque')
ax[1, 0].set_xlabel('State of Charge (SoC)')
ax[1, 0].set_ylabel('Front Torque (Nm)')

ax[1, 1].scatter(data_cleaned['UI_SOC'], data_cleaned['RearTorque1D8'], alpha=0.5, color='red')
ax[1, 1].set_title('SoC vs Rear Torque')
ax[1, 1].set_xlabel('State of Charge (SoC)')
ax[1, 1].set_ylabel('Rear Torque (Nm)')

ax[2, 0].scatter(data_cleaned['UI_SOC'], data_cleaned['FrontPower2E5'], alpha=0.5, color='blue')
ax[2, 0].set_title('SoC vs Front Power')
ax[2, 0].set_xlabel('State of Charge (SoC)')
ax[2, 0].set_ylabel('Front Power (kW)')

ax[2, 1].scatter(data_cleaned['UI_SOC'], data_cleaned['RearPower266'], alpha=0.5, color='red')
ax[2, 1].set_title('SoC vs Rear Power')
ax[2, 1].set_xlabel('State of Charge (SoC)')
ax[2, 1].set_ylabel('Rear Power (kW)')

plt.tight_layout()
plt.savefig(save_dir + r'\SOC_MotorParam.png')
plt.show()

## 5. Charge and Discharge Cycles Analysis
# Calculate charge and discharge cycles
data_cleaned['ChargeCycle'] = (data_cleaned['BMS_kwhRegenChargeTotal'].diff() > 0).cumsum()
data_cleaned['DischargeCycle'] = (data_cleaned['BMS_kwhDriveDischargeTotal'].diff() > 0).cumsum()

# Plotting charge and discharge cycles
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ChargeCycle'], label='Charge Cycles', color='green')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['DischargeCycle'], label='Discharge Cycles', color='red')
plt.title('Charge and Discharge Cycles Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Cycle Count')
plt.legend()
plt.savefig(save_dir + r'\ChargeDischargeCyclesOverTime.png')
plt.show()

# Plotting voltage and current against SoC
fig, ax = plt.subplots(2, 1, figsize=(14, 12))

ax[0].plot(data_cleaned['Time (relative)'], data_cleaned['BattVoltage132'], label='Battery Voltage', color='blue')
ax[0].set_title('Battery Voltage Over Time')
ax[0].set_xlabel('Time (relative)')
ax[0].set_ylabel('Voltage (V)')
ax[0].legend()

ax[1].plot(data_cleaned['Time (relative)'], data_cleaned['RawBattCurrent132'], label='Battery Current', color='red')
ax[1].set_title('Battery Current Over Time')
ax[1].set_xlabel('Time (relative)')
ax[1].set_ylabel('Current (A)')
ax[1].legend()

plt.tight_layout()
plt.savefig(save_dir + r'\CombinedPlot_3.png')
plt.show()

# Correlation between SoC and Voltage, Current
voltage_current_correlation = data_cleaned[['UI_SOC', 'BattVoltage132', 'RawBattCurrent132']].corr()
voltage_current_correlation

## 6. Energy Efficiency Analysis
# Calculate energy efficiency (Wh/km)
data_cleaned['EnergyEfficiency_Wh_km'] = (data_cleaned['EnergyConsumed'] / data_cleaned['DistanceTraveled']) * 1000

# Plotting energy efficiency over time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['EnergyEfficiency_Wh_km'], label='Energy Efficiency (Wh/km)', color='purple')
plt.title('Energy Efficiency Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Energy Efficiency (Wh/km)')
plt.legend()
plt.savefig(save_dir + r'\EnergyEfficiencyOverTime_2.png')
plt.show()

# Summary statistics for energy efficiency
energy_efficiency_summary = data_cleaned['EnergyEfficiency_Wh_km'].describe()
energy_efficiency_summary


## 7. Battery Voltage and Brick Voltage Analysis
# Plotting Battery Voltage and Brick Voltages over time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['BattVoltage132'], label='Battery Voltage', color='blue')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['BattBrickVoltageMax332'], label='Brick Voltage Max', color='orange')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['BattBrickVoltageMin332'], label='Brick Voltage Min', color='red')
plt.title('Battery Voltage and Brick Voltages Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.savefig(save_dir + r'\BattVoltBrickVoltoverTime.png')
plt.show()

# Correlation between Battery Voltage and Brick Voltages
battery_brick_voltage_correlation = data_cleaned[['BattVoltage132', 'BattBrickVoltageMax332', 'BattBrickVoltageMin332']].corr()
battery_brick_voltage_correlation

## 8. Smooth Battery Current vs. Raw Battery Current Analysis
# Smoothing raw battery current (e.g., using a rolling mean)
data_cleaned['SmoothBattCurrent'] = data_cleaned['RawBattCurrent132'].rolling(window=10).mean()

# Plotting Smooth Battery Current and Raw Battery Current over time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RawBattCurrent132'], label='Raw Battery Current', color='red', alpha=0.5)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['SmoothBattCurrent'], label='Smooth Battery Current', color='green')
plt.title('Raw Battery Current and Smooth Battery Current Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Current (A)')
plt.legend()
plt.savefig(save_dir + r'\RawSmoothBattCurrent.png')
plt.show()

# Correlation between Smooth Battery Current and Raw Battery Current
battery_current_correlation = data_cleaned[['RawBattCurrent132', 'SmoothBattCurrent']].corr()
battery_current_correlation


# Vehicle Stability Analysis

## 1. Brake Torque Analysis
# Plotting Brake Torques over time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrL'], label='Brake Torque Front Left', color='blue')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrR'], label='Brake Torque Front Right', color='orange')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReL'], label='Brake Torque Rear Left', color='green')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReR'], label='Brake Torque Rear Right', color='red')
plt.title('Brake Torques Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Torque (Nm)')
plt.legend()
plt.savefig(save_dir + r'\BrakeTorqueOverTime.png')
plt.show()

# Summary statistics for brake torques
brake_torque_stats = data_cleaned[['ESP_brakeTorqueFrL', 'ESP_brakeTorqueFrR', 'ESP_brakeTorqueReL', 'ESP_brakeTorqueReR']].describe()
brake_torque_stats

# Correlation between brake torques
brake_torque_correlation = data_cleaned[['ESP_brakeTorqueFrL', 'ESP_brakeTorqueFrR', 'ESP_brakeTorqueReL', 'ESP_brakeTorqueReR']].corr()
brake_torque_correlation

## 2. Yaw Rate and Vehicle Speed Analysis
# Plotting Yaw Rate and Steering Behavior over time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RCM_yawRate'], label='Yaw Rate', color='purple')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['DI_vehicleSpeed'], label='Vehicle Speed', color='brown')
plt.title('Yaw Rate and Vehicle Speed Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Value')
plt.legend()
plt.savefig(save_dir + r'\YawRateVehicleSpeedOverTime.png')
plt.show()

# Summary statistics for yaw rate and vehicle speed
yaw_speed_stats = data_cleaned[['RCM_yawRate', 'DI_vehicleSpeed']].describe()
yaw_speed_stats

# Correlation between yaw rate and vehicle speed
yaw_speed_correlation = data_cleaned[['RCM_yawRate', 'DI_vehicleSpeed']].corr()
yaw_speed_correlation

## 3. Energy Usage for Braking and Stability
# Calculating total brake energy used (simplified assumption: torque * wheel speed)
data_cleaned['BrakeEnergyFrontLeft'] = data_cleaned['ESP_brakeTorqueFrL'] * data_cleaned['WheelSpeedFL175']
data_cleaned['BrakeEnergyFrontRight'] = data_cleaned['ESP_brakeTorqueFrR'] * data_cleaned['WheelSpeedFR175']
data_cleaned['BrakeEnergyRearLeft'] = data_cleaned['ESP_brakeTorqueReL'] * data_cleaned['WheelSpeedRL175']
data_cleaned['BrakeEnergyRearRight'] = data_cleaned['ESP_brakeTorqueReR'] * data_cleaned['WheelSpeedRR175']
data_cleaned['TotalBrakeEnergy'] = data_cleaned[['BrakeEnergyFrontLeft', 'BrakeEnergyFrontRight', 'BrakeEnergyRearLeft', 'BrakeEnergyRearRight']].sum(axis=1)

# Plotting Total Brake Energy over time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['TotalBrakeEnergy'], label='Total Brake Energy', color='black')
plt.title('Total Brake Energy Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Energy')
plt.legend()
plt.savefig(save_dir + r'\TotalBrakeEnergyOverTime.png')
plt.show()

# Summary statistics for total brake energy
total_brake_energy_stats = data_cleaned['TotalBrakeEnergy'].describe()
total_brake_energy_stats

## 4. Energy Distribution Analysis
# Plotting Energy Distribution Over Time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['BMS_kwhRegenChargeTotal'], label='Regenerative Charge Total', color='green')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['BMS_kwhDriveDischargeTotal'], label='Drive Discharge Total', color='red')
plt.title('Energy Distribution Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Energy (kWh)')
plt.legend()
plt.savefig(save_dir + r'\EnergyDistributionOverTime.png')
plt.show()

## 5. Vehicle Dynamics Analysis
# Plotting Vehicle Dynamics Over Time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RCM_lateralAccel'], label='Lateral Acceleration', color='blue')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RCM_longitudinalAccel'], label='Longitudinal Acceleration', color='orange')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RCM_yawRate'], label='Yaw Rate', color='purple')
plt.title('Vehicle Dynamics Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Value')
plt.legend()
plt.savefig(save_dir + r'\VehicleDynamicsOverTime.png')
plt.show()

## 6. Wheel Rotation and Speed Analysis
# Plotting Wheel Speeds Over Time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedFL175'], label='Front Left Wheel Speed', color='blue')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedFR175'], label='Front Right Wheel Speed', color='orange')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedRL175'], label='Rear Left Wheel Speed', color='green')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedRR175'], label='Rear Right Wheel Speed', color='red')
plt.title('Wheel Speeds Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Speed (kph)')
plt.legend()
plt.savefig(save_dir + r'\WheelSpeedsOverTime.png')
plt.show()

# Correlation between wheel speeds
wheel_speed_correlation = data_cleaned[['WheelSpeedFL175', 'WheelSpeedFR175', 'WheelSpeedRL175', 'WheelSpeedRR175']].corr()
wheel_speed_correlation

## 7. Braking Force Analysis
# Plotting Brake Forces Over Time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrL'], label='Front Left Brake Torque', color='blue')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrR'], label='Front Right Brake Torque', color='orange')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReL'], label='Rear Left Brake Torque', color='green')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReR'], label='Rear Right Brake Torque', color='red')
plt.title('Brake Forces Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Torque (Nm)')
plt.legend()
plt.savefig(save_dir + r'\BrakeForcesOverTime.png')
plt.show()

## 8. Brake Torque Distribution
# Plotting Brake Torques Over Time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrL'], label='Front Left Brake Torque', color='blue')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrR'], label='Front Right Brake Torque', color='orange')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReL'], label='Rear Left Brake Torque', color='green')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReR'], label='Rear Right Brake Torque', color='red')
plt.title('Brake Torques Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Torque (Nm)')
plt.legend()
plt.savefig(save_dir + r'\BrakeTorquesOverTime.png')
plt.show()

# Correlation between brake torques
brake_torque_correlation = data_cleaned[['ESP_brakeTorqueFrL', 'ESP_brakeTorqueFrR', 'ESP_brakeTorqueReL', 'ESP_brakeTorqueReR']].corr()
brake_torque_correlation


## 9. Dynamic Responses
# Plotting Dynamic Responses Over Time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RCM_lateralAccel'], label='Lateral Acceleration', color='blue')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RCM_longitudinalAccel'], label='Longitudinal Acceleration', color='orange')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RCM_yawRate'], label='Yaw Rate', color='purple')
plt.title('Dynamic Responses Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Value')
plt.legend()
plt.savefig(save_dir + r'\DynamicResponsesOverTime.png')
plt.show()

# Correlation between dynamic responses
dynamic_responses_correlation = data_cleaned[['RCM_lateralAccel', 'RCM_longitudinalAccel', 'RCM_yawRate']].corr()
dynamic_responses_correlation

## 10. Energy Distribution during Braking
# Plotting Energy Distribution Over Time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['BMS_kwhRegenChargeTotal'], label='Regenerative Charge Total', color='green')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['BMS_kwhDriveDischargeTotal'], label='Drive Discharge Total', color='red')
plt.title('Energy Distribution Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Energy (kWh)')
plt.legend()
plt.savefig(save_dir + r'\EnergyDistributionOverTime_2.png')
plt.show()

# Correlation between energy distribution parameters
energy_distribution_correlation = data_cleaned[['BMS_kwhRegenChargeTotal', 'BMS_kwhDriveDischargeTotal']].corr()
energy_distribution_correlation

# Selected parameters for Corelation Matrix & PairPlot
selected_params = [
    'ESP_brakeTorqueFrL', 'ESP_brakeTorqueFrR', 'ESP_brakeTorqueReL', 'ESP_brakeTorqueReR',
    'WheelSpeedFL175', 'WheelSpeedFR175', 'WheelSpeedRL175', 'WheelSpeedRR175',
    'RCM_lateralAccel', 'RCM_longitudinalAccel', 'RCM_yawRate',
    'BMS_kwhRegenChargeTotal', 'BMS_kwhDriveDischargeTotal'
]

## 11. Heatmap for Correlation Matrix
# Heatmap for correlation matrix
correlation_matrix = data_cleaned[selected_params].corr()
plt.figure(figsize=(16, 12))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix for Selected Parameters')
plt.savefig(save_dir + r'\CorrelationMatrix_1.png')
plt.show()

## 12. Pairplot for Selected Parameters
# Pairplot graph
sns.pairplot(data_cleaned[selected_params])
plt.savefig(save_dir + r'\Pairplot_1.png')
plt.show()

# Analysis of Vehicle Stability During Braking Events

# Identify significant braking events based on brake torque and longitudinal acceleration
braking_events = data_cleaned[(data_cleaned['ESP_brakeTorqueFrL'] > 50) | 
                                  (data_cleaned['ESP_brakeTorqueFrR'] > 50) |
                                  (data_cleaned['ESP_brakeTorqueReL'] > 50) |
                                  (data_cleaned['ESP_brakeTorqueReR'] > 50) |
                                  (data_cleaned['RCM_longitudinalAccel'] < -2)]

# Mark braking events
data_cleaned['BrakingEvent'] = 0
data_cleaned.loc[braking_events.index, 'BrakingEvent'] = 1


## 13. Events with significant changes in Yaw, Pitch or Roll

# # Identify the relevant columns for plotting -- Test to see if data is being plotted correctly
# time_column = 'Time (relative)'
# brake_torque_column = 'ESP_brakeTorqueFrL'
# # Clean the data by removing the header row if present and converting columns to appropriate data types
# data_cleaned[time_column] = data_cleaned[time_column].astype(float)
# data_cleaned[brake_torque_column] = data_cleaned[brake_torque_column].astype(float)
# # Plot the graph
# plt.figure(figsize=(12, 6))
# plt.plot(data_cleaned[time_column], data_cleaned[brake_torque_column], label='ESP_brakeTorqueFrL')
# plt.xlabel('Time (seconds)')
# plt.ylabel('Brake Torque (Nm)')
# plt.title('ESP Brake Torque Front Left vs Time')
# plt.legend()
# plt.grid(True)
# plt.show()

# Plotting Yaw, Pitch, and Roll rates with respect to time

plt.figure(figsize=(14, 8))

# Yaw Rate
plt.subplot(3, 1, 1)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RCM_yawRate'], label='Yaw Rate', color='blue')
plt.xlabel('Time (seconds)')
plt.ylabel('Yaw Rate (deg/s)')
plt.title('Yaw Rate vs Time')
plt.grid(True)
plt.legend()

# Pitch Rate
plt.subplot(3, 1, 2)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RCM_pitchRate'], label='Pitch Rate', color='green')
plt.xlabel('Time (seconds)')
plt.ylabel('Pitch Rate (deg/s)')
plt.title('Pitch Rate vs Time')
plt.grid(True)
plt.legend()

# Roll Rate
plt.subplot(3, 1, 3)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RCM_rollRate'], label='Roll Rate', color='red')
plt.xlabel('Time (seconds)')
plt.ylabel('Roll Rate (deg/s)')
plt.title('Roll Rate vs Time')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig(save_dir + r'\YawPitchRoll_Combined.png')
plt.show()


## 14. Brake Torques For All Four Wheels Vs Time

plt.figure(figsize=(14, 12))

# Front Left Brake Torque
plt.subplot(4, 1, 1)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrL'], label='Front Left Brake Torque', color='blue')
plt.xlabel('Time (seconds)')
plt.ylabel('Brake Torque (Nm)')
plt.title('Front Left Brake Torque vs Time')
plt.legend()
plt.grid(True)

# Front Right Brake Torque
plt.subplot(4, 1, 2)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrR'], label='Front Right Brake Torque', color='green')
plt.xlabel('Time (seconds)')
plt.ylabel('Brake Torque (Nm)')
plt.title('Front Right Brake Torque vs Time')
plt.legend()
plt.grid(True)

# Rear Left Brake Torque
plt.subplot(4, 1, 3)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReL'], label='Rear Left Brake Torque', color='red')
plt.xlabel('Time (seconds)')
plt.ylabel('Brake Torque (Nm)')
plt.title('Rear Left Brake Torque vs Time')
plt.legend()
plt.grid(True)

# Rear Right Brake Torque
plt.subplot(4, 1, 4)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReR'], label='Rear Right Brake Torque', color='orange')
plt.xlabel('Time (seconds)')
plt.ylabel('Brake Torque (Nm)')
plt.title('Rear Right Brake Torque vs Time')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig(save_dir + r'\AllWheelBrakeTorquel_Combined.png')
plt.show()

## 15. Steering Angle during Stability Events vs. Time

# Set your desired ranges here
x_min, x_max = 0, 1000  # Example range for x-axis
y_min, y_max = -400, 400  # Example range for y-axis

plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['SteeringAngle129'], label='Steering Angle', color='purple')
plt.xlabel('Time (seconds)')
plt.ylabel('Steering Angle (degrees)')
plt.title('Steering Angle during Stability Events vs Time')
plt.legend()
plt.grid(True)

# Apply the axis ranges
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

# plt.xticks(ticks=np.linspace(x_min, x_max, num=20), rotation=45)  # More detailed x-axis with more tick marks

plt.savefig(save_dir + r'\SteeringAngle.png')
plt.show()


## 16. Analysis of Vehicle Stability during Stability Events and Sharp Turns

# Define thresholds for sharp turns and stability events
steering_threshold = 30  # Degrees
yaw_rate_threshold = 3  # Degrees per second (example threshold)
pitch_rate_threshold = 2  # Degrees per second (example threshold)
roll_rate_threshold = 2  # Degrees per second (example threshold)

# Identify sharp turns
sharp_turns = data_cleaned[abs(data_cleaned['SteeringAngle129']) > steering_threshold]

# Identify stability events
stability_events = data_cleaned[
    (abs(data_cleaned['RCM_yawRate']) > yaw_rate_threshold) |
    (abs(data_cleaned['RCM_pitchRate']) > pitch_rate_threshold) |
    (abs(data_cleaned['RCM_rollRate']) > roll_rate_threshold)
]

# Plot Steering Angle during identified sharp turns and stability events
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['SteeringAngle129'], label='Steering Angle', color='purple', alpha=0.5)
plt.scatter(sharp_turns['Time (relative)'], sharp_turns['SteeringAngle129'], color='red', label='Sharp Turns', marker='x')
plt.scatter(stability_events['Time (relative)'], stability_events['SteeringAngle129'], color='blue', label='Stability Events', marker='o')
plt.xlabel('Time (seconds)')
plt.ylabel('Steering Angle (degrees)')
plt.title('Steering Angle during Stability Events and Sharp Turns vs Time')
plt.legend()
plt.grid(True)
plt.savefig(save_dir + r'\SteeringAngle_SharpTurnsTime.png')
plt.show()

# Plot Yaw Rate, Pitch Rate, and Roll Rate during identified events
plt.figure(figsize=(14, 12))

# Yaw Rate
plt.subplot(3, 1, 1)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RCM_yawRate'], label='Yaw Rate', color='blue', alpha=0.5)
plt.scatter(stability_events['Time (relative)'], stability_events['RCM_yawRate'], color='red', label='Stability Events', marker='x')
plt.xlabel('Time (seconds)')
plt.ylabel('Yaw Rate (deg/s)')
plt.title('Yaw Rate during Stability Events vs Time')
plt.legend()
plt.grid(True)

# Pitch Rate
plt.subplot(3, 1, 2)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RCM_pitchRate'], label='Pitch Rate', color='green', alpha=0.5)
plt.scatter(stability_events['Time (relative)'], stability_events['RCM_pitchRate'], color='red', label='Stability Events', marker='x')
plt.xlabel('Time (seconds)')
plt.ylabel('Pitch Rate (deg/s)')
plt.title('Pitch Rate during Stability Events vs Time')
plt.legend()
plt.grid(True)

# Roll Rate
plt.subplot(3, 1, 3)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RCM_rollRate'], label='Roll Rate', color='red', alpha=0.5)
plt.scatter(stability_events['Time (relative)'], stability_events['RCM_rollRate'], color='blue', label='Stability Events', marker='o')
plt.xlabel('Time (seconds)')
plt.ylabel('Roll Rate (deg/s)')
plt.title('Roll Rate during Stability Events vs Time')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig(save_dir + r'\SteeringAngle_YawPitchRoll.png')
plt.show()

# Plot Brake Torques during identified sharp turns and stability events
plt.figure(figsize=(14, 12))

# Front Left Brake Torque
plt.subplot(4, 1, 1)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrL'], label='Front Left Brake Torque', color='blue', alpha=0.5)
plt.scatter(sharp_turns['Time (relative)'], sharp_turns['ESP_brakeTorqueFrL'], color='red', label='Sharp Turns', marker='x')
plt.scatter(stability_events['Time (relative)'], stability_events['ESP_brakeTorqueFrL'], color='blue', label='Stability Events', marker='o')
plt.xlabel('Time (seconds)')
plt.ylabel('Brake Torque (Nm)')
plt.title('Front Left Brake Torque during Stability Events vs Time')
plt.legend()
plt.grid(True)

# Front Right Brake Torque
plt.subplot(4, 1, 2)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrR'], label='Front Right Brake Torque', color='green', alpha=0.5)
plt.scatter(sharp_turns['Time (relative)'], sharp_turns['ESP_brakeTorqueFrR'], color='red', label='Sharp Turns', marker='x')
plt.scatter(stability_events['Time (relative)'], stability_events['ESP_brakeTorqueFrR'], color='blue', label='Stability Events', marker='o')
plt.xlabel('Time (seconds)')
plt.ylabel('Brake Torque (Nm)')
plt.title('Front Right Brake Torque during Stability Events vs Time')
plt.legend()
plt.grid(True)

# Rear Left Brake Torque
plt.subplot(4, 1, 3)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReL'], label='Rear Left Brake Torque', color='red', alpha=0.5)
plt.scatter(sharp_turns['Time (relative)'], sharp_turns['ESP_brakeTorqueReL'], color='blue', label='Sharp Turns', marker='x')
plt.scatter(stability_events['Time (relative)'], stability_events['ESP_brakeTorqueReL'], color='red', label='Stability Events', marker='o')
plt.xlabel('Time (seconds)')
plt.ylabel('Brake Torque (Nm)')
plt.title('Rear Left Brake Torque during Stability Events vs Time')
plt.legend()
plt.grid(True)

# Rear Right Brake Torque
plt.subplot(4, 1, 4)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReR'], label='Rear Right Brake Torque', color='orange', alpha=0.5)
plt.scatter(sharp_turns['Time (relative)'], sharp_turns['ESP_brakeTorqueReR'], color='red', label='Sharp Turns', marker='x')
plt.scatter(stability_events['Time (relative)'], stability_events['ESP_brakeTorqueReR'], color='blue', label='Stability Events', marker='o')
plt.xlabel('Time (seconds)')
plt.ylabel('Brake Torque (Nm)')
plt.title('Rear Right Brake Torque during Stability Events vs Time')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig(save_dir + r'\SteeringAngle_BrakeTorques.png')
plt.show()


# Compare ESP Performance Across Different Conditions
# Define conditions for different driving scenarios
sharp_turns = data_cleaned[abs(data_cleaned['SteeringAngle129']) > steering_threshold]
straight_line_braking = data_cleaned[(abs(data_cleaned['SteeringAngle129']) < 10) & (data_cleaned['ESP_brakeTorqueFrL'] > 0)]
curve_handling = data_cleaned[(abs(data_cleaned['SteeringAngle129']) > 10) & (abs(data_cleaned['SteeringAngle129']) <= steering_threshold)]

# Analyze potential understeer scenarios
understeer_threshold = 0.1  # Define a threshold for understeer detection (example)
understeer_events = data_cleaned[(abs(data_cleaned['SteeringAngle129']) > steering_threshold) & (data_cleaned['RCM_yawRate'] < understeer_threshold)]

# Plot ESP performance across different conditions
plt.figure(figsize=(14, 12))

# Sharp Turns
plt.subplot(3, 1, 1)
plt.plot(sharp_turns['Time (relative)'], sharp_turns['SteeringAngle129'], label='Steering Angle', color='purple', alpha=0.5)
plt.scatter(sharp_turns['Time (relative)'], sharp_turns['RCM_yawRate'], color='blue', label='Yaw Rate')
plt.scatter(sharp_turns['Time (relative)'], sharp_turns['ESP_brakeTorqueFrL'], color='red', label='Brake Torque Front Left')
plt.scatter(sharp_turns['Time (relative)'], sharp_turns['ESP_brakeTorqueReL'], color='orange', label='Brake Torque Rear Left')
plt.xlabel('Time (seconds)')
plt.ylabel('Values')
plt.title('ESP Performance during Sharp Turns')
plt.legend()
plt.grid(True)

# Straight Line Braking
plt.subplot(3, 1, 2)
plt.plot(straight_line_braking['Time (relative)'], straight_line_braking['SteeringAngle129'], label='Steering Angle', color='purple', alpha=0.5)
plt.scatter(straight_line_braking['Time (relative)'], straight_line_braking['RCM_yawRate'], color='blue', label='Yaw Rate')
plt.scatter(straight_line_braking['Time (relative)'], straight_line_braking['ESP_brakeTorqueFrL'], color='red', label='Brake Torque Front Left')
plt.scatter(straight_line_braking['Time (relative)'], straight_line_braking['ESP_brakeTorqueReL'], color='orange', label='Brake Torque Rear Left')
plt.xlabel('Time (seconds)')
plt.ylabel('Values')
plt.title('ESP Performance during Straight Line Braking')
plt.legend()
plt.grid(True)

# Curve Handling
plt.subplot(3, 1, 3)
plt.plot(curve_handling['Time (relative)'], curve_handling['SteeringAngle129'], label='Steering Angle', color='purple', alpha=0.5)
plt.scatter(curve_handling['Time (relative)'], curve_handling['RCM_yawRate'], color='blue', label='Yaw Rate')
plt.scatter(curve_handling['Time (relative)'], curve_handling['ESP_brakeTorqueFrL'], color='red', label='Brake Torque Front Left')
plt.scatter(curve_handling['Time (relative)'], curve_handling['ESP_brakeTorqueReL'], color='orange', label='Brake Torque Rear Left')
plt.xlabel('Time (seconds)')
plt.ylabel('Values')
plt.title('ESP Performance during Curve Handling')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig(save_dir + r'\CompareESPPerf.png')
plt.show()

# Analyze Data for Signs of Understeer
# Plot understeer events
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['SteeringAngle129'], label='Steering Angle', color='purple', alpha=0.5)
plt.scatter(understeer_events['Time (relative)'], understeer_events['SteeringAngle129'], color='red', label='Understeer Event', marker='x')
plt.xlabel('Time (seconds)')
plt.ylabel('Steering Angle (degrees)')
plt.title('Understeer Detection based on Steering Angle vs Yaw Rate')
plt.legend()
plt.grid(True)
plt.savefig(save_dir + r'\UndersteerAnalysis.png')
plt.show()


## 17. Comparing Understeer to Oversteer Behavior
# Define thresholds for understeer and oversteer detection
understeer_steering_threshold = 30  # Degrees
understeer_yaw_rate_threshold = 0.1  # Degrees per second (example threshold)

oversteer_yaw_rate_threshold = 3  # Degrees per second (example threshold)
oversteer_steering_threshold = 10  # Degrees

# Identify understeer events
understeer_events = data_cleaned[
    (abs(data_cleaned['SteeringAngle129']) > understeer_steering_threshold) & 
    (abs(data_cleaned['RCM_yawRate']) < understeer_yaw_rate_threshold)
]

# Identify oversteer events
oversteer_events = data_cleaned[
    (abs(data_cleaned['RCM_yawRate']) > oversteer_yaw_rate_threshold) & 
    (abs(data_cleaned['SteeringAngle129']) < oversteer_steering_threshold)
]

# Plot Steering Angle and Yaw Rate for Understeer and Oversteer
plt.figure(figsize=(14, 12))

# Understeer Events
plt.subplot(2, 1, 1)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['SteeringAngle129'], label='Steering Angle', color='purple', alpha=0.5)
plt.scatter(understeer_events['Time (relative)'], understeer_events['SteeringAngle129'], color='red', label='Understeer Event', marker='x')
plt.scatter(understeer_events['Time (relative)'], understeer_events['RCM_yawRate'], color='blue', label='Yaw Rate during Understeer', marker='o')
plt.xlabel('Time (seconds)')
plt.ylabel('Values')
plt.title('Understeer Detection based on Steering Angle and Yaw Rate')
plt.legend()
plt.grid(True)

# Oversteer Events
plt.subplot(2, 1, 2)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RCM_yawRate'], label='Yaw Rate', color='blue', alpha=0.5)
plt.scatter(oversteer_events['Time (relative)'], oversteer_events['RCM_yawRate'], color='red', label='Oversteer Event', marker='x')
plt.scatter(oversteer_events['Time (relative)'], oversteer_events['SteeringAngle129'], color='purple', label='Steering Angle during Oversteer', marker='o')
plt.xlabel('Time (seconds)')
plt.ylabel('Values')
plt.title('Oversteer Detection based on Yaw Rate and Steering Angle')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig(save_dir + r'\Understeer_OverSteer_Events.png')
plt.show()

# Plot Brake Torques for Understeer and Oversteer events
plt.figure(figsize=(14, 12))

# Brake Torques during Understeer Events
plt.subplot(2, 1, 1)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrL'], label='Front Left Brake Torque', color='blue', alpha=0.5)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrR'], label='Front Right Brake Torque', color='green', alpha=0.5)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReL'], label='Rear Left Brake Torque', color='red', alpha=0.5)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReR'], label='Rear Right Brake Torque', color='orange', alpha=0.5)
plt.scatter(understeer_events['Time (relative)'], understeer_events['ESP_brakeTorqueFrL'], color='red', label='Understeer Event', marker='x')
plt.xlabel('Time (seconds)')
plt.ylabel('Brake Torque (Nm)')
plt.title('Brake Torques during Understeer Events')
plt.legend()
plt.grid(True)

# Brake Torques during Oversteer Events
plt.subplot(2, 1, 2)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrL'], label='Front Left Brake Torque', color='blue', alpha=0.5)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrR'], label='Front Right Brake Torque', color='green', alpha=0.5)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReL'], label='Rear Left Brake Torque', color='red', alpha=0.5)
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReR'], label='Rear Right Brake Torque', color='orange', alpha=0.5)
plt.scatter(oversteer_events['Time (relative)'], oversteer_events['ESP_brakeTorqueFrR'], color='red', label='Oversteer Event', marker='x')
plt.xlabel('Time (seconds)')
plt.ylabel('Brake Torque (Nm)')
plt.title('Brake Torques during Oversteer Events')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig(save_dir + r'\Understeer_OverSteer_BrakeTorque.png')
plt.show()


# Analysis of Vehicle Stability During Braking Events
## 1. Energy Distribution During Braking Events

# Plot energy consumption and regeneration during braking events
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['BMS_kwhRegenChargeTotal'], label='Regenerative Charge Total', color='green')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['BMS_kwhDriveDischargeTotal'], label='Drive Discharge Total', color='red')
plt.scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
            data_cleaned['BMS_kwhDriveDischargeTotal'][data_cleaned['BrakingEvent'] == 1], 
            color='orange', label='Braking Events')
plt.title('Energy Distribution During Braking Events')
plt.xlabel('Time (relative)')
plt.ylabel('Energy (kWh)')
plt.legend()
plt.savefig(save_dir + r'\EnergyDistributionDuringBrakingEvents.png')
plt.show()

## 2. Vehicle Stability During Braking Events
# Plot vehicle stability parameters during braking events
fig, ax = plt.subplots(3, 1, figsize=(14, 18))

ax[0].plot(data_cleaned['Time (relative)'], data_cleaned['RCM_lateralAccel'], label='Lateral Acceleration', color='blue')
ax[0].scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
              data_cleaned['RCM_lateralAccel'][data_cleaned['BrakingEvent'] == 1], 
              color='orange', label='Braking Events')
ax[0].set_title('Lateral Acceleration During Braking Events')
ax[0].set_xlabel('Time (relative)')
ax[0].set_ylabel('Acceleration (m/s²)')
ax[0].legend()

ax[1].plot(data_cleaned['Time (relative)'], data_cleaned['RCM_longitudinalAccel'], label='Longitudinal Acceleration', color='green')
ax[1].scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
              data_cleaned['RCM_longitudinalAccel'][data_cleaned['BrakingEvent'] == 1], 
              color='orange', label='Braking Events')
ax[1].set_title('Longitudinal Acceleration During Braking Events')
ax[1].set_xlabel('Time (relative)')
ax[1].set_ylabel('Acceleration (m/s²)')
ax[1].legend()

ax[2].plot(data_cleaned['Time (relative)'], data_cleaned['RCM_yawRate'], label='Yaw Rate', color='purple')
ax[2].scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
              data_cleaned['RCM_yawRate'][data_cleaned['BrakingEvent'] == 1], 
              color='orange', label='Braking Events')
ax[2].set_title('Yaw Rate During Braking Events')
ax[2].set_xlabel('Time (relative)')
ax[2].set_ylabel('Yaw Rate (rad/s)')
ax[2].legend()

plt.tight_layout()
plt.savefig(save_dir + r'\CombinedPlot_4.png')
plt.show()

## 3. Correlation Analysis During Braking Events
# Correlation analysis during braking events
braking_corr_params = data_cleaned.loc[data_cleaned['BrakingEvent'] == 1, [
    'ESP_brakeTorqueFrL', 'ESP_brakeTorqueFrR', 'ESP_brakeTorqueReL', 'ESP_brakeTorqueReR',
    'BMS_kwhRegenChargeTotal', 'BMS_kwhDriveDischargeTotal',
    'RCM_lateralAccel', 'RCM_longitudinalAccel', 'RCM_yawRate'
]]

braking_corr_matrix = braking_corr_params.corr()

# Plot the heatmap for correlation matrix during braking events
plt.figure(figsize=(14, 12))
sns.heatmap(braking_corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix During Braking Events')
plt.savefig(save_dir + r'\CorrMatBrakingEvents.png')
plt.show()

# ESP Stability System Analysis During Sudden Braking

## 1. Brake Torques During Braking Events
# Plotting Brake Torques During Braking Events
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrL'], label='Front Left Brake Torque', color='blue')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrR'], label='Front Right Brake Torque', color='orange')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReL'], label='Rear Left Brake Torque', color='green')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReR'], label='Rear Right Brake Torque', color='red')
plt.scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
            data_cleaned['ESP_brakeTorqueFrL'][data_cleaned['BrakingEvent'] == 1], 
            color='black', label='Braking Events', marker='x')
plt.title('Brake Torques During Braking Events')
plt.xlabel('Time (relative)')
plt.ylabel('Torque (Nm)')
plt.legend()
plt.savefig(save_dir + r'\BrakeTorquesDuringBrakingEvents.png')
plt.show()

## 2. Wheel Speeds During Braking Events
# Plotting Wheel Speeds During Braking Events
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedFL175'], label='Front Left Wheel Speed', color='blue')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedFR175'], label='Front Right Wheel Speed', color='orange')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedRL175'], label='Rear Left Wheel Speed', color='green')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['WheelSpeedRR175'], label='Rear Right Wheel Speed', color='red')
plt.scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
            data_cleaned['WheelSpeedFL175'][data_cleaned['BrakingEvent'] == 1], 
            color='black', label='Braking Events', marker='x')
plt.title('Wheel Speeds During Braking Events')
plt.xlabel('Time (relative)')
plt.ylabel('Speed (kph)')
plt.legend()
plt.savefig(save_dir + r'\WheelSpeedsDuringBrakingEvents.png')
plt.show()

## 3. Vehicle Dynamics During Braking Events
# Plotting Dynamic Responses During Braking Events
fig, ax = plt.subplots(3, 1, figsize=(14, 18))

ax[0].plot(data_cleaned['Time (relative)'], data_cleaned['RCM_lateralAccel'], label='Lateral Acceleration', color='blue')
ax[0].scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
              data_cleaned['RCM_lateralAccel'][data_cleaned['BrakingEvent'] == 1], 
              color='black', label='Braking Events', marker='x')
ax[0].set_title('Lateral Acceleration During Braking Events')
ax[0].set_xlabel('Time (relative)')
ax[0].set_ylabel('Acceleration (m/s²)')
ax[0].legend()

ax[1].plot(data_cleaned['Time (relative)'], data_cleaned['RCM_longitudinalAccel'], label='Longitudinal Acceleration', color='green')
ax[1].scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
              data_cleaned['RCM_longitudinalAccel'][data_cleaned['BrakingEvent'] == 1], 
              color='black', label='Braking Events', marker='x')
ax[1].set_title('Longitudinal Acceleration During Braking Events')
ax[1].set_xlabel('Time (relative)')
ax[1].set_ylabel('Acceleration (m/s²)')
ax[1].legend()

ax[2].plot(data_cleaned['Time (relative)'], data_cleaned['RCM_yawRate'], label='Yaw Rate', color='purple')
ax[2].scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
              data_cleaned['RCM_yawRate'][data_cleaned['BrakingEvent'] == 1], 
              color='black', label='Braking Events', marker='x')
ax[2].set_title('Yaw Rate During Braking Events')
ax[2].set_xlabel('Time (relative)')
ax[2].set_ylabel('Yaw Rate (rad/s)')
ax[2].legend()

plt.tight_layout()
plt.savefig(save_dir + r'\CombinedPlot_5.png')
plt.show()

# Correlation analysis during braking events
braking_corr_params = data_cleaned.loc[data_cleaned['BrakingEvent'] == 1, [
    'ESP_brakeTorqueFrL', 'ESP_brakeTorqueFrR', 'ESP_brakeTorqueReL', 'ESP_brakeTorqueReR',
    'WheelSpeedFL175', 'WheelSpeedFR175', 'WheelSpeedRL175', 'WheelSpeedRR175',
    'RCM_lateralAccel', 'RCM_longitudinalAccel', 'RCM_yawRate',
    'BMS_kwhRegenChargeTotal', 'BMS_kwhDriveDischargeTotal'
]]

braking_corr_matrix = braking_corr_params.corr()

# Plot the heatmap for correlation matrix during braking events
plt.figure(figsize=(14, 12))
sns.heatmap(braking_corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix During Braking Events')
plt.savefig(save_dir + r'\CorrMatDuringBrakingEvents.png')
plt.show()

# Analysis of Vehicle Dynamics During Braking Events

## 1. Roll Rate During Braking Events
# Visualize Roll Rate, Yaw Rate, Longitudinal Acceleration, and Lateral Acceleration during Braking Events
fig, ax = plt.subplots(4, 1, figsize=(14, 24))

ax[0].plot(data_cleaned['Time (relative)'], data_cleaned['RCM_rollRate'], label='Roll Rate', color='blue')
ax[0].scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
              data_cleaned['RCM_rollRate'][data_cleaned['BrakingEvent'] == 1], 
              color='black', label='Braking Events', marker='x')
ax[0].set_title('Roll Rate During Braking Events')
ax[0].set_xlabel('Time (relative)')
ax[0].set_ylabel('Roll Rate (rad/s)')
ax[0].legend()

## 2. Yaw Rate During Braking Events
ax[1].plot(data_cleaned['Time (relative)'], data_cleaned['RCM_yawRate'], label='Yaw Rate', color='purple')
ax[1].scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
              data_cleaned['RCM_yawRate'][data_cleaned['BrakingEvent'] == 1], 
              color='black', label='Braking Events', marker='x')
ax[1].set_title('Yaw Rate During Braking Events')
ax[1].set_xlabel('Time (relative)')
ax[1].set_ylabel('Yaw Rate (rad/s)')
ax[1].legend()

## 3. Longitudinal and Lateral Acceleration During Braking Events
ax[2].plot(data_cleaned['Time (relative)'], data_cleaned['RCM_longitudinalAccel'], label='Longitudinal Acceleration', color='green')
ax[2].scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
              data_cleaned['RCM_longitudinalAccel'][data_cleaned['BrakingEvent'] == 1], 
              color='black', label='Braking Events', marker='x')
ax[2].set_title('Longitudinal Acceleration During Braking Events')
ax[2].set_xlabel('Time (relative)')
ax[2].set_ylabel('Acceleration (m/s²)')
ax[2].legend()

ax[3].plot(data_cleaned['Time (relative)'], data_cleaned['RCM_lateralAccel'], label='Lateral Acceleration', color='orange')
ax[3].scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
              data_cleaned['RCM_lateralAccel'][data_cleaned['BrakingEvent'] == 1], 
              color='black', label='Braking Events', marker='x')
ax[3].set_title('Lateral Acceleration During Braking Events')
ax[3].set_xlabel('Time (relative)')
ax[3].set_ylabel('Acceleration (m/s²)')
ax[3].legend()

plt.tight_layout()
plt.savefig(save_dir + r'\CombinedPlot_6.png')
plt.show()

## 4. Correlation Analysis During Braking Events
# Correlation analysis during braking events
braking_corr_params = data_cleaned.loc[data_cleaned['BrakingEvent'] == 1, [
    'ESP_brakeTorqueFrL', 'ESP_brakeTorqueFrR', 'ESP_brakeTorqueReL', 'ESP_brakeTorqueReR',
    'RCM_rollRate', 'RCM_yawRate', 'RCM_longitudinalAccel', 'RCM_lateralAccel'
]]

braking_corr_matrix = braking_corr_params.corr()

# Plot the heatmap for correlation matrix during braking events
plt.figure(figsize=(14, 12))
sns.heatmap(braking_corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix During Braking Events')
plt.savefig(save_dir + r'\CorrMatrix_BrakingEvents_2.png')
plt.show()


# Stability Analysis Under Different Speeds
## 1. Roll Rate by Speed Range

# Define speed ranges
speed_bins = [0, 20, 40, 60, 80, 100, 120, 140]
speed_labels = ['0-20', '20-40', '40-60', '60-80', '80-100', '100-120', '120-140']

# Segment data into speed ranges
data_cleaned['SpeedRange'] = pd.cut(data_cleaned['DI_vehicleSpeed'], bins=speed_bins, labels=speed_labels)

fig, ax = plt.subplots(4, 1, figsize=(14, 24), sharex=True)

# Plot Roll Rate
sns.boxplot(x='SpeedRange', y='RCM_rollRate', data=data_cleaned, ax=ax[0])
ax[0].set_title('Roll Rate by Speed Range')
ax[0].set_ylabel('Roll Rate (rad/s)')

## 2. Yaw Rate by Speed Range
# Plot Yaw Rate
sns.boxplot(x='SpeedRange', y='RCM_yawRate', data=data_cleaned, ax=ax[1])
ax[1].set_title('Yaw Rate by Speed Range')
ax[1].set_ylabel('Yaw Rate (rad/s)')

## 3. Longitudinal and Lateral Acceleration by Speed Range
# Plot Longitudinal Acceleration
sns.boxplot(x='SpeedRange', y='RCM_longitudinalAccel', data=data_cleaned, ax=ax[2])
ax[2].set_title('Longitudinal Acceleration by Speed Range')
ax[2].set_ylabel('Acceleration (m/s²)')

# Plot Lateral Acceleration
sns.boxplot(x='SpeedRange', y='RCM_lateralAccel', data=data_cleaned, ax=ax[3])
ax[3].set_title('Lateral Acceleration by Speed Range')
ax[3].set_ylabel('Acceleration (m/s²)')
ax[3].set_xlabel('Speed Range (kph)')

plt.tight_layout()
plt.savefig(save_dir + r'\CombinedPlot_7.png')
plt.show()

# Calculate summary statistics for each speed range
summary_stats = data_cleaned.groupby('SpeedRange')[['RCM_rollRate', 'RCM_yawRate', 'RCM_longitudinalAccel', 'RCM_lateralAccel']].describe()
summary_stats

## 4. Correlation Analysis Between Speed and Dynamics Parameters
# Correlation analysis between speed and dynamics parameters
correlation_params = data_cleaned[['DI_vehicleSpeed', 'RCM_rollRate', 'RCM_yawRate', 'RCM_longitudinalAccel', 'RCM_lateralAccel']]
correlation_matrix = correlation_params.corr()

# Plot the heatmap for correlation matrix
plt.figure(figsize=(14, 12))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Between Speed and Dynamics Parameters')
plt.savefig(save_dir + r'\CorrMatrix_SpeedDynamicsParam.png')
plt.show()


# Analyzing Braking Torque's Effect on Stability
## 1. Braking Torque vs Stability Parameters

fig, ax = plt.subplots(4, 1, figsize=(14, 24))

# Plot Front Left Brake Torque vs Stability Parameters
ax[0].scatter(data_cleaned['ESP_brakeTorqueFrL'], data_cleaned['RCM_rollRate'], label='Roll Rate', color='blue', alpha=0.5)
ax[0].set_title('Front Left Brake Torque vs Roll Rate')
ax[0].set_xlabel('Front Left Brake Torque (Nm)')
ax[0].set_ylabel('Roll Rate (rad/s)')

ax[1].scatter(data_cleaned['ESP_brakeTorqueFrL'], data_cleaned['RCM_yawRate'], label='Yaw Rate', color='purple', alpha=0.5)
ax[1].set_title('Front Left Brake Torque vs Yaw Rate')
ax[1].set_xlabel('Front Left Brake Torque (Nm)')
ax[1].set_ylabel('Yaw Rate (rad/s)')

ax[2].scatter(data_cleaned['ESP_brakeTorqueFrL'], data_cleaned['RCM_longitudinalAccel'], label='Longitudinal Acceleration', color='green', alpha=0.5)
ax[2].set_title('Front Left Brake Torque vs Longitudinal Acceleration')
ax[2].set_xlabel('Front Left Brake Torque (Nm)')
ax[2].set_ylabel('Acceleration (m/s²)')

ax[3].scatter(data_cleaned['ESP_brakeTorqueFrL'], data_cleaned['RCM_lateralAccel'], label='Lateral Acceleration', color='orange', alpha=0.5)
ax[3].set_title('Front Left Brake Torque vs Lateral Acceleration')
ax[3].set_xlabel('Front Left Brake Torque (Nm)')
ax[3].set_ylabel('Acceleration (m/s²)')

plt.tight_layout()
plt.savefig(save_dir + r'\CorrMatrix_SpeedDynamicsParam2.png')
plt.show()

## 2. Statistical Distribution of Stability Parameters
# Calculate summary statistics for stability parameters based on Front Left Brake Torque
brake_torque_stats = data_cleaned.groupby(pd.cut(data_cleaned['ESP_brakeTorqueFrL'], bins=10))[['RCM_rollRate', 'RCM_yawRate', 'RCM_longitudinalAccel', 'RCM_lateralAccel']].describe()
brake_torque_stats

## 3. Correlation Analysis Between Braking Torques and Stability Parameters
# Correlation analysis between braking torques and stability parameters
correlation_params = data_cleaned[['ESP_brakeTorqueFrL', 'ESP_brakeTorqueFrR', 'ESP_brakeTorqueReL', 'ESP_brakeTorqueReR',
                                       'RCM_rollRate', 'RCM_yawRate', 'RCM_longitudinalAccel', 'RCM_lateralAccel']]
correlation_matrix = correlation_params.corr()

# Plot the heatmap for correlation matrix
plt.figure(figsize=(14, 12))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Between Braking Torques and Stability Parameters')
plt.savefig(save_dir + r'\CorrMatrix_BrakeTorStabilityParam.png')
plt.show()


# Comparison of Brake Torque and Yaw Rate
## 1. Visualizing Brake Torque and Yaw Rate Over Time

# Plotting Front Left Brake Torque and Yaw Rate Over Time
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrL'], label='Front Left Brake Torque', color='blue')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RCM_yawRate'], label='Yaw Rate', color='purple')
plt.title('Front Left Brake Torque and Yaw Rate Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Value')
plt.legend()
plt.savefig(save_dir + r'\TorqueYawRateOverTime.png')
plt.show()

## 2. Scatter Plot Analysis
# Scatter Plot of Front Left Brake Torque vs Yaw Rate
plt.figure(figsize=(14, 8))
plt.scatter(data_cleaned['ESP_brakeTorqueFrL'], data_cleaned['RCM_yawRate'], alpha=0.5, color='blue')
plt.title('Front Left Brake Torque vs Yaw Rate')
plt.xlabel('Front Left Brake Torque (Nm)')
plt.ylabel('Yaw Rate (rad/s)')
plt.grid(True)
plt.savefig(save_dir + r'\ScatterPlot_1.png')
plt.show()

# Scatter Plot of Rear Left Brake Torque vs Yaw Rate
plt.figure(figsize=(14, 8))
plt.scatter(data_cleaned['ESP_brakeTorqueReL'], data_cleaned['RCM_yawRate'], alpha=0.5, color='green')
plt.title('Rear Left Brake Torque vs Yaw Rate')
plt.xlabel('Rear Left Brake Torque (Nm)')
plt.ylabel('Yaw Rate (rad/s)')
plt.grid(True)
plt.savefig(save_dir + r'\ScatterPlot_2.png')
plt.show()

## 3. Correlation Analysis Between Brake Torques and Yaw Rate
# Correlation analysis between brake torques and yaw rate
correlation_params = data_cleaned[['ESP_brakeTorqueFrL', 'ESP_brakeTorqueFrR', 'ESP_brakeTorqueReL', 'ESP_brakeTorqueReR', 'RCM_yawRate']]
correlation_matrix = correlation_params.corr()

# Plot the heatmap for correlation matrix
plt.figure(figsize=(14, 12))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Between Brake Torques and Yaw Rate')
plt.savefig(save_dir + r'\CorrMatrixBrakeTorYawRate.png')
plt.show()

# 4. Comparison of Front and Rear Brake Torque with Yaw Rate Over Time
# Plotting Front and Rear Brake Torque and Yaw Rate Over Time
plt.figure(figsize=(14, 8))

# Front Brake Torque and Yaw Rate
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrL'], label='Front Left Brake Torque', color='blue')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrR'], label='Front Right Brake Torque', color='cyan')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RCM_yawRate'], label='Yaw Rate', color='purple')

# Rear Brake Torque
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReL'], label='Rear Left Brake Torque', color='green')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReR'], label='Rear Right Brake Torque', color='lime')

plt.title('Brake Torques and Yaw Rate Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.savefig(save_dir + r'\CombinedPlot_8.png')
plt.show()


# Trend Analysis of Key Metrics Over Time
# Plotting key metrics over time
plt.figure(figsize=(14, 8))

# Plot SmoothBattCurrent132 over time
plt.plot(data_cleaned['Time (relative)'], data_cleaned['SmoothBattCurrent'], label='Smooth HV Battery Current', color='blue')

# Plot FrontMotorCurrent1A5 over time
plt.plot(data_cleaned['Time (relative)'], data_cleaned['FrontMotorCurrent1A5'], label='Front Motor Current', color='green')

# Plot RearMotorCurrent126 over time
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RearMotorCurrent126'], label='Rear Motor Current', color='red')

# Plot BMS_maxRegenPower over time
plt.plot(data_cleaned['Time (relative)'], data_cleaned['BMS_maxRegenPower'], label='Max Regenerative Power', color='purple')

plt.title('Trend Analysis of Key Metrics Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Current (A) / Power (kW)')
plt.legend()
plt.grid(True)
plt.savefig(save_dir + r'\TrendAnalysis.png')
plt.show()

# Plotting braking power trends over time
plt.figure(figsize=(14, 8))

# Plot BMS_maxRegenPower over time
plt.plot(data_cleaned['Time (relative)'], data_cleaned['BMS_maxRegenPower'], label='Max Regenerative Power', color='purple')

# Plot FrontMotorCurrent1A5 over time
plt.plot(data_cleaned['Time (relative)'], data_cleaned['FrontMotorCurrent1A5'], label='Front Motor Current', color='green')

# Plot RearMotorCurrent126 over time
plt.plot(data_cleaned['Time (relative)'], data_cleaned['RearMotorCurrent126'], label='Rear Motor Current', color='red')

plt.title('Braking Power Trends Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Current (A) / Power (kW)')
plt.legend()
plt.grid(True)
plt.savefig(save_dir + r'\RearMotorCurrentOverTime.png')
plt.show()

# Braking Power Trends Analysis
# Calculate summary statistics for braking power metrics
braking_power_stats = data_cleaned[['BMS_maxRegenPower', 'FrontMotorCurrent1A5', 'RearMotorCurrent126']].describe()
braking_power_stats

# Correlation analysis between braking power metrics and stability parameters
correlation_params = data_cleaned[['BMS_maxRegenPower', 'FrontMotorCurrent1A5', 'RearMotorCurrent126',
                                       'ESP_brakeTorqueFrL', 'ESP_brakeTorqueFrR', 'ESP_brakeTorqueReL', 'ESP_brakeTorqueReR',
                                       'RCM_yawRate', 'RCM_rollRate', 'RCM_longitudinalAccel', 'RCM_lateralAccel']]
correlation_matrix = correlation_params.corr()

## 1. Braking Power Trends Over Time
# Plot the heatmap for correlation matrix
plt.figure(figsize=(14, 12))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Between Braking Power Metrics and Stability Parameters')
plt.savefig(save_dir + r'\CorrMatrixBrakingPowandStabilityParam.png')
plt.show()

## 1. Braking Power Trends Over Time
# Plotting Max Regenerative Power During Braking Events
plt.figure(figsize=(14, 8))
plt.plot(data_cleaned['Time (relative)'], data_cleaned['BMS_maxRegenPower'], label='Max Regenerative Power', color='purple')
plt.scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
            data_cleaned['BMS_maxRegenPower'][data_cleaned['BrakingEvent'] == 1], 
            color='orange', label='Braking Events', marker='x')
plt.title('Max Regenerative Power During Braking Events')
plt.xlabel('Time (relative)')
plt.ylabel('Power (kW)')
plt.legend()
plt.grid(True)
plt.savefig(save_dir + r'\MaxRegenPowerDuringBrakingEvents.png')
plt.show()

## 1. Braking Power Trends Over Time
# Visualize Stability Parameters During Braking Events
fig, ax = plt.subplots(4, 1, figsize=(14, 24))

## 2. Statistical Distribution of Braking Power Metrics
# Plot Roll Rate During Braking Events
ax[0].plot(data_cleaned['Time (relative)'], data_cleaned['RCM_rollRate'], label='Roll Rate', color='blue')
ax[0].scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
              data_cleaned['RCM_rollRate'][data_cleaned['BrakingEvent'] == 1], 
              color='orange', label='Braking Events', marker='x')
ax[0].set_title('Roll Rate During Braking Events')
ax[0].set_xlabel('Time (relative)')
ax[0].set_ylabel('Roll Rate (rad/s)')
ax[0].legend()

## 3. Correlation Analysis Between Braking Power Metrics and Stability Parameters
# Plot Yaw Rate During Braking Events
ax[1].plot(data_cleaned['Time (relative)'], data_cleaned['RCM_yawRate'], label='Yaw Rate', color='purple')
ax[1].scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
              data_cleaned['RCM_yawRate'][data_cleaned['BrakingEvent'] == 1], 
              color='orange', label='Braking Events', marker='x')
ax[1].set_title('Yaw Rate During Braking Events')
ax[1].set_xlabel('Time (relative)')
ax[1].set_ylabel('Yaw Rate (rad/s)')
ax[1].legend()

# 4. Analysis of Energy Usage During Sudden Braking: Regeneration vs. Vehicle Stability
# Plot Longitudinal Acceleration During Braking Events
ax[2].plot(data_cleaned['Time (relative)'], data_cleaned['RCM_longitudinalAccel'], label='Longitudinal Acceleration', color='green')
ax[2].scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
              data_cleaned['RCM_longitudinalAccel'][data_cleaned['BrakingEvent'] == 1], 
              color='orange', label='Braking Events', marker='x')
ax[2].set_title('Longitudinal Acceleration During Braking Events')
ax[2].set_xlabel('Time (relative)')
ax[2].set_ylabel('Acceleration (m/s²)')
ax[2].legend()

## 5. Stability Parameters During Braking Events
# Plot Lateral Acceleration During Braking Events
ax[3].plot(data_cleaned['Time (relative)'], data_cleaned['RCM_lateralAccel'], label='Lateral Acceleration', color='orange')
ax[3].scatter(data_cleaned['Time (relative)'][data_cleaned['BrakingEvent'] == 1], 
              data_cleaned['RCM_lateralAccel'][data_cleaned['BrakingEvent'] == 1], 
              color='orange', label='Braking Events', marker='x')
ax[3].set_title('Lateral Acceleration During Braking Events')
ax[3].set_xlabel('Time (relative)')
ax[3].set_ylabel('Acceleration (m/s²)')
ax[3].legend()

plt.tight_layout()
plt.savefig(save_dir + r'\CombinedPlot_9.png')
plt.show()

## 6. Correlation Analysis Between Regenerative Power and Stability Parameters
# Correlation Analysis Between Regenerative Power and Stability Parameters
braking_corr_params = data_cleaned.loc[data_cleaned['BrakingEvent'] == 1, [
    'BMS_maxRegenPower', 'RCM_rollRate', 'RCM_yawRate', 'RCM_longitudinalAccel', 'RCM_lateralAccel'
]]

braking_corr_matrix = braking_corr_params.corr()

# Plot the heatmap for correlation matrix during braking events
plt.figure(figsize=(14, 12))
sns.heatmap(braking_corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Between Regenerative Power and Stability Parameters During Braking Events')
plt.savefig(save_dir + r'\CorrMatrixRegenPowerStabilityParam.png')
plt.show()


# Additional Observations for Powertrain
## 1. Comparison of Motor Currents During Different Driving Condition

# Create a new column to categorize driving conditions based on longitudinal acceleration
data_cleaned['DrivingCondition'] = pd.cut(data_cleaned['RCM_longitudinalAccel'], bins=[-10, -1, 1, 10], labels=['Deceleration', 'Cruising', 'Acceleration'])

# Plot the distribution of motor currents under different driving conditions
plt.figure(figsize=(14, 8))
sns.boxplot(x='DrivingCondition', y='FrontMotorCurrent1A5', data=data_cleaned)
plt.title('Front Motor Current Under Different Driving Conditions')
plt.xlabel('Driving Condition')
plt.ylabel('Front Motor Current (A)')
plt.savefig(save_dir + r'\FMotorCurrentDrivingCond.png')
plt.show()

plt.figure(figsize=(14, 8))
sns.boxplot(x='DrivingCondition', y='RearMotorCurrent126', data=data_cleaned)
plt.title('Rear Motor Current Under Different Driving Conditions')
plt.xlabel('Driving Condition')
plt.ylabel('Rear Motor Current (A)')
plt.savefig(save_dir + r'\RMotorCurrentDrivingCond.png')
plt.show()

## 2. Efficiency Analysis
# Calculate efficiency (simple example: ratio of motor currents to battery current)
data_cleaned['FrontMotorEfficiency'] = data_cleaned['FrontMotorCurrent1A5'] / data_cleaned['SmoothBattCurrent']
data_cleaned['RearMotorEfficiency'] = data_cleaned['RearMotorCurrent126'] / data_cleaned['SmoothBattCurrent']

# Plot efficiency under different driving conditions
plt.figure(figsize=(14, 8))
sns.boxplot(x='DrivingCondition', y='FrontMotorEfficiency', data=data_cleaned)
plt.title('Front Motor Efficiency Under Different Driving Conditions')
plt.xlabel('Driving Condition')
plt.ylabel('Front Motor Efficiency')
plt.savefig(save_dir + r'\FMotorEffDrivingCond.png')
plt.show()

plt.figure(figsize=(14, 8))
sns.boxplot(x='DrivingCondition', y='RearMotorEfficiency', data=data_cleaned)
plt.title('Rear Motor Efficiency Under Different Driving Conditions')
plt.xlabel('Driving Condition')
plt.ylabel('Rear Motor Efficiency')
plt.savefig(save_dir + r'\RMotorEffDrivingCond.png')
plt.show()

## 3. Drive Cycles and Power Demand
# Create a new column to categorize driving conditions based on longitudinal acceleration
data_cleaned['DrivingCondition'] = pd.cut(data_cleaned['RCM_longitudinalAccel'], bins=[-10, -1, 1, 10], labels=['Deceleration', 'Cruising', 'Acceleration'])

# Plot the distribution of energy consumption under different driving conditions
plt.figure(figsize=(14, 8))
sns.boxplot(x='DrivingCondition', y='SmoothBattCurrent', data=data_cleaned)
plt.title('Battery Current Under Different Driving Conditions')
plt.xlabel('Driving Condition')
plt.ylabel('Battery Current (A)')
plt.savefig(save_dir + r'\BattCondnUnderDiffDrivCond.png')
plt.show()

# Plot the distribution of regenerative braking power under different driving conditions
plt.figure(figsize=(14, 8))
sns.boxplot(x='DrivingCondition', y='BMS_maxRegenPower', data=data_cleaned)
plt.title('Max Regenerative Power Under Different Driving Conditions')
plt.xlabel('Driving Condition')
plt.ylabel('Max Regenerative Power (kW)')
plt.savefig(save_dir + r'\MaxRegenPowUnderDiffDrivCond.png')
plt.show()


## 4. Battery State of Charge (SoC) Dynamics --- This is removed now.
# Plotting Battery State of Charge (SoC) Over Time
# plt.figure(figsize=(14, 8))
# plt.plot(data_cleaned['Time (relative)'], data_cleaned['BMS_maxRegenPower'], label='Max Regenerative Power', color='purple')
# plt.plot(data_cleaned['Time (relative)'], data_cleaned['BMS_minRegenPower'], label='Min Regenerative Power', color='orange')
# plt.plot(data_cleaned['Time (relative)'], data_cleaned['BMS_actualPackSOH'], label='Battery SoC', color='green')
# plt.title('Battery State of Charge (SoC) Dynamics Over Time')
# plt.xlabel('Time (relative)')
# plt.ylabel('Value')
# plt.legend()
# plt.grid(True)
# plt.savefig(save_dir + r'\SOCOverTime.png')
# plt.show()

## 4. Battery State of Charge (SoC) Dynamics [MD file content]
# **Observations**:
# - Battery SoC changes dynamically with driving conditions and power demand.
# - Regenerative braking contributes to maintaining or increasing SoC during deceleration.

# **Insights**:
# - Monitoring SoC dynamics helps in managing battery health and optimizing energy usage.
# - Understanding SoC changes can guide the development of more efficient regenerative braking systems.


## 5. Impact of Vehicle Speed on Powertrain Performance

# Create a new column to categorize speed ranges
speed_bins = [0, 20, 40, 60, 80, 100, 120, 140]
speed_labels = ['0-20', '20-40', '40-60', '60-80', '80-100', '100-120', '120-140']
data_cleaned['SpeedRange'] = pd.cut(data_cleaned['DI_vehicleSpeed'], bins=speed_bins, labels=speed_labels)

# Plot the distribution of powertrain parameters under different speed ranges
plt.figure(figsize=(14, 8))
sns.boxplot(x='SpeedRange', y='SmoothBattCurrent', data=data_cleaned)
plt.title('Battery Current Under Different Speed Ranges')
plt.xlabel('Speed Range (kph)')
plt.ylabel('Battery Current (A)')
plt.savefig(save_dir + r'\BattCurrUnderDiffSpeedRanges.png')
plt.show()

plt.figure(figsize=(14, 8))
sns.boxplot(x='SpeedRange', y='FrontMotorCurrent1A5', data=data_cleaned)
plt.title('Front Motor Current Under Different Speed Ranges')
plt.xlabel('Speed Range (kph)')
plt.ylabel('Front Motor Current (A)')
plt.savefig(save_dir + r'\FMotorCurrUnderDiffSpeedRanges.png')
plt.show()

plt.figure(figsize=(14, 8))
sns.boxplot(x='SpeedRange', y='RearMotorCurrent126', data=data_cleaned)
plt.title('Rear Motor Current Under Different Speed Ranges')
plt.xlabel('Speed Range (kph)')
plt.ylabel('Rear Motor Current (A)')
plt.savefig(save_dir + r'\RMotorCurrUnderDiffSpeedRanges.png')
plt.show()

plt.figure(figsize=(14, 8))
sns.boxplot(x='SpeedRange', y='BMS_maxRegenPower', data=data_cleaned)
plt.title('Max Regenerative Power Under Different Speed Ranges')
plt.xlabel('Speed Range (kph)')
plt.ylabel('Max Regenerative Power (kW)')
plt.savefig(save_dir + r'\MaxRegenPowerUnderDiffSpeedRanges.png')
plt.show()

## 6. Torque Distribution Analysis

# Plotting Front and Rear Brake Torque Over Time
plt.figure(figsize=(14, 8))

# Front Brake Torque
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrL'], label='Front Left Brake Torque', color='blue')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueFrR'], label='Front Right Brake Torque', color='cyan')

# Rear Brake Torque
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReL'], label='Rear Left Brake Torque', color='green')
plt.plot(data_cleaned['Time (relative)'], data_cleaned['ESP_brakeTorqueReR'], label='Rear Right Brake Torque', color='lime')

plt.title('Front and Rear Brake Torque Over Time')
plt.xlabel('Time (relative)')
plt.ylabel('Brake Torque (Nm)')
plt.legend()
plt.grid(True)
plt.savefig(save_dir + r'\FRBrakeTorque.png')
plt.show()

# Plot the distribution of brake torque under different driving conditions
plt.figure(figsize=(14, 8))
sns.boxplot(x='DrivingCondition', y='ESP_brakeTorqueFrL', data=data_cleaned)
plt.title('Front Left Brake Torque Under Different Driving Conditions')
plt.xlabel('Driving Condition')
plt.ylabel('Front Left Brake Torque (Nm)')
plt.savefig(save_dir + r'\FLBrakeTorque.png')
plt.show()

plt.figure(figsize=(14, 8))
sns.boxplot(x='DrivingCondition', y='ESP_brakeTorqueReL', data=data_cleaned)
plt.title('Rear Left Brake Torque Under Different Driving Conditions')
plt.xlabel('Driving Condition')
plt.ylabel('Rear Left Brake Torque (Nm)')
plt.savefig(save_dir + r'\RLBrakeTorque.png')
plt.show()

