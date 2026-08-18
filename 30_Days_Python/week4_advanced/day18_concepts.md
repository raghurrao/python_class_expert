# Day 18: Decorators

A **Decorator** is a design pattern in Python that allows you to modify or extend the behavior of a function or class without permanently changing its source code. Today, we learn the mechanics of decorators.

---

## 1. Functions as First-Class Citizens

In Python, functions are "first-class citizens." This means they can be passed around as arguments, returned from other functions, and assigned to variables, just like integers or strings.

### Closures
A **Closure** is a nested inner function that retains access to variables from its outer (enclosing) scope even after the outer function has finished executing.

```python
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier  # Returns the inner function

double = make_multiplier(2)
print(double(5))  # Output: 10
```

---

## 2. Basic Decorators

A decorator is a function that takes another function as an argument, defines a wrapper function that runs extra code, and returns the wrapper.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator  # Syntax sugar: equivalent to say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
```

---

## 3. Preserving Metadata: `functools.wraps`

When you wrap a function, the original function name and docstrings are overwritten by the wrapper's name. To copy this metadata back to the wrapped function, use `@functools.wraps` from the standard library.

```python
import functools

def log_decorator(func):
    @functools.wraps(func)  # Keeps original func name and docstring!
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper
```

---

Now, proceed to the Day 18 Assignment: [day18_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week4_advanced/day18_assignment.py).
