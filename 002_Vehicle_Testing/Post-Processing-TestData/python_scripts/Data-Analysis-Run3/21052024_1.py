import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run3\Run3_FilterData.xlsx'
save_dir = r'E:\HDA_Lectures\001_Repository\014_AutomotivePowertrain\002_Vehicle_Testing\Post-Processing-TestData\test_data\Run3\Plots\21052024_1'
df = pd.read_excel(file_path, sheet_name='Sheet1')


## 1. Charging Patterns
# Plotting the charging patterns
plt.figure(figsize=(14, 7))

# Plotting DC Charger kWh Total
plt.subplot(2, 1, 1)
plt.plot(df['Time (relative)'], df['BMS_dcChargerKwhTotal'], label='DC Charger kWh Total')
plt.xlabel('Time (relative)')
plt.ylabel('DC Charger kWh Total')
plt.title('DC Charger kWh Total over Time')
plt.legend()

# Plotting AC Charger kWh Total
plt.subplot(2, 1, 2)
plt.plot(df['Time (relative)'], df['BMS_acChargerKwhTotal'], label='AC Charger kWh Total', color='orange')
plt.xlabel('Time (relative)')
plt.ylabel('AC Charger kWh Total')
plt.title('AC Charger kWh Total over Time')
plt.legend()

plt.tight_layout()
plt.savefig(save_dir + r'\DCACChargerKwhTotal.png')
plt.show()

# Plotting battery voltage and SOC over time
plt.figure(figsize=(14, 7))

# Plotting Battery Voltage
plt.subplot(2, 1, 1)
plt.plot(df['Time (relative)'], df['BattVoltage132'], label='Battery Voltage')
plt.xlabel('Time (relative)')
plt.ylabel('Battery Voltage (V)')
plt.title('Battery Voltage over Time')
plt.legend()

# Plotting State of Charge (SOC)
plt.subplot(2, 1, 2)
plt.plot(df['Time (relative)'], df['UI_SOC'], label='State of Charge (SOC)', color='green')
plt.xlabel('Time (relative)')
plt.ylabel('State of Charge (%)')
plt.title('State of Charge (SOC) over Time')
plt.legend()

plt.tight_layout()
plt.savefig(save_dir + r'\SOC.png')
plt.show()

## 2. Detailed Charging Event

# Identify charging events
df['DC_Charging'] = df['BMS_dcChargerKwhTotal'].diff().fillna(0) > 0
df['AC_Charging'] = df['BMS_acChargerKwhTotal'].diff().fillna(0) > 0

# Extract charging events
dc_charging_events = df[df['DC_Charging']].copy()
ac_charging_events = df[df['AC_Charging']].copy()

# Group by consecutive charging events
dc_charging_events['DC_Charge_Event'] = (dc_charging_events['DC_Charging'] != dc_charging_events['DC_Charging'].shift()).cumsum()
ac_charging_events['AC_Charge_Event'] = (ac_charging_events['AC_Charging'] != ac_charging_events['AC_Charging'].shift()).cumsum()

# Summarize charging events
dc_charging_summary = dc_charging_events.groupby('DC_Charge_Event').agg(
    {
    'Time (relative)': ['min', 'max'],
    'BMS_dcChargerKwhTotal': ['min', 'max']
    }
)

ac_charging_summary = ac_charging_events.groupby('AC_Charge_Event').agg(
    {
    'Time (relative)': ['min', 'max'],
    'BMS_acChargerKwhTotal': ['min', 'max']
    }
)

# Calculate duration and energy charged for each event
dc_charging_summary['Duration'] = dc_charging_summary[('Time (relative)', 'max')] - dc_charging_summary[('Time (relative)', 'min')]
dc_charging_summary['Energy_Charged'] = dc_charging_summary[('BMS_dcChargerKwhTotal', 'max')] - dc_charging_summary[('BMS_dcChargerKwhTotal', 'min')]

ac_charging_summary['Duration'] = ac_charging_summary[('Time (relative)', 'max')] - ac_charging_summary[('Time (relative)', 'min')]
ac_charging_summary['Energy_Charged'] = ac_charging_summary[('BMS_acChargerKwhTotal', 'max')] - ac_charging_summary[('BMS_acChargerKwhTotal', 'min')]


# Aggregate the metrics for overall understanding
total_dc_energy_added = dc_charging_summary['Energy_Charged'].sum()
total_dc_charging_duration = dc_charging_summary['Duration'].sum()

total_ac_energy_added = ac_charging_summary['Energy_Charged'].sum()
total_ac_charging_duration = ac_charging_summary['Duration'].sum()


# Plotting the entire DC charging data with the identified event highlighted
plt.figure(figsize=(14, 7))

plt.plot(df['Time (relative)'], df['BMS_dcChargerKwhTotal'], label='DC Charger kWh Total')
plt.axvspan(dc_charging_summary[('Time (relative)', 'min')][1], dc_charging_summary[('Time (relative)', 'max')][1], color='orange', alpha=0.3, label='DC Charging Event')

plt.xlabel('Time (relative)')
plt.ylabel('DC Charger kWh Total')
plt.title('DC Charger kWh Total over Time with Charging Event Highlighted')
plt.legend()
plt.savefig(save_dir + r'\DCChargerKwhTotal.png')
plt.show()

# Zooming in on the identified charging event
event_start = dc_charging_summary[('Time (relative)', 'min')][1]
event_end = dc_charging_summary[('Time (relative)', 'max')][1]

charging_event_df = df[(df['Time (relative)'] >= event_start) & (df['Time (relative)'] <= event_end)]

plt.figure(figsize=(14, 7))
plt.plot(charging_event_df['Time (relative)'], charging_event_df['BMS_dcChargerKwhTotal'], label='DC Charger kWh Total', color='orange')

plt.xlabel('Time (relative)')
plt.ylabel('DC Charger kWh Total')
plt.title('Detailed View of DC Charging Event')
plt.legend()
plt.savefig(save_dir + r'\DCChargerKwhTotal_Zommed.png')
plt.show()

## 4. Summary Statistics
dc_summary = df['BMS_dcChargerKwhTotal'].describe()
ac_summary = df['BMS_acChargerKwhTotal'].describe()

print(dc_summary)
print(ac_summary)

## 5. SoC Visualization

# Calculate the initial and after charging SoC (State of Charge) for the identified DC charging event
dc_charging_events['Initial_SoC'] = dc_charging_events.groupby('DC_Charge_Event')['UI_SOC'].transform('first')
dc_charging_events['Final_SoC'] = dc_charging_events.groupby('DC_Charge_Event')['UI_SOC'].transform('last')

# Summarize SoC for each DC charging event
dc_charging_soc_summary = dc_charging_events.groupby('DC_Charge_Event').agg({
    'Initial_SoC': 'first',
    'Final_SoC': 'last'
})

# Calculate the increase in SoC
dc_charging_soc_summary['SoC_Increase'] = dc_charging_soc_summary['Final_SoC'] - dc_charging_soc_summary['Initial_SoC']

# Plot initial vs. final SoC

plt.figure(figsize=(10, 6))

# Plotting initial and final SoC
plt.bar(['Initial SoC', 'Final SoC'], [dc_charging_soc_summary['Initial_SoC'][1], dc_charging_soc_summary['Final_SoC'][1]], color=['blue', 'green'])

plt.xlabel('State of Charge (SoC)')
plt.ylabel('Percentage (%)')
plt.title('Initial vs. Final State of Charge (SoC)')
plt.ylim(0, 100)
plt.savefig(save_dir + r'\InitialFinalSoC.png')
plt.show()