#%% 
import os
import numpy as np
#%%
## EXERCISE 1: 
#1a.  Create a 3X3 matrix with values ranging from 2-10  

x1=np.arange(2,11).reshape(3,3)
print(x1)

Ex_1= np.array([(2,3,4),(5,6,7),(8,9,10)])
print(Ex_1)
#%%
#1.b  Make a matrix with all of the even values from 2-32
Ex1b = np.arange(2,34,2).reshape(-1,4)
print (Ex1b)

# 1.c Make a matrix with all of the even values from 2-32
# But this time have the values arrange along columns rather than rows

Ex1c = Ex1b.T
print(Ex1c)
# BONUS:
# Create the same 3x3 matrix with value ranging from 2-10 as you did 
# in part a but this time do so by combining one 3X1 matrix and one 1X3 matrix


# %%
Ex_2= np.arange(2,34,2)
print (Ex_2)
# %%
x=np.reshape(np.arange(2,33,2),(4,4))

# %%
Bonus = np.array([(2),(3),(4)])
Bonus2 = Bonus.T
print (Bonus)
print (Bonus2)
# %%
bonus= np.array([(1,2,3), (1,2,3),(1,2,3)]).reshape(3,4)
print(bonus)

#%%
Ex3 = np.arange(2,5,1)
Ex3a = np.arange(0,7,3).reshape(3,1)

print(Ex3)
print (Ex3a)

Ex3+Ex3a
# %%
