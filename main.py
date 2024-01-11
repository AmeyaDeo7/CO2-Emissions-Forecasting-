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

##Shows the 
# figure = px.line(data, x="Year", y="Global average temperature anomaly relative to 1961-1990", title="Global Temperature Anomalies")
# figure.show() 

# figureTwo = px.line(dataTwo, x="Year", y="Annual CO₂ emissions (per capita)", title="Global C02 Emissions")
# figureTwo.show()

figureTwo = px.bar(dataTwo, x="Entity", y="Annual CO₂ emissions (per capita)", title="Average C02 Emissions Per Capita")
figureTwo.show()





