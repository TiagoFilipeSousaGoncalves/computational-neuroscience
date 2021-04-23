"""
Created on Wed Apr 22 15:15:16 2015

Quiz 2 code.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

import pickle

from compute_sta import compute_sta


FILENAME = 'c1p8.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

stim = data['stim']
rho = data['rho']

# print(len(stim), len(rho))



# Fill in these values
sampling_rate = 500
# Convert to ms
sampling_period = int((1/sampling_rate) * 1000)
print(f"Sampling Period: {sampling_period}")


window = 300
num_timesteps = int(window / sampling_period)
print(f"Number of Timesteps: {num_timesteps}")


# Compute STA
sta = compute_sta(stim, rho, num_timesteps)

time = (np.arange(-num_timesteps, 0) + 1) * sampling_period
# print(time, len(time))

plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')

plt.show()