
# Tesla Model 3 Data Analysis Summary

## Overview
This document summarizes the analysis performed on the Tesla Model 3 running on a straight airfield, focusing on motor currents, torque, and vehicle speed relationships.

## How to Read Scatter Plots
Scatter plots are used to determine the possible relationship between two variables. Here's a guide on how to read them:
- **Identify Axes**: Each axis represents one of the variables. For our analysis, motor current (in Amperes) and torque (in Newton-meters) were plotted.
- **Observe Data Distribution**: Look at how the data points are spread across the plot. In our plots, points generally follow a linear path upward, suggesting a positive relationship.
- **Assess Trends**: A line of best fit (if included) or the general direction of the data points can indicate trends. In our scatter plots, rising points suggest that as motor current increases, so does torque.
- **Spot Outliers**: Points that fall far from the general group of data points are outliers. These may indicate anomalies in the data or special cases. In our plots, check for any points that do not align with the general trend.

## Theoretical Expectations vs. Observations

### Motor Current and Torque
**Theoretical Expectation**:
- Torque in an electric motor is directly proportional to the current, suggesting a linear relationship.

**Observations from Scatter Plots**:
- Scatter plots showed a generally linear relationship between motor current and torque, suggesting proper motor function and sensor accuracy.

**Observations from Line Graphs**:
- Line graphs provided a clear visualization of increasing torque with increasing current, confirming the theoretical linear relationship.

### Vehicle Speed and Torque
**Theoretical Expectation**:
- Higher torque is required at lower speeds to overcome inertia; as speed increases, less torque is required.

**Observations from Scatter Plots**:
- Decrease in torque as vehicle speed increases, indicating efficient motor operation at higher speeds with reduced torque needs.

**Observations from Line Graphs**:
- The decreasing trend in torque with increased vehicle speed was clearly visible in line graphs, providing a smooth illustration of dynamic changes in torque requirements.

## Conclusions
- The data generally matches theoretical knowledge, indicating reliable sensor performance and accurate data logging. This provides a solid foundation for further detailed analysis and predictive modeling.

## Next Steps
- Proceed with regression modeling, correlation analysis, and predictive modeling to further quantify relationships and predict future performance based on current data.

## Correlation Matrix Analysis
A correlation matrix was generated to visualize the relationships between all relevant numerical parameters in the dataset. This matrix helps in identifying which variables are strongly related, which can guide further analysis and model building.

### Observations from Correlation Matrix:
- Strong correlations were observed between motor current and torque, suggesting a direct relationship as expected.
- Vehicle speed shows varying degrees of correlation with torque and current, reflecting the complex dynamics of vehicle operation.

## Regression Analysis
Regression models were built to quantify the relationships:
- **Front Motor**: The regression analysis indicated no significant linear relationship between motor current and torque.
- **Rear Motor**: A weak but statistically significant negative relationship was found, which is unusual and suggests further investigation.

## Time Series Analysis
Time series analysis was performed on the front motor torque over time:
- **Trends**: Fluctuations in torque were observed, indicating varying operational conditions.
- **Cyclic Patterns**: Repeating patterns suggest periodic driving behaviors or operational cycles.
- **Stability**: Certain periods showed stable torque, indicating consistent motor performance.

### Analysis Outcome:
- The time series plot showed how motor torque varied over time, helping identify operational trends and patterns.

## Conclusion and Next Steps
Further decomposition and stationarity checks are recommended to deepen the understanding of time-dependent behaviors in motor torque.


## Detailed Analysis of Regenerative Braking

### Correlation Matrix Findings
- **Motor Performance**: Strong correlations between motor currents and torques indicate that motors are responding predictably to changes in electrical input.
- **Energy Recovery**: The correlations between vehicle speed reductions and regenerative energy changes were less pronounced, suggesting variability in how effectively energy is recovered.

### Line Graph Analysis
- **Dynamic Relationships**: The line graph illustrated how vehicle speed, front motor current, and regenerative energy change are interconnected over time.
- **Key Observations**:
  - Decreases in vehicle speed are generally accompanied by increases in motor current and changes in regenerative energy.
  - The effectiveness of regenerative braking varies, with some events showing significant energy recovery and others showing minimal changes.

### Conclusions from Graphical Analysis
- The motor performance during regenerative braking aligns with theoretical expectations, confirming the system's responsiveness.
- The efficiency of energy recovery during regenerative braking shows inconsistencies, highlighting areas for potential system improvement or further investigation.

### Recommendations
- Further detailed time-series analysis of regenerative braking events can help in understanding the conditions under which the system performs optimally.
- Advanced predictive modeling and data validation techniques are recommended to forecast energy recovery and validate sensor accuracy.

## Detailed Analysis of Regenerative Braking Efficiency

### Correlation Matrix and Line Graph
- The correlation matrix and line graphs provided insights into how SOC levels and motor performance metrics relate to regenerative braking efficiency. 
- No clear linear trends were observed in the correlation analysis, suggesting that regenerative braking efficiency is influenced by a complex set of factors.

### Heatmap of Efficiency Distribution
- The heatmap illustrated the distribution of efficiency levels across different SOC ranges, highlighting the variability and lack of consistent trends.

### Regression Analysis Findings
- The regression model, which included motor currents, torques, vehicle speed, and SOC as predictors, showed a very low R-squared value, indicating that these variables alone do not adequately explain the variability in regenerative braking efficiency.
- High p-values for all predictors suggest that none significantly impact efficiency, pointing to the potential need for exploring non-linear relationships or additional variables.

### Conclusions
- The analysis indicates that regenerative braking efficiency is not strongly or linearly correlated with the studied parameters under the current modeling approach.
- Further investigation using more complex models or additional data might be necessary to better understand the influencing factors.

### Recommendations for Further Analysis
- Consider non-linear modeling techniques or the inclusion of additional variables such as environmental factors or more detailed driving behavior metrics.
- Review data quality and collection methods to ensure the accuracy and comprehensiveness of the dataset used for analysis.

## Visualization of Regenerative Braking Dynamics

### Graph 1: Regenerative Energy Change and Vehicle Speed
- This graph highlights the relationship between vehicle speed and regenerative energy recovery, illustrating how changes in speed directly affect the amount of energy regained during braking.

### Graph 2: Rear Motor Current and Smooth Battery Current
- The graph visualizes the electrical currents of the rear motor and the battery, providing insights into the electrical behavior during regenerative braking events. It helps in understanding how efficiently the motor and battery handle the energy recovery process.

### Insights from Split Graphs
- The separation of data into two distinct graphs allowed for a clearer analysis, reducing visual clutter and focusing on specific dynamics relevant to regenerative braking efficiency.
- Observations indicate that there are critical moments where vehicle speed reductions significantly impact energy recovery, and the interaction between motor and battery currents can inform optimizations in the vehicle's regenerative braking system.

### Conclusion
- The split graphs effectively demonstrate the complex interactions within the regenerative braking system and can guide further detailed analysis or potential system improvements based on observed trends and behaviors.

## Analysis of Motor Performance Data from Graphs and Theoretical Considerations

### Observations and Theoretical Insights
- **Motor Currents and Regenerative Braking**:
  - The increase in motor currents during braking indicates active regenerative braking, particularly with higher peaks in the rear motor suggesting its prominent role in energy recovery.
- **Motor Torques and Energy Conversion**:
  - Negative torques observed in the graphs confirm the conversion of kinetic energy into electrical energy, highlighting efficient regenerative braking.
- **Differential Motor Power Output**:
  - The rear motor's more significant negative power output during braking suggests better optimization for regenerative purposes, potentially due to vehicle design and drivetrain configuration.

### Conclusions
- The analysis demonstrates the Tesla Model 3's effective use of regenerative braking to enhance energy efficiency and extend battery life.
- Understanding the distinct roles of front and rear motors in regenerative braking can help in refining vehicle control systems for improved energy management.

### Recommendations for Vehicle Design and Control Strategies
- Further research could explore optimizing both motors’ contributions to maximize regenerative braking benefits under varying conditions.
- Vehicle design could be tweaked to balance the load and enhance regenerative braking efficiency, possibly through software updates or changes in drivetrain mechanics.
