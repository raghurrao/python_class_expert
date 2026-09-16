# Day 57: Logistic Regression (Classification Basics)

In Week 8, we predicted continuous numbers (Regression). This week, we predict categories (Classification). Will this customer churn? Is this email spam? 

---

## 1. What is Logistic Regression?
Despite having "Regression" in its name, Logistic Regression is a **classification** algorithm. It is used to predict the probability that an instance belongs to a given class (e.g., a 75% chance an email is spam). 

If the probability is $> 50\%$, the model predicts Class 1 (Spam).
If the probability is $< 50\%$, the model predicts Class 0 (Not Spam).

### The Sigmoid Function
Linear regression ($y = mx + b$) outputs values from $-\infty$ to $+\infty$. Probabilities must be between 0 and 1. We solve this by passing the output of linear regression through the **Sigmoid function**, which squashes any number into a range between 0 and 1, forming an S-shaped curve.

---

## 2. Core Concepts & Operations

### Training a Logistic Classifier
Using `scikit-learn`, training a classification model looks almost identical to training a regression model!

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np

# Sample Data
# X: [Time Spent on Website (mins), Number of Pages Visited]
X = np.array([
    [5, 2], [15, 5], [2, 1], [30, 10], [10, 4]
])
# y: Did they buy? (0 = No, 1 = Yes)
y = np.array([0, 1, 0, 1, 0])

# 1. Initialize the model
model = LogisticRegression()

# 2. Fit the model
model.fit(X, y)

# 3. Predict on a new user (e.g., spent 20 mins, visited 7 pages)
X_new = np.array([[20, 7]])

# Predict the exact class (0 or 1)
prediction = model.predict(X_new)

# Predict the probability of each class [P(Class 0), P(Class 1)]
probabilities = model.predict_proba(X_new)

print(f"Predicted Class: {prediction[0]}")
print(f"Probability of Not Buying (0): {probabilities[0][0]:.2%}")
print(f"Probability of Buying (1): {probabilities[0][1]:.2%}")
```

### Why it's useful
Logistic regression is fast, interpretable, and serves as an excellent baseline model. Because it outputs probabilities, you can adjust your threshold (e.g., only predicting "Spam" if the probability is $> 90\%$).

---

## 3. Reference Documentation
* [Scikit-Learn LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
* [Logistic Regression (Wikipedia)](https://en.wikipedia.org/wiki/Logistic_regression)