# Day 1 Assignment: Writing Pytest Tests
# -----------------------------------------------------------------
# In this assignment, you will write test cases for the functions in day1_functions.py.
# 
# Instructions:
# 1. Import 'pytest' and the functions you want to test from 'day1_functions'.
# 2. Write the test functions following the instructions in the docstrings.
# 3. Do not change the test function names, as the verification script checks for them.
# -----------------------------------------------------------------

import pytest
from day1_functions import add, divide, get_average

# ==========================================
# Task 1: Testing Addition
# ==========================================

def test_add_positive_numbers():
    """
    Task: Assert that add(a, b) correctly adds two positive numbers.
    Example: add(2, 3) should equal 5.
    """
    # Write your code here (replace 'pass' with your assertion):
    pass

def test_add_negative_numbers():
    """
    Task: Assert that add(a, b) correctly adds two negative numbers.
    Example: add(-1, -4) should equal -5.
    """
    # Write your code here:
    pass


# ==========================================
# Task 2: Testing Division
# ==========================================

def test_divide_normal():
    """
    Task: Assert that divide(a, b) correctly divides normal numbers.
    Example: divide(10, 2) should equal 5.0.
    """
    # Write your code here:
    pass

def test_divide_by_zero():
    """
    Task: Assert that divide(a, b) raises a ZeroDivisionError when dividing by 0.
    Hint: Use 'with pytest.raises(ZeroDivisionError):'
    """
    # Write your code here:
    pass


# ==========================================
# Task 3: Testing List Averages
# ==========================================

def test_get_average_normal():
    """
    Task: Assert that get_average(numbers) returns correct average for a valid list of numbers.
    Example: get_average([1, 2, 3, 4]) should equal 2.5.
    """
    # Write your code here:
    pass

def test_get_average_empty():
    """
    Task: Assert that get_average(numbers) raises a ValueError when the list is empty.
    Hint: Use 'with pytest.raises(ValueError):'
    """
    # Write your code here:
    pass
