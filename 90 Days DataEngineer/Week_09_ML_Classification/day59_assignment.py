from sklearn.tree import DecisionTreeClassifier
import numpy as np

def train_decision_tree(X: np.ndarray, y: np.ndarray, max_depth: int = 3):
    """
    Fit and return a DecisionTreeClassifier with max_depth.
    """
    model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    model.fit(X, y)
    return model