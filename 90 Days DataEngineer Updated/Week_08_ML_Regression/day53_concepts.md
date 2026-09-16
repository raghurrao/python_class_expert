# Day 53: Regularization (Ridge and Lasso)

Yesterday we learned that a model with too many features (like high-degree polynomials) can overfit the data. Regularization is a technique used to prevent overfitting by penalizing large weights in the model.

---

## 1. What is Regularization?
Regularization modifies the cost function that the model tries to minimize during training.
* **Standard Linear Regression Cost:** Minimize the Error (MSE).
* **Regularized Cost:** Minimize the Error (MSE) + a Penalty for having large weights.

By forcing the weights ($w$) to stay small, the model becomes simpler, smoother, and less sensitive to noise in the training data.

---

## 2. Core Concepts & Operations

### Ridge Regression (L2 Regularization)
Ridge adds a penalty equal to the **square** of the magnitude of coefficients.
* It shrinks the coefficients towards zero, but never exactly to zero.
* Good for when you have many features that are all somewhat useful.

### Lasso Regression (L1 Regularization)
Lasso adds a penalty equal to the **absolute value** of the magnitude of coefficients.
* It shrinks coefficients all the way to **exactly zero**.
* This performs automatic **feature selection** by entirely removing useless features.

```python
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split
import numpy as np

# X with 100 features, many of which might be noise
X = np.random.rand(100, 100) 
y = np.random.rand(100)

# alpha is the penalty strength (hyperparameter).
# High alpha = stronger penalty = smaller weights = less overfitting
alpha = 1.0 

# Ridge (L2)
ridge_model = Ridge(alpha=alpha)
ridge_model.fit(X, y)
# Most coefficients will be small, but non-zero
print(f"Ridge zero coefficients: {np.sum(ridge_model.coef_ == 0)}") 

# Lasso (L1)
lasso_model = Lasso(alpha=alpha)
lasso_model.fit(X, y)
# Many coefficients will be exactly zero!
print(f"Lasso zero coefficients: {np.sum(lasso_model.coef_ == 0)}")
```

---

## 3. Reference Documentation
* [Scikit-Learn Ridge Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)
* [Scikit-Learn Lasso Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html)
