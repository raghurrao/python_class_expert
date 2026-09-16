# Day 29: Matrix Math

Matrices are 2D arrays of numbers. They are fundamental in machine learning for representing datasets (rows are samples, columns are features) and transformations (like the weights in a neural network).

---

## 1. Why Matrices?
Instead of solving equations one by one, matrices allow us to perform operations on thousands of variables simultaneously using optimized hardware (like GPUs). 

---

## 2. Core Concepts & Operations

### Matrix Multiplication
Unlike element-wise multiplication, true matrix multiplication (the dot product of matrices) involves multiplying rows of the first matrix by columns of the second matrix. 
**Rule:** For matrices A (shape $m \times n$) and B (shape $p \times q$) to be multiplied, the inner dimensions must match ($n = p$). The resulting matrix will have the shape $m \times q$.

```python
import numpy as np

A = np.array([[1, 2], 
              [3, 4]])  # 2x2

B = np.array([[5, 6], 
              [7, 8]])  # 2x2

# Matrix multiplication using np.matmul or the @ operator
C = A @ B 
# Equivalent to np.matmul(A, B) or np.dot(A, B) for 2D arrays
```

### Matrix Transpose
Transposing a matrix flips it over its diagonal. Rows become columns and columns become rows.

```python
A_t = A.T
# [[1, 3],
#  [2, 4]]
```

### Solving Systems of Linear Equations
A system of equations like:
$2x + 3y = 8$
$5x - y = -2$

Can be written in matrix form as $Ax = B$, where $A$ is the matrix of coefficients, $x$ is the column vector of variables, and $B$ is the column vector of constants.

```python
# Coefficients matrix A
A_sys = np.array([[2, 3], 
                  [5, -1]])

# Constants vector B
B_sys = np.array([8, -2])

# Solve for x (returns [x, y])
# np.linalg.solve is much faster and more numerically stable than finding the inverse of A
solution = np.linalg.solve(A_sys, B_sys)
print(f"x = {solution[0]}, y = {solution[1]}")
```

---

## 3. Reference Documentation
* [Numpy linalg.solve](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html)
* [Matrix Multiplication (Wikipedia)](https://en.wikipedia.org/wiki/Matrix_multiplication)