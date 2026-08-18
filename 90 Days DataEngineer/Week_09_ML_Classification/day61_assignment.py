from sklearn.ensemble import GradientBoostingClassifier
import numpy as np

def train_gradient_boosting(X: np.ndarray, y: np.ndarray):
    """
    Fit and return a GradientBoostingClassifier.
    """
    model = GradientBoostingClassifier(random_state=42)
    model.fit(X, y)
    return model