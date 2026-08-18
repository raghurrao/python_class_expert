# Day 5: Dictionaries & Sets

Today, we cover two highly important unordered data structures in Python: **Dictionaries** (hash maps) and **Sets** (unique collections).

---

## 1. Dictionaries (Key-Value Pairs)

A **dictionary** is an unordered collection of items where each item is stored as a **key-value pair**. Keys must be unique and immutable (like strings, numbers, or tuples), while values can be of any data type.

### Syntax
```python
# Definition
student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Physics"]
}

# Accessing values
print(student["name"])  # Output: Alice
```

### Safe Lookups with `.get()`
If you try to access a key that doesn't exist using `student["grades"]`, Python will raise a `KeyError`. To avoid this, use the `.get()` method, which returns `None` (or a custom default value) if the key is missing:
```python
print(student.get("grades"))         # Output: None
print(student.get("grades", "N/A"))  # Output: N/A
```

### Modifying and Deleting
```python
student["age"] = 21           # Update value
student["graduated"] = False  # Add new key-value pair

del student["courses"]        # Delete key using 'del'
removed_val = student.pop("age")  # Removes key and returns its value
```

### Iteration
You can loop through dictionaries using `.keys()`, `.values()`, or `.items()`:
```python
for key, value in student.items():
    print(f"{key}: {value}")
```

---

## 2. Sets (Unique Collections)

A **set** is an unordered collection of unique elements. Sets are written with curly braces `{}` (just like dicts, but without colons).

```python
# Definition
numbers = {1, 2, 2, 3, 4}
print(numbers)  # Output: {1, 2, 3, 4} (Duplicates are automatically removed!)
```

> [!NOTE]
> To create an empty set, you must use `set()`. Using `{}` will create an empty dictionary!

### Adding and Removing Elements
```python
my_set = {1, 2}
my_set.add(3)
my_set.remove(2)  # Raises KeyError if not present
my_set.discard(5) # Safe: does not raise error if 5 is not present
```

### Set Operations
Sets are incredibly fast for checking membership (using the `in` keyword) and support mathematical operations:
```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union (all elements in either set)
print(set_a.union(set_b))         # Output: {1, 2, 3, 4, 5, 6}

# Intersection (elements in both sets)
print(set_a.intersection(set_b))  # Output: {3, 4}

# Difference (elements in set_a but not in set_b)
print(set_a.difference(set_b))    # Output: {1, 2}
```

---

Now, proceed to the Day 5 Assignment: [day5_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week1_basics/day5_assignment.py).
