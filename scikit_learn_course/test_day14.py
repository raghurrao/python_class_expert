import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, ElasticNet
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import make_regression
np.random.seed(42)
X_mock, _ = make_regression(n_samples=500, n_features=8, noise=0.5, random_state=42)
columns = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
df = pd.DataFrame(X_mock, columns=columns)
# Make it highly non-linear
df['MedHouseVal'] = (df['MedInc']**2 * 3.5) + (df['HouseAge'] * df['AveRooms']) + np.sin(df['Latitude']*5) * 10 + np.cos(df['Longitude']*5) * 10 + np.random.randn(500) * 0.5


X = df.drop('MedHouseVal', axis=1)
y = df['MedHouseVal']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])
preprocessor = ColumnTransformer([
    ('num', num_pipeline, list(X.columns))
])

models = {
    'Linear Regression': LinearRegression(),
    'Ridge Regression (alpha=1.0)': Ridge(alpha=1.0, random_state=42),
    'Random Forest (n=10)': RandomForestRegressor(n_estimators=10, random_state=42)
}

results = {}
for name, model in models.items():
    full_pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', model)
    ])
    full_pipeline.fit(X_train, y_train)
    y_pred = full_pipeline.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    results[name] = {'RMSE': rmse, 'R2': r2}

# Random Forest should beat Linear Regression
assert results['Random Forest (n=10)']['RMSE'] < results['Linear Regression']['RMSE']

# Extract feature importance
rf_pipe = Pipeline([
    ('preprocessor', preprocessor),
    ('rf', RandomForestRegressor(n_estimators=10, random_state=42))
])
rf_pipe.fit(X_train, y_train)
importances = rf_pipe.named_steps['rf'].feature_importances_
assert len(importances) == X.shape[1]

# ElasticNet Mini Project
elastic_pipe = Pipeline([
    ('preprocessor', preprocessor),
    ('model', ElasticNet(alpha=0.5, l1_ratio=0.5, random_state=42))
])
elastic_pipe.fit(X_train, y_train)
y_pred_el = elastic_pipe.predict(X_test)
assert r2_score(y_test, y_pred_el) < results['Random Forest (n=10)']['R2']

print("All Day 14 codes executed successfully!")
