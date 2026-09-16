"""
Day 3 Assignment: NumPy Vectorization & Math Operations

Complete the exercises below by writing your code inside the designated functions.
Do not change the names of the functions, as the test runner relies on them.
"""

import numpy as np

# =====================================================================
# Exercise 1: Log-1p Transformation
# =====================================================================

def log_transform_features(features: np.ndarray) -> np.ndarray:
    """
    Given a 1D or 2D array of non-negative features (e.g. household incomes),
    apply the log(1 + x) transformation element-wise.
    
    Formula: y = ln(1 + x)
    (Hint: Use NumPy's built-in function for log1p)
    """
    # TODO: Implement your solution here
    pass


# =====================================================================
# Exercise 2: Row-wise Softmax
# =====================================================================

def softmax_rows(scores: np.ndarray) -> np.ndarray:
    """
    Given a 2D matrix of shape (M, N) containing raw logits/scores:
    Compute the Softmax activation for each row.
    
    Softmax Formula for a row vector x:
    S(x) = exp(x) / sum(exp(x))
    
    Make sure:
    1. To calculate the exponential of elements.
    2. Sum along the correct axis (axis=1).
    3. Keep dimensions matching during division using `keepdims=True` in sum, or shape management.
    """
    # TODO: Implement your solution here
    pass


# =====================================================================
# Exercise 3: Argmax Classification
# =====================================================================

def predict_class(probabilities: np.ndarray) -> np.ndarray:
    """
    Given a 2D matrix of prediction probabilities of shape (M, C)
    where M is the number of samples and C is the number of classes:
    
    Return a 1D array of shape (M,) containing the index of the class with 
    the highest probability for each sample.
    """
    # TODO: Implement your solution here
    pass
