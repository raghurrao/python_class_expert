# Day 54: Regression Metrics

How do you know if your regression model is actually any good? We need objective metrics to evaluate the distance between our model's predictions ($\hat{y}$) and the true values ($y$).

---

## 1. Why multiple metrics?
Different metrics penalize errors differently. Some metrics are easy to interpret in the original units, while others are relative percentages.

---

## 2. Core Metrics

### Mean Squared Error (MSE)
Calculates the average of the *squared* differences between predictions and actuals.
* **Pros:** Because of the square, it heavily penalizes large errors (outliers). Mathematically very clean to differentiate (useful for gradient descent).
* **Cons:** Not in the same units as the target variable (e.g., if predicting dollars, MSE is in dollars squared).

### Root Mean Squared Error (RMSE)
The square root of the MSE.
* **Pros:** Back in the original units! If predicting house prices in dollars, an RMSE of 5000 means your predictions are off by about $5,000 on average.

### R-Squared ($R^2$)
Measures the proportion of the variance in the dependent variable that is predictable from the independent variables.
* **Interpretation:** 1.0 is perfect prediction. 0.0 means the model is no better than just predicting the average $y$ every single time. Negative values mean the model is worse than predicting the average.

```python
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])

# 1. MSE
mse = mean_squared_error(y_true, y_pred)
print(f"MSE: {mse:.2f}")

# 2. RMSE
rmse = np.sqrt(mse)
print(f"RMSE: {rmse:.2f}")

# 3. R-Squared
r2 = r2_score(y_true, y_pred)
print(f"R-Squared: {r2:.2f}")
```

---

## 3. Reference Documentation
* [Scikit-Learn Regression Metrics](https://scikit-learn.org/stable/modules/classes.html#regression-metrics)
