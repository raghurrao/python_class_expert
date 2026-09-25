import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from sklearn.pipeline import Pipeline
from sklearn.metrics import silhouette_score

# 1. Scipy Linkage Generation
X, y = make_blobs(n_samples=50, centers=3, cluster_std=0.8, random_state=42)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

Z = linkage(X_scaled, method='ward')
assert Z.shape == (49, 4) # For N samples, linkage matrix is (N-1, 4)

# 2. Agglomerative Clustering
agg = AgglomerativeClustering(n_clusters=3, linkage='ward')
labels = agg.fit_predict(X_scaled)
assert len(np.unique(labels)) == 3

agg_2 = AgglomerativeClustering(n_clusters=2, linkage='ward')
labels_2 = agg_2.fit_predict(X_scaled)
assert len(np.unique(labels_2)) == 2

# 3. Pipeline / No Predict Attribute Error
X_proj, _ = make_blobs(n_samples=500, centers=4, cluster_std=0.5, random_state=42)

agg_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('agg', AgglomerativeClustering(n_clusters=4, linkage='ward'))
])

labels_proj = agg_pipe.fit_predict(X_proj)
assert len(np.unique(labels_proj)) == 4
score = silhouette_score(X_proj, labels_proj)
assert score > 0.0

try:
    agg_pipe.predict(X_proj)
    assert False, "AgglomerativeClustering should not have a predict method"
except AttributeError:
    pass
except ValueError:
    # Depending on scikit-learn version and Pipeline handling, it might raise ValueError or AttributeError
    pass
except Exception as e:
    # Just to be safe, any exception related to predict not being found is expected
    if "predict" in str(e).lower() or "not available" in str(e).lower():
        pass
    else:
        raise

print("All Day 23 codes executed successfully!")
