# Imports
import _pickle as cPickle
import numpy as np
import matplotlib.pyplot as plt
import math

# Open data
with open("tuning_34.pickle", "rb") as f:
    data = cPickle.load(f)

# print(data.keys())
# print(data["neuron1"].shape)
# print(data["stim"].shape)

# Create matrix to append the mean of each neuron
mean_neurons = np.zeros(shape=(4, 24))

# Populate
for idx, neuron in enumerate([data["neuron1"], data["neuron2"], data["neuron3"], data["neuron4"]]):
    for stim in range(data["stim"].shape[0]):
        mean_neurons[idx, stim] = np.mean(neuron[:, stim])


# Get max rates per neuron
max_rates = np.zeros(shape=(4,))
for i in range(mean_neurons.shape[0]):
    max_rates[i] = np.max(mean_neurons[i, :])

# print(max_rates)

# Open data
with open("pop_coding_34.pickle", "rb") as f:
    data = cPickle.load(f)

# print(data.keys())
# print(data["r1"].shape)
# print(data["c1"].shape)

# Get lists
r = [data["r1"], data["r2"], data["r3"], data["r4"]]
c = [data["c1"], data["c2"], data["c3"], data["c4"]]

# Get the final direction vector
F = np.array([0., 0.])
for index, (ri, ci) in enumerate(zip(r, c)):
    # print(index, ri, ci)
    for ri_ in ri:
        F += (ri_ - max_rates[index]) * ci

# Print final F
print(F)

# Compute the angle in radians
angle_rad = math.atan2(F[1], F[0])
print(f"Angle in Radians: {angle_rad}")
print(f"Angle in Radians: {2*math.pi + angle_rad}")
angle_deg = math.degrees(angle_rad)
print(f"Angle in Degrees: {angle_deg}")
print(f"Angle in Degrees: {360 + angle_deg}")
print(f"Angle in Degrees: {round(360 + angle_deg)}")