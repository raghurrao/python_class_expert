# Day 13: Container & Sequence Protocols

Welcome to Day 13! Today we look at how to build objects that behave exactly like lists, tuples, or dictionaries. This is called implementing the **Container** or **Sequence** protocol.

By writing just a few dunder methods, your custom objects will support indexing, slicing, length queries, item deletion, and the `in` membership operator.

We will cover:
1. **Length Query (`__len__`)**
2. **Indexing & Key Lookup (`__getitem__`, `__setitem__`, `__delitem__`)**
3. **Membership Check (`__contains__`)**

---

## 1. Length Query: `__len__`

To make your object return a size when passed to the built-in `len()` function, implement `__len__(self)`. It must return a non-negative integer.

```python
class Team:
    def __init__(self):
        self.members = []

    def __len__(self):
        return len(self.members)
```

---

## 2. Indexing: `__getitem__` & `__setitem__`

To read and write values using square bracket notation (`obj[key]`), implement these methods:

*   **`__getitem__(self, key)`**: Triggers on `value = obj[key]`.
*   **`__setitem__(self, key, value)`**: Triggers on `obj[key] = value`.
*   **`__delitem__(self, key)`**: Triggers on `del obj[key]`.

### Example: A custom dictionary-like Config class
```python
class CustomConfig:
    def __init__(self):
        self._data = {}

    def __getitem__(self, key):
        # We can validate or modify keys before returning
        return self._data[key.lower()]

    def __setitem__(self, key, value):
        self._data[key.lower()] = value

    def __delitem__(self, key):
        del self._data[key.lower()]
```

Usage:
```python
cfg = CustomConfig()
cfg["Theme"] = "Dark"  # Triggers __setitem__, stores as 'theme'
print(cfg["theme"])    # Triggers __getitem__, returns "Dark"
```

---

## 3. Membership Check: `__contains__`

To support the `in` operator (e.g. `"admin" in user_roles`), implement `__contains__(self, item)`. It should return a boolean value.

```python
class CustomConfig:
    # ...
    def __contains__(self, key):
        return key.lower() in self._data
```

Usage:
```python
cfg = CustomConfig()
cfg["Port"] = 8080
print("port" in cfg)  # Output: True
```

> [!TIP]
> If a class defines `__getitem__` but does **not** define `__contains__`, Python will fallback to performing a sequential lookup by trying indices `0, 1, 2, ...` until an `IndexError` is raised. However, defining `__contains__` explicitly is far more efficient (especially for dictionary-like hashes).

---
Let's proceed to [day13_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week3_dunder_methods/day13_assignment.py) to build a custom list-like Deck of Cards!
