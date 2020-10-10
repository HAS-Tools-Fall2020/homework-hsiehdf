# %%

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime

# %%
flow = np.random.randn(100)
day = range(len(flow))

flow_error1 = flow * .75
flow_error2 = flow * 1.25



# %%
dy = flow*0.25
plt.errorbar(day, flow, yerr=dy, fmt='.k')

# %%
flow = np.random.randn(100)
day = np.arange(100)+1
# %%
flow_down = flow*(0.75)
flow_up = flow*(1.25)

# %%
fig, ax = plt.subplots()
ax.plot(flow, color='grey', linewidth=2, label='flow')
ax.plot(flow_down, color='blue', linewidth=2, label='flow-25%')
ax.plot(flow_up, color='red', linewidth=2, label='flow+25%')
ax.set(title="Flows", xlabel="Date", ylabel="Weekly Avg Flow [cfs]")
ax.legend()
plt.show()

# %%
low = np.random.randn(100)
day = range(len(flow))
stdev = 0.25
upperrange = flow + flow*0.25
lowerrange = flow - flow*0.25

fig, ax = plt.subplots()
ax.plot(flow, color='blue', linewidth=2, label='flow')
ax.plot(upperrange, color='orange', linewidth=1, label='stdev')
ax.plot(lowerrange, color='orange', linewidth=1, label='flow')
ax.legend()


# %%
fig, ax = plt.subplots()
ax.plot(day, flow)
ax.fill_between(day, flow*0.75, flow*1.25, color='gray', alpha=0.2)
# %%
