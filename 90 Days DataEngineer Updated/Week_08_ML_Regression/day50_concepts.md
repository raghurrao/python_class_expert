# Day 50: Linear Regression Fundamentals

Welcome to the Machine Learning section! We start with the simplest, yet most widely used algorithm in the world: Linear Regression.

---

## 1. What is Linear Regression?
Linear regression attempts to model the relationship between two variables by fitting a linear equation (a straight line) to observed data. 
* **Independent Variable ($X$):** The feature you are using to predict. (e.g., Square footage of a house)
* **Dependent Variable ($y$):** The outcome you are trying to predict. (e.g., Price of the house)

The goal is to find the best-fitting line: $y = mx + b$
Where $m$ is the slope (weight) and $b$ is the intercept (bias).

---

## 2. Core Concepts & Operations

### Calculating Slope and Intercept Manually
For simple linear regression (only one feature $X$), we can calculate the optimal slope and intercept directly using the covariance and variance of the data, bypassing the need for iterative gradient descent.

* **Slope ($m$):** $m = \frac{\text{Covariance}(X, y)}{\text{Variance}(X)}$
* **Intercept ($b$):** $b = \bar{y} - m\bar{X}$ (where $\bar{y}$ is the mean of $y$ and $\bar{X}$ is the mean of $X$)

```python
import numpy as np
import matplotlib.pyplot as plt

# Sample data
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# 1. Calculate Slope (m)
# np.cov returns a 2x2 covariance matrix. The covariance of X and y is at index [0, 1]
# ddof=1 means we use sample variance/covariance (N-1 degrees of freedom)
slope = np.cov(X, y, ddof=1)[0, 1] / np.var(X, ddof=1)

# 2. Calculate Intercept (b)
intercept = np.mean(y) - slope * np.mean(X)

print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")

# Plotting the result
plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X, slope*X + intercept, color='red', label='Line of Best Fit')
plt.legend()
plt.show()
```

### Why do this manually?
In practice, you will almost always use a library like `scikit-learn` for regression. However, calculating it manually once helps demystify the algorithm and proves it's just statistics under the hood!

---

## 3. Reference Documentation
* [Simple linear regression (Wikipedia)](https://en.wikipedia.org/wiki/Simple_linear_regression)
