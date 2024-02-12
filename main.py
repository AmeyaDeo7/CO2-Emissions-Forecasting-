import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 

# data = pd.read_csv("dataSets/temperature-anomaly.csv")
# print(data.head)

dataTwo = pd.read_csv("dataSets/co-emissions-per-capita.csv")
print(dataTwo.head)

# print("<------------------->\n")
# print(data.describe())

# print("<------------------->\n")
# print(data.info())

# print("<------------------->\n")
# print(data.describe())

##Shows the temperature anomolies over the course of ~30 years 
# figure = px.line(data, x="Year", y="Global average temperature anomaly relative to 1961-1990", title="Global Temperature Anomalies")
# figure.show() 

##Shows the line chart relating to the CO₂ Emissions that were released over the time span
# figureTwo = px.line(dataTwo, x="Year", y="Annual CO₂ emissions (per capita)", title="Global C02 Emissions")
# figureTwo.show()


##Used a bar graph to show a different representation of the data, easier to read and understand
# figureTwo = px.bar(dataTwo, x="Entity", y="Annual CO₂ emissions (per capita)", title="Average C02 Emissions Per Capita")
# figureTwo.show()

##Used a scatter plot that allowed 
# figureTwo = px.scatter(data_frame= dataTwo, x='Year', y='Annual CO₂ emissions (per capita)', size='Annual CO₂ emissions (per capita)', trendline= 'ols',
#                        title="Relationship between country and Annual CO2 Emissions")
# figureTwo.show()


## Analyzing the change in CO2 Emissions:
print(dataTwo.head)



