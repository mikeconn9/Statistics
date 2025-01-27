from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt

# Generate mock data
np.random.seed(42)
data = np.random.rand(100, 2)  # 100 points with 2 features

# DBSCAN clustering
dbscan = DBSCAN(eps=0.1, min_samples=5)
labels = dbscan.fit_predict(data)

# Plot clusters
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
plt.title("DBSCAN Clustering")
plt.show()
