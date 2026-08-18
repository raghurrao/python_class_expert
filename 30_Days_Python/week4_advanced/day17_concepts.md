# Day 17: Generators & Context Managers

Today, we cover two advanced Python concepts focused on performance and resource safety: **Generators** (for lazy, memory-efficient data processing) and **Context Managers** (for resource management).

---

## 1. Generators & `yield`

A **Generator** is a special type of function that returns an iterator. Instead of returning a value and terminating (like `return`), a generator uses the **`yield`** keyword to pause execution and send a value back to the caller. When called again, it resumes exactly where it left off.

### Memory Efficiency
If you need to process 1 million numbers, creating a list `[0, 1, ..., 999999]` stores all 1 million numbers in RAM at once. A generator calculates each number one-by-one on demand (lazy evaluation), utilizing almost zero memory.

```python
# Generator function
def count_down(num):
    print("Starting countdown...")
    while num > 0:
        yield num
        num -= 1

# Creating generator object
counter = count_down(3)

# Accessing values
print(next(counter))  # Output: Starting countdown... \n 3
print(next(counter))  # Output: 2
```

---

## 2. Context Managers & `with` blocks

A **Context Manager** is an object that controls resource allocation and cleanup using the `with` statement. The protocol consists of two methods:
1.  **`__enter__(self)`**: Sets up the resource. Returns the target variable of the `as` clause.
2.  **`__exit__(self, exc_type, exc_val, exc_tb)`**: Handles cleanup (closing files, releasing locks). Runs even if exceptions occur in the block.

```python
class DatabaseConnection:
    def __enter__(self):
        print("Connecting to Database...")
        return "DB_CONNECTION_OBJECT"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing Database Connection...")
        # If we return True, any exceptions raised inside the with block are suppressed.

# Usage
with DatabaseConnection() as conn:
    print(f"Executing query on {conn}...")
# Output:
# Connecting to Database...
# Executing query on DB_CONNECTION_OBJECT...
# Closing Database Connection...
```

---

Now, proceed to the Day 17 Assignment: [day17_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week4_advanced/day17_assignment.py).
