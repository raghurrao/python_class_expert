# Day 2: Variables, Operators & Basic Data Types

In Python, we store data in variables. Unlike some languages (like Java or C++), Python is dynamically typed—you don't need to declare what type of data a variable holds before using it. Python automatically figures it out.

---

## 1. Core Data Types

Python has several built-in basic data types:
*   **Integer (`int`)**: Whole numbers, positive or negative. E.g., `count = 10`, `temp = -5`
*   **Float (`float`)**: Decimal numbers. E.g., `price = 19.99`, `pi = 3.14159`
*   **String (`str`)**: Text enclosed in single, double, or triple quotes. E.g., `name = "Alice"`, `multiline = """Line 1\nLine 2"""`
*   **Boolean (`bool`)**: Can only be `True` or `False`. E.g., `is_active = True`, `has_passed = False`

### Checking Types
You can check the type of any object using the built-in `type()` function:
```python
x = 5.0
print(type(x))  # Output: <class 'float'>
```

---

## 2. Type Casting (Conversion)

Sometimes you need to convert a value from one type to another. This is called type casting:
*   `int(value)`: Converts value to an integer. (e.g. `int("10") -> 10`, `int(5.7) -> 5`)
*   `float(value)`: Converts value to a float. (e.g. `float(5) -> 5.0`)
*   `str(value)`: Converts value to a string. (e.g. `str(100) -> "100"`)
*   `bool(value)`: Converts value to boolean. In Python, empty sequences (`""`, `[]`), zero (`0`, `0.0`), and `None` are `False`. Almost everything else is `True`.

---

## 3. Basic Operators

Python uses standard symbols for mathematical and logical operations:

### Arithmetic Operators
*   `+` (Addition): `5 + 3 -> 8`
*   `-` (Subtraction): `5 - 3 -> 2`
*   `*` (Multiplication): `5 * 3 -> 15`
*   `/` (Division): `5 / 2 -> 2.5` (always returns a float!)
*   `//` (Floor Division): `5 // 2 -> 2` (divides and rounds down to nearest whole number)
*   `%` (Modulo / Remainder): `5 % 2 -> 1`
*   `**` (Exponentiation / Power): `2 ** 3 -> 8` (2 to the power of 3)

### Comparison Operators
These return boolean values (`True`/`False`):
*   `==` (Equal to): `5 == 5 -> True`
*   `!=` (Not equal to): `5 != 5 -> False`
*   `>` (Greater than), `<` (Less than)
*   `>=` (Greater or equal), `<=` (Less or equal)

---

## 4. F-Strings (Formatted Strings)

Formatted string literals (f-strings) let you embed expressions inside string literals using curly braces `{}`. This is the modern, Pythonic way to format strings.

```python
name = "Bob"
age = 25
# Put an 'f' before the opening quote:
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting) # Output: Hello, my name is Bob and I am 25 years old.
```

Inside the curly braces, you can run calculations, format decimals, or call methods:
```python
price = 49.953
# Format float to 2 decimal places:
print(f"Price is ${price:.2f}")  # Output: Price is $49.95
```

---

Now, proceed to the Day 2 Assignment: [day2_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week1_basics/day2_assignment.py).
