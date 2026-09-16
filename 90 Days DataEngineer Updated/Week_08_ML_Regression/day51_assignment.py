from sklearn.linear_model import LinearRegression
import numpy as np

def train_sklearn_regression(X: np.ndarray, y: np.ndarray):
    """
    Fit a LinearRegression model on X and y, and return a tuple:
    (fitted_model, coefficients_array, intercept_value)
    """
    model = LinearRegression()
    model.fit(X, y)
    return model, model.coef_, model.intercept_