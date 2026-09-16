# Day 65: Hyperparameter Tuning (GridSearchCV)

When you initialize a model in scikit-learn (e.g., `RandomForestClassifier()`), it comes with default settings. These settings, known as **Hyperparameters**, control how the algorithm learns. 

---

## 1. Parameters vs Hyperparameters
* **Parameters:** Learned by the model during training (e.g., the weights and biases in Linear Regression, or the splits in a Decision Tree).
* **Hyperparameters:** Set by the *human* before training begins (e.g., the `max_depth` of a tree, or the `learning_rate` in gradient boosting).

How do you know the best `max_depth`? You have to test a bunch of them and see which one performs best.

---

## 2. Core Concepts & Operations

### GridSearchCV
GridSearchCV (Grid Search Cross Validation) automates this process. 
1. You give it a "grid" of hyperparameters to try.
2. It trains a model for *every possible combination* of those hyperparameters.
3. It evaluates them using Cross-Validation to ensure the results are robust.
4. It returns the best model.

```python
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Sample Data
X = np.random.rand(100, 5)
y = np.random.randint(0, 2, 100)

# Define the grid of hyperparameters you want to test
param_grid = {
    'max_depth': [3, 5, 10, None],
    'min_samples_split': [2, 5, 10],
    'criterion': ['gini', 'entropy']
}

# Initialize GridSearchCV
# cv=3 means 3-fold cross validation.
# Note: It will train (4 * 3 * 2) = 24 models, times 3 folds = 72 training runs!
grid_search = GridSearchCV(
    estimator=DecisionTreeClassifier(random_state=42), 
    param_grid=param_grid, 
    cv=3
)

# Fit it (This runs the search)
grid_search.fit(X, y)

print("Best Hyperparameters Found:")
print(grid_search.best_params_)

print(f"Best Cross-Validation Score: {grid_search.best_score_:.4f}")

# You can now use grid_search exactly like a normal model to predict!
# It automatically uses the best model it found.
# prediction = grid_search.predict(X_new)
```

---

## 3. Reference Documentation
* [Scikit-Learn GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
* [Hyperparameter optimization (Wikipedia)](https://en.wikipedia.org/wiki/Hyperparameter_optimization)
