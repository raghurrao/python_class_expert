import numpy as np

def compute_eigen_metrics(A: np.ndarray):
    """
    Compute and return:
    (eigenvalues, eigenvectors, trace_of_A)
    """
    eigenvalues, eigenvectors = np.linalg.eig(A)
    trace_val = np.trace(A)
    return eigenvalues, eigenvectors, trace_val