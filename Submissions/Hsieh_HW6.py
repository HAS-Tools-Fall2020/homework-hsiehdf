# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime


# %%
# Set the file name and path to where you have stored the data
filename = 'streamflow_week6.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)


# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
        parse_dates=['datetime']
        )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregate flow values to weekly 
flow_weekly = data.resample("W", on='datetime').mean()

#%%

# Created a for loop to shift data 20 tiemes 

for k in range (1, 21):
        flow_weekly[k] = flow_weekly['flow'].shift(k)

# Step 2 - I used all the data and chose to use the first 1200 weeks
# Dropped the first twenty weeks since they wont have lagged data
# to go with them  
train = flow_weekly[21:1200][['flow', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13,\
         14, 15, 16, 17, 18, 19, 20]]
test = flow_weekly[1200:][['flow', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13,\
         14, 15, 16, 17, 18, 19,20]]

#Note, I tried to use data from the last 10 years, but that gave me an r2 of 0.11
#Therefore I abondoned this approach.
#flow_weekly = flow_weekly_all [(flow_weekly_all["year"] >=2010)]

# %%
# I did 20 lags with my model, 1-20. 

model2 = LinearRegression()
x2=train[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15, 16, 17, 18, \
        19, 20]]
y2=train['flow'].values
model2.fit(x2,y2)
r_sq = model2.score(x2, y2)
print('coefficient of determination:', np.round(r_sq,2))
print('intercept:', np.round(model2.intercept_, 2))
print('slope:', np.round(model2.coef_, 2))

# generating preditions with the funciton
q_pred2_train = model2.predict(train[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12,\
         13, 14, 15, 16, 17, 18, 19, 20]])
q_pred2_test = model2.predict(test[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13,\
         14, 15, 16, 17, 18, 19, 20]])

#Prediction for this week using my model

this_week_pred = model2.intercept_
for x in range (1, 21):
        this_week_pred = this_week_pred + model2.coef_[x-1] * test[x].tail(1)
print (this_week_pred)


# %% 
# 1. Timeseries of observed flow values
# Note that date is the index for the dataframe so it will 
# automatically treat this as our x axis unless we tell it otherwise

#This is the range of my training data
fig, ax = plt.subplots()
ax.plot(train['flow'], color='gold', linestyle= "-", label='training')
ax.set(title="Observed Flow", xlabel="Date", 
        ylabel="Weekly Avg Flow [cfs]",
        yscale='log')
ax.grid (True)
ax.legend()

#This is the range of my testing data
fig, ax = plt.subplots()
ax.plot(test['flow'], '-c', label='test')
ax.set(title="Testing Flow", xlabel="Date", 
        ylabel="Weekly Avg Flow [cfs]",
        yscale='log')
ax.grid (True)
ax.legend()

#combined training and range data
fig, ax = plt.subplots()
ax.plot(test['flow'], '-c', label='test')
ax.plot(train['flow'], color='gold', linestyle = '-', label='training')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
        yscale='log')
ax.grid (True)
ax.legend()

fig.set_size_inches(5,3)
fig.savefig("Range of Training and Test Flow.png")

#2. Time series of flow values with the x axis range limited
fig, ax = plt.subplots()
ax.plot(test['flow'], '-c', label='test')
ax.plot(train['flow'], color='gold', linestyle = '-', label='training')
ax.set(title="Limited X Axis Flow Values", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
        yscale='log', xlim=[datetime.date(2004, 1, 26),         
        datetime.date(2020, 10, 4)])
ax.grid (True)
ax.legend()

fig.set_size_inches(5,3)
fig.savefig("Limited X Axis Flow Values.png")

# 3. Line  plot comparison of predicted and observed flows
fig, ax = plt.subplots()
ax.plot(train['flow'], color='plum', linewidth=2, label='observed')
ax.plot(train.index, q_pred2_train, color='yellow', linestyle='-', 
        label='simulated')
ax.set(title="Predicted vs. Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
        yscale='log')
ax.legend(loc='upper center', frameon = False)

#Saving the figure
fig.set_size_inches(5,3)
fig.savefig("Predicted vs Observed Flow.png")

plt.show()
# %%
