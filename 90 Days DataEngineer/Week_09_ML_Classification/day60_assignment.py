from sklearn.ensemble import RandomForestClassifier
import numpy as np

def train_random_forest(X: np.ndarray, y: np.ndarray, n_estimators: int = 50):
    """
    Fit and return a RandomForestClassifier.
    """
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    model.fit(X, y)
    return model