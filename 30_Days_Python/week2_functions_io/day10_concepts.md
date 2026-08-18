# Day 10: Modules, Packages, and `pip`

As your application grows, keeping all code in a single file becomes unmanageable. Python provides **Modules** and **Packages** to organize code into reusable components, and **pip** to install third-party packages written by the community.

---

## 1. Modules & Import Styles

A **Module** is simply a Python file containing function definitions and statements. You can use code from one module in another using the `import` statement.

There are three common import styles:
```python
# 1. Importing the entire module
import math
print(math.sqrt(16))  # Output: 4.0

# 2. Importing specific items directly (no math. prefix needed)
from math import sqrt, pi
print(sqrt(9))  # Output: 3.0

# 3. Importing with an alias
import datetime as dt
print(dt.date.today())
```

---

## 2. Preventing Code Execution: `__name__ == '__main__'`

When Python imports a module, it runs all top-level statements in that file. If you write testing/runnable code at the bottom of a module file, it will execute automatically when imported by another file.

To prevent this, use the namespace check:
```python
def add(a, b):
    return a + b

# This block only runs if the script is executed directly, NOT if it is imported
if __name__ == '__main__':
    print("Testing add function:")
    print(add(2, 3))
```

---

## 3. Useful Standard Library Modules

Python comes with a battery of pre-built standard modules:
*   **`random`**: Random numbers, shuffling, choosing random elements.
    *   `random.randint(1, 10)`: Random integer between 1 and 10.
    *   `random.choice(sequence)`: Selects a random element from a list/tuple.
*   **`datetime`**: Working with dates and times.
    *   `datetime.datetime.now()`: Current local date and time.
*   **`math`**: Mathematical constants and functions (`sin`, `cos`, `log`, `sqrt`).

---

## 4. Packages and `pip`

A **Package** is a folder containing multiple Python modules.

`pip` is the package installer for Python. It allows you to download and install packages from PyPI (Python Package Index).
```powershell
# From your system command prompt/powershell:
pip install requests
```
Once installed, you can import them into your code just like built-in libraries:
```python
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
```

---

Now, proceed to the Day 10 Assignment: [day10_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week2_functions_io/day10_assignment.py).
