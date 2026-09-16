# Day 51: Multiple Linear Regression with Scikit-Learn

Yesterday we predicted $y$ using a single feature $X$. Today, we use `scikit-learn` to predict $y$ using multiple features ($X_1, X_2, X_3...$). This is called Multiple Linear Regression.

---

## 1. The Scikit-Learn API
`scikit-learn` (or `sklearn`) is the industry standard library for traditional machine learning in Python. It has a beautiful, consistent API. Almost every model uses the same three steps:
1. **Initialize:** `model = ModelName()`
2. **Fit (Train):** `model.fit(X_train, y_train)`
3. **Predict:** `predictions = model.predict(X_test)`

---

## 2. Core Concepts & Operations

### Multiple Linear Regression
The equation expands from $y = mx + b$ to:
$y = w_1X_1 + w_2X_2 + ... + w_nX_n + b$
* $w$: Weights (coefficients)
* $b$: Bias (intercept)

```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample Data
# 3 samples, 2 features (e.g., [Square Footage, Number of Bedrooms])
X = np.array([
    [1500, 3],
    [2000, 4],
    [1200, 2]
])
# Target (e.g., Price in thousands)
y = np.array([300, 400, 250])

# 1. Initialize the model
model = LinearRegression()

# 2. Fit the model to the data
model.fit(X, y)

# 3. Inspect the learned parameters
print("Coefficients (Weights):", model.coef_)
print("Intercept (Bias):", model.intercept_)

# 4. Make a prediction on new data
# E.g., A house with 1800 sqft and 3 bedrooms
X_new = np.array([[1800, 3]])
prediction = model.predict(X_new)
print(f"Predicted Price: ${prediction[0]:.2f}k")
```

### Important Rule of Scikit-Learn
Scikit-Learn expects `X` to always be a 2D array (a matrix of shape `[n_samples, n_features]`), even if you only have one feature. It expects `y` to be a 1D array of shape `[n_samples]`.

---

## 3. Reference Documentation
* [Scikit-Learn LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)