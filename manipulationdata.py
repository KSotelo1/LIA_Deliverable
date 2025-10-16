import pandas as pd

path = r"C:\Users\miado\OneDrive\Desktop\Forest_Fires_Dataset.csv"

# Most likely fixes on Windows CSVs:
df = pd.read_csv(path, usecols=[0,3,7], encoding="cp1252")
print(df)

# Exact match (case-insensitive)
df_qc = df[df['Jurisdiction'].astype(str).str.strip().str.casefold() == 'quebec'].reset_index(drop=True)
print(df_qc)

# --- Quebec entries with number between 100 and 500 ---
df_qc_100_500 = df_qc[pd.to_numeric(df_qc["Number"], errors='coerce').between(100, 500)].reset_index(drop=True)
print(df_qc_100_500)

# --- Quebec entries with number between 100 and 500 from years 2003 to 2018---
df_qc_100_500_2003_2018 = df_qc_100_500[pd.to_numeric(df_qc["Year"], errors='coerce').between(2003, 2018)].reset_index(drop=True)
print(df_qc_100_500_2003_2018)

# --- Quebec entries with years between 2003 to 2018---
df_qc_2003_2018 = df_qc[pd.to_numeric(df_qc["Year"], errors='coerce').between(2003, 2018)].reset_index(drop=True)
print(df_qc_2003_2018)

