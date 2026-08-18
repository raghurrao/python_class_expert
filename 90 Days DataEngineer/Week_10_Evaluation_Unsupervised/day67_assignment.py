from sklearn.cluster import KMeans
import numpy as np

def run_kmeans(X: np.ndarray, n_clusters: int) -> tuple:
    """
    Fit a KMeans model on X, and return a tuple:
    (fitted_model, cluster_labels, cluster_centers)
    """
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
    model.fit(X)
    return model, model.labels_, model.cluster_centers_