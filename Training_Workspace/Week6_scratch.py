# %%
# Building an autoregressive model 
# You can learn more about the approach I'm following by walking 
# Through this tutorial
# https://realpython.com/linear-regression-in-python/

# Step 1: setup the arrays you will build your model on
# This is an autoregressive model so we will be building
# it based on the lagged timeseries

#Created my testing using data from September and October from 2017-2018
training_two_weeks9 = data[(data["day"] >=20) & (data["day"] <=30) & \
        (data['month']==9) & (data['year'] >=2017) & (data['year'] <=2018)]

training_two_weeks10 = data[(data["day"] >=1) & (data["day"] <=10) & \
        (data['month']==10) & (data['year'] >=2017) & (data['year'] <=2018)] 

training_four_weeks = pd.concat((two_weeks9, two_weeks10))
training_four_weeks_average = four_weeks.groupby('day').mean()
training_fwas = four_weeks_average.sort_values(['month','day'])
training_fwas_weekly = training_fwas.resample("W", on='datetime').mean()

training_fwas['flow_tm1'] = training_fwas['flow'].shift(1)
training_fwas['flow_tm2'] = training_fwas['flow'].shift(2)

#Creating my testing data from 2019- present
two_weeks9 = data[(data["day"] >=20) & (data["day"] <=30) & (data['month']==9) & \
        (data['year'] >=2019)]

two_weeks10 = data[(data["day"] >=1) & (data["day"] <=10) & (data['month']==10) & \
        (data['year'] >=2019)] 

four_weeks = pd.concat((two_weeks9, two_weeks10))
four_weeks_average = four_weeks.groupby('day').mean()
fwas = four_weeks_average.sort_values(['month','day'])

fwas['flow_tm1'] = fwas['flow'].shift(1)
fwas['flow_tm2'] = fwas['flow'].shift(2)


# Step 2 - pick what portion of the time series you want to use as training data
# here I'm grabbing the first 800 weeks 
# Note1 - dropping the first two weeks since they wont have lagged data
# to go with them  
train = training_fwas[2:][['flow', 'flow_tm1', 'flow_tm2']]
test = fwas[2:][['flow', 'flow_tm1', 'flow_tm2']]
