from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
import numpy as np

def tune_decision_tree(X: np.ndarray, y: np.ndarray, param_grid: dict):
    """
    Run GridSearchCV using a DecisionTreeClassifier and search param_grid.
    Return: (best_params_dict, best_score)
    """
    gs = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid, cv=3)
    gs.fit(X, y)
    return gs.best_params_, float(gs.best_score_)