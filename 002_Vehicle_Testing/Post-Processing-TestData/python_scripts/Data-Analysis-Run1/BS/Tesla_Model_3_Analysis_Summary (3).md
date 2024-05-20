
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

