import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression

np.random.seed(42)
X = 2 * np.random.rand(100, 1)
X = X * 10
y = 30000 + 5000 * X + np.random.randn(100, 1) * 10000

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
assert lin_reg.intercept_[0] > 0
assert lin_reg.coef_[0][0] > 0

y_pred = lin_reg.predict(X_test)
plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred)
plt.close()

# Manual Math Prediction
pred_val = lin_reg.predict(np.array([[5]]))[0][0]
assert pred_val > 0

# Normal Equation (NumPy)
X_b = np.c_[np.ones((80, 1)), X_train]
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)
assert np.isclose(theta_best[0][0], lin_reg.intercept_[0])
assert np.isclose(theta_best[1][0], lin_reg.coef_[0][0])

# Debugging Challenge
try:
    X_buggy = np.array([1, 2, 3, 4, 5])
    y_buggy = np.array([2, 4, 6, 8, 10])
    model_buggy = LinearRegression()
    model_buggy.fit(X_buggy, y_buggy)
except Exception as e:
    print('Caught expected bug:', type(e).__name__)

# Model evaluation
r2 = lin_reg.score(X_test, y_test)
assert r2 > 0

# Mini Project
X_multi, y_multi = make_regression(n_samples=500, n_features=3, noise=15.0, random_state=42)
X_tr, X_te, y_tr, y_te = train_test_split(X_multi, y_multi, test_size=0.2, random_state=42)
multi_model = LinearRegression()
multi_model.fit(X_tr, y_tr)
assert multi_model.score(X_te, y_te) > 0.0

print("All Day 8 codes executed successfully!")
