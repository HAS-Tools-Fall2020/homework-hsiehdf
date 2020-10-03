
#%%
import os
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np



# %%
fig = plt.figure()
ax = plt.axes()
x = np.linspace (0, 10, 1000)
ax.plot (np.sin(x))

# %%
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x), 'o', color='purple')
# %%
x = np.linspace(0, 10, 30)
y = np.sin(x)

plt.plot(x, y, 'o', color='black');
# %%
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar()
# %%
x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), '-b', label='Sine')
ax.plot(x, np.cos(x), '--r', label='Cosine')
ax.axis('equal')
leg = ax.legend();
# %%
