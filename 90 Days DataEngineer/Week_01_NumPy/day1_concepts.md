# Day 1: NumPy Array Basics, Slicing & Shapes

Welcome to Day 1! Today, we master **NumPy** (Numerical Python), the fundamental package for scientific computing in Python. It provides high-performance multidimensional arrays and tools to manipulate them efficiently.

---

## 1. Why NumPy?
In Python, lists are dynamic containers that hold pointers to objects. This flexibility comes with significant overhead:
* **Pointers:** Every element is a separate object with header overhead.
* **Cache Locality:** Python list items are scattered in memory, causing CPU cache misses.
* **Loops:** Modifying list values in loops is slow because of Python's dynamic typing.

**NumPy arrays (`ndarray`) solve this by:**
1. Storing data in **contiguous** blocks of memory.
2. Enforcing a **single data type (homogeneity)** per array, which allows compiled C code to run operations at hardware speeds.
3. Enabling **Vectorization**: performing operations on entire arrays at once without writing slow Python `for` loops.

---

## 2. Core Concepts & Operations

### Array Creation
You can create arrays from python lists or use built-in functions:
```python
import numpy as np

# 1D Array from list
arr_1d = np.array([1, 2, 3])

# 2D Array (Matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Handy initializers
zeros = np.zeros((3, 3))       # 3x3 matrix of zeros
ones = np.ones((2, 4))         # 2x4 matrix of ones
rng = np.arange(0, 10, 2)      # Array: [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5) # Array: [0.0, 0.25, 0.5, 0.75, 1.0]
```

### Shape and Reshaping
An array's shape determines its dimensions:
```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.shape) # Output: (2, 3) (2 rows, 3 columns)

# Reshaping changes dimensions without altering the data.
# The total number of elements must remain identical (2 * 3 = 6).
reshaped = matrix.reshape((3, 2))
# Output:
# [[1, 2],
#  [3, 4],
#  [5, 6]]
```

### Slicing and Filtering
Slicing in 2D follows the format: `array[row_slice, column_slice]`.
```python
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(data[0:2, 1:3])
# Output (Rows 0 & 1, Columns 1 & 2):
# [[20, 30],
#  [50, 60]]
```

**Boolean Masking (Filtering):**
By applying a conditional operator to an array, you get an array of Booleans. Passing this boolean "mask" back into the array filters out elements that evaluate to `False`.
```python
arr = np.array([10, 15, 20, 25])
mask = arr > 18 # [False, False, True, True]
filtered = arr[mask] # [20, 25]
```

### Broadcasting
Broadcasting is NumPy's ability to perform arithmetic operations on arrays of different shapes. The smaller array is "broadcast" across the larger one to make their shapes compatible.
Rules for dimension matching (checked right to left):
1. The dimensions are equal, OR
2. One of the dimensions is exactly 1.

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])  # Shape (2, 3)
row_vector = np.array([10, 20, 30])         # Shape (3,)

# The row vector is added to both rows of the matrix
result = matrix + row_vector
# Output:
# [[11, 22, 33],
#  [14, 25, 36]]
```

---

## 3. Reference Documentation
* [NumPy Quickstart Guide](https://numpy.org/doc/stable/user/quickstart.html)
* [Broadcasting Rules Explained](https://numpy.org/doc/stable/user/basics.broadcasting.html)
