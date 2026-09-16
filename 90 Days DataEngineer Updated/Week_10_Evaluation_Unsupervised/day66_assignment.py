from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

def build_scaling_pipeline():
    """
    Build and return a Scikit-Learn Pipeline containing:
    - 'scaler': StandardScaler
    - 'classifier': LogisticRegression
    """
    return Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression())
    ])