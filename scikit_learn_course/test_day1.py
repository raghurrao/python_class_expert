import sklearn
print(f'Scikit-learn version: {sklearn.__version__}')

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# 1. Create data (Features X, Target y)
X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)

# 2. Initialize the model
model = LogisticRegression()

# 3. Train the model
model.fit(X, y)

# 4. Inference (Predict)
predictions = model.predict(X[:5])
print('First 5 true targets:', y[:5])
print('First 5 predictions: ', predictions)

# Test plotting without blocking
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', edgecolor='k')
plt.title('Synthetic Classification Data')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
# plt.show() - disabled for testing
plt.close()

model2 = LogisticRegression()
model2.fit(X, y)
predictions2 = model2.predict(X)
proba = model2.predict_proba(X)
print('Shape of predictions2:', predictions2.shape)
print('Shape of proba:', proba.shape)

# Exercise testing
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
X_reg, y_reg = make_regression(n_samples=200, n_features=1, noise=15)
model_reg = LinearRegression()
model_reg.fit(X_reg, y_reg)
print("Regression fitted successfully.")

import numpy as np
X_bug = np.array([1, 2, 3, 4, 5])
y_bug = np.array([2, 4, 6, 8, 10])
model_bug = LinearRegression()
try:
    model_bug.fit(X_bug, y_bug)
except Exception as e:
    print("Caught expected bug:", type(e).__name__)

accuracy = model.score(X, y)
print(f'Model Accuracy: {accuracy * 100:.2f}%')
print("All Day 1 codes executed successfully!")
