# Day 14: Special (Dunder) Methods

In Python, **Dunder** (Double Underline) or **Magic** methods are special, predefined methods that start and end with double underscores (e.g. `__init__`). They allow custom objects to interact with Python's built-in syntax (operators, printing, checking length, etc.).

---

## 1. Object Presentation: `__str__` vs. `__repr__`

These two methods customize how your object is converted to a string:
*   **`__str__`**: Returns a user-friendly, readable string. Used by `print()` and `str()`.
*   **`__repr__`**: Returns an unambiguous, developer-focused string that could ideally be used to recreate the object. Used by debuggers and when inspect objects in interactive terminals.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(3, 4)
print(str(p))   # Output: (3, 4) (Calls __str__)
print(repr(p))  # Output: Point(x=3, y=4) (Calls __repr__)
```

---

## 2. Equality Checks: `__eq__`

By default, Python compares objects by their memory address (using the `is` logic). To compare objects by their actual data values, override the `__eq__` method.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # Output: True (Without __eq__, this would be False!)
```

---

## 3. Operator Overloading: `__add__`, `__len__`, etc.

You can override arithmetic and comparison operators by implementing corresponding dunder methods:
*   `__add__(self, other)`: Overloads the `+` operator.
*   `__sub__(self, other)`: Overloads the `-` operator.
*   `__len__(self)`: Overloads the `len()` function. Must return an integer >= 0.

```python
class Box:
    def __init__(self, volume):
        self.volume = volume

    def __add__(self, other):
        if isinstance(other, Box):
            return Box(self.volume + other.volume)
        return NotImplemented

b1 = Box(10)
b2 = Box(20)
b3 = b1 + b2  # Calls b1.__add__(b2)
print(b3.volume)  # Output: 30
```

---

Now, proceed to the Day 14 Assignment: [day14_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week3_oop/day14_assignment.py).
