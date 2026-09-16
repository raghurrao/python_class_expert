# Day 2: Array Manipulation & Attributes

Welcome to Day 2! Today we focus on manipulating existing arrays: changing their shapes, flattening them, stacking them together, and splitting them. These skills are essential when preparing data features for machine learning models.

---

## 1. Core Concepts & Operations

### Array Attributes
Recall the properties of an array:
* `ndim`: Number of dimensions (axes).
* `shape`: Tuple of array dimensions.
* `size`: Total number of elements.
* `dtype`: Data type of elements.

### Reshaping Arrays
Reshaping changes the shape of an array without changing its data. The total number of elements must remain constant.
```python
import numpy as np

arr = np.arange(12)  # [0, 1, 2, ..., 11], size 12
grid = arr.reshape(3, 4)  # Reshaped to 3 rows, 4 columns
```

**Using `-1` in reshape:**
If you specify `-1` for one of the dimensions, NumPy automatically calculates the exact size of that dimension based on the total elements.
```python
grid = arr.reshape(2, -1)  # Automatically becomes (2, 6)
```

### Flattening Arrays
To convert a multi-dimensional array to a 1D array:
* `flatten()`: Returns a **copy** of the array. Modifying it does not affect the original array.
* `ravel()`: Returns a **view** (if possible). Modifying it will modify the original array.

```python
matrix = np.array([[1, 2], [3, 4]])
flat = matrix.flatten()  # [1, 2, 3, 4]
```

### Stacking and Joining Arrays
You often need to combine different feature columns or data sources:
* `np.concatenate((arr1, arr2), axis)`: Joins a sequence of arrays along an existing axis.
* `np.vstack((arr1, arr2))`: Stacks arrays vertically (row-wise).
* `np.hstack((arr1, arr2))`: Stacks arrays horizontally (column-wise).
* `np.stack((arr1, arr2), axis)`: Joins arrays along a *new* axis.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

v_stacked = np.vstack((a, b))
# Output:
# [[1, 2, 3],
#  [4, 5, 6]]

h_stacked = np.hstack((a, b))
# Output:
# [1, 2, 3, 4, 5, 6]
```

### Splitting Arrays
* `np.split(arr, sections, axis)`: Splits an array into multiple sub-arrays.
* `np.vsplit(arr, sections)`: Splits vertically.
* `np.hsplit(arr, sections)`: Splits horizontally.
