# Day 61: Gradient Boosting

Random Forests build many trees independently at the same time and average their results (Bagging). Gradient Boosting takes a different approach: it builds trees *sequentially*, where each new tree tries to fix the mistakes of the previous trees (Boosting).

---

## 1. What is Gradient Boosting?
1. Train a simple, shallow Decision Tree (a "weak learner").
2. Calculate the errors (residuals) of that tree.
3. Train a *second* tree specifically to predict those errors.
4. Add the second tree's predictions to the first tree's predictions.
5. Repeat this process hundreds of times.

Because it focuses specifically on the hardest-to-predict examples, Gradient Boosting models (like XGBoost, LightGBM, and scikit-learn's GradientBoostingClassifier) are often the highest-performing algorithms for tabular (structured) data in competitive machine learning (like Kaggle).

---

## 2. Core Concepts & Operations

### Training Gradient Boosting

```python
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np

# Sample Data
X = np.random.rand(15, 3)
y = np.random.randint(0, 2, 15)

# Initialize the model
# learning_rate controls how strongly each new tree attempts to correct the previous errors.
# Smaller learning rates require more n_estimators but usually lead to better generalization.
model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# Fit the model
model.fit(X, y)

# Predict
print("Prediction:", model.predict([X[0]]))
```

### The Trade-off
Gradient Boosting is extremely powerful, but:
* It is **slower to train** than Random Forests because trees must be built one after another (cannot be parallelized easily).
* It is **easier to overfit** if you set `n_estimators` too high or `learning_rate` too high. It requires more careful hyperparameter tuning.

---

## 3. Reference Documentation
* [Scikit-Learn GradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html)
* [Gradient boosting (Wikipedia)](https://en.wikipedia.org/wiki/Gradient_boosting)
