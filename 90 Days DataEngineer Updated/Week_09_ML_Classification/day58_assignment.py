from sklearn.svm import SVC
import numpy as np

def train_svm_classifier(X: np.ndarray, y: np.ndarray, kernel: str = 'rbf'):
    """
    Fit and return an SVM classifier (SVC) with the specified kernel.
    """
    model = SVC(kernel=kernel)
    model.fit(X, y)
    return model