import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X, y = make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 1. GridSearchCV SVM
param_grid = {
    'kernel': ['linear', 'rbf'],
    'C': [0.1, 1, 10],
    'gamma': ['scale', 'auto'] 
}
grid_search = GridSearchCV(estimator=SVC(random_state=42), param_grid=param_grid, cv=3, n_jobs=-1)
grid_search.fit(X_scaled, y)

assert grid_search.best_score_ > 0.5
assert 'kernel' in grid_search.best_params_
assert len(grid_search.predict(X_scaled[:5])) == 5

# 2. RandomizedSearchCV RandomForest
rf_grid = {
    'n_estimators': [10, 50, 100],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}
rf_random = RandomizedSearchCV(
    estimator=RandomForestClassifier(random_state=42), 
    param_distributions=rf_grid, 
    n_iter=5, 
    cv=3, 
    random_state=42, 
    n_jobs=-1
)
rf_random.fit(X, y)
assert rf_random.best_score_ > 0.5
assert 'n_estimators' in rf_random.best_params_

# 3. Pipeline tuning
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('svc', SVC(random_state=42))
])
pipe_grid = {
    'svc__C': [0.1, 1, 10],
    'svc__kernel': ['linear', 'rbf']
}
pipe_search = GridSearchCV(pipe, param_grid=pipe_grid, cv=3, n_jobs=-1)
pipe_search.fit(X, y)

assert pipe_search.best_score_ > 0.5
assert 'svc__C' in pipe_search.best_params_

print("All Day 27 codes executed successfully!")
