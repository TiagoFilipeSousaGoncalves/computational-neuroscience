# Imports
import _pickle as cPickle

# Open data
with open("tuning_34.pickle", "rb") as f:
    data = cPickle.load(f)

print(data.keys())