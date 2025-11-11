# Collaborators: Mia Doan (2483330) & Kaira Sotelo (6293070)


# Imports 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 

# Dataset 
data = pd.read_csv("Forest_Fires_Dataset.csv", encoding="cp1252")
df = pd.read_csv("Forest_Fires_Dataset.csv", encoding="cp1252")


# Q2. Prelimiary steps
# a) Initial Data Inspection: 
print()
print(data.head())
print("Number of rows and columns in the dataset:")
print(data.shape)
print("Summary of dataset:")
print(data.info())
print("Basic descriptive statistics for each column:")
print(data.describe())
print("Type of value in each column:")
print(data.dtypes)
print("Memory usage of each column")
print(data.memory_usage())

# b) Handle duplicate entries
print()
print("Number of duplicated rows:")
print(data.duplicated())
print("After removing duplicates:")
print(data.drop_duplicates())

# c) Identify and manage missing values
print()
print(data.isnull().sum())
#There are no missing values

# d) Correct data types and formats
print()
data["Year"] = pd.to_datetime(data["Year"])



# Q3. Univariate non-graphical EDA
print()
print("The mean is:")
print(data["Number"].mean())
print("The median is:")
print(data["Number"].median())
print("The mode is:")
print(data["Number"].mode())
print("The standard deviation is:")
print(data["Number"].std())
print("The variance is:")
print(data["Number"].var)
print("The skewness is:")
print(data["Number"].skew())
print("The kurtosis is:")
print(data["Number"].kurtosis())
print("The quartiles are:")
print(data["Number"].quantile([0.25, 0.5,0.75]))

#For each categorical variables

for col in df.select_dtypes(exclude=[np.number]):
    print("The frequency count is:")
    print(df[col].value_counts())
    print("The proportion is")
    print(df[col].value_counts(normalize=True) * 100)
    # The normalize = True calculates the relative frequency (proportion) and * 100 changes the values into percentage
    print("The mode is")
    print(df[col].mode()[0])
    print("The number of unique categories:")
    print(df[col].nunique())
    
#Q4. Univariate graphical EDA
#Section 1: visualizing distribution of data 

#select only numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns

#numeric variable 
#a)Histograms with custom and appropriate number of bins
sns.histplot(df, x="Number", bins=20, kde=False, color="blue")
plt.title("Histogram of Number of Fires for 20 bins")
plt.xlabel("Number of Fires")
plt.ylabel("count")
plt.show()
####!!!!!!!!!!!!
    
#b) Conditioning on other variables using jurisdiction for example
   
sns.histplot(data=df, x="Number", hue="Jurisdiction", bins=15)
plt.title("Number of Fires by Jurisdiction")
plt.xlabel(col)
plt.ylabel("count")
plt.show()
        
#c) Stacked histogram
   
sns.histplot(data=df,  x="Number", hue="Jurisdiction", multiple = "stack", bins=15)
plt.title("stacked histograms of Number of Fires by Jurisdiction")
plt.xlabel(col)
plt.ylabel("count")
plt.show()
        
#d) Dodge bars
    
sns.histplot(data=df, x="Number", hue="Jurisdiction", multiple="dodge", bins=15)
plt.title("Dodge histogram of Number of Fires by Jurisdiction")
plt.xlabel(col)
plt.ylabel("count")
plt.show()
        
#e) Normalized histogram statistics
sns.histplot(df,  x="Number", bins=15, stat="count", color="red")
plt.title("Normalized histogram (count) of Number of Fires") 
plt.xlabel(col)
plt.ylabel("count")
plt.show()
        
#f)  Kernel density estimation (choosing the smoothing bandwidth)
sns.kdeplot(df,  x="Number", fill=True, color="green")
plt.title("Kernel Density Estimation plot of Number of Fires") 
plt.xlabel(col)
plt.ylabel("density")
plt.show()
    
#g)  Empirical cumulative distributions
sns.ecdfplot(df,  x="Number", color="pink")
plt.title("Empirical cumulative distributions of Number of Fires") 
plt.xlabel(col)
plt.ylabel("cumulative probability")
plt.show()
    
#Q5. Multivariate non-graphical EDA
#intersection between jurisdiction and causes
cause_per_jurisdiction = pd.crosstab(data["Cause"], data["Jurisdcition"], normalize=True)

    
    
    