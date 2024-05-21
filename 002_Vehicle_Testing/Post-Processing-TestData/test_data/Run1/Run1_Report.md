# Tesla Model 3 Vehicle Testing Data Analysis

## Overview
This report provides an analysis of vehicle testing data for a Tesla Model 3 conducted on an airfield. The analysis includes statistical summaries, visualizations, and interpretations of key parameters such as regenerative braking, motor efficiecny, vehicle stability, battery life, voltage, speed, state of charge, and range.

## Objective
The main objective of this analysis is to understand general trends, identify potential outliers, and observe any anomalies in the dataset that could provide insights into vehicle performance and behavior during the test.

## Data Summary
The dataset consists of 746 entries, each representing a different time point during the vehicle testing. Key parameters analyzed include motor relevant parameters such as current, torque, voltage etc, battery energy, voltages, wheel speeds, state of charge, and driving range, ESP vehicle stability parameters etc.

## Observations: Statistical Summary

### Brief
- **Battery Life**: Constant at 74.5 kWh.
- **Battery Voltages**: Ranges observed from as low as 2.984 V to as high as 3.820 V, indicating variations likely due to load changes or other test conditions.
- **Wheel Speeds**: Showed a broad range from 0 km/h (stationary) to 144 km/h (likely during high-speed tests), with mean speeds around 15-16 km/h.
- **State of Charge**: Relatively stable around 47%, with minor fluctuations indicating balanced battery usage.
- **Range**: Reported consistently between 150 to 162 miles. (241 to 240 Km)

### Visualizations
Time-series plots were created for battery voltages, state of charge, and wheel speeds, illustrating:
- Fluctuations in battery voltages that could be tied to specific test conditions.
- Stable state of charge throughout the testing period.
- Variation in wheel speeds from stationary phases to high-speed runs.

### Significant Findings
- Voltage variations could be explored further to understand the impact of different test maneuvers or environmental conditions.
- The stability of the state of charge and the battery management system's effectiveness during diverse testing scenarios.
- High-speed tests are clearly indicated by the wheel speed data, highlighting the vehicle's performance capabilities.

### Inference from Statistical Summary
The analysis provided valuable insights into the vehicle's performance under test conditions. Further detailed analysis could focus on specific periods of interest or additional parameters to deepen the understanding of vehicle dynamics and battery performance.

# Vehicle Testing Data Analysis

## 1. Battery Voltage Stability vs. Wheel Speed

**Observations from the Graph:**
- The scatter plot reveals a distribution of battery voltage across various wheel speeds. Notably, there does not appear to be a clear trend indicating a direct relationship between speed and voltage, suggesting that battery voltage remains relatively stable across different speeds.
- The color hue indicates variations in voltage at similar speed levels, showing some degree of variability that does not seem directly tied to the speed.

**Theoretical Insights:**
- Battery voltage stability across a range of operating conditions (like different speeds) is crucial for reliable vehicle performance. Theoretical knowledge suggests that good battery management systems should regulate voltage effectively, maintaining it within a safe and functional range despite the demand changes due to speed variations.
- A stable voltage despite varied speeds supports the efficiency of the vehicle’s power system, indicating robustness in the battery's ability to handle different power demands without significant performance degradation.

**Insightful Conclusion:**
- The observed stability in battery voltage across a broad range of speeds is a positive indication of the vehicle’s electrical system performance. It suggests that the battery management system efficiently handles the power requirements at different speeds without causing significant voltage drops or spikes, which are critical for the longevity and safety of the battery.
- However, the variations in voltage at similar speeds suggest that factors other than speed, possibly environmental conditions or internal system efficiencies, might influence voltage levels. Further detailed analysis could focus on these factors to optimize battery performance and vehicle reliability.

## 2. Energy Efficiency Over Time

**Observations from the Graph:**
- The graph shows fluctuations in energy efficiency (measured in kWh per km) over the test period.
- There are periods of increased energy efficiency, suggesting less energy is consumed per kilometer, and periods of decreased efficiency, indicating higher energy consumption.

**Theoretical Insights:**
- Energy efficiency in electric vehicles can be influenced by factors such as driving behavior, terrain, and vehicle load. Theoretically, steady and moderate speeds on flat terrains should yield better energy efficiency compared to high speeds, frequent acceleration, or driving on hilly terrains.
- Variations in efficiency may also reflect changes in external conditions (e.g., wind resistance, road surface) and internal vehicle dynamics (e.g., battery temperature, drivetrain efficiency).

**Insightful Conclusion:**
- Identifying periods of low efficiency can help diagnose potential issues with driving habits or vehicle performance. For instance, if low efficiency coincides with periods of high speed or frequent acceleration, driving behavior modifications can be suggested.
- Continuous monitoring and analysis of energy efficiency trends can guide improvements in vehicle design and battery management systems, optimizing overall energy consumption and extending the vehicle's range.

## 3. Battery Discharge Rate Over Time

**Observations from the Graph:**
- The graph shows variations in the battery discharge rate (measured in kWh per second) throughout the test period.
- There are spikes in the discharge rate, indicating periods where the vehicle demanded higher power, possibly due to acceleration or other high-power activities.

**Theoretical Insights:**
- The discharge rate should correlate with the vehicle's power demands. High discharge rates typically occur during acceleration, uphill driving, or when additional power is needed for auxiliary systems.
- The battery management system should ideally smooth out these demands to prevent excessive strain on the battery, which can degrade its performance and lifespan over time.

**Insightful Conclusion:**
- Periods with high discharge rates could signal opportunities to optimize power management, such as smoothing out power demands through regenerative braking or better acceleration control.
- Consistent monitoring of discharge rates can help in predictive maintenance by identifying patterns that lead to high battery strain, thus allowing preemptive actions to extend battery life and maintain vehicle performance.

## 4. Correlation Between State of Charge and Battery Voltage

**Observations from the Graph:**
- The scatter plot shows the relationship between the battery voltage and the state of charge (SOC). There is a general trend where higher voltages correspond to higher states of charge.
- The points are dispersed, but a positive correlation can be observed.

**Theoretical Insights:**
- In theory, as the battery discharges (lower SOC), the voltage should drop. Conversely, a fully charged battery (higher SOC) typically exhibits higher voltage levels.
- This relationship is critical for the battery management system to accurately estimate the remaining range and ensure safe operating conditions by preventing over-discharge or overcharge.

**Insightful Conclusion:**
- The observed positive correlation aligns with theoretical expectations, indicating that the battery voltage can be a reliable indicator of the state of charge.
- Monitoring this relationship helps in maintaining battery health by ensuring it operates within safe voltage and SOC ranges, thereby extending battery life and optimizing performance.

## 5. Anomaly Detection in Wheel Speeds

**Observations from the Graph:**
- The plot shows the speeds of all four wheels over time. Generally, the wheel speeds follow a similar pattern, suggesting consistent driving conditions.
- There are periods where wheel speeds drop to zero, indicating stops or idle periods.
- Any significant discrepancies between wheel speeds at the same timestamp could indicate sensor issues or mechanical problems.

**Theoretical Insights:**
- In a well-functioning vehicle, the speeds of all four wheels should be closely aligned, especially when driving straight. Differences might occur during turns due to differential speed requirements.
- Significant deviations could signal potential problems like sensor malfunctions, tire issues, or differential problems, which could impact vehicle safety and performance.

**Insightful Conclusion:**
- Consistent wheel speeds indicate good vehicle alignment and proper functioning of the drivetrain. This consistency is crucial for maintaining vehicle stability and safety.
- Identifying anomalies or discrepancies can help in early detection of mechanical issues or sensor faults, allowing for timely maintenance and preventing potential safety hazards.

# Motor Performance During Braking Analysis

## 1. Motor Currents During Braking

**Observations:**
- Spikes in motor currents during braking events.
- Distinct patterns in front and rear motor currents.
- Front Motor Current (FrontMotorCurrent1A5): Mostly around 989 A, suggesting consistent motor behavior during braking.
- Rear Motor Current (RearMotorCurrent126): Similar behavior but with a greater spread, up to 1800 A, indicating a potentially different or additional role in braking dynamics.

**Theoretical Insights:**
- During regenerative braking, motor currents should increase as the motors act as generators to recover energy.
- In electric vehicles, motor currents during braking are indicative of regenerative braking where the motors act as generators. Higher currents in the rear motor may suggest a configuration where the rear motor is more actively involved in regenerative braking, possibly due to its positioning or the vehicle’s weight distribution.

**Insightful Conclusions:**
- The spikes in motor currents confirm the occurrence of regenerative braking, where the vehicle recovers energy and stores it back in the battery.
- The rear motor exhibits higher peaks potentially indicating a higher contribution to braking efforts or the influence of regenerative braking dynamics.

## 2. Motor Torques During Braking

**Observations:**
- Negative torque values during braking events.
- Front Torque (FrontTorque1D5): Negative values primarily, averaging around -5.62 Nm, which supports regenerative braking by generating torque in the opposite direction of travel.
- Rear Torque (RearTorque1D8): Also negative, averaging -15.51 Nm, a more pronounced effect possibly indicating greater regenerative contribution from the rear.

**Theoretical Insights:**
- Negative torques indicate the motors are providing braking force, which is typical for regenerative braking.
- Negative torques in this context mean that the motors are working to slow the vehicle down, converting kinetic energy back into electrical energy. The magnitude of these torques can provide insights into the efficiency of energy conversion.
- The front and rear motors may exhibit different torque profiles due to weight distribution, braking system design, and the specific algorithms used for brake force distribution.

**Insightful Conclusions:**
- The negative torques suggest effective regenerative braking (generating torque opposite to the direction of wheel rotation), reducing wear on mechanical brakes and improving energy efficiency.
- The rear motor occasionally reaches positive values, perhaps indicating moments where it supports propulsion or stabilizes the vehicle during braking.
- The front and rear motors may exhibit different torque profiles due to weight distribution, braking system design, and the specific algorithms used for brake force distribution.
- The variations in torque values suggest that the braking system dynamically adjusts the braking forces on the front and rear axles, potentially optimizing for stability and energy recovery.
- Analyzing these torque trends can help improve the design of braking systems and algorithms to enhance vehicle safety and efficiency, particularly in regenerative braking scenarios.

## 3. Motor Power During Braking

**Observations:**
- Power values drop significantly during braking.
- Front Power (FrontPower2E5) and Rear Power (RearPower266): Both show negative values indicating power generation, which is characteristic of regenerative braking. The rear shows more significant power generation.

**Theoretical Insights:**
- Lower power consumption during braking indicates energy recovery instead of energy expenditure.
- Negative power values confirm the operation of regenerative braking. The greater negative values in the rear suggest a higher efficiency or a greater contribution to energy recovery, which might be due to better optimization of the rear drivetrain for regenerative purposes.

**Insightful Conclusions:**
- The reduced power values corroborate the effectiveness of regenerative braking in conserving energy.
- Both motors show fluctuations between positive and negative values, with negative values predominant, which indicates power generation during braking. 
- The rear motor generally contributes more to power generation, consistent with its higher torque readings.

## 4. Motor Efficiencies Over Time

**Observations:**
- Significant fluctuations in efficiencies for both front and rear motors over time.
- Frequent zero and occasional negative efficiency values.

**Theoretical Insights:**
- Ideal motor efficiency should be high (typically above 80%) under normal operating conditions. The observed low mean efficiency values suggest measurement issues or periods where the motors are not under load.
- Fluctuations in efficiency can be attributed to varying operational conditions such as acceleration, deceleration, and regenerative braking.

**Insightful Conclusions:**
- The efficiency trends highlight the importance of context in interpreting efficiency data. High fluctuations and frequent zero values suggest motors are not consistently under load throughout the test period.
- Identifying periods of high efficiency could provide insights into optimal operating conditions for the motors, whereas low or zero efficiency periods might correspond to idling or low-demand phases.
- Filtering data to exclude periods where motors are not actively used could provide more meaningful efficiency metrics.


## 5. Front and Rear Motor Efficiency & Mechanical Output Over Time

**Front Motor Efficiency**
- **Observation**: The front motor efficiency varies over time, with some noticeable fluctuations. The efficiency remains below 0.15 throughout the test.
- **Insight**: The relatively low efficiency values suggest that the front motor might not be operating at optimal conditions for most of the time. The fluctuations indicate varying load conditions and possibly frequent transitions between motoring and regenerative braking modes.

**Rear Motor Efficiency**
- **Observation**: The rear motor efficiency also fluctuates over time, with efficiency values generally staying below 0.15. The plot shows several gaps, which might be due to periods where the efficiency could not be calculated (e.g., when the power input is zero or very low).
- **Insight**: Similar to the front motor, the rear motor's efficiency is relatively low and variable. This indicates non-ideal operating conditions and frequent changes in load and operating modes.

**Comparison of Front and Rear Motor Efficiency**
- **Insight**: Both motors exhibit low and fluctuating efficiencies, suggesting that they are not always operating within their optimal efficiency ranges. This could be due to the nature of the test conditions, which likely involve frequent acceleration and deceleration, leading to variable load conditions.

**Mechanical Power Output Over Time**
**Front and Rear Mechanical Power**
- **Observation**: The mechanical power output for both the front and rear motors shows significant fluctuations over time. There are periods of positive power (motoring) and negative power (regenerative braking).
- **Insight**: The spikes in mechanical power output correspond to periods of heavy acceleration or braking. The positive peaks indicate times when the motors are providing significant driving force, while the negative peaks indicate regenerative braking events where the motors are recovering energy.

**Comparison of Mechanical Power Output**
- **Insight**: Both the front and rear motors contribute to the vehicle's mechanical power output, with the rear motor showing slightly higher peaks in both positive and negative directions. This suggests that the rear motor might be more actively involved in both driving and regenerative braking.

**Overall Analysis**

**Motor Efficiency**
- The overall low efficiency values for both motors suggest that the vehicle's motors are often operating under suboptimal conditions. This could be due to the dynamic nature of the test, involving frequent changes in speed and load.
- The fluctuating efficiency values indicate that the motors are transitioning between different operating modes, such as acceleration, cruising, and regenerative braking.

**Mechanical Power Output**
- The significant fluctuations in mechanical power output reflect the vehicle's dynamic performance during the test. The periods of high positive and negative power correspond to heavy acceleration and braking events, respectively.
- The rear motor seems to be more actively involved in both driving and regenerative braking, as indicated by the slightly higher peaks in mechanical power output.

**Insightful Conclusions:**
- The visualizations provide insights into the vehicle's motor performance during the test. Both the front and rear motors exhibit low and fluctuating efficiencies, suggesting non-ideal operating conditions. The mechanical power output shows significant variations, reflecting the dynamic nature of the test. The rear motor appears to play a slightly more active role in both driving and regenerative braking compared to the front motor. This analysis highlights the importance of optimizing motor operation to improve overall efficiency and performance.

# Regenerative Braking Analysis

## 1. Regenerative Efficiency Calculation

**Observations:**
- The refined plot now shows regenerative efficiency over time, with values fluctuating significantly.
- Efficiency values range from near zero to around 100%, indicating variability in the effectiveness of regenerative braking during different driving conditions.

**Theoretical Insights:**
- Regenerative braking efficiency can vary based on several factors such as vehicle speed, braking intensity, and battery state. High efficiency indicates effective energy recovery, while low efficiency suggests less effective regeneration.
- The fluctuations are expected due to the dynamic nature of driving conditions and braking events.

**Insightful Conclusions:**
- The observed fluctuations in regenerative efficiency highlight the variable nature of energy recovery during different driving conditions.
- Identifying periods of high efficiency can provide insights into optimal conditions for regenerative braking, which can inform strategies to maximize energy recovery.

## 2. Impact on Battery State of Charge (SOC)

**Observations:**
- The SOC shows a gradual decline with intermittent increases, indicating periods of discharge and recharge.
- Increases in SOC correspond to regenerative braking events where energy is recovered and stored in the battery.

**Theoretical Insights:**
- Regenerative braking should positively impact SOC by recharging the battery during braking events. The SOC should increase during these periods, reflecting the energy recovered.
- A well-designed regenerative braking system can extend the range of the vehicle by effectively utilizing braking events to recharge the battery.

**Insightful Conclusions:**
- The observed increases in SOC during regenerative braking events confirm the effectiveness of the regenerative braking system in recharging the battery.
- Monitoring SOC trends in conjunction with regenerative braking can help optimize the balance between energy consumption and recovery, enhancing overall vehicle efficiency.

## 3. Dynamic Braking Strategy

**Observations:**
- Both front and rear power during braking events show significant variations.
- The power distribution between the front and rear motors varies, indicating a dynamic braking strategy that adjusts based on driving conditions.

**Theoretical Insights:**
- Dynamic braking strategies aim to optimize braking performance and energy recovery by distributing braking power between the front and rear motors. This distribution can enhance vehicle stability and maximize regenerative braking efficiency.
- The variations in power suggest adaptive control mechanisms that respond to different driving scenarios.

**Insightful Conclusions:**
- The observed dynamic power distribution between the front and rear motors highlights the sophistication of the braking strategy, which adapts to optimize performance and energy recovery.
- Understanding these power distribution patterns can inform improvements in braking algorithms to further enhance regenerative braking efficiency and vehicle stability.

## 4. Energy Recovered During Braking Events

**Observations:**
- The cumulative energy recovered graph shows a steady increase over time, reflecting the total energy recovered during braking events.
- The total energy recovered during the test period is approximately 0.214 kWh.

**Theoretical Insights:**
- Effective regenerative braking systems should show a steady increase in cumulative energy recovered, indicating consistent energy recovery during braking events.
- The amount of energy recovered depends on the frequency and intensity of braking events, as well as the efficiency of the regenerative braking system.

**Insightful Conclusions:**
- The steady increase in cumulative energy recovered confirms the consistent performance of the regenerative braking system.
- Quantifying the total energy recovered provides valuable insights into the contribution of regenerative braking to overall energy efficiency and vehicle range.

# Energy Related Study
## 1. Energy Consumption During Acceleration

**Observations:**
- The graph shows the energy consumed during acceleration events, with noticeable spikes indicating periods of significant energy use.
- The energy consumption is not uniform, reflecting varying degrees of acceleration.

**Theoretical Insights:**
- During acceleration, especially rapid or intense acceleration, the energy consumption of an electric vehicle increases significantly. This is because the motors draw more power to increase the vehicle's speed.
- The efficiency of the powertrain and the state of charge of the battery can also affect the energy consumption during these periods.

**Insightful Conclusions:**
- The spikes in energy consumption during acceleration events highlight the periods of high power demand. Understanding these patterns can help optimize driving strategies to improve energy efficiency.
- By analyzing energy consumption during acceleration, we can identify driving behaviors that lead to excessive energy use and develop strategies to mitigate them, such as smoother acceleration practices or optimizing the vehicle's powertrain for better efficiency.

## 2. Energy Efficiency During Acceleration

**Observations:**
- The graph shows significant fluctuations in energy efficiency during acceleration events.
- Efficiency values range widely, with some periods exhibiting higher efficiency and others showing lower efficiency.

**Theoretical Insights:**
- Energy efficiency during acceleration can be influenced by various factors, including the state of the battery, the powertrain's efficiency, and the driving conditions (e.g., road incline, vehicle load).
- The efficiency is expected to be lower during rapid or intense acceleration due to higher power demands and potential losses in the powertrain.

**Insightful Conclusions:**
- The observed fluctuations in energy efficiency during acceleration highlight the dynamic nature of energy use in electric vehicles. Identifying the conditions that lead to higher efficiency can inform driving strategies to optimize energy use.
- Periods of lower efficiency suggest areas for potential improvement in the vehicle's powertrain or battery management system to better handle high-power demands.
- Further analysis could focus on specific factors that influence efficiency, such as battery temperature, vehicle load, and driving conditions, to develop more refined strategies for improving energy efficiency during acceleration.

## 3. Correlation Between Energy Consumption and Speed

**Observations from the Scatter Plot:**
- The scatter plot shows a positive correlation between energy consumption and speed. As the speed increases, energy consumption also increases.
- The data points are dispersed, indicating variability in energy consumption at different speeds.

**Observations from the Line Plot:**
- The line plot illustrates how energy consumption and speed vary over time.
- Peaks in energy consumption often coincide with peaks in speed, suggesting higher energy use during higher speeds.

**Correlation Coefficient:**
- The calculated correlation coefficient is approximately 0.718, indicating a strong positive correlation between energy consumption and speed.

**Theoretical Insights:**
- Higher speeds generally require more power, leading to increased energy consumption. This is consistent with the observed positive correlation.
- The variability in energy consumption at similar speeds could be due to factors such as road conditions, driving behavior, and vehicle load.

**Insightful Conclusions:**
- The strong positive correlation between speed and energy consumption highlights the impact of driving speed on energy efficiency. Reducing speed can significantly decrease energy consumption, extending the vehicle's range.
- The variability in energy consumption suggests that other factors also play a role. Further analysis could focus on isolating these factors to better understand their impact on energy efficiency.
- Identifying optimal speed ranges that balance performance and energy efficiency can inform driving strategies to maximize range and reduce energy costs.

# Powertrain Performance During Acceleration

## 1. Motor Currents During Acceleration

**Observations:**
- The graph shows the front and rear motor currents during acceleration events.
- Both front and rear motor currents increase significantly during acceleration, with the front motor current generally being higher than the rear motor current.

**Theoretical Insights:**
- Higher motor currents during acceleration indicate increased electrical power being supplied to the motors to achieve the desired acceleration.
- The front motor often handles more power due to the vehicle's weight distribution and design, which may favor front-wheel drive or balanced all-wheel drive configurations.

**Insightful Conclusions:**
- The significant increase in motor currents during acceleration highlights the power demand on the vehicle's electrical system.
- Understanding the distribution of current between the front and rear motors can help optimize the powertrain for better performance and efficiency.

## 2. Motor Torques During Acceleration

**Observations:**
- The graph shows the front and rear motor torques during acceleration events.
- Both front and rear torques increase during acceleration, with the front torque generally being higher than the rear torque.

**Theoretical Insights:**
- Torque is directly related to the force applied by the motors to propel the vehicle. Higher torques during acceleration are necessary to overcome inertia and increase vehicle speed.
- The distribution of torque between the front and rear motors can affect the vehicle's handling and stability.

**Insightful Conclusions:**
- The increase in motor torques during acceleration underscores the mechanical demands on the vehicle's powertrain.
- Optimizing torque distribution can enhance vehicle performance, handling, and stability during acceleration.

## 3. Motor Power Outputs During Acceleration

**Observations:**
- The graph shows the front and rear motor power outputs during acceleration events.
- Both front and rear motor power outputs increase significantly during acceleration, with the front motor power output generally being higher than the rear motor power output.

**Theoretical Insights:**
- Power output is the product of current and voltage. Higher power outputs during acceleration indicate the combined electrical and mechanical effort required to increase vehicle speed.
- The power distribution between the front and rear motors reflects the vehicle's design and performance characteristics.

**Insightful Conclusions:**
- The significant increase in motor power outputs during acceleration highlights the energy demand on the vehicle's powertrain.
- Analyzing power distribution can help improve the efficiency and performance of the vehicle's acceleration capabilities.

## 4. Average Energy Efficiency at Various Speeds

**Observations:**
- The bar plot shows the average energy efficiency at different speed ranges (bins).
- Energy efficiency tends to decrease as the speed increases, indicating higher energy consumption per unit distance at higher speeds.

**Theoretical Insights:**
- Energy efficiency in electric vehicles is typically higher at lower speeds due to reduced aerodynamic drag and rolling resistance. At higher speeds, these resistive forces increase, leading to higher energy consumption.
- The vehicle's powertrain is optimized for a certain speed range, and deviations from this range can result in decreased efficiency.

**Insightful Conclusions:**
- The observed trend of decreasing energy efficiency with increasing speed aligns with theoretical expectations. This suggests that maintaining moderate speeds can help optimize energy efficiency and extend the vehicle's range.
- The efficiency drop at higher speeds indicates a need for optimizing the vehicle's aerodynamics and powertrain management to mitigate energy losses.
- Understanding the relationship between speed and energy efficiency can inform driving strategies and vehicle design improvements aimed at enhancing overall energy performance.

# Dynamic Braking Across Different Speeds and Its Efficiency

## 1. Average Regenerative Efficiency at Various Speeds

**Observations:**
- The bar plot shows the average regenerative efficiency at different speed ranges (bins).
- Regenerative efficiency varies across different speeds, with some speed ranges showing higher efficiency than others.

**Theoretical Insights:**
- Regenerative braking efficiency can be influenced by several factors, including the speed at which braking occurs, the state of the battery, and the braking system's design.
- Higher speeds might lead to more effective energy recovery due to the greater kinetic energy available to be converted back into electrical energy.

**Insightful Conclusions:**
- The variation in regenerative efficiency across different speeds suggests that certain speed ranges are more optimal for energy recovery through regenerative braking.
- Identifying these optimal speed ranges can help in designing braking strategies and powertrain management systems to maximize energy recovery.


<!---
## Motor Currents During Braking

**Observations:**
- The graph shows the front and rear motor currents during braking events.
- Both front and rear motor currents increase during braking, with variations indicating dynamic adjustments.

**Theoretical Insights:**
- Higher motor currents during braking indicate the regenerative braking process, where the motors act as generators to convert kinetic energy back into electrical energy.
- The distribution of current between the front and rear motors can reflect the vehicle's braking strategy, which aims to optimize energy recovery and maintain stability.

**Insightful Conclusions:**
- The increase in motor currents during braking events confirms the activation of regenerative braking.
- The dynamic adjustments in motor currents highlight the vehicle's braking system's ability to optimize energy recovery and ensure stable braking performance.

## Motor Torques During Braking

**Observations:**
- The graph shows the front and rear motor torques during braking events.
- Both front and rear torques exhibit negative values during braking, indicating the application of braking forces.

**Theoretical Insights:**
- Negative torque values during braking indicate the motors are providing a braking force, which is essential for regenerative braking.
- The distribution of torque between the front and rear motors affects the vehicle's handling and braking efficiency.

**Insightful Conclusions:**
- The negative torques during braking events confirm the application of regenerative braking forces.
- Understanding the torque distribution can help improve the design and control of the braking system to enhance energy recovery and vehicle stability.

## Motor Power Outputs During Braking

**Observations:**
- The graph shows the front and rear motor power outputs during braking events.
- Both front and rear motor power outputs exhibit negative values, indicating power generation during regenerative braking.

**Theoretical Insights:**
- Negative power outputs indicate that the motors are generating power rather than consuming it, which is a characteristic of regenerative braking.
- The power distribution between the front and rear motors reflects the braking system's efficiency and effectiveness in energy recovery.

**Insightful Conclusions:**
- The negative power outputs during braking events confirm the occurrence of regenerative braking, where the vehicle's kinetic energy is converted back into electrical energy.
- Analyzing the power distribution can provide insights into optimizing the braking system for better energy recovery and overall efficiency.
-->

# Regenerative Braking

## 1. Correlation Analysis of Relevant Parameters for Regen. Braking
### A. Observations from the Correlation Heatmap

### Strong Positive Correlations:
- **FrontTorque1D5 and FrontPower2E5 (0.91)**: Strong correlation indicating that higher torque results in higher power output.
- **RearTorque1D8 and RearPower266 (0.73)**: Similar strong correlation for the rear motor.
- **BMS_kwhRegenChargeTotal and BMS_kwhDriveDischargeTotal (0.99)**: Indicates that the total energy discharged and regenerated are closely related, likely due to the overall energy flow in the battery management system.
- **DI_accelPedalPos and FrontPower2E5 (0.74) and RearPower266 (0.75)**: Indicates that higher accelerator pedal positions result in higher power outputs.

### Strong Negative Correlations:
- **BMS_kwhRegenChargeTotal and UI_SOC (-0.89)**: Indicates that more regenerative energy correlates with a decrease in state of charge (SOC), likely because the energy is being recovered into the battery.
- **BMS_kwhDriveDischargeTotal and UI_SOC (-0.95)**: Similarly, more energy discharged results in a lower SOC.

### Moderate Positive Correlations:
- **DI_vehicleSpeed and FrontPower2E5 (0.73), RearPower266 (0.62)**: Indicates that higher vehicle speeds are associated with higher power outputs from both front and rear motors.

### Moderate Negative Correlations:
- **IBST_driverBrakeApply and DI_vehicleSpeed (-0.39)**: Indicates that braking events generally occur at lower speeds.
- **BMS_kwhRegenChargeTotal and DI_vehicleSpeed (-0.27)**: Indicates that more energy is regenerated at lower speeds.

### B. Insights from the Correlation Matrix:

### Braking and Regenerative Efficiency:
- The negative correlation between `IBST_driverBrakeApply` and `DI_vehicleSpeed` indicates that braking tends to occur at lower speeds, which is typical in urban driving conditions.
- The strong correlation between `BMS_kwhRegenChargeTotal` and `BMS_kwhDriveDischargeTotal` with `UI_SOC` underscores the importance of regenerative braking in maintaining battery SOC. Effective regenerative braking can significantly impact the vehicle's range by replenishing the battery.

### Power Output and Accelerator Position:
- The strong correlation between `DI_accelPedalPos` and motor power outputs (`FrontPower2E5`, `RearPower266`) highlights the direct relationship between the driver's acceleration demand and the power delivered by the motors.
- This relationship is crucial for understanding driving behavior and optimizing powertrain control strategies to balance performance and efficiency.

### Energy Flow and Vehicle Speed:
- The correlations between `DI_vehicleSpeed` and motor parameters (torque, power) indicate that vehicle speed directly influences powertrain performance. At higher speeds, the power demand increases, affecting energy efficiency.
- The moderate negative correlation between regenerative energy (`BMS_kwhRegenChargeTotal`) and vehicle speed suggests that more regenerative braking occurs at lower speeds, which aligns with the typical behavior of regenerative braking systems.

## 2. Correlation Analysis of Relevant Parameters for Regen. Braking [Split-Up Graphs]

### Part 1: Driver Inputs and Vehicle Dynamics

**Correlation Heatmap:**
- **Driver Brake Apply (`IBST_driverBrakeApply`)**
- **Accelerator Pedal Position (`DI_accelPedalPos`)**
- **Vehicle Speed (`DI_vehicleSpeed`)**

**Observations:**
- **Negative Correlation** between `IBST_driverBrakeApply` and `DI_accelPedalPos` (-0.36): Indicates that when the brake is applied, the accelerator pedal position tends to be low.
- **Negative Correlation** between `IBST_driverBrakeApply` and `DI_vehicleSpeed` (-0.39): Suggests that braking events are more common at lower speeds.
- **Positive Correlation** between `DI_accelPedalPos` and `DI_vehicleSpeed` (0.49): Indicates that higher accelerator pedal positions are associated with higher vehicle speeds.

**Theoretical Insights:**
- These correlations align with typical driving behavior, where braking reduces speed and acceleration increases speed.

**Insightful Conclusions:**
- Understanding these correlations can help optimize vehicle control strategies to balance acceleration and braking for better energy efficiency and driving dynamics.

### Part 2: Motor and Powertrain Parameters

**Correlation Heatmap:**
- **Front Motor Current (`FrontMotorCurrent1A5`)**
- **Rear Motor Current (`RearMotorCurrent126`)**
- **Front Torque (`FrontTorque1D5`)**
- **Rear Torque (`RearTorque1D8`)**
- **Front Power (`FrontPower2E5`)**
- **Rear Power (`RearPower266`)**

**Observations:**
- **Strong Positive Correlation** between `FrontTorque1D5` and `FrontPower2E5` (0.76): Indicates that higher torque results in higher power output.
- **Strong Positive Correlation** between `RearTorque1D8` and `RearPower266` (0.73): Similar correlation for the rear motor.
- **Moderate Positive Correlation** between `FrontTorque1D5` and `RearTorque1D8` (0.59): Suggests that torque in the front and rear motors are related but not identical.

**Theoretical Insights:**
- Higher torque typically results in higher power output, reflecting the powertrain's response to driving demands.

**Insightful Conclusions:**
- These correlations highlight the relationship between motor torque and power output, crucial for optimizing powertrain performance and efficiency.

### Part 3: Battery and Energy Parameters

**Correlation Heatmap:**
- **Regenerated Energy (`BMS_kwhRegenChargeTotal`)**
- **Energy Discharged (`BMS_kwhDriveDischargeTotal`)**
- **State of Charge (`UI_SOC`)**

**Observations:**
- **Strong Positive Correlation** between `BMS_kwhRegenChargeTotal` and `BMS_kwhDriveDischargeTotal` (0.99): Indicates that the total energy discharged and regenerated are closely related.
- **Strong Negative Correlation** between `BMS_kwhRegenChargeTotal` and `UI_SOC` (-0.89): Indicates that more regenerative energy correlates with a decrease in state of charge (SOC), likely because the energy is being recovered into the battery.
- **Strong Negative Correlation** between `BMS_kwhDriveDischargeTotal` and `UI_SOC` (-0.95): Similarly, more energy discharged results in a lower SOC.

**Theoretical Insights:**
- The energy flow in and out of the battery significantly impacts the SOC, which is crucial for maintaining battery health and vehicle range.

**Insightful Conclusions:**
- Effective regenerative braking is essential for maintaining battery SOC, extending the vehicle's range by replenishing the battery during braking events.

## 3. Front vs Rear Motor - Who generates more regen power?

**Observations:**
- The blue line represents the front motor torque over time.
- The red line represents the rear motor torque over time.
- The horizontal line at \( y = 0 \) marks the boundary between driving torque (positive values) and regenerative braking torque (negative values).

**Insights:**
- **Regenerative Braking Involvement**: The rear motor (red line) shows more significant negative torque values compared to the front motor (blue line), indicating a higher involvement in regenerative braking.
- **Torque Fluctuations**: Both front and rear motor torques fluctuate over time, showing periods of both driving and regenerative braking.
- **Torque Coordination**: The patterns suggest that both motors are actively managed to optimize the vehicle's performance, with the rear motor taking a more prominent role in regenerative braking.

**Theoretical Insights:**
- **Regenerative Braking**: In electric vehicles like the Tesla Model 3, regenerative braking is a key feature that helps in recovering energy during braking events. The negative torque values indicate the amount of energy being recuperated by the motors.
- **Motor Dynamics**: The involvement of both front and rear motors in driving and regenerative braking aligns with the theoretical understanding of dual-motor systems. Typically, the rear motor might be more involved in regeneration to enhance stability and energy recovery efficiency.
- **Energy Efficiency**: By analyzing the torque values, it can be inferred that the vehicle's control systems are designed to balance performance and energy efficiency, utilizing both motors appropriately based on driving conditions.

**Insightful Conclusions:**
- The analysis confirms that the rear motor is more actively involved in regenerative braking compared to the front motor. This behavior is consistent with the design principles of electric vehicles, where optimizing energy recovery and maintaining vehicle stability are crucial.

## 4. Booster Brake Pedal Force and Regenerative Charge Over Time

**Booster Brake Pedal Force Over Time**
- **Observation**: The brake pedal force shows distinct, significant peaks where the force is applied, followed by periods of no brake force.
- **Insight**: This pattern indicates discrete braking events rather than continuous braking. The distinct peaks suggest the driver applies substantial brake force during these events, likely related to sudden braking or deceleration scenarios.

**Regenerative Charge Over Time**
- **Observation**: The regenerative charge shows a steady increase over time, with noticeable steps during certain periods.
- **Insight**: This indicates that the vehicle is effectively recovering energy through regenerative braking during the test. The steps in regenerative charge correspond to periods of deceleration and braking events, as indicated by the booster brake pedal force plot.

**Correlation Between Brake Force and Regenerative Charge**
- **Insight**: The increase in regenerative charge aligns with the periods of high brake pedal force, suggesting that the vehicle utilizes regenerative braking alongside mechanical braking to recover energy. This dual approach improves overall energy efficiency and extends the vehicle's driving range.

## 5. Acclerator Pedal Vs Brake Pedal for Regeneration

**Accelerator Pedal Position Over Time**
- **Observation**: The accelerator pedal position shows multiple spikes, indicating periods where the driver is accelerating.
- **Insight**: The pedal position rarely reaches 100%, suggesting the driver is not frequently performing full-throttle accelerations. Instead, there are moderate accelerations which could be due to normal driving behavior or controlled acceleration during testing.

**Booster Brake Pedal Force Over Time**
- **Observation**: The brake pedal force shows distinct peaks where the force is applied, followed by periods of no brake force.
- **Insight**: This pattern indicates distinct braking events rather than continuous braking. The peaks suggest the driver applies significant brake force during these events, which could be related to the sudden braking or deceleration scenarios.

**Vehicle Speed Over Time**
- **Observation**: The vehicle speed fluctuates throughout the period. There are periods of acceleration followed by deceleration.
- **Insight**: The speed profile indicates that the vehicle is undergoing various speed tests, including acceleration, cruising, and braking phases. The speed peaks and subsequent drops correspond to the braking events observed in the brake pedal force plot.

**Regenerative Charge Over Time**
- **Observation**: The regenerative charge shows a gradual increase over time.
- **Insight**: This indicates that the vehicle is continuously recovering energy through regenerative braking during the test. The steady rise in regenerative charge suggests that the vehicle effectively uses regenerative braking during deceleration phases, contributing to energy recovery.

**Correlation and Theoretical Insights**
- **Regenerative Braking**: The regenerative charge increase correlates with periods of deceleration and braking. During these phases, the electric motors convert kinetic energy back into electrical energy, which is stored in the battery. This is evident from the rising regenerative charge during braking events indicated by the booster brake pedal force.
- **Driving Behavior**: The accelerator pedal position and vehicle speed plots show how the driver modulates acceleration and speed. The braking events (high brake pedal force) followed by regenerative charge increase indicate the vehicle's dual use of mechanical and regenerative braking systems.
- **Energy Efficiency**: The regenerative charge plot highlights the vehicle's ability to recover energy during deceleration, which improves overall energy efficiency and extends the driving range of the electric vehicle.

**Insightful Conclusions:**
- The visualization provides a comprehensive view of the vehicle's dynamic performance during the test. The data shows effective use of regenerative braking during deceleration phases, as indicated by the increasing regenerative charge. The driving behavior, characterized by multiple acceleration and braking events, aligns with the expected test conditions for evaluating vehicle performance. This analysis confirms the vehicle's efficient energy recovery system and provides insights into driver interactions with the accelerator and brake pedals.

## 6. Motor Torque and Regenerative Energy During Sudden Braking and Instability Events
**Motor Torque (Front and Rear) Over Time**
- **Observation**: The front and rear motor torque show fluctuations, with both positive and negative values, indicating periods of acceleration (positive torque) and regenerative braking (negative torque).
- **Insight**: The rear motor torque generally shows more significant negative values compared to the front motor torque, suggesting a higher involvement in regenerative braking by the rear motor.

**Total Regenerative Charge Over Time**
- **Observation**: The total regenerative charge increases gradually over time, with more substantial steps during certain periods.
- **Insight**: The increasing regenerative charge indicates continuous energy recovery during deceleration and braking events. The steps align with the peaks in negative motor torque values, confirming the effectiveness of regenerative braking during these events.

**Correlation Between Motor Torque and Regenerative Charge**
- **Insight**: The periods where the rear motor torque shows significant negative values correspond to increases in regenerative charge, indicating that the rear motor plays a crucial role in energy recovery during braking events. The front motor also contributes, but to a lesser extent. This distribution of braking effort enhances vehicle stability and energy efficiency.

**Insightful Conclusions:**
- The visualizations provide a comprehensive view of the vehicle's dynamic performance during the test. The data shows effective use of regenerative braking during deceleration phases, as indicated by the increasing regenerative charge. The driving behavior, characterized by multiple acceleration and braking events, aligns with the expected test conditions for evaluating vehicle performance. This analysis confirms the vehicle's efficient energy recovery system and provides insights into the interactions between mechanical and regenerative braking.

# Battery Parameters Analysis

## 1. Energy Recovered Over Time

**Observations:**
- The cumulative energy recovered increases steadily over time, indicating consistent regenerative braking events throughout the test period.

**Theoretical Insights:**
- Regenerative braking is designed to recover energy during braking events, converting kinetic energy back into electrical energy stored in the battery.
- The steady increase in cumulative energy recovered is expected in a well-functioning regenerative braking system.

**Insightful Conclusions:**
- The consistent increase in cumulative energy recovered confirms the effective operation of the regenerative braking system.
- Monitoring the cumulative energy recovered can provide insights into the overall efficiency and effectiveness of the regenerative braking system.

## 2. State of Charge (SoC) Over Time

**Observations:**
- The SoC shows a general declining trend with intermittent increases, corresponding to charging events or regenerative braking.

**Theoretical Insights:**
- The SoC represents the remaining battery capacity and should decrease as the vehicle is driven and energy is consumed.
- Increases in SoC can occur during regenerative braking or when the battery is being charged.

**Insightful Conclusions:**
- The observed SoC trend is typical for electric vehicles, where the battery discharges during driving and recharges during braking or at charging stations.
- Tracking SoC over time helps in understanding the vehicle's range and battery usage patterns.

## 3. Battery Degradation Over Time

**Observations:**
- The SoC shows periodic decreases and increases, while the energy discharged shows a cumulative increase.

**Theoretical Insights:**
- Battery degradation can be inferred from a decreasing trend in maximum SoC over time, indicating reduced battery capacity.
- The cumulative energy discharged provides an indication of the total energy usage over time.

**Insightful Conclusions:**
- No clear signs of significant battery degradation are observed within the test period, as the SoC does not show a long-term declining trend beyond normal usage patterns.
- Continuous monitoring over a longer period would be necessary to accurately assess battery degradation.

## 4. Correlation Between SoC and Motor Parameters

**Correlation Matrix:**
- Positive correlations between `UI_SOC` and `FrontTorque1D5` (0.28), `FrontPower2E5` (0.17), and `RearPower266` (0.09).
- Negative correlations between `UI_SOC` and `RearTorque1D8` (-0.12).

**Theoretical Insights:**
- Positive correlations indicate that higher SoC is associated with higher torque and power outputs, suggesting efficient energy usage from the battery.
- Negative correlations may indicate variations in energy distribution between the front and rear motors.

**Insightful Conclusions:**
- The correlations suggest that maintaining a higher SoC can support higher motor performance in terms of torque and power output.
- Understanding these relationships can help optimize energy management strategies to balance performance and battery life.

## 5. Charge and Discharge Cycles Analysis

**Charge Cycles**

**Definition**: A charge cycle is counted when the battery's state of charge increases due to regenerative braking.

**Calculation**: Increment the charge cycle count whenever there is a positive change in `BMS_kwhRegenChargeTotal`.

**Discharge Cycles**

**Definition**: A discharge cycle is counted when the battery's state of charge decreases as the vehicle uses energy to drive.

**Calculation**: Increment the discharge cycle count whenever there is a positive change in `BMS_kwhDriveDischargeTotal`.

**Observations**

- The number of charge cycles increases consistently, reflecting frequent regenerative braking events.
- The number of discharge cycles also increases steadily, indicating continuous usage of the battery to power the vehicle.

**Theoretical Insights**

- Charge and discharge cycles are fundamental to understanding battery usage and health. Each cycle represents a full discharge and recharge, impacting battery life and performance.
- The rates of charge and discharge cycles can provide insights into driving behavior, energy usage patterns, and the efficiency of the regenerative braking system.

**Insightful Conclusions**

- The consistent increase in charge cycles suggests effective regenerative braking, contributing to energy recovery and efficient battery usage.
- Steady discharge cycles indicate regular battery usage, essential for powering the vehicle's operations.
- Monitoring these cycles can help in assessing battery health and optimizing energy management strategies.

## 6. Energy Efficiency Analysis

**Definition**: Energy efficiency is calculated as the amount of energy consumed per kilometer traveled (Wh/km).

**Observations:**
- The energy efficiency graph shows fluctuations over time, reflecting changes in driving conditions and power demands.
- Summary statistics provide a comprehensive range of energy efficiency values, highlighting average efficiency and variability.

**Theoretical Insights:**
- Energy efficiency is influenced by various factors, including speed, driving behavior, terrain, and environmental conditions. Higher efficiency (lower Wh/km) indicates more effective energy usage, while lower efficiency (higher Wh/km) suggests higher energy consumption.
- Fluctuations in energy efficiency are normal due to varying driving conditions, such as acceleration, deceleration, and regenerative braking events.

**Insightful Conclusions:**
- Monitoring energy efficiency helps identify patterns in energy usage, which can be crucial for improving driving habits and vehicle performance.
- Understanding factors that influence energy efficiency can inform strategies to optimize energy usage, extend vehicle range, and reduce overall energy consumption.
- Regular analysis of energy efficiency can contribute to more sustainable vehicle operation and better battery management.

## 7. Battery Voltage and Brick Voltage Analysis

**Observations**:
- The battery voltage (`BattVoltage132`) and the brick voltages (`BattBrickVoltageMax332` and `BattBrickVoltageMin332`) show similar trends over time, with the battery voltage fluctuating between the maximum and minimum brick voltages.
- The brick voltages follow the battery voltage closely, indicating consistent behavior among the individual bricks.

**Correlation Insights**:
- **Battery Voltage and Max Brick Voltage**: Strong positive correlation (0.9618).
- **Battery Voltage and Min Brick Voltage**: Strong positive correlation (0.9622).
- **Max and Min Brick Voltage**: Almost perfect positive correlation (0.9998).

**Theoretical Insights**:
- The strong correlations confirm that the brick voltages are closely related to the overall battery voltage, as expected. This indicates that the battery pack's bricks are functioning correctly and uniformly.
- Any significant deviation between brick voltages and the battery voltage could indicate issues with specific bricks, potentially leading to battery performance issues.

**Insightful Conclusions**:
- The consistent behavior and strong correlations between battery and brick voltages suggest good health and uniform performance of the battery bricks.
- Regular monitoring of brick voltages alongside battery voltage can help in early detection of potential issues within the battery pack.

## 8. Smooth Battery Current vs. Raw Battery Current Analysis

**Observations**:
- The raw battery current (`RawBattCurrent132`) shows significant fluctuations, indicating noise and rapid changes in current.
- The smoothed battery current (`SmoothBattCurrent`) provides a clearer trend, with reduced noise and more stable values.

**Correlation Insights**:
- **Raw and Smooth Battery Current**: Moderate positive correlation (0.2592).

**Theoretical Insights**:
- Smoothing the battery current helps in reducing noise and provides a clearer understanding of the current trends and overall behavior.
- The moderate correlation indicates that while the smoothed current follows the general trend of the raw current, it effectively reduces short-term fluctuations.

**Insightful Conclusions**:
- Using smoothed battery current helps in better understanding the overall current trends without the interference of noise.
- This can be particularly useful for diagnosing issues and understanding the battery's performance under different conditions.
- Regular analysis of both raw and smoothed battery currents can help in comprehensive battery management and monitoring.

# Vehicle Stability Analysis

## 1. Brake Torque Analysis

**Observations**:
- Front and rear brake torques are expected to show significant values during braking events.
- The distribution of brake torques among the wheels helps in maintaining vehicle stability during sudden braking or skidding.

**Theoretical Insights**:
- The Electronic Stability Program (ESP) adjusts brake torques on individual wheels to maintain vehicle stability during emergency braking and skidding.
- A balanced application of brake torque on the front and rear wheels ensures that the vehicle maintains its intended path and minimizes the risk of skidding.

**Insightful Conclusions**:
- Consistent brake torque application on all wheels indicates effective stability control.
- Variations in brake torque among wheels can suggest adjustments made by the ESP to counteract skidding or maintain stability.

## 2. Yaw Rate and Vehicle Speed Analysis

**Observations**:
- The yaw rate provides insights into the vehicle's rotational dynamics, particularly during turns or skidding.
- Vehicle speed is expected to decrease during braking events, with possible spikes in yaw rate indicating instability or skidding.

**Theoretical Insights**:
- Yaw rate is a critical parameter for understanding vehicle stability. High yaw rates combined with low vehicle speed can indicate loss of control or skidding.
- ESP systems aim to control yaw rate by adjusting brake torques and reducing vehicle speed to maintain stability.

**Insightful Conclusions**:
- Monitoring yaw rate and vehicle speed together can provide early warnings of stability issues.
- Effective ESP systems should show a controlled yaw rate even during emergency braking, indicating successful stability management.

## 3. Energy Usage for Braking and Stability

**Observations**:
- Total brake energy is expected to show significant spikes during braking events.
- Energy usage patterns can indicate the effectiveness of the braking system and stability controls.

**Theoretical Insights**:
- Energy used for braking is a combination of mechanical braking and regenerative braking. High energy usage during braking events is typical.
- Effective braking systems should efficiently manage energy distribution to maintain vehicle stability and minimize skidding.

**Insightful Conclusions**:
- High total brake energy during braking events indicates effective braking but should be balanced to avoid excessive wear on the braking system.
- Analyzing energy usage patterns helps in assessing the effectiveness of the ESP and overall vehicle stability during emergency maneuvers.

## 4. Energy Distribution Analysis

**Observations**:
- During sudden braking or skidding events, spikes in `BMS_kwhRegenChargeTotal` due to increased regenerative braking.
- `BMS_kwhDriveDischargeTotal` should decrease as the vehicle slows down.

**Theoretical Insights**:
- Regenerative braking is designed to recover energy during deceleration.
- The energy discharged should decrease when the vehicle is not accelerating or is decelerating.

**Insightful Conclusions**:
- Effective regenerative braking improves vehicle efficiency by recovering energy.
- Monitoring these parameters helps assess the effectiveness of the regenerative braking system.

## 5. Vehicle Dynamics Analysis

**Observations**:
- Sudden changes in `RCM_lateralAccel` and `RCM_yawRate` during emergency braking or skidding indicate instability.
- High values in `RCM_longitudinalAccel` during braking events indicate strong deceleration.

**Theoretical Insights**:
- Vehicle stability systems aim to control these parameters to maintain stability.
- Effective stability control should minimize these values even during sudden maneuvers.

**Insightful Conclusions**:
- Monitoring vehicle dynamics helps evaluate stability system performance.
- Effective control of lateral acceleration and yaw rate is crucial for maintaining stability.

## 6. Wheel Rotation and Speed Analysis

**Observations**:
- During skidding, irregular patterns in wheel speeds and possible differences between front and rear wheels.
- Sudden changes in wheel rotation direction during skidding or emergency braking.

**Theoretical Insights**:
- Wheel speeds should be similar for all wheels under normal conditions. Differences indicate skidding or loss of traction.
- Sudden changes in wheel rotation direction can indicate skidding or instability.

**Insightful Conclusions**:
- Monitoring wheel speeds and rotations can provide early warnings of skidding or loss of traction.
- Consistent wheel speed and direction indicate stable vehicle dynamics and effective traction control.

## 7. Braking Force Analysis

**Observations**:
- High values for brake torques on all wheels during emergency braking.
- Distribution of brake torques among the wheels indicates how braking force is managed.

**Theoretical Insights**:
- Effective braking systems distribute braking forces to maintain stability. Higher forces are typically applied to the front wheels.
- Uneven distribution can lead to instability or skidding.

**Insightful Conclusions**:
- Monitoring brake torques helps assess braking system performance.
- Even distribution of braking forces is crucial for maintaining stability during emergency maneuvers.

## 8. Brake Torque Distribution

**Observations**:
- During sudden braking or emergency braking events, high values for brake torques on all wheels.
- Distribution of brake torques among the wheels indicates how the braking force is managed to maintain stability.

**Theoretical Insights**:
- Brake torque distribution is critical for vehicle stability. The front wheels generally experience higher brake torques due to weight transfer during braking.
- Effective stability control systems balance brake torques to prevent skidding and maintain control.

**Insightful Conclusions**:
- Consistent brake torque application across all wheels indicates effective stability control.
- Uneven distribution of brake torques can suggest adjustments made by the Electronic Stability Program (ESP) to counteract skidding or maintain stability.

## 9. Dynamic Responses

**Observations**:
- Sudden changes in lateral acceleration and yaw rate during emergency braking or skidding events indicate instability.
- High longitudinal acceleration values during braking events indicate strong deceleration.

**Theoretical Insights**:
- Vehicle stability systems aim to control these parameters to maintain stability. High lateral acceleration and yaw rate can indicate loss of control.
- Effective stability control should minimize these values even during sudden maneuvers.

**Insightful Conclusions**:
- Monitoring vehicle dynamics helps in evaluating the performance of stability control systems.
- Effective control of lateral acceleration and yaw rate is crucial for maintaining vehicle stability during sudden maneuvers.

## 10. Energy Distribution during Braking

**Observations**:
- During sudden braking or skidding events, spikes in regenerative charge total due to increased regenerative braking.
- Drive discharge total should decrease as the vehicle slows down.

**Theoretical Insights**:
- Regenerative braking is designed to recover energy during deceleration. Higher values during braking events indicate effective energy recovery.
- The energy discharged should decrease when the vehicle is not accelerating or is decelerating.

**Insightful Conclusions**:
- Effective regenerative braking can significantly improve vehicle efficiency by recovering energy that would otherwise be lost.
- Monitoring these parameters helps assess the effectiveness of the regenerative braking system.


## 11. Heatmap for Correlation Matrix

**Observations**:
- **Strong Correlations**:
  - Between `ESP_brakeTorqueFrL` and `ESP_brakeTorqueFrR`, indicating similar braking behavior for the front wheels.
  - Between `WheelSpeedFL175` and `WheelSpeedFR175`, indicating similar speeds for the front wheels.

- **Moderate Correlations**:
  - Between `RCM_lateralAccel` and `RCM_yawRate`, suggesting that lateral movements are related to yaw changes.
  - Between `BMS_kwhRegenChargeTotal` and `BMS_kwhDriveDischargeTotal`, indicating the relationship between energy recovered and energy used.

**Insightful Conclusions**:
- Strong correlations between front wheel speeds and brake torques indicate consistent braking and traction control for the front wheels.
- Moderate correlations between lateral acceleration and yaw rate can help in understanding vehicle dynamics during maneuvers.

## 12. Pairplot for Selected Parameters

**Observations**:
- The pairplots reveal distributions and relationships between various parameters.
- Identifying any anomalies or outliers in these relationships can help diagnose stability or performance issues.

**Insightful Conclusions**:
- Visualizing these relationships helps in identifying patterns and potential issues in vehicle stability and dynamics.
- Detailed pairplot analysis can reveal deeper insights into how different parameters interact under various driving conditions.

## 13. Events with significant changes in Yaw, Pitch or Roll

**Observations**:
- **Yaw Rate vs. Time**: The yaw rate graph shows how the vehicle's rotational speed around the vertical axis changes over time.
Sharp peaks and troughs indicate moments of rapid turning or spinning, which can be linked to significant steering inputs.

- **Pitch Rate vs. Time**: The pitch rate graph illustrates the vehicle's rotational speed around the lateral axis.
Variations in pitch rate may correspond to acceleration and braking events, where the vehicle pitches forward or backward.

- **Roll Rate vs. Time**: The roll rate graph shows the vehicle's rotational speed around the longitudinal axis.
Changes in roll rate often occur during cornering or when the vehicle experiences lateral forces, causing it to roll to the side.


## 14. Brake Torques For All Four Wheels Vs Time

**Observations**:
- The graph shows the brake torque applied to each of the four wheels over time.
- **Front Wheels (Blue and Green)**: The front left and front right brake torques generally follow a similar pattern, indicating synchronized braking efforts for the front wheels.
- **Front Left Brake Torque (Top Left)**: Displays the brake torque applied to the front left wheel over time. Notable peaks and troughs indicate braking events.
- **Front Right Brake Torque (Top Right)**: Shows the brake torque applied to the front right wheel. The pattern is similar to the front left, indicating synchronized braking.
- **Rear Wheels (Red and Orange)**: Similarly, the rear left and rear right brake torques exhibit synchronized behavior, although the magnitudes might be slightly different from the front wheels.
- **Rear Left Brake Torque (Bottom Left)**: Represents the brake torque for the rear left wheel. The magnitude and pattern of changes are comparable to the front wheels but might have slight differences.
- **Rear Right Brake Torque (Bottom Right)**: Illustrates the brake torque for the rear right wheel. The synchronization with the rear left wheel can be observed here.
- **Dynamic Adjustments**: The brake torques for all four wheels show dynamic adjustments, likely corresponding to driving conditions such as acceleration, braking, and turning.

## 15. Steering Angle during Stability Events vs. Time
**Observations**:
- The graph shows the variation in the steering angle over time.
- Significant changes in the steering angle indicate moments of sharp turns or corrective maneuvers, which are critical during stability events.
- Peaks and troughs in the graph represent the vehicle's steering adjustments to maintain stability.

## 16. Analysis of Vehicle Stability during Stability Events and Sharp Turns

**Observations**:
- Steering Angle during Stability Events and Sharp Turns:
- Red markers indicate sharp turns (steering angle > ±30 degrees).
- Blue markers indicate stability events (significant changes in yaw, pitch, or roll rates).
- The graph shows that sharp turns often coincide with stability events, as significant steering inputs typically require stability control interventions.

**Yaw Rate, Pitch Rate, and Roll Rate during Stability Events**:

- **Yaw Rate**: Red markers indicate that stability events often involve significant changes in yaw rate, corresponding to rapid directional changes.
- **Pitch Rate**: Stability events also show notable changes in pitch rate, often due to acceleration or braking forces affecting the vehicle's longitudinal stability.
- **Roll Rate**: The roll rate changes indicate lateral forces acting on the vehicle, such as during sharp turns or skidding.

**Brake Torques during Stability Events and Sharp Turns**:

- Front Left and Front Right Brake Torques: The brake torques on the front wheels are dynamically adjusted during sharp turns and stability events, showing synchronized efforts to counteract skidding or loss of control.
- Rear Left and Rear Right Brake Torques: Similarly, the rear wheel brake torques are adjusted, but with slightly different magnitudes, reflecting the distribution of braking forces to maintain stability.

**Interpretation**:
- **Steering and Yaw Dynamics**: During sharp turns, significant changes in steering angle lead to rapid adjustments in yaw rate, necessitating stability control interventions to prevent oversteer or understeer.
- **Pitch and Roll Adjustments**: Stability events often involve changes in pitch and roll rates, indicating the vehicle's response to longitudinal and lateral forces. Stability control systems adjust brake torques to manage these forces and maintain balance.
- **Brake Torque Modulation**: The ESP system dynamically adjusts brake torques across all four wheels to manage stability during sharp turns and stability events. This helps in preventing skidding and maintaining control.


**Comparision of ESP Performance Across Different Conditions**:

- **Sharp Turns**: Defined by significant steering angle changes.
- **Straight Line Braking**: Analyze how ESP maintains stability when the vehicle is primarily moving straight but undergoing heavy braking.
- **Curve Handling**: Defined by moderate and consistent steering angles.
Analyze ESP performance in maintaining stability by observing yaw, pitch, roll rates, and brake torques.


**Analyze Data for Signs of Understeer**: 
- Understeer occurs when the vehicle turns less than intended by the driver, typically seen when the front wheels lose traction. Signs of understeer include:

- **Increased Steering Angle without Proportional Yaw Rate Increase**: Significant increase in steering angle with a smaller increase in yaw rate.
- **Brake Torque Adjustments**: ESP might apply more braking force to the rear wheels to balance the vehicle.

**Implementation of filtering and analyzing data for signs of understeer**:

- **Sharp Turns**: The plot shows significant steering angle changes (sharp turns) with corresponding adjustments in yaw rate and brake torques. During sharp turns, the ESP system dynamically adjusts brake torques (especially front left and rear left) to stabilize the vehicle. The yaw rate changes in response to these steering inputs, helping to prevent oversteer or understeer.
- **Straight Line Braking**: This plot focuses on scenarios where the vehicle is primarily moving straight but undergoing heavy braking. During straight-line braking, the steering angle remains minimal while brake torques on the front and rear wheels are applied to decelerate the vehicle. The yaw rate remains relatively stable, indicating that the vehicle maintains a straight path.
- **Curve Handling**: This plot examines moderate and consistent steering angles, indicative of handling curves. The ESP system adjusts brake torques to maintain stability while navigating curves. Yaw rate changes correspond to the curved path, with brake torque adjustments preventing excessive roll or yaw.

**Understeer Detection**
- Understeer occurs when the vehicle's front wheels lose traction, causing it to turn less than intended by the driver.
- Significant steering angle without a proportional increase in yaw rate. Identified by red markers indicating understeer events.

**Insightful Inference**:
- Steering Angle vs. Yaw Rate: The red markers indicate potential understeer events, where the steering angle is high, but the yaw rate is not proportionally increasing. This can be a sign of the front wheels losing traction, and the ESP system might respond by adjusting brake torques to regain control.
- The ESP system effectively adjusts brake torques and yaw rates to maintain stability during sharp turns, straight-line braking, and curve handling.
Understeer detection highlights scenarios where the vehicle's response does not match the steering input, indicating potential traction loss.


## 17. Comparing Understeer to Oversteer Behavior

**Understeer:** 
- Understeer occurs when the front wheels lose traction, causing the vehicle to turn less than intended.
- Significant increase in steering angle with a smaller increase in yaw rate.
- The vehicle tends to continue in a straight line despite steering inputs.
- The ESP system may apply braking to the rear wheels to help regain front traction.

**Oversteer:**
- Oversteer occurs when the rear wheels lose traction, causing the vehicle to turn more than intended.
- Smaller steering angle with a disproportionately large increase in yaw rate.
- The rear of the vehicle tends to slide outward, causing the vehicle to rotate more.
- The ESP system may apply braking to the front wheels to counteract the excessive yaw.

**Identifying and Analyzing Understeer and Oversteer Events:**
- Identifying Understeer Events: Use high steering angle without a proportional increase in yaw rate.
- Identifying Oversteer Events: Use high yaw rate with a smaller steering angle.


**Insights to Implementation**:
- Identify understeer events using high steering angle and low yaw rate.
- Identify oversteer events using high yaw rate and low steering angle.
- Compare the brake torques and yaw rates during these events.

**Define Thresholds for Detection**:
- Understeer: High steering angle (> 30 degrees), Low yaw rate (< 0.1 degrees per second)
- Oversteer: High yaw rate (> 3 degrees per second), Low steering angle (< 10 degrees).

**Comparison of Understeer and Oversteer Behavior**:

- **Understeer Detection characteristics:**
    - High Steering Angle with Low Yaw Rate
    - Significant increase in steering angle without a proportional increase in yaw rate indicates understeer.
    - The vehicle tends to turn less than intended, continuing in a straight line despite steering inputs.

- **ESP Response:**
    - Brake Torques: During understeer events, the ESP system may increase braking force on the rear wheels to regain front traction.
    - Graph Analysis: The red markers in the upper plot indicate understeer events, showing significant steering angles with low yaw rates. The lower plot shows brake torque adjustments, with the rear wheels receiving more braking force to mitigate understeer.

- **Oversteer Detection characteristics:**
    - High Yaw Rate with Low Steering Angle
    - Disproportionate increase in yaw rate with a small steering angle indicates oversteer.
    - The vehicle turns more than intended, with the rear sliding outwards.

- **ESP Response:**
    - Brake Torques: During oversteer events, the ESP system may increase braking force on the front wheels to counteract the excessive yaw.
    - Graph Analysis: The red markers in the upper plot indicate oversteer events, showing significant yaw rates with low steering angles. The lower plot shows brake torque adjustments, with the front wheels receiving more braking force to mitigate oversteer.

**Summary of Observations**:

- **Understeer**: Detected by high steering angle with low yaw rate. ESP Responses in increased braking on rear wheels to regain front traction. Visual indicators with red markers in the upper plot for understeer events and corresponding brake torque adjustments in the lower plot.

- **Oversteer**: Detected by high yaw rate with low steering angle. ESP Responses in Increased braking on front wheels to counteract excessive yaw. Visual indicators with red markers in the upper plot for oversteer events and corresponding brake torque adjustments in the lower plot.

# Analysis of Vehicle Stability During Braking Events

## 1. Energy Distribution During Braking Events

**Observations**:
- Spikes in `BMS_kwhRegenChargeTotal` during braking events indicate increased energy recovery.
- Decrease in `BMS_kwhDriveDischargeTotal` corresponds with vehicle deceleration.

**Insights**:
- Effective regenerative braking during braking events can be confirmed by spikes in `BMS_kwhRegenChargeTotal`.
- Reduced `BMS_kwhDriveDischargeTotal` during these events indicates effective deceleration.

## 2. Vehicle Stability During Braking Events

**Observations**:
- Sudden changes in `RCM_lateralAccel` and `RCM_yawRate` during braking events may indicate instability or skidding.
- High values in `RCM_longitudinalAccel` during braking events indicate strong deceleration.

**Insights**:
- Consistent `RCM_lateralAccel` and controlled `RCM_yawRate` during braking events suggest effective stability control.
- Monitoring these parameters helps evaluate the performance of stability control systems during emergency maneuvers.

## 3. Correlation Analysis During Braking Events

**Observations**:
- High correlations between brake torques and stability parameters can indicate the effectiveness of braking force distribution in maintaining stability.
- Correlations between energy parameters and stability parameters can reveal insights into how energy usage impacts vehicle stability.

**Insights**:
- Strong correlations between brake torques and stability parameters indicate effective braking force distribution.
- Understanding the relationship between energy usage and stability helps optimize braking strategies to maintain control and efficiency.

# ESP Stability System Analysis During Sudden Braking

## 1. Brake Torques During Braking Events

**Observations**:
- Balanced brake torques on all wheels during braking events.
- High brake torques on the front wheels due to weight transfer.

**Insights**:
- Balanced brake torque application suggests effective ESP functionality.
- Higher front brake torques are typical during sudden

## 2. Wheel Speeds During Braking Events

**Observations**:
- Consistent wheel speeds without significant discrepancies during braking events.
- Minimal differences in wheel rotation directions indicating no skidding.

**Insights**:
- Consistent wheel speeds and rotations suggest good traction control and stability during braking.
- Minimal skidding indicates effective ESP intervention.

## 3. Vehicle Dynamics During Braking Events

**Observations**:
- Controlled lateral acceleration and yaw rate during braking events.
- Strong longitudinal deceleration indicating effective braking.
- High correlations between brake torques and stability parameters.
- Moderate correlations between energy parameters and stability parameters.

**Insights**:
- Controlled lateral acceleration and yaw rate suggest effective ESP functionality.
- Strong deceleration confirms effective braking performance.
- Correlation Analysis During Braking Events
- High correlations indicate effective braking force distribution and stability control.
- Energy usage is correlated with stability, suggesting optimized energy management during braking.

# Analysis of Vehicle Dynamics During Braking Events

## 1. Roll Rate During Braking Events

**Observations**:
- Changes in roll rate during braking events can indicate lateral instability or vehicle roll.

**Insights**:
- Minimal changes in roll rate suggest effective ESP functionality in maintaining lateral stability.

## 2. Yaw Rate During Braking Events

**Observations**:
- Changes in yaw rate during braking events can indicate rotational instability or skidding.

### Insights
- Controlled yaw rate during braking events suggests effective ESP functionality in maintaining rotational stability.

## 3. Longitudinal and Lateral Acceleration During Braking Events

**Observations**:
- High longitudinal acceleration indicates strong deceleration during braking events.
- Changes in lateral acceleration can indicate lateral instability or skidding.

**Insights**:
- Consistent longitudinal and lateral acceleration values during braking events suggest effective stability control by ESP.

## 4. Correlation Analysis During Braking Events

**Observations**:
- High correlations between brake torques and dynamics parameters can indicate effective braking force distribution and stability control.

**Insights**:
- Strong correlations between dynamics parameters and braking forces indicate that ESP is effectively managing stability during braking events.

# Stability Analysis Under Different Speeds

## 1. Roll Rate by Speed Range

**Observations**:
- Variations in roll rate across different speed ranges can indicate changes in vehicle stability.
- Higher roll rates at higher speeds may suggest increased lateral instability.

**Insights**:
- Consistent roll rates across speed ranges suggest effective stability control.
- Monitoring roll rates helps evaluate lateral stability under different speed conditions.

## 2. Yaw Rate by Speed Range

**Observations**:
- Changes in yaw rate across speed ranges can indicate rotational stability.
- Higher yaw rates at higher speeds may suggest increased rotational instability.

**Insights**:
- Controlled yaw rates across speed ranges suggest effective ESP functionality.
- Monitoring yaw rates helps evaluate rotational stability under different speed conditions.

## 3. Longitudinal and Lateral Acceleration by Speed Range

**Observations**:
- High longitudinal acceleration at higher speeds indicates effective braking.
- Consistent lateral acceleration across speeds suggests good lateral stability.

**Insights**:
- Monitoring longitudinal and lateral acceleration helps evaluate overall stability and control.
- Effective stability control systems should maintain consistent acceleration values across different speeds.

## 4. Correlation Analysis Between Speed and Dynamics Parameters

**Observations**:
- High correlations between speed and dynamics parameters indicate strong relationships.
- Understanding these relationships helps optimize stability control systems.

**Insights**:
- Strong correlations suggest that vehicle dynamics parameters are significantly influenced by speed.
- Optimizing stability control systems based on these correlations can enhance vehicle stability.

# Analyzing Braking Torque's Effect on Stability

## 1. Braking Torque vs Stability Parameters

**Observations**:
- Scatter plots show the relationship between braking torques and stability parameters.
- Higher braking torques impact roll rate, yaw rate, longitudinal acceleration, and lateral acceleration.

**Insights**:
- High braking torques might increase roll rate and yaw rate, indicating potential instability.
- Effective stability control should minimize the impact of braking torques on roll rate and yaw rate.

## 2. Statistical Distribution of Stability Parameters

**Observations**:
- Summary statistics show how stability parameters vary across different levels of braking torque.

**Insights**:
- Consistent values of stability parameters across different braking torques suggest effective stability control.
- Significant variations might indicate areas where stability control can be improved.

## 3. Correlation Analysis Between Braking Torques and Stability Parameters

**Observations**:
- Correlation matrix reveals the strength and direction of relationships between braking torques and stability parameters.

**Insights**:
- Strong correlations between braking torques and stability parameters can indicate how braking forces influence vehicle stability.
- Understanding these relationships helps in optimizing stability control systems to handle different braking scenarios.

# Comparison of Brake Torque and Yaw Rate

## 1. Visualizing Brake Torque and Yaw Rate Over Time

**Observations**:
- The time-series plot shows how brake torque and yaw rate change over time, highlighting the immediate effects of braking on vehicle rotation.

**Insights**:
- Sudden spikes in brake torque might correspond to changes in yaw rate, indicating the stability system's response to braking forces.

## 2. Scatter Plot Analysis

**Observations**:
- Scatter plots illustrate the relationship between brake torque and yaw rate.
- Clusters or trends might indicate how yaw rate changes with different levels of brake torque.

**Insights**:
- A clear trend or pattern in the scatter plots suggests a direct relationship between brake torque and yaw rate.
- Understanding this relationship helps evaluate how effectively the stability control system manages rotational stability during braking.

## 3. Correlation Analysis Between Brake Torques and Yaw Rate

**Observations**:
- The correlation matrix quantifies the strength and direction of the relationship between brake torque and yaw rate.

**Insights**:
- Strong positive or negative correlations indicate a significant relationship between brake torque and yaw rate.
- These correlations help in understanding the impact of braking forces on vehicle rotation and the effectiveness of the stability control system.

# 4. Comparison of Front and Rear Brake Torque with Yaw Rate Over Time

**Observations**:
- The line graph shows how front and rear brake torques and yaw rate change over time.
- By overlaying these parameters, it is possible to observe how changes in both front and rear brake torques correspond to changes in yaw rate.

**Insights**:
- Spikes in both front and rear brake torques that correspond to significant changes in yaw rate indicate the stability control system's response to braking forces.
- Consistent yaw rate despite changes in brake torques suggests effective stability control.

# Trend Analysis of Key Metrics Over Time

**Observations**:
- The line graph shows how each of the key metrics changes over time.
- By plotting these metrics together, it is possible to observe their behavior and relationships during different driving conditions.

**Insights**:
- **Smooth HV Battery Current**: This metric shows the overall current drawn from the HV battery. Spikes or drops in this metric could indicate periods of high power demand or regeneration.
- **Front Motor Current**: This metric shows the current drawn by the front motor. It helps in understanding the power distribution to the front motor during driving and regeneration.
- **Rear Motor Current**: This metric shows the current drawn by the rear motor. It helps in understanding the power distribution to the rear motor during driving and regeneration.
- **Max Regenerative Power**: This metric shows the maximum power recovered through regenerative braking. High values indicate effective energy recovery during braking events.

# Braking Power Trends Analysis

## 1. Braking Power Trends Over Time

**Observations**:
- The line graph shows how braking power metrics such as regenerative power and motor currents change over time.
- By plotting these metrics together, it is possible to observe their behavior during braking events.

**Insights**:
- **Max Regenerative Power**: This metric shows the maximum power recovered through regenerative braking. High values indicate effective energy recovery during braking events.
- **Front and Rear Motor Currents**: These metrics show the current drawn by the front and rear motors, respectively. They help in understanding the power distribution to the motors during braking and regeneration.

## 2. Statistical Distribution of Braking Power Metrics

**Observations**:
- Summary statistics show the distribution of braking power metrics during the data collection period.

**Insights**:
- Consistent values of braking power metrics suggest stable braking performance.
- Significant variations might indicate areas where braking performance can be improved.

## 3. Correlation Analysis Between Braking Power Metrics and Stability Parameters

**Observations**:
- The correlation matrix reveals the strength and direction of relationships between braking power metrics and stability parameters.

**Insights**:
- Strong correlations between braking power metrics and stability parameters can indicate how braking forces influence vehicle stability.
- Understanding these relationships helps in optimizing braking and stability control systems.

## 4. Analysis of Energy Usage During Sudden Braking: Regeneration vs. Vehicle Stability - Regenerative Power Trends During Braking Events

**Observations**:
- The line graph shows how max regenerative power changes during sudden braking events.
- Highlighting braking events helps observe the relationship between regenerative power and these events.

**Insights**:
- Spikes in max regenerative power during braking events indicate effective energy recovery.
- Consistent regenerative power values during braking events suggest stable energy recovery performance.

## 5. Stability Parameters During Braking Events

**Observations**:
- The graphs show how roll rate, yaw rate, longitudinal acceleration, and lateral acceleration change during sudden braking events.
- Highlighting braking events helps observe the impact of braking on these stability parameters.

**Insights**:
- Significant changes in stability parameters during braking events indicate the vehicle's dynamic response.
- Consistent stability parameters despite braking events suggest effective stability control.

## 6. Correlation Analysis Between Regenerative Power and Stability Parameters

**Observations**:
- The correlation matrix reveals the strength and direction of relationships between regenerative power and stability parameters during braking events.

**Insights**:
- Strong correlations between regenerative power and stability parameters indicate how braking forces influence vehicle stability and energy recovery.
- Understanding these relationships helps in optimizing braking and stability control systems for better energy recovery and vehicle control.


# Additional Observations for Powertrain

## 1. Comparison of Motor Currents During Different Driving Conditions

**Observations**:
- Motor currents vary significantly between acceleration, cruising, and deceleration.
- The front motor current shows different patterns compared to the rear motor.

**Insights**:
- Understanding the distribution of motor currents under different conditions helps in optimizing powertrain performance.
- Analyzing motor currents can provide insights into load distribution and efficiency.

## 2. Efficiency Analysis

**Observations**:
- Efficiency metrics (e.g., motor currents to battery current ratio) vary under different driving conditions.
- Efficiency tends to be higher during cruising compared to aggressive acceleration or deceleration.

**Insights**:
- Analyzing efficiency helps in understanding how effectively the vehicle uses energy under different conditions.
- Efficiency metrics can guide improvements in powertrain design and control strategies.

## 3. Drive Cycles and Power Demand

**Observations**:
- Power demand patterns vary significantly across different drive cycles (e.g., urban, highway).
- Regenerative braking efficiency differs between drive cycles.

**Insights**:
- Understanding power demand and regenerative braking efficiency across drive cycles can inform powertrain optimization.
- Analyzing drive cycles helps in designing better energy management systems.

## 5. Impact of Vehicle Speed on Powertrain Performance

**Observations**:
- Vehicle speed significantly influences powertrain parameters such as motor currents and regenerative power.
- High speeds generally lead to higher power demand and different regenerative braking efficiency.

**Insights**:
- Analyzing the impact of vehicle speed on powertrain performance helps in optimizing control strategies for different driving conditions.
- Understanding speed vs. power demand profiles can guide the development of more efficient powertrain systems.

## 6. Torque Distribution Analysis

**Observations**:
- Torque distribution between the front and rear wheels varies under different driving conditions.
- Effective torque vectoring contributes to enhanced vehicle stability and performance.
- Brake torque is distributed differently between the front and rear wheels under various driving conditions.
- Front brake torque tends to be higher during aggressive braking events compared to rear brake torque.

**Insights**:
- Analyzing torque distribution helps in understanding the effectiveness of torque vectoring systems.
- Insights from torque distribution analysis can guide the development of better traction control systems.
- Effective torque distribution between the front and rear wheels is crucial for maintaining vehicle stability and performance.
- Analyzing torque distribution helps in understanding the effectiveness of torque vectoring systems.

## 7. Impact of Acceleration and Deceleration

**Observations**:
- Battery current varies significantly between acceleration, cruising, and deceleration.
- Regenerative braking power shows different patterns during deceleration compared to acceleration.

**Insights**:
- Aggressive acceleration increases battery current demand, impacting overall efficiency.
- Effective regenerative braking during deceleration helps recover energy and improve efficiency.

## 8. Battery State of Charge (SoC) Dynamics

**Observations**:
- Battery SoC changes dynamically with driving conditions and power demand.
- Regenerative braking contributes to maintaining or increasing SoC during deceleration.

**Insights**:
- Monitoring SoC dynamics helps in managing battery health and optimizing energy usage.
- Understanding SoC changes can guide the development of more efficient regenerative braking systems.

## 9. Impact of Vehicle Speed on Powertrain Performance

**Observations**:
- Battery current varies across different speed ranges, with higher speeds generally leading to higher power demand.
- Front and rear motor currents show distinct patterns under different speed ranges.
- Max regenerative power varies with speed, indicating different efficiency levels at different speeds.

**Insights**:
- Understanding the impact of vehicle speed on powertrain performance helps in optimizing control strategies for different driving conditions.
- Analyzing speed vs. power demand profiles can guide the development of more efficient powertrain systems.
