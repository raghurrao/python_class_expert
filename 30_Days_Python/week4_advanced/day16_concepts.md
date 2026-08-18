# Day 16: List Comprehensions & Advanced Iterators

Today we transition to Python's advanced syntax, starting with **Comprehensions** (elegant ways to generate lists, sets, and dictionaries in a single line) and the underlying **Iterator Protocol**.

---

## 1. List, Set, and Dictionary Comprehensions

Comprehensions provide a concise way to create lists (and other collections) from existing iterables.

### List Comprehensions
*   **Syntax**: `[expression for item in iterable if condition]`

```python
# Traditional approach
squares = []
for x in range(5):
    squares.append(x * x)

# Comprehension approach
squares_comp = [x * x for x in range(5)]
print(squares_comp)  # Output: [0, 1, 4, 9, 16]

# Comprehension with condition
even_squares = [x * x for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]
```

### Set Comprehensions
Uses curly braces `{}`. Automatically removes duplicates.
```python
names = ["alice", "bob", "alice"]
unique_caps = {name.title() for name in names}
print(unique_caps)  # Output: {'Alice', 'Bob'}
```

### Dictionary Comprehensions
Uses curly braces `{}` and a key-value format `key: value`.
```python
names = ["Alice", "Bob"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # Output: {'Alice': 5, 'Bob': 3}
```

---

## 2. The Iterator Protocol (`__iter__` and `__next__`)

In Python, loops like `for item in collection` work because of the **Iterator Protocol**. An object can be iterated over if it defines two methods:
1.  **`__iter__(self)`**: Returns the iterator object itself (usually `self`).
2.  **`__next__(self)`**: Returns the next item. If there are no more items, it must raise a **`StopIteration`** exception.

```python
class CountUpTo:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

# Usage
counter = CountUpTo(3)
for num in counter:
    print(num)  # Output: 1, 2, 3
```

---

Now, proceed to the Day 16 Assignment: [day16_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week4_advanced/day16_assignment.py).
