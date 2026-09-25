import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# 1. Base K-Means Test
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X)
team_labels = kmeans.labels_
centroids = kmeans.cluster_centers_

assert len(np.unique(team_labels)) == 4
assert centroids.shape == (4, 2)
assert kmeans.inertia_ > 0

# 2. Forced K=2 Test
kmeans_k2 = KMeans(n_clusters=2, random_state=42)
kmeans_k2.fit(X)
assert len(np.unique(kmeans_k2.labels_)) == 2

# 3. Elbow Method Generation Test
inertias = []
K_range = range(1, 11)
for k in K_range:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X)
    inertias.append(km.inertia_)

assert len(inertias) == 10
# Inertia should generally decrease as K increases.
# Instead of strict decrease, just assert the first is much bigger than the last.
assert inertias[0] > inertias[-1]

# 4. Pipeline with Distortion Test
X_distorted = np.random.rand(150, 3)
X_distorted[:, 0] *= 10000 

kmeans_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('kmeans', KMeans(n_clusters=3, random_state=42))
])
kmeans_pipe.fit(X_distorted)

trained_kmeans = kmeans_pipe.named_steps['kmeans']
assert trained_kmeans.cluster_centers_.shape == (3, 3)

print("All Day 21 codes executed successfully!")
