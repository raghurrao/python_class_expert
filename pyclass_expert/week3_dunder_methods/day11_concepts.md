# Day 11: Object Presentation and Hashing

Welcome to Week 3! This week is all about **Magic Methods** (also called **Dunder Methods**, short for *Double Underscore*). These are special methods prefixed and suffixed by `__` that let you hook your classes into Python's built-in syntax.

Today we cover how classes represent themselves as strings and how to make custom classes usable as dictionary keys or set elements.

We will cover:
1. **`__str__` vs. `__repr__`**
2. **Object Equality (`__eq__`) & Hashability (`__hash__`)**

---

## 1. `__str__` vs. `__repr__`

When you print an object or inspect it in the terminal, Python looks for these two methods:

*   **`__str__`**: Returns a user-friendly, readable string representation. Triggers when you call `print(obj)` or `str(obj)`.
*   **`__repr__`**: Returns an unambiguous developer-facing representation, ideally looking like valid Python code to recreate the object. Triggers when you inspect the object in a shell, or call `repr(obj)`.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # Human-friendly
        return f"{self.name} ({self.age} years old)"

    def __repr__(self):
        # Developer-facing
        return f"Person(name={self.name!r}, age={self.age})"
```

Usage:
```python
p = Person("Alice", 25)
print(str(p))   # Output: Alice (25 years old)   <-- (__str__)
print(repr(p))  # Output: Person(name='Alice', age=25) <-- (__repr__)
```

---

## 2. Object Equality (`__eq__`) & Hashability (`__hash__`)

By default, Python compares objects using their memory addresses. If you create two separate points at coordinates (1, 2), they will compare as unequal:

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # Output: False
```

### Implementing `__eq__`
To compare based on attribute values, implement `__eq__`:

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y
```

Now `p1 == p2` will evaluate to `True`.

### Implementing `__hash__`
However, once you implement `__eq__`, Python makes the object **unhashable**, meaning you cannot store it in a `set` or use it as a key in a `dict`:

```python
# set([p1, p2])  # ❌ TypeError: unhashable type: 'Point'
```

To make it hashable again, implement `__hash__`. An object's hash **must not change** over its lifetime, so hashable classes should represent immutable values:

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        # Hash a tuple containing the unique, immutable attributes
        return hash((self.x, self.y))
```

Now we can store points in sets and check for membership based on value:
```python
point_set = {Point(1, 2), Point(1, 2)}
print(len(point_set))  # Output: 1 (Duplicates are filtered correctly!)
```

---
Let's head to [day11_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week3_dunder_methods/day11_assignment.py) to implement these dunders!
