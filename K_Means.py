from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Generate mock data
np.random.seed(42)
data = np.random.rand(100, 2)  # 100 points with 2 features

# K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(data)

# Labels and cluster centers
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Plot clusters
for i in range(3):
    cluster_points = data[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f"Cluster {i}")
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red', marker='X', label='Centroids')
plt.legend()
plt.show()
