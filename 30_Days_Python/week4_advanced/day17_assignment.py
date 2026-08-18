# Day 17 Assignment: Generators & Context Managers
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by filling in the blanks.
# Do not change the class or function names. You can run 'python day17_test.py'
# to check your solutions.

# ======================================================================
# Exercise 1: Fibonacci Generator
# ======================================================================
# Task: Write a generator function 'fibonacci' that yields Fibonacci numbers
# up to and including 'limit'.
#
# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Formula: F(n) = F(n-1) + F(n-2) with F(0)=0, F(1)=1.
#
# E.g. list(fibonacci(10)) -> [0, 1, 1, 2, 3, 5, 8]

def fibonacci(limit):
    # TODO: Implement generator using yield. Loop while current Fibonacci is <= limit
    pass


# ======================================================================
# Exercise 2: Temporary File Simulator Context Manager
# ======================================================================
# Task: Implement a class 'TemporaryFileMock' that acts as a context manager.
# 1. Constructor should take a 'filename' (str).
# 2. Add an instance attribute 'self.is_open' set to False initially.
# 3. In '__enter__':
#    - Set 'self.is_open' to True.
#    - Return the string "FILE_HANDLE:<filename>"
# 4. In '__exit__':
#    - Set 'self.is_open' to False.
#    - (Do not suppress any exceptions, i.e., return None or False).

class TemporaryFileMock:
    def __init__(self, filename):
        self.filename = filename
        # TODO: Initialize is_open flag
        pass

    def __enter__(self):
        # TODO: Mark is_open as True and return string handle
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Mark is_open as False
        pass
