# Day 1: Introduction to Pytest & Test-Driven Foundations

Welcome to Day 1 of your Pytest Mastery course! Today, we will lay down the foundations of unit testing and learn how to run your very first tests using **pytest**.

---

## 1. Why Do We Test?
Automated testing is the practice of writing code that checks if your application code works correctly. 
* **Prevent Regressions**: Ensure new changes don't break existing features.
* **Documentation**: Tests serve as live, executable documentation of how your functions behave.
* **Design Aid**: Writing tests forces you to design clean, modular, and decoupled code.

---

## 2. Unittest vs. Pytest
Python comes with a built-in testing library called `unittest`. However, it inherits heavy Java-like OOP boilerplate. 

Here is a side-by-side comparison:

### Standard `unittest` (Boilerplate-heavy)
```python
import unittest
from my_module import add

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
```

### Modern `pytest` (Clean and Pythonic)
```python
from my_module import add

def test_add():
    assert add(1, 2) == 3
```

**Key Pytest advantages:**
1. **No boilerplate**: You write simple, standard python functions starting with `test_`.
2. **Simple assertions**: No need to memorize `self.assertEqual`, `self.assertTrue`, `self.assertRaises`, etc. You use the standard Python `assert` keyword.
3. **Advanced failure reports**: Pytest dynamically rewrites assertions under the hood to show you exactly what variables had what values during a failure.

---

## 3. Pytest Naming Conventions
For pytest to automatically discover your tests in a workspace, you **must** follow these naming rules:

1. **Test Files**: Must start with `test_` (e.g. `test_math.py`) or end with `_test.py` (e.g. `math_test.py`).
2. **Test Classes (Optional)**: Must start with `Test` (e.g. `class TestCalculator`). Note that these classes should not have an `__init__` constructor.
3. **Test Functions**: Must start with `test_` (e.g. `def test_addition()`).

---

## 4. Writing Assertions
In pytest, you check conditions using `assert <expression>`. If the expression evaluates to `False`, the test fails.

```python
def test_lists():
    list_a = [1, 2, 3]
    assert 2 in list_a  # Passes
    assert len(list_a) == 3  # Passes
```

### Testing for Exceptions
If you expect a function to raise an exception under certain inputs, you use `pytest.raises` as a context manager:

```python
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```
This test passes because a `ZeroDivisionError` was raised inside the `with` block. If the block finishes *without* raising that exception, the test fails.

---

## 5. Running Pytest Commands
You run pytest from your shell/terminal inside your project directory:

* Run all discovered tests in the directory:
  ```bash
  pytest
  ```
* Run tests inside a specific file:
  ```bash
  pytest test_math.py
  ```
* Run a single specific test function inside a file:
  ```bash
  pytest test_math.py::test_add
  ```
* Verbose mode (shows detailed progress and test names):
  ```bash
  pytest -v
  ```
* Stop on first failure:
  ```bash
  pytest -x
  ```
