# Day 14: Iterables & Callables

Welcome to Day 14! Today we explore two key concepts that make Python classes feel dynamic: **Iterators** and **Callables**.

We will cover:
1. **The Iterator Protocol (`__iter__` & `__next__`)**
2. **Callable Objects (`__call__`)**

---

## 1. The Iterator Protocol

When you run a `for element in my_object:` loop, Python does this under the hood:
1. Calls `iterator = iter(my_object)`, which lookups the `__iter__` method to get an iterator.
2. Continually calls `next(iterator)` to fetch the next element (looks up `__next__`).
3. Stops the loop when `next()` raises a `StopIteration` exception.

### Implementing a custom Iterator
Let's build a custom Countdown timer class:

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        # An object that implements __next__ is an iterator.
        # Often, a class returns itself as its own iterator.
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Tells the loop to stop
        
        val = self.current
        self.current -= 1
        return val
```

Usage:
```python
for num in Countdown(3):
    print(num)
# Output:
# 3
# 2
# 1
```

---

## 2. Callable Objects (`__call__`)

Have you ever wanted to treat an object instance as if it were a function? 
For example: `my_object(arg1, arg2)`.

To do this, implement the `__call__(self, *args, **kwargs)` method in your class. This is excellent for creating stateful function objects or helpers.

### Example: A stateful multiplier
```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor
```

Usage:
```python
triple = Multiplier(3)

# We call the object like a function!
print(triple(10))  # Output: 30
print(triple(5))   # Output: 15
```

This is a clean way to hold configuration state without needing global variables or complex closures.

---
Let's head to [day14_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week3_dunder_methods/day14_assignment.py) to implement an iterative Fibonacci generator and callable function cache!
