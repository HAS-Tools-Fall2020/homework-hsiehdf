# %%
# %%
import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

filename = 'streamflow_week8.txt'
filepath = os.path.join('../data', filename)
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     parse_dates=['datetime'], index_col='datetime'
                     )

# %%
data.head(3:5) 

# %%
data(data("flow").iloc[2:5]
# %%
data[(data.index.month==1) & (data.index.day <=5) &(data.index.day>=3)

# %%
data['flow'].iloc[2:5]

# %%
