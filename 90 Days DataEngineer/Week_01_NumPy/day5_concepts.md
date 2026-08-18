# Day 5: Boolean Indexing & Filtering

Welcome to Day 5! Today we focus on conditional filtering of arrays. In data analysis, you often need to select data points matching complex criteria. Boolean masking allows you to do this in parallel, running at full hardware speed without dynamic loop checking.

---

## 1. Core Concepts & Operations

### Generating Boolean Masks
Applying comparative operators (`>`, `<`, `==`, `!=`) to ndarrays produces element-wise Boolean masks of the same shape.
```python
import numpy as np

arr = np.array([10, 20, 30, 40])
mask = arr >= 25  # [False, False, True, True]
```

### Filtering with Masks
When you index an array with a Boolean mask, NumPy returns a **1D array** containing only the elements where the mask evaluates to `True`.
```python
filtered = arr[mask]  # [30, 40]
```

### Combining Conditions
To combine multiple conditions, you **must** use bitwise logical operators and wrap each condition in **parentheses**:
* `&`: logical AND
* `|`: logical OR
* `~`: logical NOT

```python
# Select values between 15 and 35
combined_mask = (arr > 15) & (arr < 35)
print(arr[combined_mask])  # [20, 30]
```

### Conditional Assignment
You can modify specific elements in-place using boolean masks:
```python
# Replace all values less than 25 with 0
arr[arr < 25] = 0  # arr becomes [0, 0, 30, 40]
```

### `np.where`
The `np.where(condition, x, y)` function returns elements from `x` where the condition is True, and `y` where it is False. This is a vectorized ternary operator (`if-else`).
```python
# If element > 25, replace with 1, else replace with -1
transformed = np.where(arr > 25, 1, -1)
```
If only the condition is provided, `np.where(condition)` returns the *indices* of elements that are True.
