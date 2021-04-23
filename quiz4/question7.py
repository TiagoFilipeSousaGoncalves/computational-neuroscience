# Imports
import _pickle as cPickle
import numpy as np
import matplotlib.pyplot as plt

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


# Plot the results
for i in range(mean_neurons.shape[0]):
    plt.plot(data["stim"], mean_neurons[i, :], label=f"neuron{i+1}")
    plt.legend()
    plt.show()