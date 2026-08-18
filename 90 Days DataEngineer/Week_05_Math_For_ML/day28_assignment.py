import numpy as np

def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    Compute cosine similarity from scratch.
    Formula: v1 . v2 / (||v1|| * ||v2||)
    """
    return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
