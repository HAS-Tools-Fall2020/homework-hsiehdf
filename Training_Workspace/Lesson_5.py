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
