import numpy as np

def compute_quadratic_gradient(x: float, y: float) -> np.ndarray:
    """
    Given function: f(x, y) = 3*x^2 + 2*y^2 - 4*x*y
    Compute the gradient vector [df/dx, df/dy] at point (x, y).
    
    Partial derivatives:
    df/dx = 6*x - 4*y
    df/dy = 4*y - 4*x
    """
    df_dx = 6 * x - 4 * y
    df_dy = 4 * y - 4 * x
    return np.array([df_dx, df_dy])