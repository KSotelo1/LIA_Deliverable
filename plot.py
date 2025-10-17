import pandas as pd
import numpy as np

path = r"C:\Users\miado\OneDrive\Desktop\Forest_Fires_Dataset.csv"

import matplotlib.pyplot as plt 
df = pd.read_csv(path, usecols=[0, 3, 7], encoding="cp1252")

#column names
df.columns = ["year", "jurisdiction", "area"]

#1st plot where x = years and y = wildfires


plt.scatter(df["year"], df["area"])
plt.title("Area Burned vs Year")
plt.xlabel("year")
plt.ylabel("Area Burned (hectares)")
plt.show()

#comments: This scatter plot shows a lot of variations of fires throughout the years

#historgram
plt.hist(df["area"])
plt.title("Area Burned")
plt.xlabel("area")
plt.show()

#comments: This histogram shows the variation in areas burned.

#Bar plot
plt.bar(df["area"], df["year"])
plt.title("Area Burned vs Year")
plt.xlabel("year")
plt.ylabel("Area Burned (hectares)")
plt.show()

#comments: This bar plot describes the areas categories of the fires to distinguish if they are big or small (in hectares). 

#pie chart
labels = df["jurisdiction"]
plt.pie()
plt.title("Pie Chart of Areas burned by Jurisdiction")
plt.axis("equal")
plt.show()

