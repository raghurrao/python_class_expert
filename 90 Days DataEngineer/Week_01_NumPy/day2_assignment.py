"""
Day 2 Assignment: Array Manipulation & Attributes

Complete the exercises below by writing your code inside the designated functions.
Do not change the names of the functions, as the test runner relies on them.
"""

import numpy as np

# =====================================================================
# Exercise 1: Sensor Data Reshaping
# =====================================================================

def reshape_sensor_data(sensor_readings: np.ndarray) -> np.ndarray:
    """
    Given a flat 1D array of 120 sensor readings, reshape it into a 3D matrix
    representing:
    - 10 samples
    - 4 timesteps per sample
    - 3 features per timestep
    
    Return the reshaped 3D array.
    """
    # TODO: Implement your solution here
    pass


# =====================================================================
# Exercise 2: Feature Stacking
# =====================================================================

def combine_features(student_ids: np.ndarray, math_scores: np.ndarray, verbal_scores: np.ndarray) -> np.ndarray:
    """
    Given three 1D arrays:
    - student_ids (shape: (N,))
    - math_scores (shape: (N,))
    - verbal_scores (shape: (N,))
    
    Stack them horizontally as columns to create a single 2D matrix of shape (N, 3).
    Return the combined matrix.
    """
    # TODO: Implement your solution here
    pass


# =====================================================================
# Exercise 3: Train-Test Split (Row splitting)
# =====================================================================

def split_dataset(dataset: np.ndarray, split_index: int):
    """
    Given a 2D dataset matrix (shape: (M, N)) and a row split_index:
    Split the dataset vertically (row-wise) into two matrices:
    - train_set: containing rows from 0 up to split_index (exclusive)
    - test_set: containing rows from split_index to the end.
    
    Return a tuple: (train_set, test_set)
    """
    # TODO: Implement your solution here
    pass
