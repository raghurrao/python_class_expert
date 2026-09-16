import numpy as np

def recommend_similar_items(item_similarities: np.ndarray, item_index: int, top_n: int = 2) -> np.ndarray:
    """
    Given an (N, N) similarity matrix and an item_index:
    Return the indices of the top_n most similar items (excluding item_index itself).
    """
    scores = item_similarities[item_index].copy()
    scores[item_index] = -1.0 # exclude self
    return np.argsort(scores)[::-1][:top_n]