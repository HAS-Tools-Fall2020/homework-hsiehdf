#%%
data = np.ones((7,3))
data_frame = pd.DataFrame(data, 
                columns = ['data1', 'data2', 'data3'],
                index=['a','b','c','d','e','f','g'])



D) Do the same thing without using loc


#%%
import os
import numpy as np
import pandas as pd 


# %%
data = np.ones((7,3))
data_frame = pd.DataFrame(data, 
                columns = ['data1', 'data2', 'data3'],
                index=['a','b','c','d','e','f','g'])
# %%
data_frame
# %%
#A) Change the values for all of the vowel rows to 3
data[(data_frame.index=='a') | (data_frame.index =='e')]=3

data_frame.loc[['a','e']]=3
# %%
#B) multiply the first 4 rows by 7

data_frame = data_frame.iloc[:4, :]
# %%
#C) Make the dataframe into a checkerboard  of 0's and 1's using loc
data = np.ones((7,3))
data_frame = pd.DataFrame(data, 
                columns = ['data1', 'data2', 'data3'],
                index=['a','b','c','d','e','f','g'])


#make a list!
# %%
