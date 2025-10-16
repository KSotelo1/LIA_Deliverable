# Collaborators: Mia Doan (2483330) & Kaira Sotelo (6293070)
# Description: dataset to plot graph of the area burned in the last 10 years by forest fires  

# import 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

# Read dataset 
dataset = pd.read_csv("Area_burned_dataset.csv")

# variables
year = df['Year']
jurisdiction = df["Jurisdiction"]

    