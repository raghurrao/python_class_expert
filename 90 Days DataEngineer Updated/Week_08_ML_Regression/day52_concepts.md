# Day 52: Polynomial Regression

Linear regression assumes the relationship between $X$ and $y$ is a straight line. But what if the data curves? 

---

## 1. Non-Linear Relationships
If you try to fit a straight line to a U-shaped curve, the model will be terrible (this is called **underfitting**). We can solve this without changing our algorithm; we just change our data! By engineering new features that are powers of our original features, we can fit curves using standard linear regression.

---

## 2. Core Concepts & Operations

### Polynomial Features
Instead of predicting $y$ using just $X$, we predict $y$ using $X$, $X^2$, $X^3$, etc.
$y = w_1X + w_2X^2 + b$

Notice that this equation is still *linear* with respect to the weights ($w$). That's why it's still called Linear Regression!

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample Data (a curve)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 4, 9, 16, 25]) # y = X^2

# 1. Transform the features
# degree=2 means we want X and X^2
# include_bias=False prevents adding a column of 1s (LinearRegression handles the bias/intercept itself)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

print("Original X:\n", X)
print("Polynomial X (X, X^2):\n", X_poly)

# 2. Fit standard Linear Regression on the transformed features
model = LinearRegression()
model.fit(X_poly, y)

print(f"Learned Coefficients: {model.coef_}") # Should be close to [0, 1] for 0*X + 1*X^2
```

### The Danger of Overfitting
If you set the degree too high (e.g., degree 15 on 15 data points), the curve will zigzag wildly to pass exactly through every single training point. It will have zero error on the training data, but it will make absurd predictions for any new data. This is called **overfitting**.

---

## 3. Reference Documentation
* [Scikit-Learn PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)
