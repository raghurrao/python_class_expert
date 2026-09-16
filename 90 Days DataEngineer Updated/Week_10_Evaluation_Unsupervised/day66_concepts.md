# Day 66: Scikit-Learn Pipelines

In machine learning, you rarely just feed raw data straight into a model. You usually have to clean it, scale it, and transform it first. But doing this manually for the training set, the test set, and new production data is a recipe for data leakage and bugs.

---

## 1. What is a Pipeline?
A `Pipeline` chains together multiple data processing steps and a final machine learning model into a single object. 
When you call `pipeline.fit(X)`, it automatically calls `fit_transform()` on all the preprocessing steps and then `fit()` on the final model. 
When you call `pipeline.predict(X)`, it automatically calls `transform()` on all the preprocessing steps and then `predict()` on the final model.

---

## 2. Core Concepts & Operations

### Building a Pipeline
Let's combine standard scaling (which makes all features have a mean of 0 and std of 1) with a Logistic Regression model.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

# Sample Data
X_train = np.array([[1000, 2], [5000, 4], [2000, 1]])
y_train = np.array([0, 1, 0])

X_test = np.array([[3000, 3], [1500, 2]])

# 1. Define the Pipeline steps
# It's a list of tuples: ('name', StepObject())
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

# 2. Fit the pipeline (Scales X_train, then fits LogisticRegression)
pipeline.fit(X_train, y_train)

# 3. Predict with the pipeline (Automatically scales X_test using the logic learned from X_train!)
predictions = pipeline.predict(X_test)
print("Predictions:", predictions)
```

### Why use Pipelines?
1. **Prevents Data Leakage:** If you scale your entire dataset *before* splitting into train/test, information from the test set leaks into the training process (the scaler uses the global mean). Pipelines ensure the scaler only learns from the training data during cross-validation.
2. **Clean Code:** You only have one object to save, load, and manage.
3. **Grid Search Compatibility:** You can use `GridSearchCV` on a Pipeline to optimize hyperparameters for *both* your preprocessing steps and your model simultaneously!

---

## 3. Reference Documentation
* [Scikit-Learn Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)
