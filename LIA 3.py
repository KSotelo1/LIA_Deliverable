# Collaborators: Mia Doan (2483330) & Kaira Sotelo (6293070)


# IMPORTS
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 

# DATASET
data = pd.read_csv("Forest_Fires_Dataset.csv", encoding="cp1252")

#########################################################################

# Q2 - PRELIMINARY STEPS
# a) Initial Data Inspection: 
    
# head fct
print("First five rows of the dataset:")
print(data.head())

# shape fct
print("Number of rows and columns in the dataset:")
print(data.shape)

# info fct 
print("Summary of dataset:")
print(data.info())

# describe fct
print("Basic descriptive statistics for each column:")
print(data.describe())

# dtype fct
print("Type of value in each column:")
print(data.dtypes)

# memory_usage fct
print("Memory usage of each column")
print(data.memory_usage())


# b) Handle duplicate entries

# duplicates
print()
print("Number of duplicated rows:")
print(data.duplicated())

# remove duplicates
print("After removing duplicates:")
print(data.drop_duplicates())


# c) Identify and manage missing values
print()
print(data.isnull().sum())
#There are no missing values, since the isnull and sum functions return 0.

# d) Correct data types and formats
print()
data["Year"] = pd.to_datetime(data["Year"])

# pd.to_numeric isn't necessary since the numerical value, such as "Number", are already identified as numbers

###############################################################################

# Q3 - UNIVARIATE NON-GRAPHICAL EDA 
# For the "Number" column, since it's the onl categorical variable

# mean
print()
print("The mean is:")
print(data["Number"].mean())

# median 
print("The median is:")
print(data["Number"].median())

# mode
print("The mode is:")
print(data["Number"].mode())

# standard deviation
print("The standard deviation is:")
print(data["Number"].std())

# variance 
print("The variance is:")
print(data["Number"].var)

# skewness
print("The skewness is:")
print(data["Number"].skew())

# kurtosis
print("The kurtosis is:")
print(data["Number"].kurtosis())

# quartiles
print("The quartiles are:")
print(data["Number"].quantile([0.25, 0.5,0.75]))


for col in data.select_dtypes(exclude=[np.number]):
    # repeat loop for all categorical variables
    # frequency count
    print("The frequency count is:")
    print(data[col].value_counts())
    # proportion
    print("The proportion is")
    print(data[col].value_counts(normalize=True) * 100)
    # The normalize = True calculates the relative frequency (proportion) and * 100 changes the values into percentage
    # mode
    print("The mode is")
    print(data[col].mode()[0])
    # number of unique categories
    print("The number of unique categories:")
    print(data[col].nunique())
    
    
################################################################################

# Q4 - UNIVARIATE GRAPHICAL EDA 

# VIZUALING DISTRIBUTION OF DATA 

# selection of numerical variable columns
numeric_cols = data.select_dtypes(include=[np.number]).columns

# a) Histogram: custom/appropriate number of bins 
sns.histplot( data, x="Number", bins=20, kde=False, color="blue")
plt.title("Histogram of Number of Fires for 20 bins")
plt.xlabel("Number of Fires")
plt.ylabel("Count")
plt.show()
####!!!!!!!!!!!!
    
# b) Conditioning on other variables 
# using "Jurisdiction"
sns.histplot( data=data, x="Number", hue="Jurisdiction", bins=15)
plt.title("Number of Fires by Jurisdiction")
plt.xlabel("Number of fires")
plt.ylabel("count")
plt.show()
        
# c) Stacked histogram
sns.histplot( data=data,  x="Number", hue="Jurisdiction", multiple = "stack", bins=15)
plt.title("stacked histograms of Number of Fires by Jurisdiction")
plt.xlabel("Number of fires")
plt.ylabel("Count")
plt.show()
        
# d) Dodge bars 
sns.histplot( data=data, x="Number", hue="Jurisdiction", multiple="dodge", bins=15)
plt.title("Dodge histogram of Number of Fires by Jurisdiction")
plt.xlabel("Number of fires")
plt.ylabel("Count")
plt.show()
        
# e) Normalized histogram statistics
sns.histplot( data,  x="Number", bins=15, stat="count", color="red")
plt.title("Normalized histogram (count) of Number of Fires") 
plt.xlabel("Number of fires")
plt.ylabel("Count")
plt.show()
        
# f) Kernel Density Estimation (choosing the smoothing bandwidth)
# bandwidth of 0.5 allows for more less smoothing and more detail
sns.kdeplot( data,  x="Number", fill=True, color="green", bw_adjust = 0.5)
plt.title("Kernel Density Estimation plot of Number of Fires") 
plt.xlabel("Number of fires")
plt.ylabel("Density")
plt.show()
    
# g) Empirical cumulative distributions
sns.ecdfplot( data,  x="Number", color="pink")
plt.title("Empirical cumulative distributions of Number of Fires") 
plt.xlabel("Number of fires")
plt.ylabel("Cumulative probability")
plt.show()
    
# Q5 - MULTIVARIATE NON-GRAPHICAL EDA
# Since we only have 2 categorical variables, we can only use the crosstab function to verify the intersection between 2 varibles once

# Intersection between "Cause" and "Jurisdiction" 
cause_per_jurisdiction = pd.crosstab( data["Cause"], data["Jurisdcition"], normalize=True)
print(cause_per_jurisdiction)

# Intersection between more than 2 variables
three_way_frequency_table = pd.crosstab( data["Cause"], data["Jurisdiction"], data["Year"], data["Data Qualifier"])
print(three_way_frequency_table)
    

# Q6 - MULTIVARIATE GRAPHICAL EDA 

# 6.1: statistical relationships 
# a) Faceting 
# b) x,y,hue,size,col
# c) line 
# d) standard deviation 
# e) linear regression 

# 6.2: Categorical data 
# a) Scatter plot, with jitter
# b) Scatter plot, without jitter
# c) Beeswarm plot
# d) Box plot, with 3 variables 
# e) Boxenplot
# f) split violin plot 
# g) violin plot, with scatter points
# h) bar plot, 97% CI
# i) bar plot, 90% CI 
# j) bar plot, with number of observations

# 6.3: Bivariate distributions 
# a) Heatmap plot, with 2 variables
# b) Dstribution plot
# c) Heatmap plot, with 3 varibles