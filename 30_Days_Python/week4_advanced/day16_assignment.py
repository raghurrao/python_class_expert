# Day 16 Assignment: List Comprehensions & Advanced Iterators
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by filling in the blanks.
# Do not change the class or function names. You can run 'python day16_test.py'
# to check your solutions.

# ======================================================================
# Exercise 1: Squared Odd Numbers
# ======================================================================
# Task: Complete the function 'get_squared_odds' using a list comprehension.
# It takes a list of integers 'numbers' and returns a new list containing the
# squares of only the odd numbers in the list.
#
# Example: get_squared_odds([1, 2, 3, 4, 5]) -> [1, 9, 25]

def get_squared_odds(numbers):
    # TODO: Implement using a list comprehension and return
    pass


# ======================================================================
# Exercise 2: Dictionary Inverter
# ======================================================================
# Task: Complete the function 'invert_dictionary' using a dictionary comprehension.
# It takes a dictionary 'd' and returns a new dictionary where the keys are
# the values of 'd', and the values are the keys of 'd'.
# (Assume all values in 'd' are unique and hashable).
#
# Example: invert_dictionary({'a': 1, 'b': 2}) -> {1: 'a', 2: 'b'}

def invert_dictionary(d):
    # TODO: Implement using a dictionary comprehension and return
    pass


# ======================================================================
# Exercise 3: Countdown Custom Iterator
# ======================================================================
# Task: Complete the class 'Countdown' which acts as a custom iterator.
# 1. Constructor should take a starting integer 'start'.
# 2. Iteration should countdown from 'start' down to 1.
# 3. Upon reaching below 1, it must raise a 'StopIteration' exception.
#
# Example: list(Countdown(3)) -> [3, 2, 1]

class Countdown:
    def __init__(self, start):
        self.start = start
        # TODO: Initialize tracking attributes
        pass

    def __iter__(self):
        # TODO: Return the iterator object (self)
        pass

    def __next__(self):
        # TODO: Return next count or raise StopIteration
        pass
