#%%
import os

import matplotlib.pyplot as plt
import pandas as pd
import earthpy as et

# Download file from URL
et.data.get_data(url=avg_monthly_precip_url)

# Set working directory to earth-analytics
os.chdir(os.path.join(et.io.HOME, 
                      "earth-analytics", 
                      "data"))
                      
# %%

# Import data from .csv file
fname = os.path.join("earthpy-downloads",
                     "avg-precip-months-seasons.csv")

avg_monthly_precip = pd.read_csv(fname)

avg_monthly_precip
#%%
filename = 'streamflow_week4.txt'
filepath = os.path.join('../data',filename)


print(os.getcwd())
print(filename)

avg_monthly_precip = pd.read_cvs(filepath)
# %%
data.columns
#All of the data. Not most helpful, only shows 10 rows (first 5 last 5)
#Does include number or rows and columns though
print (data)
#The first 5 rows
data.head()
#Last five rows
data.tail()
#Super helpful! Tells us what each column is made up of

data.info()

#normal, tells us the dimensions of array. 
data.shape

#%%
#Grouped by months
data.groupby(["month"])[["flow"]].describe()

data.groupby(["month"])[["flow"]].mean()
# %%
y= data.iloc[:, 3]
print (y)
# %%
data[data["flow"]<=64.9 and >=53.1]