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
# Since we only have 3 categorical variables ( Year, Cause and Jurisdiction ), we can only use the crosstab function to verify the intersection variables twice

# Intersection between "Cause" and "Jurisdiction" 
cause_per_jurisdiction = pd.crosstab( data["Cause"], data["Jurisdiction"], normalize=True)
print(cause_per_jurisdiction)

# Intersection between "Year" and "Cause" 
cause_per_year = pd.crosstab( data["Cause"], data["Year"], normalize=True)
print(cause_per_year)

# Intersection between more than 2 variables
three_way_frequency_table = pd.crosstab( index = [data["Cause"], data["Jurisdiction"]], columns =  data["Year"])
print(three_way_frequency_table)


   

####################################################################################


# Q6 - MULTIVARIATE GRAPHICAL EDA 

# 6.1: statistical relationships 

# a) Faceting 
sns.relplot( data = data, x = data['Number'], y = data["Cause"], col = "Jurisdiction")
plt.title(" Relationship between Number of fires and Cause, based on Jurisdiction")
plt.show()

# b) x,y,hue,size,col
sns.relplot( data = data, x = data['Number'], y = data["Cause"], hue = "Jurisdiction", col = "Cause")
plt.title(" Relationship between Number of fires and Cause, based on Jurisdiction")
plt.show()

# c) line 
sns.relplot( data = data, x = data["Number"], y = data["Jurisdiction"], hue = "Cause", kind = "line")
plt.title(" Line relationship between Number of fires and Cause, based on Jurisdiction")
plt.show()
# it makes sense to make the number of fires a linear plot, since we can better visualize the variation between them

# d) standard deviation 
sns.relplot( data = data, x = data['Number'], y = data["Cause"], col = "Jurisdiction", kind="line", errorbar = "sd",)
plt.title(" Relationship between Number of fires and Cause, based on Jurisdiction, with standard deviation")
plt.show()

# e) linear regression 
#In order to have only numeric values, we have to convert "Year" column into a number before plotting it
data["Year"] = pd.to_datetime(data["Year"], errors="coerce").dt.year
data["Year"] = pd.to_numeric(data["Year"], errors="coerce")

sns.lmplot( data = data, x ='Year', y = "Number", hue = "Jurisdiction", col = "Jurisdiction")
plt.title(" Linear relationship between Number of fires and Cause, based on Jurisdiction")
plt.show()

# 6.2: Categorical data 
# a) Scatter plot, with jitter
#Use of sns.stripplot because we only have categorical scatter plot 
sns.stripplot(data=data, x="Cause", y="Number", jitter=True, hue="Jurisdiction")
plt.title("Categorical Scatter Plot (Jitter enabled)")
plt.show()

# b) Scatter plot, without jitter
sns.stripplot(data=data, x="Cause", y="Number", jitter=False, hue="Jurisdiction")
plt.title("Categorical Scatter Plot (Jitter disabled)")
plt.show()

# c) Beeswarm plot representing 3 variables
sns.swarmplot(data=data, x="Cause", y="Number", hue="Jurisdiction")
plt.title("Beeswarm Plot: Number of Fires by Cause and Jurisdiction")
plt.show()

# d) Box plot, with 3 variables 
sns.boxplot(data=data, x="Cause", y="Number", hue="Jurisdiction")
plt.title("Box Plot Showing Distribution Shape of Number of Fires by Cause")
plt.show()

# e) Boxenplot showing the shape of the distribution
sns.boxenplot(data=data, x="Cause", y="Number", hue="Jurisdiction")
plt.title("Box Plot Showing Distribution Shape of Number of Fires by Cause")
plt.show()

# f) split violin plot 
sns.violinplot(data=data, x="Cause", y="Number", hue="Jurisdiction", split=True, bw_adjust=0.6)
#Choice of bandwith 0.6 to add more detail, especially since there is distribution overlap
plt.title("Split Violin Plot (with bw_adjust=0.6) Showing Number of Fires by Cause")
plt.show()

# g) violin plot, with scatter points
sns.violinplot(data=data, x="Cause", y="Number", inner=None, color="pink")
sns.stripplot(data=data, x="Cause", y="Number", color="blue", size=3)
plt.title("Violin PLot with Scatter Points Inside")
plt.show()
#The inner=None removes the default inner lines or dots from the violin plot to have a shape that is clearer and size=3 makes the overlaped scatter points small to offer a clearer observations

# h) bar plot, 97% CI
sns.barplot(data=data, x="Cause", y="Number", hue="Jurisdiction", ci=97)
plt.title("Bar Plot (with 97% Confidence Interval): Number of Fires by Cause and Jurisdiction")
plt.show()

# i) bar plot, 90% CI 
sns.pointplot(data=data, x="Cause", y="Number", hue="Jurisdiction", ci=90, linestyles="--")
plt.title("Point plot (with 90% Confidence Interval and Dashed Lines): Number of Fires by Cause and Jurisdiction")
plt.show()

# j) bar plot, with number of observations
sns.countplot(data=data, x="Cause", hue="Jurisdiction")
plt.title("Count of Observations of Number of Fires per Cause and Jurisdiction")
plt.show()

# 6.3: Bivariate distributions 
# a) Heatmap plot, with 2 variables
sns.displot(data=data, x= "Number", y= "Year", bins=(20,20), cmap="coolwarm", cbar=True)
plt.title("Heatmap of Number of Fires vs Year with Color Intensity bar and Adjusted Bin Width")
plt.show()

# b) Distribution plot with bivariate density contours (KDE)
#Making sure all data is numeric and drop the missing values
data["Year"] = pd.to_numeric(data["Year"], errors="coerce")
data["Number"] = pd.to_numeric(data["Number"], errors="coerce")
data = data.dropna(subset=["Year","Number"])

sns.displot( data, x = "Number", y = "Year", kind = "kde", fill=True, levels=15, thresh=0.5, cmap="rocket", cbar=True) 
plt.title("Bivariate KDE plot: Number of Fires vs Year with Contour Levels") 
plt.show() 

# c) Heatmap plot, with 3 varibles 
sns.displot( data, x = "Number", y = 'Year', hue = "Jurisdiction", kind="kde", fill=True, levels=10, thresh=0.1, cmap="crest") 
plt.title("Heatmap Plot: Number of Fires vs Year by Jurisdiction")
plt.show()
#The fill=True will fill the contours of the distribution plot, the levels=# is the number of contour lines and the thresh=# if the lowest contour level that filters low-density areas






