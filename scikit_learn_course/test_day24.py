import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# 1. 50D to 2D Test
X, y = make_classification(n_samples=500, n_features=50, n_informative=10, random_state=42)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca_2d = PCA(n_components=2, random_state=42)
X_pca_2d = pca_2d.fit_transform(X_scaled)
assert X_pca_2d.shape == (500, 2)

variance_kept = sum(pca_2d.explained_variance_ratio_)
assert 0 < variance_kept < 1.0

# 2. Percentage based compression Test
pca_90 = PCA(n_components=0.90, random_state=42)
X_pca_90 = pca_90.fit_transform(X_scaled)
assert sum(pca_90.explained_variance_ratio_) >= 0.90
assert pca_90.n_components_ < 50
assert pca_90.n_components_ > 2 # Because 2 components didn't keep 90%

# 3. The Unscaled Disaster Test
np.random.seed(42)
X_bad = np.random.rand(100, 3)
X_bad[:, 1] *= 1000000

bad_pca = PCA(n_components=2)
bad_pca.fit(X_bad)
# Without scaling, PC1 is almost 100% just Feature 1
assert bad_pca.components_[0][1] > 0.99 

good_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=2))
])
good_pipe.fit(X_bad)
good_pca = good_pipe.named_steps['pca']
# With scaling, PC1 is built out of a fair mix of all features, not just Feature 1
assert good_pca.components_[0][1] < 0.99

print("All Day 24 codes executed successfully!")
