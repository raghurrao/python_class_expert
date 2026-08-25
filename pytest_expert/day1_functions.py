# Day 1: Target Functions
# These are the functions you need to test in test_day1_assignment.py.

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def divide(a, b):
    """Returns the division of a by b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def get_average(numbers):
    """
    Returns the average of numbers in a list.
    Raises ValueError if the list is empty.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)
