# Day 3: NumPy Vectorization & Math Operations

Welcome to Day 3! Today we examine NumPy's mathematical power. We will explore element-wise arithmetic, mathematical transformations (log, exponential, square root), trigonometric operations, and aggregations (sum, mean, min, max) using vectorized functions (ufuncs).

---

## 1. Core Concepts & Operations

### Universal Functions (ufuncs)
A ufunc is a function that operates on ndarrays in an element-by-element fashion. Unlike standard python functions applied to lists, ufuncs are written in highly optimized C and run extremely fast.

Common single-array math functions:
* `np.log(x)`: Natural logarithm (element-wise).
* `np.exp(x)`: Exponential ($e^x$).
* `np.sqrt(x)`: Square root.
* `np.abs(x)`: Absolute value.

Common double-array math functions:
* `np.add(x, y)` (or `x + y`)
* `np.multiply(x, y)` (or `x * y`)
* `np.power(x, y)` (or `x ** y`)

```python
import numpy as np

arr = np.array([1, 2, 3])
print(np.exp(arr)) # [2.718, 7.389, 20.085]
```

### Statistical Aggregations & Axes
Aggregations compress dimensions by calculating summary statistics across axes:
* **No axis specified:** Aggregates the entire array, returning a scalar.
* **`axis=0`:** Aggregates down the columns (collapsing rows). Shape shifts from (M, N) to (N,).
* **`axis=1`:** Aggregates across the rows (collapsing columns). Shape shifts from (M, N) to (M,).

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.sum(matrix))          # Output: 21 (overall sum)
print(np.sum(matrix, axis=0))  # Output: [5, 7, 9] (sum of each column)
print(np.sum(matrix, axis=1))  # Output: [6, 15] (sum of each row)
```

Common aggregation functions:
* `np.sum()`, `np.mean()`, `np.median()`, `np.std()`, `np.var()`.
* `np.min()`, `np.max()`.
* `np.argmin()`, `np.argmax()`: Returns the *indices* of the minimum/maximum values. Very useful for model predictions (e.g. classification output probabilities).
