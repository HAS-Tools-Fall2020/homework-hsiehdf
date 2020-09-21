# Starter code for Homework 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week4.txt'
filepath = os.path.join('../../../homework-hsiehdf-git/data/', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Question 2
print ("Flow_data is an array composed of 11,584 rows and 4 columns of data.\
        The columns are year, month, day, and flow.")
print ("the values in flow_data are composed of:", flow_data.dtype)
print ("the dimensions of the flow data are:", flow_data.shape)
print ("the flow data total size is:", flow_data.size)

# %%
# Question 3
#How many times was daily flow greater than your prediction in the month of September?

Prediction = 55
# Count the number of values with flow > 55 and month ==9
flow_count = np.sum((flow_data[:,3] > 55) & (flow_data[:,1]==9))

# this gives a list of T/F where the criteria are met
(flow_data[:,3] > 55) & (flow_data[:,1]==9)

# this give the flow values where that criteria is met
flow_pick = flow_data[(flow_data[:,3] > 55) & (flow_data[:,1]==9), 3]

# this give the year values where that criteria is met
year_pic = flow_data[(flow_data[:,3] > 55) & (flow_data[:,1]==9), 0]

# this give the all rows  where that criteria is met
all_pic = flow_data[(flow_data[:,3] > 55) & (flow_data[:,1]==9), ]

# Calculate the average flow for these same criteria 
flow_mean = np.mean(flow_data[(flow_data[:,3] > 55) & (flow_data[:,1]==9),3])

print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")
#print ((flow_data[:,3] > 55) & (flow_data[:,1]==9))
#print(flow_pick)
#print (year_pic)
#print (all_pic)
#print (flow_mean)

Flow_count2= np.sum(flow_data[:,1]==9)
Flow_Precentage= (flow_count/Flow_count2)*100
print ("The percentage daily flow was greater than my prediction was:" , Flow_Precentage)

# %%
#Question 4
year_pic_less_than_2000 = flow_data[(flow_data[:,3] > 55) & \
         (flow_data[:,1]==9) & (flow_data[:,0]<=2000), 0]
print ("the number of times daily flow was greater than my\
        prediction for years before 2000:" ,len(year_pic_less_than_2000))
Percentage_less_2000= len(year_pic_less_than_2000)/ len(flow_data[(flow_data[:,1]==9) & \
        (flow_data[:,0]<=2000) , ])*100
print ("The percentage daily flow was greater than my\
        prediction for years before 2000:" , Percentage_less_2000)
year_pic_greater_than_2010 = flow_data[(flow_data[:,3] > 55) & \
         (flow_data[:,1]==9) & (flow_data[:,0]>=2010), 0]
print ("the number of times daily flow was greater than my\
        prediction for years on or after 2010:" ,len(year_pic_greater_than_2010))
Percentage_Greater_2010= len(year_pic_greater_than_2010)/ len(flow_data[(flow_data[:,1]==9) & \
        (flow_data[:,0]>=2010) , ])*100
print ("The percentage daily flow was greater than my\
        prediction for years before 2000:" , Percentage_Greater_2010)


# %%
#Question 5
 
First_Half_Sept_Mean = np.mean(flow_data[(flow_data[:,2]<=15) & (flow_data[:,1]==9), 3])
print ("this is the mean for first half of September:", First_Half_Sept_Mean)
Second_Half_Sept_Mean = np.mean(flow_data[(flow_data[:,2]>15) & (flow_data[:,1]==9), 3])
print ("this is the mean for second half of September:", Second_Half_Sept_Mean)
print ("The flow decreased from the first half of September to the second half of September")

