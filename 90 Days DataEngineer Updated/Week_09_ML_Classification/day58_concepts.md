# Day 58: Support Vector Machines (SVM)

Logistic Regression tries to draw a line through the data. Support Vector Machines (SVM) take it a step further: they try to draw a line (or a hyperplane) that is as *far away* from the data points as possible.

---

## 1. What is an SVM?
Imagine you have red dots and blue dots on a piece of paper, and you want to draw a line to separate them. You could draw many different lines. SVM finds the **optimal hyperplane**—the line that maximizes the "margin" (the distance between the line and the closest dots of either color). 

Those closest dots that the margin touches are called the **Support Vectors**.

### The Kernel Trick
What if the dots are arranged in a circle (red in the middle, blue on the outside)? You can't draw a straight line to separate them. 

SVM uses the **Kernel Trick** to project the data into a higher-dimensional space where it *is* possible to draw a flat plane to separate them.
* **Linear Kernel:** Just a straight line/flat plane.
* **RBF (Radial Basis Function) Kernel:** The most common. Allows for highly non-linear, curved boundaries.

---

## 2. Core Concepts & Operations

### Training an SVM
We use `SVC` (Support Vector Classification) in scikit-learn. 

```python
from sklearn.svm import SVC
import numpy as np

# Sample Data (Non-linear pattern)
X = np.array([
    [1, 1], [2, 2], # Class 0 (bottom left)
    [8, 8], [9, 9], # Class 0 (top right)
    [5, 5], [4, 6]  # Class 1 (middle)
])
y = np.array([0, 0, 0, 0, 1, 1])

# Initialize the model using the RBF kernel for non-linear data
# 'C' is the regularization parameter. 
# Small C = wider margin, but more misclassifications allowed.
# Large C = smaller margin, tries to classify everything perfectly.
model = SVC(kernel='rbf', C=1.0)

# Fit the model
model.fit(X, y)

# Predict a point in the middle
print("Prediction for [5, 6]:", model.predict([[5, 6]]))
```

---

## 3. Reference Documentation
* [Scikit-Learn SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
* [Support-vector machine (Wikipedia)](https://en.wikipedia.org/wiki/Support-vector_machine)
