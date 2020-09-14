# Start code for assignment 3
# this code sets up the lists you will need for your homework
# and provides some examples of operations that will be helpful to you

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week3.txt'
filepath = os.path.join('data', filename)
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

#make lists of the data
flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Here is some starter code to illustrate some things you might like to do
# Modify this however you would like to do your homework.
# From here on out you should use only the lists created in the last block:
# flow, date, yaer, month and day

# Calculating some basic properites
print(min(flow))
print(max(flow))
print(np.mean(flow))
print(np.std(flow))

# Making and empty list that I will use to store
# index values I'm interested in
ilist = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
for i in range(len(flow)):
        if flow [i] > 600 and month[i] == 7:
                ilist.append(i)

# see how many times the criteria was met by checking the length
# of the index list that was generated
print(len(ilist))

# Alternatively I could have  written the for loop I used
# above to  create ilist like this
ilist2 = [i for i in range(len(flow)) if flow[i] > 600 and month[i]==7]
print(len(ilist2))

# Grabbing out the data that met the criteria
# This  subset of data is just the elements identified
# in the ilist
subset = [flow[j] for j in ilist]


#%%
#Question 2 and 3

# Week 1
#This tells us index numbers that have days 1-7 in Sept with flow >59 and the length of alist
alist = []
for a in range(len(flow)):
        if flow [a] > 59 and month[a] ==9 and day [a] >=1 and day [a] <=7:
                alist.append(a)
print("number of days where flow is > 59:", len(alist))

#This tells us how many total days are in first week of september for data set
slist = []
for s in range(len(flow)):
        if month[s] ==9 and day [s] >=1 and day [s] <=7:
                slist.append(s)
print("number of days in first week of September:", len(slist))

#This creates a list of flows based on the index numbers extracted above
subset = [flow[h] for h in alist]

#This calculates the percentage of days greater than prediction
p= 100* len(subset)/len(slist)
print("percentage of days greater than prediction:", p)

#this tells us number of days with flow greater than 59 for years less than or equal to 2000
blist = []
for b in range(len(flow)):
        if flow [b] > 59 and month[b] ==9 and day [b]>=1 and day [b] <=7 and year[b] <=2000:
               blist.append(b)
print("number of days with flow greater than 59 for years <=2000:", len(blist))

#This tells us the percentage of daily flow exceeding the prediction, considered for years <= 2000


slist = []
for s in range(len(flow)):
        if month[s] ==9 and day [s] >=1 and day [s] <=7 and year[s] <=2000:
                slist.append(s)
g= 100* len(blist)/len(slist)

print("percentage of days greater than prediction before 2000:", g)

#This tells us the flow for years greater than or equal to 2010
clist = []
for c in range(len(flow)):
        if flow [c] > 59 and month[c] ==9 and day [c]>=1 and day [c] <=7 and  year[c] >= 2010:
                clist.append(c)
print("number of days with flow greater than 59 for years >=2010:", len(clist))

#This tells us the percentage of daily flow exceeding the prediction, considered for years >= 2010

slist = []
for s in range(len(flow)):
        if month[s] ==9 and day [s] >=1 and day [s] <=7 and year[s] >=2010:
                slist.append(s)
t= 100* len(clist)/len(slist)
print("percentage of days greater than prediction after 2010:", t)

# %%
# Week 2

#This tells us index numbers that have days 8-14 in Sept with flow >40 and the length of alist
alist = []
for a in range(len(flow)):
        if flow [a] > 40 and month[a] ==9 and day [a] >=8 and day [a] <=14:
                alist.append(a)
print("number of days where flow is > 40:", len(alist))

#This tells us how many total days are in second week of september for data set
slist = []
for s in range(len(flow)):
        if month[s] ==9 and day [s] >=8 and day [s] <=14:
                slist.append(s)
print("number of days in second week of September:", len(slist))

#This creates a list of flows based on the index numbers extracted above
subset = [flow[h] for h in alist]

#This calculates the percentage of days greater than prediction
p= 100* len(subset)/len(slist)
print("percentage of days greater than prediction:", p)

#this tells us number of days with flow greater than 40 for years less than or equal to 2000
blist = []
for b in range(len(flow)):
        if flow [b] > 40 and month[b] ==9 and day [b]>=8 and day [b] <=14 and year[b] <=2000:
               blist.append(b)
print("number of days with flow greater than 40 for years <=2000:", len(blist))

#This tells us the percentage of daily flow exceeding the prediction, considered for years <= 2000


slist = []
for s in range(len(flow)):
        if month[s] ==9 and day [s] >=8 and day [s] <=14 and year[s] <=2000:
                slist.append(s)
g= 100* len(blist)/len(slist)

print("percentage of days greater than prediction before 2000:", g)

#This tells us the flow for years greater than or equal to 2010
clist = []
for c in range(len(flow)):
        if flow [c] > 40 and month[c] ==9 and day [c]>=8 and day [c] <=14 and  year[c] >= 2010:
                clist.append(c)
print("number of days with flow greater than 40 for years >=2010:", len(clist))

#This tells us the percentage of daily flow exceeding the prediction, considered for years >= 2010

slist = []
for s in range(len(flow)):
        if month[s] ==9 and day [s] >=8 and day [s] <=14 and year[s] >=2010:
                slist.append(s)
t= 100* len(clist)/len(slist)
print("percentage of days greater than prediction after 2010:", t)

# %%

#Week 3
#This tells us index numbers that have days 15-21 in Sept with flow >38 and the length of alist
alist = []
for a in range(len(flow)):
        if flow [a] > 38 and month[a] ==9 and day [a] >=15 and day [a] <=21:
                alist.append(a)
print("number of days where flow is > 38:", len(alist))

#This tells us how many total days are in third week of september for data set
slist = []
for s in range(len(flow)):
        if month[s] ==9 and day [s] >=15 and day [s] <=21:
                slist.append(s)
print("number of days in third week of September:", len(slist))

#This creates a list of flows based on the index numbers extracted above
subset = [flow[h] for h in alist]

#This calculates the percentage of days greater than prediction
p= 100* len(subset)/len(slist)
print("percentage of days greater than prediction:", p)

#this tells us number of days with flow greater than 38 for years less than or equal to 2000
blist = []
for b in range(len(flow)):
        if flow [b] > 38 and month[b] ==9 and day [b]>=15 and day [b] <=21 and year[b] <=2000:
               blist.append(b)
print("number of days with flow greater than 38 for years <=2000:", len(blist))

#This tells us the percentage of daily flow exceeding the prediction, considered for years <= 2000


slist = []
for s in range(len(flow)):
        if month[s] ==9 and day [s] >=15 and day [s] <=21 and year[s] <=2000:
                slist.append(s)
g= 100* len(blist)/len(slist)

print("percentage of days greater than prediction before 2000:", g)

#This tells us the flow for years greater than or equal to 2010
clist = []
for c in range(len(flow)):
        if flow [c] > 38 and month[c] ==9 and day [c]>=15 and day [c] <=21 and  year[c] >= 2010:
                clist.append(c)
print("number of days with flow greater than 38 for years >=2010:", len(clist))

#This tells us the percentage of daily flow exceeding the prediction, considered for years >= 2010

slist = []
for s in range(len(flow)):
        if month[s] ==9 and day [s] >=15 and day [s] <=21 and year[s] >=2010:
                slist.append(s)
t= 100* len(clist)/len(slist)
print("percentage of days greater than prediction after 2010:", t)

# %%

#week 4

#This tells us index numbers that have days 22-28 in Sept with flow >35 and the length of alist
alist = []
for a in range(len(flow)):
        if flow [a] > 35 and month[a] ==9 and day [a] >=22 and day [a] <=28:
                alist.append(a)
print("number of days where flow is > 35:", len(alist))

#This tells us how many total days are in fourth week of september for data set
slist = []
for s in range(len(flow)):
        if month[s] ==9 and day [s] >=22 and day [s] <=28:
                slist.append(s)
print("number of days in fourth week of September:", len(slist))

#This creates a list of flows based on the index numbers extracted above
subset = [flow[h] for h in alist]

#This calculates the percentage of days greater than prediction
p= 100* len(subset)/len(slist)
print("percentage of days greater than prediction:", p)

#this tells us number of days with flow greater than 35 for years less than or equal to 2000
blist = []
for b in range(len(flow)):
        if flow [b] > 35 and month[b] ==9 and day [b]>=22 and day [b] <=28 and year[b] <=2000:
               blist.append(b)
print("number of days with flow greater than 35 for years <=2000:", len(blist))

#This tells us the percentage of daily flow exceeding the prediction, considered for years <= 2000


slist = []
for s in range(len(flow)):
        if month[s] ==9 and day [s] >=22 and day [s] <=28 and year[s] <=2000:
                slist.append(s)
g= 100* len(blist)/len(slist)

print("percentage of days greater than prediction before 2000:", g)

#This tells us the flow for years greater than or equal to 2010
clist = []
for c in range(len(flow)):
        if flow [c] > 35 and month[c] ==9 and day [c]>=22 and day [c] <=28 and  year[c] >= 2010:
                clist.append(c)
print("number of days with flow greater than 35 for years >=2010:", len(clist))

#This tells us the percentage of daily flow exceeding the prediction, considered for years >= 2010

slist = []
for s in range(len(flow)):
        if month[s] ==9 and day [s] >=22 and day [s] <=28 and year[s] >=2010:
                slist.append(s)
t= 100* len(clist)/len(slist)
print("percentage of days greater than prediction after 2010:", t)

# %%
# Question 4
#These code tell us the index and flow values for september 1-15 and 16-30
vlist = []
for v in range(len(flow)):
        if month[v] ==9 and day [v] >=1 and day [v] <=15:
                vlist.append(v)
print(len(vlist))

subset = [flow[x] for x in vlist]
print(sum(subset)/len(subset))

vvlist = []
for vv in range(len(flow)):
        if month[vv] ==9 and day [vv] >=16 and day [vv] <=30:
                vvlist.append(vv)
print(len(vvlist))

subset2 = [flow[x] for x in vvlist]
print(sum(subset2)/len(subset2))
