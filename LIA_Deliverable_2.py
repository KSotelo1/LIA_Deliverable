# collaborators
# Mia Doan (2483330) & Kaira Sotelo (6293070)

# import 
import numpy as np

# variables
year, jurisdiction, area_in_hectares = np.loadtxt("Area_burned_dataset.csv", skiprows = 1, usecols = (0,3,7), unpack = True )

# loops 
for i in year: 
    if year  < 2010 or year  > 2021: 
        
    
    