from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt

lam = 5  # Expected events per time period
x = np.arange(0, 15)
plt.bar(x, poisson.pmf(x, lam))
plt.title("Poisson Distribution")
plt.show()
