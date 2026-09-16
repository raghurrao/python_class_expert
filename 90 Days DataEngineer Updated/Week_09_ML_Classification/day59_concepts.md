# Day 59: Decision Trees

While Logistic Regression and SVMs rely on complex math to draw boundaries, Decision Trees learn by asking a series of simple Yes/No questions.

---

## 1. What is a Decision Tree?
A decision tree breaks down a dataset into smaller and smaller subsets based on rules. 
For example, to predict if someone will play tennis:
1. Is it raining? (Yes -> Don't Play. No -> Go to step 2)
2. Is it highly humid? (Yes -> Don't Play. No -> Play)

This structure makes them **highly interpretable**. You can literally print out the tree and show it to non-technical stakeholders to explain exactly why the model made a certain decision.

---

## 2. Core Concepts & Operations

### Training a Decision Tree
We use `DecisionTreeClassifier` in scikit-learn.

```python
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Sample Data
# [Age, Salary (thousands)]
X = np.array([
    [22, 30], [25, 40], [30, 80], [35, 120], [40, 150], [50, 60]
])
# Target: Bought a luxury car (0 = No, 1 = Yes)
y = np.array([0, 0, 1, 1, 1, 0])

# Initialize the model
# max_depth limits how many questions the tree can ask. 
# Without it, the tree will ask questions until every leaf has exactly 1 data point (massive overfitting).
model = DecisionTreeClassifier(max_depth=3, random_state=42)

# Fit the model
model.fit(X, y)

# Predict for a 33 year old making 90k
print("Prediction:", model.predict([[33, 90]]))
```

### The Overfitting Problem
Decision Trees are notorious for overfitting. If you let a tree grow infinitely deep, it will memorize the training data. This is why we almost always use hyperparameters like `max_depth`, `min_samples_split`, or `min_samples_leaf` to "prune" the tree.

---

## 3. Reference Documentation
* [Scikit-Learn DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
* [Decision tree learning (Wikipedia)](https://en.wikipedia.org/wiki/Decision_tree_learning)
