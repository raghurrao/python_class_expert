from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import joblib
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day86_pipeline

def train_and_serialize_best_model(df: pd.DataFrame, model_path: str = "best_churn_model.pkl"):
    """
    1. Separate features X (age, tenure, monthly_charges, contract_type) and target y (churn).
    2. Build a pipeline combining the preprocessor from Day 86 and RandomForestClassifier.
    3. Run a GridSearchCV over n_estimators parameter: [10, 50].
    4. Fit, serialize the best model to model_path, and return best estimator.
    """
    X = df[['age', 'tenure', 'monthly_charges', 'contract_type']]
    y = df['churn']
    
    preprocessor = day86_pipeline.build_preprocessing_pipeline()
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(random_state=42))
    ])
    
    param_grid = {
        'classifier__n_estimators': [10, 50]
    }
    
    grid = GridSearchCV(pipeline, param_grid, cv=3)
    grid.fit(X, y)
    
    joblib.dump(grid.best_estimator_, model_path)
    return grid.best_estimator_