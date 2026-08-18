# Day 15: Context Managers (with blocks)

Welcome to Day 15! Today we look at Python's resource manager: the `with` statement. 

You have likely used context managers to safely open files:
```python
with open("file.txt", "r") as f:
    content = f.read()
# The file is automatically closed here, even if errors occur!
```

To create your own context manager, you implement the **Context Manager Protocol**: `__enter__` and `__exit__`.

We will cover:
1. **The Context Manager Protocol (`__enter__` & `__exit__`)**
2. **Handling Exceptions inside `__exit__`**

---

## 1. The Context Manager Protocol

A context manager is a class that implements two methods:

*   **`__enter__(self)`**: Executes at the start of the `with` block. It sets up the resource and returns the object we bind to the variable after the `as` keyword (if any).
*   **`__exit__(self, exc_type, exc_val, exc_tb)`**: Executes at the end of the `with` block. It handles clean-up (like closing a file or database connection).

```python
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"Connecting to database {self.db_name}...")
        return self  # This is what binds to the variable after 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name}...")
        # Connection clean-up happens here!
```

Usage:
```python
with DatabaseConnection("production_db") as db:
    print("Performing SQL queries...")
# Output:
# Connecting to database production_db...
# Performing SQL queries...
# Closing connection to production_db...
```

---

## 2. Handling Exceptions inside `__exit__`

The `__exit__` method accepts three arguments describing any exception raised *inside* the `with` block:
*   `exc_type`: The exception class (e.g., `ValueError`).
*   `exc_val`: The exception object (e.g., `ValueError("invalid parameter")`).
*   `exc_tb`: The traceback object.

If no exception occurred, all three will be `None`.

### Controlling Exception Propagation
*   **Suppress the error**: If `__exit__` returns **`True`**, Python swallows the exception and execution continues normally after the `with` block.
*   **Propagate the error**: If `__exit__` returns **`False`** (or `None`), Python allows the exception to propagate and crash the program (unless caught by an outer try/catch).

```python
class SuppressErrors:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Caught and suppressed: {exc_val}")
            return True  # returning True suppresses the exception!
        return False
```

Usage:
```python
with SuppressErrors():
    raise ZeroDivisionError("Cannot divide by zero!")
print("This line still runs!") 
# Output:
# Caught and suppressed: Cannot divide by zero!
# This line still runs!
```

---
Let's head to [day15_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week3_dunder_methods/day15_assignment.py) to build an HTML tag builder and transactions manager!
