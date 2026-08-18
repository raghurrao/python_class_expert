# Day 7 Assignment: Scope & Functional Helpers
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by filling in the blanks.
# Do not change the function names. You can run 'python day7_test.py'
# to check your solutions.

# ======================================================================
# Exercise 1: Square Even Numbers
# ======================================================================
# Task: Complete the function 'square_even_numbers' that accepts a list
# of integers 'numbers'.
# 1. Filter out only the even numbers.
# 2. Square each of those filtered numbers.
# 3. Return the final values as a list.
#
# Requirements: Use the built-in 'map' and 'filter' functions combined with
# lambda expressions (do not use loops or list comprehensions).

def square_even_numbers(numbers):
    # TODO: Implement using map(), filter(), and lambda functions
    pass


# ======================================================================
# Exercise 2: Combine Names and Ages
# ======================================================================
# Task: Complete the function 'combine_names_and_ages' that accepts two
# parallel lists: 'names' (list of strings) and 'ages' (list of integers).
# Use 'zip()' to iterate over both lists simultaneously and return a list
# of dictionaries where each dictionary contains two keys:
# - 'name': the corresponding name string.
# - 'age': the corresponding age integer.
#
# Example: combine_names_and_ages(["Alice", "Bob"], [25, 30]) should return:
# [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]

def combine_names_and_ages(names, ages):
    # TODO: Zip inputs, build list of dictionaries, and return
    pass


# ======================================================================
# Exercise 3: Indexed Words
# ======================================================================
# Task: Complete the function 'index_words' that takes a list of strings
# 'words' and returns a new list of strings formatted as:
# "<index>: <word>"
#
# Requirements: Use 'enumerate()' to get the index and value (do not track
# counter variables manually).
#
# Example: index_words(["apple", "banana"]) should return ["0: apple", "1: banana"]

def index_words(words):
    # TODO: Use enumerate() to format the strings and return a list
    pass
