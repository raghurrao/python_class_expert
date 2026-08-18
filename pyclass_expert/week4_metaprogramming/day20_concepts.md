# Day 20: Dataclasses & Slots Optimization

Welcome to Day 20! Today we explore modern utilities that make writing classes faster and optimizing their memory footprints incredibly simple.

We will cover:
1. **The `@dataclass` Decorator**
2. **Dataclass Customizations (frozen, field, `__post_init__`)**
3. **Memory Optimization with `__slots__`**

---

## 1. The `@dataclass` Decorator

Introduced in Python 3.7, the `@dataclass` decorator automatically generates boilerplate methods like `__init__`, `__repr__`, `__eq__`, and type annotations:

```python
from dataclasses import dataclass

@dataclass
class User:
    username: str
    email: str
    age: int = 18  # Default value
```

Under the hood, this generates a constructor, a nice representation, and standard comparison checks:
```python
u = User("alice", "alice@ex.com")
print(u)  # Output: User(username='alice', email='alice@ex.com', age=18)
```

---

## 2. Advanced Dataclasses

### Immutability with `frozen=True`
If you want to create a read-only object that is also hashable, freeze it:
```python
@dataclass(frozen=True)
class Coordinate:
    x: float
    y: float
```

### Dynamic Defaults with `field(default_factory=...)`
Never use mutable default arguments like `list` or `dict` directly (e.g. `items: list = []`). Instead, use `field(default_factory=list)` to create a new list for each instance:

```python
from dataclasses import dataclass, field

@dataclass
class ShoppingCart:
    # Generates a new list instance for each shopping cart created
    items: list = field(default_factory=list)
```

### The Post-Initialization Hook: `__post_init__`
If you need to perform calculations after the auto-generated `__init__` constructor completes, write a `__post_init__(self)` method:

```python
@dataclass
class InvoiceItem:
    name: str
    price: float
    quantity: int
    total: float = field(init=False)  # Exclude from generated __init__ constructor parameters

    def __post_init__(self):
        # Calculate total price after init arguments are set
        self.total = self.price * self.quantity
```

---

## 3. Memory Optimization with `__slots__`

By default, Python store instance attributes in a dictionary called `__dict__`. This dictionary allows you to dynamically attach new attributes to objects at runtime, but has significant memory overhead.

If you are creating millions of small coordinate or pixel objects, `__dict__` will consume gigabytes of RAM.

To optimize this, define `__slots__` as a tuple containing the exact attribute names. This tells Python to store attributes in a highly optimized, fixed-size array instead of a dictionary.

```python
class OptimizedPoint:
    __slots__ = ("x", "y")  # Only 'x' and 'y' are allowed

    def __init__(self, x, y):
        self.x = x
        self.y = y
```

### Benefits of `__slots__`
1.  **Massive Memory Savings**: Objects use up to 60-70% less memory.
2.  **Faster Lookups**: Accessing slot-based attributes is faster.
3.  **Strict Attribute Safety**: Prevents users from accidentally adding typos as new attributes (`pt.ys = 10` raises AttributeError).

---
Let's head to [day20_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week4_metaprogramming/day20_assignment.py) to write some optimized coordinate and frozen student records!
