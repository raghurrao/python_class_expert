"""
Day 4 Assignment: NumPy Broadcasting Rules

Complete the exercises below by writing your code inside the designated functions.
Do not change the names of the functions, as the test runner relies on them.
"""

import numpy as np

# =====================================================================
# Exercise 1: Standardize Features (Column-wise Z-score)
# =====================================================================

def standardize_matrix(X: np.ndarray) -> np.ndarray:
    """
    Standardize the features (columns) of a 2D matrix X of shape (M, N).
    Z-Score formula for each column:
    Z = (X - mean) / std
    
    Calculate the mean and standard deviation for each column (axis=0).
    Use broadcasting to subtract the mean and divide by std.
    Assume standard deviations are non-zero.
    """
    # TODO: Implement your solution here
    pass


# =====================================================================
# Exercise 2: Row-wise Bias Addition
# =====================================================================

def add_bias_to_rows(features: np.ndarray, bias: np.ndarray) -> np.ndarray:
    """
    Given:
    - features: 2D array of shape (M, N)
    - bias: 1D array of shape (M,)
    
    Add the bias vector to features such that:
    result[i, j] = features[i, j] + bias[i]
    
    You must reshape/expand the bias vector to shape (M, 1) to allow correct broadcasting.
    """
    # TODO: Implement your solution here
    pass


# =====================================================================
# Exercise 3: Pairwise Distance Matrix (Advanced Broadcasting)
# =====================================================================

def compute_pairwise_distances(coords: np.ndarray) -> np.ndarray:
    """
    Given coordinates of N points in a 2D space, coords of shape (N, 2).
    Calculate the pairwise Euclidean distance matrix D of shape (N, N)
    where D[i, j] is the distance between point i and point j.
    
    Euclidean Distance Formula:
    dist = sqrt((x1 - x2)^2 + (y1 - y2)^2)
    
    Hint:
    Use broadcasting! Expand coords into two 3D arrays:
    - coords[:, np.newaxis, :]  -> shape (N, 1, 2)
    - coords[np.newaxis, :, :]  -> shape (1, N, 2)
    Subtract them, square the differences, sum along the coordinate axis (axis=2),
    and take the square root.
    """
    # TODO: Implement your solution here
    pass
