import numpy as np

def solve_linear_system(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Solve the system of linear equations Ax = b.
    Return the vector x.
    """
    return np.linalg.solve(A, b)