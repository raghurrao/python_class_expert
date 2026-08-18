"""
Day 1 Assignment: NumPy Array Basics, Slicing & Shapes

Complete the exercises below by writing your code inside the designated functions or sections.
Do not change the names of the functions or predefined variables, as the test runner relies on them.
"""

import numpy as np

# =====================================================================
# Exercise 1: Temperature Data Analysis
# =====================================================================

def analyze_temperatures(temps_f: np.ndarray):
    """
    1. Convert all temperatures from Fahrenheit to Celsius using vectorization.
       Formula: C = (F - 32) * 5/9
    2. Filter out temperatures that are greater than 25°C.
    3. Calculate and return a tuple:
       (celsius_temperatures, count_above_25, mean_of_hot_days)
       
       Note: If no day is above 25°C, mean_of_hot_days should be 0.0.
    """
    # TODO: Implement your solution here
    pass


# =====================================================================
# Exercise 2: Min-Max Scaling (Data Normalization)
# =====================================================================

def min_max_scale(data: np.ndarray) -> np.ndarray:
    """
    Scale a 1D NumPy array so that all values are scaled between 0 and 1.
    Formula: scaled_val = (val - min_val) / (max_val - min_val)
    
    If all values in the array are identical (min_val == max_val), return a new array of zeros.
    """
    # TODO: Implement your solution here
    pass


# =====================================================================
# Exercise 3: Column-wise Normalization
# =====================================================================

def normalize_columns(features: np.ndarray) -> np.ndarray:
    """
    Given a 2D matrix representing features, divide each column by its maximum value
    so that the maximum value in each column becomes 1.0.
    
    Use broadcasting and make sure to specify the correct axis.
    Assume all maximum values are greater than zero.
    """
    # TODO: Implement your solution here
    pass
