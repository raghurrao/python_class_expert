from sklearn.metrics import precision_score, recall_score, f1_score
import numpy as np

def compute_classification_metrics(y_true: np.ndarray, y_pred: np.ndarray):
    """
    Compute and return: (precision, recall, f1)
    """
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    return float(precision), float(recall), float(f1)