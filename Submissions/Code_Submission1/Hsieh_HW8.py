# %%
import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# %%
# Here is my first function!


def get_mean(days_of_flow):
    """Fuction to get my mean from x amount of days ago

    This function will give us the mean flows from the *tail* end of our data.
    We can ask it to give us last weeks mean (i.e., last 7 days) or however
    many days we ask it to look back to.

    two_week_mean is an int or float
    """

    mean = np.mean(data.tail(days_of_flow)['flow'])
    return mean

# %%
# Set the file name and path to where you have stored the data


filename = 'streamflow_week8.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

# %%
# Read the data into a pandas dataframe

data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime', 'flow',
                            'code'], parse_dates=['datetime']
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

train = flow_weekly[21:1200][['flow', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                             13, 14, 15, 16, 17, 18, 19, 20]]
test = flow_weekly[1200:][['flow', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                           13, 14, 15, 16, 17, 18, 19, 20]]


# %%
# This fit my data into a linear regressoin model. My x axis is my shifted flow
# values. My y axis is the flow values.

model = LinearRegression()
x = train[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
           19, 20]]
y = train['flow'].values
model.fit(x, y)
r_sq = model.score(x, y)
print('The coefficient of determination is:', np.round(r_sq, 2))
print('The Y intercept is:', np.round(model.intercept_, 2))
print('The slopes are:', np.round(model.coef_, 2))


# Prediction for week 1 using my AR model. I used a for loop that would make a
# line with the equation y = m1x1 + m2x2 ... m20x20 + b

this_week_pred = model.intercept_

for f in range(1, 21):
    this_week_pred = model.coef_[f-1] * test[f].tail(1) + this_week_pred
print("this is the first week AR prediction:", np.int(this_week_pred.values))

# Prediction for week 2 using my model. This code is interesting, as I had to
# use my weekly flow value I predicted above and use it in my second
# weeks prediction. I did this by first setting "next_week_pred" equal to my
# model.intercept_, then added m1 (model.coef_[0]) times x1 (this_week_pred).
# This gave me y= m1x1 + b. Then I only made the for loop go 1-20 (instead of
# 1-21) because my first week was already acounted for. This gave me the
# same equation as above y = m1x1 + m2x2 ... m20x20 + b using my newest
# weekly flow and all other x values shifted by one week.

next_week_pred = model.intercept_

next_week_pred = this_week_pred * model.coef_[0] + next_week_pred

for p in range(1, 20):
    next_week_pred = model.coef_[p] * test[p].tail(1) + next_week_pred

print("this is the second week AR prediction:", np.int(next_week_pred))

# %%
# Now after all that work with my model, let's ignore it.
# Please use this method to decide my actual predictions.
# I am using my function from above to get means from the last 2 weeks.
# The average mean (rounded down using "int" function) is my week 1 prediction,
# and week 2 is 1 cfs less than week 1.

week1_pred = get_mean(14)
week1_pred_rounded = int(week1_pred)
print("my week 1 rounded prediction is", week1_pred_rounded)

#I just assume week 2 will have a slightly lower mean than week one because of 
# historical trends. This why my second week prediction has a -1. 

week2_pred = week1_pred_rounded - 1
print("my week 2 rounded prediction is", week2_pred)

# %%
