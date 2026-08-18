from sklearn.linear_model import LogisticRegression
import numpy as np

def train_logistic_classifier(X: np.ndarray, y: np.ndarray):
    """
    Fit and return a LogisticRegression classifier.
    """
    model = LogisticRegression()
    model.fit(X, y)
    return model