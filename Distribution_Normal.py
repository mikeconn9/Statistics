import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu, sigma = 0, 1  # Standard normal distribution
x = np.linspace(-4, 4, 100)
plt.plot(x, norm.pdf(x, mu, sigma))
plt.title("Normal Distribution")
plt.show()
