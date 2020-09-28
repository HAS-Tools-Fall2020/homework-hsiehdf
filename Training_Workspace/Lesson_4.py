#%%
import os
import numpy as np
import earthpy as et

# %%
os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))
fname = os.path.join("data", "earthpy-downloads","avg-monthly-precip.txt")

avg_monthly_precip = np.loadtxt(fname)

print(avg_monthly_precip)

# %%
fname = os.path.join("data", "earthpy-downloads",
                     "monthly-precip-2002-2013.csv")

precip_2002_2013 = np.loadtxt(fname, delimiter = ",")

print(precip_2002_2013)

# %%
print(avg_monthly_precip.shape)
print(precip_2002_2013.shape)


# %%
print("shape of avg monthly precip:", avg_monthly_precip.shape)
print(" the shape of precip_2002_2013:", precip_2002_2013.shape)
print("avg monthly precip:" ,avg_monthly_precip)
print("precip 2002 2013:", precip_2002_2013)


#%%
print(precip_2002_2013[1:2,10:13]) #is tshis 3.2 and 1.18
print(precip_2002_2013[0:1,6:9]) #is this [1.03 to 2.24]
print(precip_2002_2013[::,::]) #is this all of them?
print(precip_2002_2013[0:1,-1]) #is this 0.5?

# %%

np.max(precip_2002_2013, axis=0)
print(np.mean(precip_2002_2013, axis=0))
print(np.mean(precip_2002_2013, axis=1))
avg_monthly_precip[2:5]
precip_2002_2013 [1,2]
precip_2002_2013[1,8]
precip_2002_2013[0:2,5:8]
