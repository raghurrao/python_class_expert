from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
import numpy as np

def run_regression_pipeline(X: np.ndarray, y: np.ndarray, alpha: float):
    """
    1. Perform a train/test split (80% train, 20% test, random_state=42).
    2. Fit a Ridge model with given alpha.
    3. Return a tuple: (train_score_r2, test_score_r2)
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = Ridge(alpha=alpha)
    model.fit(X_train, y_train)
    return model.score(X_train, y_train), model.score(X_test, y_test)