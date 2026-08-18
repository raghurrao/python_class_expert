# Day 12: Operator Overloading

Welcome to Day 12! Today we learn how to make custom objects work with Python's mathematical operators (`+`, `-`, `*`) and comparisons (`<`, `>`, `<=`, `>=`). This is called **Operator Overloading**.

By implementing specific dunder methods, your objects can interact with operators natively.

We will cover:
1. **Mathematical Overloading (`__add__`, `__sub__`)**
2. **Comparison Overloading (`__lt__`, `__gt__`)**
3. **Reflected/Right-Hand Operators (`__radd__`)**

---

## 1. Mathematical Overloading

If you build a class representing a `Vector`, it makes natural sense to add two vectors together using the `+` symbol:

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    # Overloading the + operator
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)
```

Now we can write:
```python
v1 = Vector(2, 4)
v2 = Vector(1, 3)
v3 = v1 + v2
print(v3)  # Output: Vector(3, 7)
```

---

## 2. Comparison Overloading

Python lets you overload comparison operations. You only need to define a few (like `<` and `==`), and Python can automatically infer the others (like `>` or `!=`) in many contexts, although it is best to be explicit.

*   `__lt__(self, other)`: Less than (`<`)
*   `__le__(self, other)`: Less than or equal (`<=`)
*   `__gt__(self, other)`: Greater than (`>`)
*   `__ge__(self, other)`: Greater than or equal (`>=`)

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # Compare based on score
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.score < other.score
```

Now we can sort students directly using Python's built-in `sorted()` function!
```python
alice = Student("Alice", 90)
bob = Student("Bob", 85)
print(alice > bob)  # Output: True (Python infers > from __lt__)
```

---

## 3. Reflected/Right-Hand Operators

What happens when you add an integer to our `Vector` class: `v1 + 5`? 
If we want `5 + v1` to work, the integer `5` doesn't know how to add a `Vector`. Python handles this by looking for `__radd__` (reflected add) on the right-hand object:

```python
class Vector:
    # ...
    def __add__(self, other):
        # Handle Vector + scalar (int/float)
        if isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        # Handle Vector + Vector
        elif isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    # Reflected add: called when: integer + Vector
    def __radd__(self, other):
        # Addition is commutative, so we can redirect to __add__
        return self.__add__(other)
```

Now:
```python
v = Vector(1, 2)
print(v + 10)  # Output: Vector(11, 12)  (triggers __add__)
print(10 + v)  # Output: Vector(11, 12)  (triggers __radd__)
```

---
Let's go to [day12_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week3_dunder_methods/day12_assignment.py) to build a custom currency converter!
