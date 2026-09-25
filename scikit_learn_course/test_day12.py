import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

np.random.seed(42)
X = 6 * np.random.rand(100, 1) - 3
y = 0.5 * X**2 + X + 2 + np.random.randn(100, 1)

tree_unconstrained = DecisionTreeRegressor(random_state=42)
tree_unconstrained.fit(X, y)

tree_constrained = DecisionTreeRegressor(max_depth=3, random_state=42)
tree_constrained.fit(X, y)

assert tree_unconstrained.score(X, y) == 1.0
assert tree_constrained.score(X, y) < 1.0

small_tree = DecisionTreeRegressor(max_depth=1, random_state=42)
small_tree.fit(X, y)
assert len(np.unique(small_tree.predict(X))) <= 2

tree_min_samples = DecisionTreeRegressor(min_samples_split=20, random_state=42)
tree_min_samples.fit(X, y)
assert tree_min_samples.score(X, y) < 1.0

# Mini Project (Scaling doesn't matter)
tree1 = DecisionTreeRegressor(max_depth=2, random_state=42)
tree1.fit(X, y)

tree2 = DecisionTreeRegressor(max_depth=2, random_state=42)
tree2.fit(X * 1000, y)

pred1 = tree1.predict([[2.5]])
pred2 = tree2.predict([[2500]])
assert np.isclose(pred1[0], pred2[0])

print("All Day 12 codes executed successfully!")
