# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime

# %%
# Here is my first function!

# LC - Nice documentation
def get_mean(days_of_flow):
    """Function to get my mean from x amount of days ago

    This function will give us the mean flows from the *tail* end of our data.
    We can ask it to give us last weeks mean (i.e., last 7 days) or however
    many days we ask it to look back to.

    two_week_mean is an int or float
    """

    mymean = np.mean(data.tail(days_of_flow)['flow'])
    return mymean
# %%

# Below is the USGS streamgauge website that we will read to predict
# streamflow
url = 'https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=' \
      'rdb&site_no=09506000&referred_module=sw&period=&begin_date' \
      '=1989-01-01&end_date=2020-11-14'


# Read the data into a pandas dataframe
data = pd.read_table(url, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime', 'flow',
                            'code'], parse_dates=['datetime'], 
                     )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregate flow values to weekly
flow_weekly = data.resample("W", on='datetime').mean()

# %%
# Created a for loop to shift/lag my flow data 20 times which also creates
# new columns (1-20) of the shifted flow data.

for k in range(1, 21):
    flow_weekly[k] = flow_weekly['flow'].shift(k)

# I used the entire data set (1989 forward) and chose to use the first
# 1200 weeks for my training set. I dropped the first twenty weeks since
# they didn't have lagged data to go with them. My test set is composed
# of rows 1200 onward.


# LC - you could set the 21 and 1200 values as variables 
# also you can use a series to create your 1-20 values without typing them all out. 
# list(range(20))+1
shifts = list(range(1,21))
shifts_and_flow = ["flow"] + shifts


training_start = 21
training_end = 1200

train = flow_weekly[training_start:training_end][shifts_and_flow]
test = flow_weekly[training_end:][shifts_and_flow]


# %%
# This fit my data into a linear regressoin model. My x axis is my shifted flow
# values. My y axis is the flow values.

model = LinearRegression()

# LC - see comment above on the series. 
# This section would be good to put in a function. 
x = train[shifts]
y = train['flow'].values
model.fit(x, y)
r_sq = model.score(x, y)
print('The coefficient of determination is:', np.round(r_sq, 2))
print('The Y intercept is:', np.round(model.intercept_, 2))
print('The slopes are:', np.round(model.coef_, 2))


# Prediction for week 1 using my AR model. I used a for loop that would make a
# line with the equation y = m1x1 + m2x2 ... m20x20 + b

this_week_ARpred = model.intercept_

for f in range(1, 21):
    this_week_ARpred = model.coef_[f-1] * test[f].tail(1) + this_week_ARpred
print("this is the first week AR prediction:", np.int(this_week_ARpred.values))

# Prediction for week 2 using my model. This code is interesting, as I had to
# use my weekly flow value I predicted above and use it in my second
# weeks prediction. I did this by first setting "next_week_pred" equal to my
# model.intercept_, then added m1 (model.coef_[0]) times x1 (this_week_pred).
# This gave me y= m1x1 + b. Then I only made the for loop go 1-20 (instead of
# 1-21) because my first week was already acounted for. This gave me the
# same equation as above y = m1x1 + m2x2 ... m20x20 + b using my newest
# weekly flow and all other x values shifted by one week.

next_week_ARpred = model.intercept_

next_week_ARpred = this_week_ARpred * model.coef_[0] + next_week_ARpred

for p in range(1, 20):
    next_week_ARpred = model.coef_[p] * test[p].tail(1) + next_week_ARpred

print("this is the second week AR prediction:", np.int(next_week_ARpred))

# %%

# I am including one graph that shows clearly my training and test data range
fig, ax = plt.subplots()
ax.plot(test['flow'], '-c', label='test')
ax.plot(train['flow'], color='gold', linestyle='-', label='training')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
       yscale='log')
ax.grid(True)
ax.legend()

# Saving the figure
fig.set_size_inches(5, 3)
fig.savefig("Range of Training and Test Flow.png")

# %%
# Now after all that work with my model, let's ignore it.
# Please use this method to decide my actual predictions.
# I am using my function from above to get means from the last 2 weeks.
# The average mean (rounded down using "int" function) is my week 1 prediction

week1_pred = int(get_mean(14))
print("my actual week 1 prediction is", week1_pred)

# I'm assuming my week 2 prediction will be slightly higher based on the past two
# weeks trend. Therefore I just added 1 cfs for week 2's prediction. 

week2_pred = week1_pred + 1
print("my actual week 2 prediction is", week2_pred)

# Here I am adding the 16 week prediction "code". These are really just blind
# guesses based loosly on historical trends and wishful thinking.

seasonal_prediction = pd.Series([58, 45, 40, 51, 57, 56, 65, 70, 80, 90,
110, 115, 700, 300, 400, 400], index= ["lt_week1", "lt_week2", "lt_week3", "lt_week4",
"lt_week5", "lt_week6", "lt_week7", "lt_week8", "lt_week9", "lt_week10", 
"lt_week11", "lt_week12" , "lt_week13", "lt_week14" , "lt_week15", "lt_week16"])
print (seasonal_prediction)

# %%
