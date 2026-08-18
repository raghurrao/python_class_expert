import numpy as np

def optimize_quadratic(start_point: np.ndarray, lr: float, steps: int) -> np.ndarray:
    """
    Minimize f(x, y) = x^2 + 3*y^2
    Gradient: [2*x, 6*y]
    """
    point = start_point.copy().astype(float)
    for _ in range(steps):
        grad = np.array([2 * point[0], 6 * point[1]])
        point -= lr * grad
    return point