# Analysis of Neurons’ Information in Deep Spiking Neural Networks using Information Theory

## About
Implementation of the paper [_"Analysis of Neurons’ Information in Deep Spiking Neural Networks using Information Theory"_](paper.pdf) by Leonardo Capozzi, Tiago Gonçalves, Jaime S. Cardoso and Ana Rebelo.

## Abstract
Deep learning methodologies have been very successful in a large number of tasks, sometimes surpassing human performance. One of the most simple neural network architectures is the multi-layer perceptron (MLP) which tries to mimic the brain in some ways. These methodologies are generally trained using gradient descent as they are differentiable. In recent years, a new methodology called spiking neural networks (SNNs) was proposed. These networks can be seen as a more biologically realistic approach than artificial neural networks (ANNs), as they use discrete spikes to transmit information, instead of continuous values. In this paper, we study these networks, and present results achieved by training these models. We also evaluate several information theory quantities such as entropy and mutual information of these networks to extract the relationship between the inputs and the outputs.

## Clone this repository
To clone this repository, open a Terminal window and type:
```bash
$ git clone git@github.com:TiagoFilipeSousaGoncalves/computational-neuroscience.git
```
Then go to the repository's main directory:
```bash
$ cd computational-neuroscience
```

## Dependencies
### Install the necessary Python packages
We advise you to create a virtual Python environment first (Python 3.7). To install the necessary Python packages run:
```bash
$ pip install -r requirements.txt
```

## Data
To know more about the data used in this paper, please send an e-mail to  [**tiago.f.goncalves@inesctec.pt**](mailto:tiago.f.goncalves@inesctec.pt) or to [**leonardo.g.capozzi@inesctec.pt**](mailto:leonardo.g.capozzi@inesctec.pt).


## Usage
### Reproduce the Experiments
To reproduce the experiments on the CIFAR-10 database:
```bash
$ python code/train_cifar10.py
$ python code/test_cifar10.py
```

To reproduce the experiments on the Fashion-MNIST database:
```bash
$ python code/train_fashionmnist.py
$ python code/test_fashionmnist.py
```

To reproduce the experiments on the MNIST database:
```bash
$ python code/train_mnist.py
$ python code/test_mnist.py
```

### Compute the metrics
To compute the information theory metrics:
```bash
$ python code/compute_it_metrics.py
```

### Plot the Results
To plot the results:
```bash
$ python code/create_figures.py
```




## Citation
If you use this repository in your research work, please cite this paper:
```bibtex
@inproceedings{capozzigoncalves2023recpad,
	author = {Leonardo Capozzi, Tiago Gonçalves, Jaime S. Cardoso and Ana Rebelo},
	title = {{Analysis of Neurons’ Information in Deep Spiking Neural Networks using Information Theory}},
	booktitle = {29th Portuguese Conference in Pattern Recognition (RECPAD)},
	year = {2023},
    address = {Coimbra, Portugal}
}
```