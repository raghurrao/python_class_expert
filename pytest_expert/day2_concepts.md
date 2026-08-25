# Day 2: Assertion Magic & Raising Exceptions

Today we will dive deeper into pytest's assertions and learn how to assert that exceptions are raised correctly, capture exception details, and verify error messages.

---

## 1. How Pytest Rewrites Assertions
In standard Python, `assert x == y` simply raises an `AssertionError` with no detail. 
In pytest, the test runner interceptor parses the Abstract Syntax Tree (AST) before running the file. When an assertion fails, pytest prints a rich diff:
* For **strings**: Shows where they differ.
* For **lists/tuples**: Shows extra/missing items.
* For **dicts**: Shows key/value differences.
* For **sets**: Shows symmetric differences.

```python
def test_dict():
    a = {"name": "Alice", "role": "admin"}
    b = {"name": "Alice", "role": "user"}
    assert a == b  # Pytest will print: Omitting 1 identical key, Differing value: 'role': 'admin' != 'user'
```

---

## 2. Advanced Exception Assertions
Yesterday, you learned the basic usage of `pytest.raises`:
```python
with pytest.raises(ValueError):
    int("invalid_number")
```

Today, we will learn how to verify **the exact error message** inside the exception.

### Method A: Inspecting the Exception Object (Using `excinfo`)
You can store the exception in a variable using the `as` keyword:
```python
with pytest.raises(ValueError) as excinfo:
    int("invalid_number")

# excinfo.value contains the actual exception object raised
assert "invalid literal for int()" in str(excinfo.value)
```

### Method B: Using the `match` Parameter (Regex matching)
Pytest allows a `match` parameter directly in `pytest.raises`. This checks if the string representation of the exception matches a regular expression:
```python
# This will pass if ValueError is raised AND the message contains "invalid literal"
with pytest.raises(ValueError, match="invalid literal"):
    int("invalid_number")
```
> [!IMPORTANT]
> The `match` argument uses regular expression searching (`re.search`). If your exception message contains special regex characters like `(`, `)`, `[`, `]`, `?`, etc., you must escape them using `re.escape()` or use `excinfo`.

---

## 3. Testing Type Errors and Key Errors
When testing dictionary accesses that are missing, Python raises `KeyError`. Note that `str(excinfo.value)` for a `KeyError` contains the string representation of the key (which has quotes in Python).
```python
with pytest.raises(KeyError) as excinfo:
    data = {}
    x = data["username"]

# For KeyError, the value string is usually the quoted key representation: "'username'"
assert "username" in str(excinfo.value)
```
