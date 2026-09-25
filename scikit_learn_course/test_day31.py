import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

# 1. XGBoost Tests (skip if not installed)
try:
    from xgboost import XGBClassifier
    
    X, y = make_classification(n_samples=500, n_features=20, n_informative=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    xgb_model = XGBClassifier(n_estimators=10, learning_rate=0.1, max_depth=3, random_state=42)
    xgb_model.fit(X_train, y_train)
    y_pred = xgb_model.predict(X_test)
    assert len(y_pred) == 100
    
    advanced_pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', XGBClassifier(n_estimators=10, max_depth=3, random_state=42, n_jobs=-1))
    ])
    
    scores = cross_val_score(advanced_pipe, X, y, cv=3, scoring='accuracy')
    assert len(scores) == 3
    assert scores.mean() > 0.5
    print("XGBoost tests executed successfully!")

except ImportError:
    print("xgboost not installed, skipping tests. (This is expected if the user hasn't pip installed it yet)")

print("All Day 31 codes executed successfully!")
