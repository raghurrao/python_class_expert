from sklearn.linear_model import Ridge, Lasso
import numpy as np

def train_regularized_model(X: np.ndarray, y: np.ndarray, alpha: float, penalty: str):
    """
    Fit a regularized regression model on X and y:
    - penalty == 'ridge': use Ridge regression
    - penalty == 'lasso': use Lasso regression
    
    Return the fitted model.
    """
    if penalty == "ridge":
        model = Ridge(alpha=alpha)
    else:
        model = Lasso(alpha=alpha)
    model.fit(X, y)
    return model