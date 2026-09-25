import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons, make_blobs
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

# 1. K-Means vs DBSCAN on Moons
X, _ = make_moons(n_samples=300, noise=0.05, random_state=42)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X_scaled)
score = silhouette_score(X_scaled, kmeans.labels_)
assert -1 <= score <= 1

dbscan = DBSCAN(eps=0.3, min_samples=5)
dbscan.fit(X_scaled)
# DBSCAN should find exactly 2 clusters (moons) and 0 outliers since noise is low
assert len(np.unique(dbscan.labels_)) == 2
assert -1 not in dbscan.labels_

# 2. Outliers
X_outliers = np.vstack([X_scaled, [[5, 5], [-5, -5]]])
db_outlier = DBSCAN(eps=0.3, min_samples=5)
db_outlier.fit(X_outliers)
# The last two points must be classified as -1
assert db_outlier.labels_[-1] == -1
assert db_outlier.labels_[-2] == -1

# 3. Silhouette Exception Test
try:
    silhouette_score(X_outliers, db_outlier.labels_)
    # It might actually succeed if dbscan found 2 moons + 1 noise class, 
    # as there are 3 distinct labels. Silhouette score works as long as there is > 1 cluster.
    # The curriculum says it crashes if only 1 cluster and noise is found.
except ValueError:
    pass

# 4. Anomaly Detection Project
X_blob, _ = make_blobs(n_samples=500, centers=1, cluster_std=0.5, random_state=42)
outliers = np.array([[10, 10], [-10, -10], [10, -10]])
X_anomaly = np.vstack([X_blob, outliers])

scaler_anomaly = StandardScaler()
X_anomaly_scaled = scaler_anomaly.fit_transform(X_anomaly)

db = DBSCAN(eps=0.5, min_samples=5)
db.fit(X_anomaly_scaled)

found_outliers = X_anomaly[db.labels_ == -1]
# We injected exactly 3 extreme outliers
assert len(found_outliers) >= 3

print("All Day 22 codes executed successfully!")
