# Imports
import numpy as np
import matplotlib.pyplot as plt
import os

# Entropy
from scipy.stats import entropy

# Mutual Information
from sklearn.feature_selection import mutual_info_classif



# Global Variables
time = 250

# Directories
results = "results/predictions"
datasets = ["MNIST", "FashionMNIST", "CIFAR10"]


for dataset in datasets:
    print(f"Dataset: {dataset}")
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
        print(f"Label: {label}")
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


        # Marginal probabilities per mapped neuron
        # Col-0 prob(x=0), Col-1 prob(x=1)
        batch_probs = np.zeros((batch.shape[1], 2))
        for neuron in range(batch.shape[1]):
            batch_probs[neuron, 1] = np.sum(batch[:, neuron]) / time
            batch_probs[neuron, 0] = 1. - (np.sum(batch[:, neuron]) / time)
            # print(np.sum(batch_probs[neuron, :]))
        # print(batch_probs)
        

        # Compute Entropy Input Neurons
        in_neurons_entropy = np.zeros((batch_probs.shape[0], ))
        for neuron in range(batch_probs.shape[0]):
            entropy_value = entropy(pk=[batch_probs[neuron, 0], batch_probs[neuron, 1]], base=2)
            in_neurons_entropy[neuron] = entropy_value
        
        # Marginal probabilities per spike neuron
        # Col-0 prob(x=0), Col-1 prob(x=1)
        s_probs = np.zeros((spike.shape[1], 2))
        for neuron in range(spike.shape[1]):
            s_probs[neuron, 1] = np.sum(spike[:, neuron]) / time
            s_probs[neuron, 0] = 1. - (np.sum(spike[:, neuron]) / time)
            # print(np.sum(s_probs[neuron, :]))
        # print(s_probs)
        
        # Compute Entropy Output Neurons
        out_neurons_entropy = np.zeros((s_probs.shape[0], ))
        for neuron in range(s_probs.shape[0]):
            entropy_value = entropy(pk=[s_probs[neuron, 0], s_probs[neuron, 1]], base=2)
            out_neurons_entropy[neuron] = entropy_value
        

        # Debug prints (Entropies)
        # print(list(in_neurons_entropy))
        # print(list(out_neurons_entropy))


        # Compute MI
        mi_array = np.zeros((spike.shape[1], batch.shape[1]))

        for i in range(spike.shape[1]):
            # print(i)
            mi = mutual_info_classif(X=np.array(batch, dtype=int), y=np.array(spike[:, i], dtype=int), discrete_features=True)
            mi_array[i] = mi
            # print(mi)


        for i in range(mi_array.shape[0]):
            if np.sum(mi_array[i, :]) > 1e-6:
                print(f"Mutual Information of the Input Neurons and Output Neuron {i}: {np.sum(mi_array[i, :])}")