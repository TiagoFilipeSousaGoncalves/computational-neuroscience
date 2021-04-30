# Imports
import numpy as np
import matplotlib.pyplot as plt
import os



# Function: Map input dims to output dims through a sliding window
def map_inp_to_out_dims(input_arr, out_dim, offset):
    # Create mapped_array
    mapped_array = np.zeros((input_arr.shape[0], out_dim))

    # Map spikes through a sliding window
    _input_arr = input_arr.copy()[:, offset::]

    # Go through
    step = int((input_arr.shape[1] - offset) / out_dim)

    for r in range(mapped_array.shape[0]):
        tmp = _input_arr[r, :]
        
        init_idx = 0
        for c in range(out_dim):
            mapped_array[r, c] = 1 if np.mean(tmp[init_idx:init_idx+step]) > 0 else 0
            init_idx += step

    return mapped_array

# Global Variables
time = 250

# Directories
results = "results/predictions"
dataset = "MNIST"
# dataset = "FashionMNIST"
# dataset = "CIFAR10"

# Open directory
files = os.listdir(os.path.join(results, dataset))
files = [i for i in files if not i.startswith('.')]
files.sort()
# print(files)

# Get batches
batches = [f for f in files if f.startswith('b')]
batches.sort()
# print(batches)

# Get spikes
spikes = [f for f in files if f.startswith('s')]
spikes.sort()
# print(spikes)


# Go through pairs
for label, files in enumerate(zip(batches, spikes)):
    # Get batch and files
    b, s = files
    print(b, s)

    # Load batch
    batch = np.load(file=os.path.join(results, dataset, b), allow_pickle=True)
    batch = np.reshape(a=batch, newshape=(time, -1))
    # print(batch.shape)

    # Load spike
    spike = np.load(file=os.path.join(results, dataset, s), allow_pickle=True)
    spike = np.reshape(a=spike, newshape=(time, -1))
    # print(spike.shape)


    # Perform a sliding window to map input spikes to output spikes dimensions
    b_mapped = map_inp_to_out_dims(input_arr=batch, out_dim=spike.shape[1], offset=4)

    # Marginal probabilities per mapped neuron
    # Col-0 prob(x=0), Col-1 prob(x=1)
    b_mapped_probs = np.zeros((b_mapped.shape[1], 2))
    for neuron in range(b_mapped.shape[1]):
        b_mapped_probs[neuron, 1] = np.sum(b_mapped[:, neuron]) / time
        b_mapped_probs[neuron, 0] = 1 - (np.sum(b_mapped[:, neuron]) / time)
        # print(np.sum(b_mapped_probs[neuron, :]))

    
    # Marginal probabilities per spike neuron
    # Col-0 prob(x=0), Col-1 prob(x=1)
    s_probs = np.zeros_like(b_mapped_probs)
    for neuron in range(spike.shape[1]):
        s_probs[neuron, 1] = np.sum(spike[:, neuron]) / time
        s_probs[neuron, 0] = 1 - (np.sum(spike[:, neuron]) / time)
        # print(np.sum(s_probs[neuron, :]))