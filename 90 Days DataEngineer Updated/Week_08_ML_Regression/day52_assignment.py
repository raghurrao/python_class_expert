from sklearn.preprocessing import PolynomialFeatures
import numpy as np

def generate_polynomial_features(X: np.ndarray, degree: int) -> np.ndarray:
    """
    Generate polynomial features of given degree for the matrix X.
    """
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    return poly.fit_transform(X)