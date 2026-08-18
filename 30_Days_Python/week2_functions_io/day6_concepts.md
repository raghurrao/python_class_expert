# Day 6: Functions & Arguments

Functions are reusable blocks of code that perform specific tasks. Today, we dive deeper into Python functions, exploring various ways to define parameters, accept dynamic arguments, and return values.

---

## 1. Defining Functions & Return Values

To define a function, use the `def` keyword.
*   **Parameters**: The variable names in the function definition.
*   **Arguments**: The actual values passed to the function when calling it.

```python
def add(a, b):  # a and b are parameters
    return a + b  # Return sends a value back to the caller

result = add(5, 3)  # 5 and 3 are arguments
print(result)       # Output: 8
```

> [!NOTE]
> If a function doesn't have a `return` statement (or has an empty `return`), it implicitly returns `None`.

---

## 2. Argument Types

Python supports multiple types of arguments:

### Positional Arguments
Arguments passed in the correct positional order.
```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("dog", "Buddy")  # Output: I have a dog named Buddy.
```

### Keyword Arguments
Arguments passed by explicitly specifying the parameter name. Order does not matter.
```python
describe_pet(pet_name="Buddy", animal_type="dog")  # Same output!
```

### Default Parameters
You can provide default values for parameters. If the argument is omitted, the default is used.
```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Alice"))            # Output: Hello, Alice!
print(greet("Bob", "Good morning"))  # Output: Good morning, Bob!
```

> [!WARNING]
> Parameters with default values MUST be placed *after* parameters without default values. E.g., `def greet(message="Hello", name):` is a syntax error.

---

## 3. Variable-Length Arguments (`*args` and `**kwargs`)

Sometimes you don't know beforehand how many arguments will be passed to your function.

### `*args` (Arbitrary Positional Arguments)
Collects extra positional arguments into a **tuple**.
```python
def sum_all(*args):
    # args is a tuple of all positional arguments passed
    print(args)  # Output: (1, 2, 3, 4)
    return sum(args)

print(sum_all(1, 2, 3, 4))  # Output: 10
```

### `**kwargs` (Arbitrary Keyword Arguments)
Collects extra keyword arguments into a **dictionary**.
```python
def print_profile(**kwargs):
    # kwargs is a dictionary
    print(kwargs)  # Output: {'name': 'Alice', 'role': 'Admin'}

print_profile(name="Alice", role="Admin")
```

---

Now, proceed to the Day 6 Assignment: [day6_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week2_functions_io/day6_assignment.py).
