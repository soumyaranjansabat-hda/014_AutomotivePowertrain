
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


-----


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Load the data
file_path = 'path_to_your_data.xlsx'
data_df = pd.read_excel(file_path, sheet_name='Data', skiprows=[1])

# Select relevant columns for analysis
motor_columns = [
    'FrontHighVoltage1A5', 'FrontMotorCurrent1A5', 'FrontPower2E5', 'FrontTorque1D5',
    'RearHighVoltage126', 'RearMotorCurrent126', 'RearPower266', 'RearTorque1D8', 'DI_vehicleSpeed'
]
motor_data_df = data_df[motor_columns]

# Visualization: Correlation Matrix
correlation_matrix = motor_data_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix Heatmap')
plt.show()

# Regression Analysis: Motor Current vs. Torque
# Prepare data for regression analysis
front_motor_X = sm.add_constant(motor_data_df['FrontMotorCurrent1A5'])
rear_motor_X = sm.add_constant(motor_data_df['RearMotorCurrent126'])

# Response variables
front_motor_y = motor_data_df['FrontTorque1D5']
rear_motor_y = motor_data_df['RearTorque1D8']

# Fit regression models
front_motor_model = sm.OLS(front_motor_y, front_motor_X).fit()
rear_motor_model = sm.OLS(rear_motor_y, rear_motor_X).fit()

# Get the regression summary for both models
print(front_motor_model.summary())
print(rear_motor_model.summary())

# Time Series Analysis: Front Motor Torque Over Time
# Convert 'Time (relative)' to a numeric format and set it as the index
data_df['Time (relative)'] = pd.to_numeric(data_df['Time (relative)'], errors='coerce')
time_series_df = data_df.set_index('Time (relative)')

# Plotting Front Motor Torque over Time
plt.figure(figsize=(12, 6))
plt.plot(time_series_df['FrontTorque1D5'], label='Front Motor Torque')
plt.title('Front Motor Torque Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Torque (Nm)')
plt.legend()
plt.show()


----