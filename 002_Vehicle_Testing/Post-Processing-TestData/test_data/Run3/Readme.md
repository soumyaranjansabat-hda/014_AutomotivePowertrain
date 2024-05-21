# Vehicle Charging Data Analysis

## Overview
This analysis provides insights into the charging patterns and battery performance of a Tesla Model 3 during a city drive. The data includes various parameters such as battery voltage, state of charge (SOC), and energy charged via DC and AC chargers.

## 1. Charging Patterns

- **DC Charger kWh Total over Time**: This plot illustrates the cumulative energy added to the battery via DC charging over time.

- **AC Charger kWh Total over Time**: This plot illustrates the cumulative energy added to the battery via AC charging over time.

- **Battery Voltage over Time**:
This plot shows how the battery voltage changes over time, providing insight into the battery's behavior during the charging process.

- **State of Charge (SOC) over Time**:
This plot displays the SOC as a percentage, indicating the battery's charge level over time.

- **Insigtful Conclusion**: The analysis highlights the charging patterns and battery performance during the city drive. The cumulative energy charged via DC and AC chargers provides an understanding of the charging behavior, while the battery voltage and SOC plots offer insights into the battery's performance.


## 2. Vehicle Charging Event Analysis

- This analysis provides insights into the charging patterns and battery performance of a Tesla Model 3 during a city drive. The data includes various parameters such as battery voltage, state of charge (SOC), and energy charged via DC and AC chargers.

### Charging Events Summary

- **DC Charging Events**: The summary of the identified DC charging events is as follows:

    - **DC_Charge_Event:** 1
    - **Time Start (relative)**: 368
    - **Time End (relative)**: 836
    - **Duration**: 468
    - **Energy Charged (kWh)**: 18.674

- **AC Charging Events**: There were no AC charging events identified in the data provided.

### Aggregated Charging Metrics

- **DC Charging**
    - **Total Energy Added**: 18.674 kWh
    - **Total Charging Duration**: 468 units of relative time

- **AC Charging**
    - **Total Energy Added**: 0 kWh
    - **Total Charging Duration**: 0 units of relative time

- **DC Charging Event Highlight**: This plot shows the entire timeline of DC charging, with the identified charging event highlighted in orange. It gives an overview of where the charging event occurs within the entire dataset.

- **Detailed View of DC Charging Event**: This plot zooms in on the identified charging event, showing the detailed energy charged over the duration of the event. It provides a closer look at how the energy accumulated over time during the charging process.

### Insigtful Conclusion
- The analysis highlights the charging patterns and battery performance during the city drive. The cumulative energy charged via DC and AC chargers provides an understanding of the charging behavior, while the battery voltage and SOC plots offer insights into the battery's performance.

## 4. Summary Statistics

### DC Charger kWh Total

- **Count**: 837
- **Mean**: 194.01 kWh
- **Standard Deviation**: 6.20 kWh
- **Minimum**: 188.79 kWh
- **25th Percentile**: 188.79 kWh
- **Median (50th Percentile)**: 190.47 kWh
- **75th Percentile**: 199.24 kWh
- **Maximum**: 207.49 kWh

### AC Charger kWh Total

- **Count**: 837
- **Mean**: 5072.03 kWh
- **Standard Deviation**: 9.10e-13 kWh (effectively zero, indicating no variation)
- **Minimum**: 5072.03 kWh
- **25th Percentile**: 5072.03 kWh
- **Median (50th Percentile)**: 5072.03 kWh
- **75th Percentile**: 5072.03 kWh
- **Maximum**: 5072.03 kWh

### Key Insights
- The **DC Charger** kWh total shows variation over time, with a mean of 194.01 kWh and a standard deviation of 6.20 kWh.
- The **AC Charger** kWh total remains constant at 5072.03 kWh across all measurements, indicating that there were no changes in AC charging during the observed period.

### Insightful Conclusion
- The analysis successfully identified charging events and calculated relevant metrics.
- The summary statistics provide insights into the distribution and variation of energy added during DC and AC charging sessions.
- The visualization provides a clear representation of the charging patterns for the Tesla Model 3.

### 5. SoC Visualization
- This plot shows the initial and final State of Charge (SoC) for the identified DC charging event:

### DC Charging Event Highlight
- This plot shows the entire timeline of DC charging, with the identified charging event highlighted in orange. It gives an overview of where the charging event occurs within the entire dataset.

### Detailed View of DC Charging Event
- This plot zooms in on the identified charging event, showing the detailed energy charged over the duration of the event. It provides a closer look at how the energy accumulated over time during the charging process.

### Insigtful Conclusion
- The analysis highlights the charging patterns and battery performance during the city drive. The cumulative energy charged via DC chargers provides an understanding of the charging behavior, while the battery voltage and SoC plots offer insights into the battery's performance.