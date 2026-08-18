# Day 9: Error & Exception Handling

Even well-written programs encounter errors. Rather than allowing your program to crash abruptly, Python provides a mechanism called **Exception Handling** to catch and recover from errors gracefully.

---

## 1. Try, Except, Else, and Finally

We handle exceptions using the `try-except` structure:
*   **`try`**: The block of code that might raise an error.
*   **`except`**: Runs if an error occurs in the `try` block. You can specify which error type to catch.
*   **`else`**: Runs only if the `try` block runs *without* raising any exceptions.
*   **`finally`**: Runs *always*, whether an exception occurred or not. Useful for resource cleanups (like closing a database connection).

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That was not a valid integer!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Division result: {result}")
finally:
    print("Operation completed.")
```

---

## 2. Raising Exceptions

You can intentionally trigger an exception in your code using the `raise` keyword. This is useful for validating parameters or enforcing custom business rules.

```python
def check_positive(number):
    if number <= 0:
        raise ValueError("Number must be strictly positive!")
    return number

# Usage
try:
    check_positive(-5)
except ValueError as e:
    print(f"Caught expected error: {e}")  # Output: Caught expected error: Number must be strictly positive!
```

---

## 3. Creating Custom Exceptions

For larger projects, standard Python exceptions might not describe your error precisely enough. You can define custom exceptions by creating a new class that inherits from the built-in `Exception` class.

```python
# Definition
class InsufficientFundsError(Exception):
    """Exception raised when a bank account withdrawal exceeds the balance."""
    pass

# Usage
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw ${amount} from balance of ${balance}.")
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
```

---

Now, proceed to the Day 9 Assignment: [day9_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week2_functions_io/day9_assignment.py).
