from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def compute_regression_metrics(y_true: np.ndarray, y_pred: np.ndarray):
    """
    Compute and return: (MSE, RMSE, R2)
    """
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    return float(mse), float(rmse), float(r2)