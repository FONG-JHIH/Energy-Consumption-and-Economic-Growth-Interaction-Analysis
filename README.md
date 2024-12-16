# Multidimensional Data Analysis: Correlation Study between Taiwan's Electricity Consumption and Manufacturing GDP
# Project Overview
This project focuses on the correlation between electricity consumption and GDP in Taiwan's manufacturing sector. By analyzing data from 2019 to 2023, it explores the relationship between energy consumption and economic growth. The study employs multidimensional data analysis, leveraging Python for data processing and visualization, to provide in-depth insights and clear graphical representations.
# Project Objectives
1.	Analyze the correlation between Taiwan's manufacturing electricity consumption and GDP, exploring the impact of energy efficiency on economic output.
2.	Investigate the energy consumption structure and trends within various subsectors of the manufacturing industry.
3.	Use diverse types of charts (e.g., area plots, stacked bar charts, and dual-axis line graphs) to visualize the changes in Taiwan's manufacturing energy consumption and economic patterns.
# Key Features
1.	Data Cleaning and Integration
o	Automates data cleaning, including handling missing values, unit conversion, and data normalization.
o	Merges multi-year data to establish a structured analysis framework.
2.	Correlation Analysis
o	Calculates the correlation coefficient between electricity consumption and GDP using NumPy to quantify their relationship.
3.	Data Visualization
o	Area Plot: Shows overall trends in electricity consumption and GDP in Taiwan's manufacturing sector.
o	Dual-Axis Line Graph: Compares annual changes in electricity consumption and GDP.
o	Stacked Chart: Displays the structural proportions of electricity consumption in different subsectors.
o	Bar Chart: Highlights electricity consumption trends in electronic components manufacturing subsectors.
# Technical Details
1.	Technology Stack:
o	Python: Uses Pandas and NumPy for data processing and Matplotlib for visualization.
o	Data Format: Data sourced from CSV files and standardized after cleaning.
2.	Data Processing Logic:
o	Data cleaning: Removes empty values and anomalies, fills in missing industry classifications.
o	Analysis framework: Groups data by year and industry, generating annual summaries and percentage distributions.
3.	Correlation Analysis Methodology:
o	Uses NumPy to calculate Pearson correlation coefficients to evaluate the relationship between electricity consumption and GDP.
# Execution Steps
1.	Install Dependencies:
pip install pandas numpy matplotlib
2.	Prepare Data:
o	Ensure data files (e.g., Industry_electricity.csv and GDP by industry Report.csv) are stored in the project directory.
3.	Run the Script:
Multidimensional Data Analysis Correlation Study between Taiwan's Electricity Consumption and Manufacturing GDP.py
4.	View Results:
o	After execution, charts will be generated and displayed in the local environment.
# Analysis Findings
1.	The correlation coefficient between electricity consumption and GDP in Taiwan's manufacturing sector is 0.92, indicating a strong relationship between energy consumption and economic output.
2.	Electricity consumption in the semiconductor manufacturing subsector has been increasing annually, becoming a key driver of growth in the manufacturing sector.
3.	The energy structure of various industries shows a continuous optimization trend, with the proportion of high-energy-consuming industries gradually decreasing, reflecting a shift toward more efficient energy use in manufacturing.
# Future Prospects
1.	Expanding the Scope of Analysis: Extend the study to other industries (e.g., services and high-tech industries) to explore broader economic patterns.
2.	Green Energy and Carbon Emission Analysis: Incorporate green energy indicators and CO2 emission data to examine low-carbon transition pathways in the manufacturing sector.
3.	Dynamic Reporting and Real-Time Updates: Deploy the system on cloud platforms to enable real-time data updates and dynamic analysis results.








