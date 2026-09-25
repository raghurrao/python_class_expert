import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

np.random.seed(42)
X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(X).ravel() + np.random.randn(80) * 0.2

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

tree = DecisionTreeRegressor(random_state=42)
tree.fit(X_train, y_train)

forest = RandomForestRegressor(n_estimators=100, random_state=42)
forest.fit(X_train, y_train)

tree_rmse = np.sqrt(mean_squared_error(y_test, tree.predict(X_test)))
forest_rmse = np.sqrt(mean_squared_error(y_test, forest.predict(X_test)))
assert forest_rmse < tree_rmse

forest_constrained = RandomForestRegressor(n_estimators=100, max_depth=2, random_state=42)
forest_constrained.fit(X_train, y_train)
assert forest_constrained.score(X_test, y_test) > 0.0

# Debugging challenge (Extrapolation fails)
historical_sales = np.array([[1], [2], [3], [4], [5]])
historical_revenue = np.array([50, 75, 100, 125, 150])
rf_debug = RandomForestRegressor(n_estimators=10, random_state=42)
rf_debug.fit(historical_sales, historical_revenue)
future_month = np.array([[6]])
assert rf_debug.predict(future_month)[0] <= 150.0

# Feature Importance
X_multi = np.random.rand(100, 5)
y_multi = 10 * X_multi[:, 0] + np.random.randn(100) 

rf_feat = RandomForestRegressor(n_estimators=50, random_state=42)
rf_feat.fit(X_multi, y_multi)
importances = rf_feat.feature_importances_
assert importances[0] > 0.8 # Feature 0 should hold massive importance

print("All Day 13 codes executed successfully!")
