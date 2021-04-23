# Imports
from scipy.stats import norm


g1 = norm(5, 0.5)
g2 = norm(7, 1)

values = [5.667, 5.830, 5.978, 2.69]

for v in values:
    print(f"{2 * g1.pdf(v)} < {g2.pdf(v)}? {2 * g1.pdf(v) < g2.pdf(v)}")