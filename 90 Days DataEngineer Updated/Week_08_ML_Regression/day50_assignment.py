import numpy as np

def manual_linear_regression(x: np.ndarray, y: np.ndarray):
    """
    Calculate linear slope and intercept:
    slope = cov(x, y) / var(x)
    intercept = mean(y) - slope * mean(x)
    """
    slope = np.cov(x, y)[0, 1] / np.var(x, ddof=1)
    intercept = np.mean(y) - slope * np.mean(x)
    return slope, intercept
