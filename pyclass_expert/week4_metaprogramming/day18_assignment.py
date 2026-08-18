# Day 18 Assignment: Object Creation Lifecycle (__new__ vs. __init__)
# ----------------------------------------------------------------------
# Instructions: Complete the LoggerPool (Singleton) and UppercaseString classes.
# Run 'python day18_test.py' to verify your solutions.

# ======================================================================
# Exercise 1: LoggerPool (Singleton Pattern)
# ======================================================================
class LoggerPool:
    """
    A singleton logging coordinator.
    Requirements:
    1. Define class attribute '_instance = None'.
    2. Implement '__new__(cls, *args, **kwargs)' to ensure only one instance is created.
    3. Implement '__init__(self)' to initialize an empty list 'self.logs' ONLY ONCE.
       - Use an internal flag (e.g. self._initialized) to check if already configured.
    4. Implement 'log(self, message)' to append 'message' to 'self.logs'.
    """
    # TODO: Implement LoggerPool


# ======================================================================
# Exercise 2: UppercaseString (Subclassing Immutable Types)
# ======================================================================
class UppercaseString(str):
    """
    A custom string subclass that automatically capitalizes all inputs at creation.
    Requirements:
    1. Inherit from 'str'.
    2. Implement '__new__(cls, value)':
       - Capitalize 'value' (value.upper()).
       - Call super().__new__(cls, value_upper) to allocate the immutable string.
       - Return the resulting string.
    """
    # TODO: Implement UppercaseString
    pass
