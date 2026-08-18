# Day 20: Unit Testing & Best Practices

Writing code is only half the battle. Verifying that it works correctly and continues to work as you add features is critical. Today, we will study **Unit Testing** using Python's built-in **`unittest`** library.

---

## 1. What is Unit Testing?

A **Unit Test** is a small script that verifies the correctness of a specific, isolated "unit" of code (such as a single function or method). 
*   **Why test?** Tests prevent regression (breaking old features when adding new code), document how code is expected to behave, and force you to write cleaner, more modular code.

---

## 2. Using the `unittest` Library

Python's built-in `unittest` module is modelled after Java's JUnit. To write tests, you create a class that inherits from `unittest.TestCase`.

```python
import unittest

# The function we want to test
def double(x):
    return x * 2

# The test class
class TestDoubleFunction(unittest.TestCase):
    
    def test_double_positive(self):
        # Assert methods check if outputs match expectations
        self.assertEqual(double(3), 6)
        
    def test_double_negative(self):
        self.assertEqual(double(-2), -4)

# Run tests
if __name__ == '__main__':
    unittest.main()
```

### Key Assert Methods
*   `self.assertEqual(a, b)`: Checks if `a == b`.
*   `self.assertNotEqual(a, b)`: Checks if `a != b`.
*   `self.assertTrue(x)`: Checks if `x` is `True`.
*   `self.assertFalse(x)`: Checks if `x` is `False`.
*   `self.assertIn(item, container)`: Checks if `item in container`.
*   `self.assertRaises(ErrorType)`: Verifies that a block of code raises a specific exception.
    ```python
    with self.assertRaises(ValueError):
        int("not_a_number")
    ```

---

Now, proceed to the Day 20 Assignment: [day20_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week4_advanced/day20_assignment.py).
