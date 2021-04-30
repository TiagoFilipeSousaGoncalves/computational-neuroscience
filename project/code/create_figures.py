# Imports
import numpy as np
import matplotlib.pyplot as plt
import os

# Global Variables
time = 250


# Directories
results = "results/predictions"
datasets = ["MNIST", "FashionMNIST", "CIFAR10"]

# Go through datasets
for dataset in datasets:
    print(f"Dataset: {dataset}")
    dataset_plot_dir = os.path.join("results", "figures", dataset)

    if os.path.isdir(dataset_plot_dir) == False:
        os.makedirs(dataset_plot_dir)

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


        # Create some good plots
        x = list()
        y = list()
        for t in range(batch.shape[0]):
            for n_idx in batch[t, :].nonzero()[0]:
                # print(n_idx)
                x.append(t)
                y.append(n_idx)

        """
        # print(len(x), len(y))
        plt.title(f"Input Spikes | Label {label}")
        plt.xlim(-50, 300)
        plt.xlabel("Time (ms)")
        plt.ylim(0, batch.shape[1]+10)
        plt.ylabel("Neuron Index")
        plt.scatter(x, y)
        plt.savefig(fname=os.path.join(dataset_plot_dir, f"in_spikes_{label}.png"), bbox_inches="tight", pad_inches=0.0)
        plt.show()
        """




        # Load spike
        spike = np.load(file=os.path.join(results, dataset, s), allow_pickle=True)
        spike = np.reshape(a=spike, newshape=(time, -1))
        # print(spike.shape)

        # Create some good plots
        x = list()
        y = list()
        for t in range(spike.shape[0]):
            for n_idx in spike[t, :].nonzero()[0]:
                # print(n_idx)
                x.append(t)
                y.append(n_idx)

        # Print unique n_idx
        print(f"Unique n_idx: {np.unique(y)}")

        """
        # print(len(x), len(y))
        plt.title(f"Output Spikes | Label {label}")
        plt.xlim(-50, 300)
        plt.xlabel("Time (ms)")
        plt.ylim(0, spike.shape[1]+10)
        plt.ylabel("Neuron Index")
        plt.scatter(x, y)
        plt.savefig(fname=os.path.join(dataset_plot_dir, f"out_spikes_{label}.png"), bbox_inches="tight", pad_inches=0.0)
        plt.show()
        """