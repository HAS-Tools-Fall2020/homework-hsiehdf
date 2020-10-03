# %%
import numpy as np
import pandas as pd

 # %%
data_frame = pd.DataFrame([[1, np.nan, 2],
                            [2, 3, 5],
                            [np.nan, 4, 6]])

# %%
#1) Use the function fill.na to fill the na values with 999

e = data_frame.fillna(999)

# %%

#2) Turn the 999 values back to nas. See how many different ways you can do this
d=np.where(e==999, np.nan, e)
d

# %%
# put it in brackets and it will understand that this is what we're looking for
#implicit masking
data_frame[data_frame == 999] = np.nan
data_frame
# %%
data_frame9 = data_frame.fillna(999)
data_frame9[data_frame.isnull()] = np.nan
# %%
data_frame9 = data_frame.fillna(999)
data_frame9 = data_frame9 +data_frame
data_frame9
# %%
data_frame9 = data_frame.fillna(999)   
data_frame9.replace(999, np.nan)
# %%
#%%
import os
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
# %%
x = np.linspace (0,10,100)
y=np.sin(x)
# %%
plt.plot(x,y)
# %%
