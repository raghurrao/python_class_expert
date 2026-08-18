from sklearn.decomposition import PCA
import numpy as np

def run_pca(X: np.ndarray, n_components: int) -> tuple:
    """
    Fit a PCA model on X, project the data, and return a tuple:
    (projected_data, explained_variance_ratio)
    """
    pca = PCA(n_components=n_components)
    projected = pca.fit_transform(X)
    return projected, pca.explained_variance_ratio_