import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error

np.random.seed(42)
X = 6 * np.random.rand(100, 1) - 3
y = 0.5 * X**2 + X + 2 + np.random.randn(100, 1)

lin_reg = LinearRegression()
lin_reg.fit(X, y)

poly_pipe = Pipeline([
    ('poly', PolynomialFeatures(degree=2, include_bias=False)),
    ('model', LinearRegression())
])
poly_pipe.fit(X, y)

lin_rmse = np.sqrt(mean_squared_error(y, lin_reg.predict(X)))
poly_rmse = np.sqrt(mean_squared_error(y, poly_pipe.predict(X)))
assert poly_rmse < lin_rmse

poly_features = PolynomialFeatures(degree=3, include_bias=False)
X_dummy = np.array([[2.0], [3.0]])
X_dummy_poly = poly_features.fit_transform(X_dummy)
assert X_dummy_poly.shape == (2, 3)
assert X_dummy_poly[0, 2] == 8.0

# Coding Exercise (Overfitting)
crazy_pipe = Pipeline([
    ('poly', PolynomialFeatures(degree=50, include_bias=False)),
    ('scaler', StandardScaler()), 
    ('model', LinearRegression())
])
crazy_pipe.fit(X, y)
assert crazy_pipe.score(X, y) > 0.0

# Mini Project
tiny_X = pd.DataFrame({'Temp': [10, 20], 'Pressure': [5, 10]})
poly2 = PolynomialFeatures(degree=2, include_bias=False)
poly2.fit_transform(tiny_X)
features = poly2.get_feature_names_out()
assert 'Temp Pressure' in features or 'Temp Pressure' in [f.replace(' ', '') for f in features] or any('Temp' in f and 'Pressure' in f for f in features)

print("All Day 11 codes executed successfully!")
