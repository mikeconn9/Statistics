from scipy.stats import uniform
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)
plt.plot(x, uniform.pdf(x, 0, 1))
plt.title("Uniform Distribution (0,1)")
plt.show()
