from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np

def run_classification_pipeline(X: np.ndarray, y: np.ndarray):
    """
    1. Perform a train/test split (80/20, random_state=42).
    2. Fit a RandomForestClassifier.
    3. Return a tuple: (train_accuracy, test_accuracy, fitted_model)
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model.score(X_train, y_train), model.score(X_test, y_test), model