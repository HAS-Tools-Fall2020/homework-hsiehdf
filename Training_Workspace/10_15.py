# %%

#Write a function and use it to calculate the mean of every colum
#If you have time try doing it with and without a for loop

import os
import numpy as np
import pandas as pd

# %%

data = np.random.rand(4, 5)

# %%

def get_mean(data):
    mean = data.mean(axis=0)
    return mean

get_mean(data)
# %%

for i in range(1,21)


# %%

data = np.random.rand(4, 5)
ans=[]
for i in range(5):
    ans.append(data[:,i].mean())

print(ans)

# %%
