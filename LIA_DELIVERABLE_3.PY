# Collaborators: Mia Doan (2483330) & Kaira Sotelo (6293070)


# Imports 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 

# Dataset 
data = pd.read_csv("Forest_Fires_Dataset.csv")

# a) Initial Data Inspection: 
print()
print(data.head())
print("Number of rows and columns in the dataset:")
print(data.shape())
print("Summary of dataset:")
print(data.info())
print("Basic descriptive statistics for each column:")
print(data.describe())
print("Type of value in each column:")
print(data.dtypes())
print("Memory usage of each column")
print(data.memory_usage())

# b) Duplicates:
duplicates = data.duplicated().sum()
print("This dataset has ", duplicates, "empty values.")
if duplicates > 0: 
    data = data.drop_duplicates()
    print("Duplicates have been removed")
    
else: 
    print("No duplicates have been found")