from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

n, p = 10, 0.5  # 10 trials, 50% success probability
x = np.arange(0, 11)
plt.bar(x, binom.pmf(x, n, p))
plt.title("Binomial Distribution")
plt.show()

n, p = 10, 0.95  # 10 trials, 95% good quality probability
x = np.arange(0, 11)
plt.bar(x, binom.pmf(x, n, p))
plt.title("Binomial Distribution")
plt.show()