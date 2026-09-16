from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np

def build_clustering_pipeline(n_components: int, n_clusters: int) -> Pipeline:
    """
    Build a pipeline containing:
    - 'pca': PCA with n_components
    - 'kmeans': KMeans with n_clusters
    """
    return Pipeline([
        ('pca', PCA(n_components=n_components)),
        ('kmeans', KMeans(n_clusters=n_clusters, random_state=42, n_init='auto'))
    ])