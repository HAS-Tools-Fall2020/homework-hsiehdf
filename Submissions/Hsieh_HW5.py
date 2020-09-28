# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)


# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

#%%

#Question 1
print("the column names are:", data.columns)

#The index is 0-11591, and the data types are: objects, int64, float64, and int32.
data.index
print(data.info())

#%%
#Question 2

#Summary of flow column including min, mean, max and SD and quartiles 
data_flow= data.iloc[:,3]
data_flow2= data_flow.describe()
print(data_flow2.to_markdown())

#%%
#Question 3
#provide same info but on monthly basis
data_month= data.groupby(["month"])[["flow"]].describe()
print(data_month.to_markdown())

#%% 

#Question 4
#Provide a table with the 5 highest adn 5 flowest flow values. 
#include date month and flow values

#Gives the lowst values to highest values in data
low_five = data.sort_values(by="flow",ascending = True)
low_five2 = low_five.head(n=5) 
print(low_five2.to_markdown())
#Gives the highest to lowest values in data
high_five = data.sort_values(by="flow",ascending = False)
high_five2= high_five.head(n=5)
print(high_five2.to_markdown())

#%%
#Question 5

#Find the highest and lowest flow values for every month of the year 
#(i.e. you will find 12 maxes and 12 mins) and report back what year
# these occurred in.

data.groupby(["month"])[["flow"]].describe()

m1_max= data[data["flow"]==63400.0]
print(m1_max.to_markdown())
m1_min= data[(data["flow"]==158.0) & (data["month"]==1)]
print(m1_min.to_markdown())

m2_max= data[(data["flow"]==61000.0) & (data["month"]==2)]
print(m2_max.to_markdown())
m2_min= data[(data["flow"]==136.0) & (data["month"]==2)]
print(m2_min.to_markdown())

m3_max= data[(data["flow"]==30500.0)& (data["month"]==3)]
print(m3_max.to_markdown())
m3_min= data[(data["flow"]==97.0) & (data["month"]==3)]
print(m3_min.to_markdown())

m4_max= data[(data["flow"]==4690.0) & (data["month"]==4)]
print(m4_max.to_markdown())
m4_min= data[(data["flow"]==64.9) & (data["month"]==4)]
print(m4_min.to_markdown())

m5_max= data[(data["flow"]==546.0) & (data["month"]==5)]
print(m5_max.to_markdown())
m5_min= data[(data["flow"]==46.0) & (data["month"]==5)]
print(m5_min.to_markdown())

m6_max= data[(data["flow"]==481.0) & (data["month"]==6)]
print(m6_max.to_markdown())
m6_min= data[(data["flow"]==22.1) & (data["month"]==6)]
print(m6_min.to_markdown())

m7_max= data[(data["flow"]==1040.0) & (data["month"]==7)]
print(m7_max.to_markdown())
m7_min= data[(data["flow"]==19.0) & (data["month"]==7)]
print(m7_min.to_markdown())

m8_max= data[(data["flow"]==5360.0)& (data["month"]==8)]
print(m8_max.to_markdown())
m8_min= data[(data["flow"]==29.6) & (data["month"]==8)]
print(m8_min.to_markdown())

m9_max= data[(data["flow"]==5590.0)& (data["month"]==9)]
print(m9_max.to_markdown())
m9_min= data[(data["flow"]==36.6) & (data["month"]==9)]
print(m9_min.to_markdown())

m10_max= data[(data["flow"]==1910.0)& (data["month"]==10)]
print(m10_max.to_markdown())
m10_min= data[(data["flow"]==69.9) & (data["month"]==10)]
print(m10_min.to_markdown())

m11_max= data[(data["flow"]==4600.0)& (data["month"]==11)]
print(m11_max.to_markdown())
m11_min= data[(data["flow"]==117.0) & (data["month"]==11)]
print(m11_min.to_markdown())

m12_max= data[(data["flow"]==28700.0)& (data["month"]==12)]
print(m12_max.to_markdown())
m12_min= data[(data["flow"]==155.0) & (data["month"]==12)]
print(m12_min.to_markdown())

#%%
#Question 6

#Povide a list of historical dates with flows that are  # within 10% of your 
# week 1 forecast value. If there are none than increase the %10 window until 
# you have at least one other value and report the date and the new window you used

historical_flow= data[(data["flow"]<=64.9) & (data["flow"]>=53.1)]
print(historical_flow.to_markdown())
