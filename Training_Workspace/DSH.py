#%%

import numpy as np
np.random.seed (0)

x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array
# %%
print(x1)
print (x2)
print(x3)

# %%
def my_function():
    print ("hello from a function")

my_function()
# %%
L = np.random.random(100)
sum (L)

# %%
