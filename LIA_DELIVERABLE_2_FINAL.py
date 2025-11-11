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

#comments: This bar plot does not give significant results 

#pie chart
labels = [ "Alberta", "Quebec", "Saskatchewan", "Manitoba", "British-Columbia", "New-Brunswick", "Nova Scotia", "Prince Edward Island", " Northwest territories", "Newfoundland & labrador", "Ontario", "Yukon"]
size = [29365, 17338, 12457, 10618, 35406, 10963, 9002, 561, 6963, 4027, 27867, 3373]
colors = ["red", "orange", "yellow", "green", "blue", "pink", "purple", "brown", "cyan", "magenta", "white", "black" ]
plt.pie(size, labels = labels, colors = colors, startangle=140)
plt.title("Pie Chart of Areas burned by Jurisdiction")
plt.axis("equal")
plt.show()

#1 plot of any type containing 2 subplots side by side
fig, axes = plt.subplots(1, 2, figsize=(10, 4))  # 1 row, 2 columns

#left subplot: scatter of area vs year
axes[0].scatter(df["year"], df["area"], color="teal")
axes[0].set_title("Scatter: Area vs Year")
axes[0].set_xlabel("Year")
axes[0].set_ylabel("Area Burned (hectares)")

# Right subplot: histogram of area burned
axes[1].hist(df["area"], bins=20, color="salmon", edgecolor="black")
axes[1].set_title("Histogram: Distribution of Burned Area")
axes[1].set_xlabel("Area Burned (hectares)")
axes[1].set_ylabel("Frequency")

# Main title for both
fig.suptitle("Two Subplots: Area Trends and Distribution", fontsize=14)
plt.tight_layout()
plt.show()

#comments: these two subplots show how burned area changes over the years (the one on the left) and how the areas are distributed (the one on the right)

