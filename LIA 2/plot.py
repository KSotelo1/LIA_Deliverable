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

#historgram + grid
plt.hist(df["area"])
plt.grid(True)
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

#comments: This bar plot shows the variation in areas burned per year, however it is irrelevant in our case since we cannot find other variables to make a better bar plot

#pie chart
labels = [ "Alberta", "Quebec", "Saskatchewan", "Manitoba", "British-Columbia", "New-Brunswick", "Nova Scotia", "Prince Edward Island", " Northwest territories", "Newfoundland & labrador", "Ontario", "Yukon"]
size = [29365, 17338, 12457, 10618, 35406, 10963, 9002, 561, 6963, 4027, 27867, 3373]
colors = ["red", "orange", "yellow", "green", "blue", "pink", "purple", "brown", "cyan", "magenta", "white", "black" ]
plt.pie(sizes, labels = labels, colors = colors, startangle=140)
plt.title("Pie Chart of Areas burned by Jurisdiction")
plt.axis("equal")
plt.show()

#comment: This pie chart shows the numbers of fires per jurisdiction

#2 subplots 

