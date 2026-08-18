# Day 7: Scope & Functional Helpers

Today, we will learn about variable visibility (Scope) and look at powerful, built-in functional programming helpers that make operating on collections cleaner and more concise.

---

## 1. Scope (Local vs. Global)

**Scope** determines where a variable is accessible in your program.
*   **Global Scope**: Variables defined outside of any function are global. They are accessible anywhere in the file.
*   **Local Scope**: Variables defined inside a function are local to that function. They cannot be accessed from outside.

```python
x = "global"  # Global variable

def my_func():
    y = "local"  # Local variable
    print(x)     # Accessible: prints "global"
    print(y)     # Accessible: prints "local"

my_func()
print(y)  # NameError: name 'y' is not defined (Outside scope!)
```

### Variable Shadowing
If you define a local variable with the same name as a global variable, Python "shadows" the global one, meaning the local definition takes precedence inside the function without modifying the global variable.

---

## 2. Lambda (Anonymous) Functions

A **lambda function** is a small, one-line anonymous function defined without a name using the `lambda` keyword.
*   **Syntax**: `lambda arguments: expression`

```python
# Regular function
def square(x):
    return x * x

# Equivalent Lambda function
square_lambda = lambda x: x * x

print(square(5))         # Output: 25
print(square_lambda(5))  # Output: 25
```

Lambdas are mostly used as quick arguments to other functions that take functions as inputs.

---

## 3. Functional Helpers

Python provides four key built-in functions to process iterables efficiently:

### `map(function, iterable)`
Applies a function to all items in an iterable.
```python
nums = [1, 2, 3]
squares = list(map(lambda x: x * x, nums))
print(squares)  # Output: [1, 4, 9]
```

### `filter(function, iterable)`
Filters elements of an iterable based on a function that returns `True` or `False`.
```python
nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4]
```

### `zip(*iterables)`
Aggregates elements from two or more iterables into tuples.
```python
names = ["Alice", "Bob"]
scores = [85, 90]
combined = list(zip(names, scores))
print(combined)  # Output: [('Alice', 85), ('Bob', 90)]
```

### `enumerate(iterable)`
Takes a collection and returns it as an enumerate object containing index-value pairs.
```python
fruits = ["apple", "banana"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
```

---

Now, proceed to the Day 7 Assignment: [day7_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week2_functions_io/day7_assignment.py).
