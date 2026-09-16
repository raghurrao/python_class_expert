# Day 30: Eigenvalues and Trace

Today we delve deeper into matrix properties. Eigenvalues and eigenvectors are fundamental to dimensionality reduction techniques like Principal Component Analysis (PCA) and understanding the behavior of dynamic systems.

---

## 1. Core Concepts

### Trace
The trace of a square matrix is simply the sum of the elements on its main diagonal (from the top left to the bottom right). It has several useful properties, such as being equal to the sum of the matrix's eigenvalues.

```python
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Calculate trace: 1 + 5 + 9 = 15
trace_A = np.trace(A)
```

### Eigenvalues and Eigenvectors
When you multiply a matrix $A$ by a vector $v$, the result is usually a new vector pointing in a completely different direction. However, for every square matrix, there are special vectors that don't change direction when multiplied by the matrix—they only change in length (scale).
* These special vectors are called **Eigenvectors**.
* The factor by which they are scaled is called the **Eigenvalue** ($\lambda$).

Equation: $Av = \lambda v$

```python
# Create a square matrix
M = np.array([[4, -2],
              [1,  1]])

# Calculate eigenvalues and eigenvectors
# w contains the eigenvalues, v contains the corresponding eigenvectors (as columns)
eigenvalues, eigenvectors = np.linalg.eig(M)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Verification: M * v = lambda * v
# Let's take the first eigenvalue and eigenvector
lambda_1 = eigenvalues[0]
v_1 = eigenvectors[:, 0] # First column

print("M * v1:", M @ v_1)
print("lambda_1 * v1:", lambda_1 * v_1)
# These should be approximately equal (allowing for floating point imprecision)
```

---

## 2. Why do we care?
In PCA, we calculate the eigenvectors of a covariance matrix to find the "principal components" (the directions of maximum variance in the data). The eigenvalues tell us how much variance is explained by each component.

---

## 3. Reference Documentation
* [Numpy linalg.eig](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html)
* [Numpy trace](https://numpy.org/doc/stable/reference/generated/numpy.trace.html)