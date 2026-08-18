# Day 18 Assignment: Decorators
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by filling in the blanks.
# Do not change the function names. You can run 'python day18_test.py'
# to check your solutions.

import functools

# ======================================================================
# Exercise 1: Execution Logger Decorator
# ======================================================================
# Task: Complete the decorator 'log_execution'.
# It should print: "[LOG] Executing <func_name>..." right before calling the function.
# Ensure that:
# 1. The wrapped function can accept any arbitrary arguments (*args, **kwargs).
# 2. The wrapped function returns the correct output of the decorated function.
# 3. Use @functools.wraps to preserve original function details.

def log_execution(func):
    # TODO: Implement logging decorator
    pass


# ======================================================================
# Exercise 2: Integer Arguments Validator Decorator
# ======================================================================
# Task: Complete the decorator 'validate_ints'.
# 1. It checks if ALL arguments (*args) passed to the decorated function are integers.
# 2. If any argument is not an int, raise a TypeError with message: "All arguments must be integers"
# 3. Otherwise, call the function and return its result.
# 4. Use @functools.wraps.

def validate_ints(func):
    # TODO: Implement validation decorator
    pass
