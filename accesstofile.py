
import pandas as pd

path = r"C:\Users\miado\OneDrive\Desktop\Forest_Fires_Dataset.csv"

# Most likely fixes on Windows CSVs:
df = pd.read_csv(path, usecols=[0,3,7], encoding="cp1252", skiprows=1)
print(df)


