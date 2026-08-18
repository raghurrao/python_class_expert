# Day 4: NumPy Broadcasting Rules

Welcome to Day 4! Today we explore **Broadcasting**, one of the most powerful and unique features of NumPy. Broadcasting defines how NumPy treats arrays with different shapes during arithmetic operations.

---

## 1. Core Concepts & Operations

### The Broadcasting Rules
Subject to certain constraints, the smaller array is "broadcast" across the larger array so that they have compatible shapes. Broadcasting occurs without making unnecessary copies of data, keeping it memory-efficient.

When operating on two arrays, NumPy compares their shapes element-wise, starting from the **rightmost (trailing) dimensions** and working left. Two dimensions are compatible if:
1. They are **equal**, or
2. One of them is **1**.

If these conditions are not met, a `ValueError: operands could not be broadcast together` is thrown.

### Visualizing Compatibility

#### Example 1: Matrix and Vector
* Array A: Shape `(3, 4)`
* Array B: Shape `(4,)` (effectively treated as `(1, 4)`)
Comparing right-to-left:
* Last dimension: A is 4, B is 4. (Compatible - equal)
* Next dimension: A is 3, B is 1 (implicit). (Compatible - B is 1)
*Resulting Shape:* `(3, 4)`. Array B is stretched vertically to match A.

#### Example 2: Incompatible Shapes
* Array A: Shape `(3, 4)`
* Array B: Shape `(3,)` (effectively treated as `(1, 3)`)
Comparing right-to-left:
* Last dimension: A is 4, B is 3. **Incompatible!** They are not equal, and neither is 1.

#### Example 3: Reshaping to Force Broadcasting
If you want to broadcast a vector of shape `(3,)` across a matrix of shape `(3, 4)` along the rows, you must explicitly expand its dimensions to shape `(3, 1)`.
* Array A: Shape `(3, 4)`
* Array B: Shape `(3, 1)`
Comparing right-to-left:
* Last dimension: A is 4, B is 1. (Compatible - B is 1)
* Next dimension: A is 3, B is 3. (Compatible - equal)
*Resulting Shape:* `(3, 4)`. Array B is stretched horizontally.

```python
import numpy as np

matrix = np.ones((3, 4))
vector = np.array([10, 20, 30])  # Shape (3,)

# This will fail: matrix + vector
# Instead, add a dimension:
vector_col = vector[:, np.newaxis]  # Shape (3, 1) or vector.reshape(3, 1)
result = matrix + vector_col
```
`np.newaxis` or `None` splits a dimension, creating a new axis of length 1.
