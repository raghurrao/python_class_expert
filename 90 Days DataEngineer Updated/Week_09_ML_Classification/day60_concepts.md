# Day 60: Random Forests (Ensemble Learning)

A single Decision Tree is prone to overfitting and can be highly sensitive to small changes in the training data. What if, instead of relying on one tree, we trained an entire forest of them and let them vote?

---

## 1. What is a Random Forest?
A Random Forest is an **Ensemble Method**—it combines the predictions of multiple machine learning models together to create a much stronger, more robust model.

How it works (Bagging):
1. **Random Sampling:** It takes random subsets of the training data (with replacement).
2. **Random Features:** At each split in a tree, it only considers a random subset of the features.
3. **Voting:** It trains hundreds of shallow trees this way. When predicting, all trees vote, and the majority wins.

Because the trees are trained on slightly different data and look at different features, they make *uncorrelated* errors. When you average them out, the errors cancel out!

---

## 2. Core Concepts & Operations

### Training a Random Forest
It's just as easy as training a single tree!

```python
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Sample Data (10 samples, 4 features)
X = np.random.rand(10, 4)
y = np.array([0, 1, 1, 0, 1, 0, 0, 1, 1, 0])

# Initialize the model
# n_estimators is the number of trees in the forest
model = RandomForestClassifier(n_estimators=50, random_state=42)

# Fit the model
model.fit(X, y)

# Predict
print("Prediction:", model.predict([X[0]]))

# Feature Importance
# Random Forests give us a great freebie: they tell us which features were most useful across all trees!
print("Feature Importances:", model.feature_importances_)
```

---

## 3. Reference Documentation
* [Scikit-Learn RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
* [Random forest (Wikipedia)](https://en.wikipedia.org/wiki/Random_forest)
