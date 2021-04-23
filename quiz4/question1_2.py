# Imports
import math
import numpy as np

# Q1
# F
prob_F = [0.9, 0.1]

# Compute entropy
entropy = 0

for prob in prob_F:
    entropy += (prob * math.log2(prob))

entropy *= -1

print(f"Entropy is {entropy}")


# Q2
# S
prob_S = np.array([0.9, 0.1])

# F|S
prob_F_given_S = np.array([[1/18, 1/2],[17/18, 1/2]])

# F
prob_F = np.zeros_like(prob_S)
prob_F[1] = prob_S[0] * prob_F_given_S[0, 0] + prob_S[1] * prob_F_given_S[0, 1]
prob_F[0] = 1 - prob_F[1]



# H(F)
entropy_F = 0
for prob in prob_F:
    entropy += (prob * math.log2(prob))
entropy *= -1

# H(F|S=s)
entropy_F_given_S = 0
for idx in range(prob_S.shape[0]):
    entropy_F_given_S += -1 * prob_S[idx] * prob_F_given_S[0, idx] * math.log2(prob_F_given_S[0, idx])
    entropy_F_given_S += -1 * prob_S[idx] * prob_F_given_S[1, idx] * math.log2(prob_F_given_S[1, idx])


# MI(FS)
MI = entropy_F - entropy_F_given_S
print(f"MI is: {MI}")