import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

np.random.seed(42)
X_mock, _ = make_blobs(n_samples=2000, centers=4, n_features=5, cluster_std=1.5, random_state=42)
df = pd.DataFrame(X_mock, columns=['Age', 'Annual_Income', 'Spending_Score', 'Family_Size', 'Distance_to_Store'])
df['Age'] = np.abs(df['Age'] * 5 + 40).astype(int)
df['Annual_Income'] = np.abs(df['Annual_Income'] * 15000 + 60000)
df['Spending_Score'] = np.clip(np.abs(df['Spending_Score'] * 10 + 50), 1, 100)
df['Family_Size'] = np.clip(np.abs(df['Family_Size'] + 3), 1, 6).astype(int)
df['Distance_to_Store'] = np.abs(df['Distance_to_Store'] * 2 + 5)

prep_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=2, random_state=42))
])
X_2d = prep_pipe.fit_transform(df)

# Test PCA output shape
assert X_2d.shape == (2000, 2)

# Test Elbow Generation
inertias = []
K_range = range(1, 11)
for k in K_range:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_2d)
    inertias.append(km.inertia_)

assert len(inertias) == 10
assert inertias[0] > inertias[-1]

# Test Final Clustering
final_kmeans = KMeans(n_clusters=4, random_state=42)
cluster_labels = final_kmeans.fit_predict(X_2d)

score = silhouette_score(X_2d, cluster_labels)
assert -1 <= score <= 1

# Test Profiling output
df['Persona_ID'] = cluster_labels
persona_profiles = df.groupby('Persona_ID').mean()
assert persona_profiles.shape == (4, 5)

print("All Day 25 codes executed successfully!")
