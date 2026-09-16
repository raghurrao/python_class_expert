"""
Day 5 Assignment: Boolean Indexing & Filtering

Complete the exercises below by writing your code inside the designated functions.
Do not change the names of the functions, as the test runner relies on them.
"""

import numpy as np

# =====================================================================
# Exercise 1: Outlier Filtration
# =====================================================================

def filter_outliers(prices: np.ndarray) -> np.ndarray:
    """
    Given a 1D array of prices:
    1. Calculate the mean and standard deviation of the prices.
    2. Define boundaries: lower = mean - 2 * std, upper = mean + 2 * std.
    3. Filter and return a new array containing only the prices that fall
       WITHIN these boundaries (inclusive).
    """
    # TODO: Implement your solution here
    pass


# =====================================================================
# Exercise 2: ReLU Activation (Negative capping)
# =====================================================================

def relu_activation(X: np.ndarray) -> np.ndarray:
    """
    In deep learning, the ReLU activation function sets all negative values to zero.
    Given an input array X (any dimension):
    Modify X in-place to replace all elements < 0 with 0, and return the modified X.
    """
    # TODO: Implement your solution here
    pass


# =====================================================================
# Exercise 3: Find Points Inside Circle (Index Filtering)
# =====================================================================

def find_points_in_circle(coords: np.ndarray, radius: float) -> np.ndarray:
    """
    Given a 2D array of point coordinates coords of shape (N, 2)
    where row i represents (x_i, y_i):
    
    Find the indices of all points that lie strictly inside a circle of 
    given radius centered at (0, 0).
    
    Formula: x^2 + y^2 < radius^2
    
    Return a 1D NumPy array containing the indices (row index numbers).
    Hint: Use np.where(condition) to get the index arrays.
    Make sure to return only the 1D index array (using [0] on the np.where output).
    """
    # TODO: Implement your solution here
    pass
