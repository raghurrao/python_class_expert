# Day 6 Assignment: Functions & Arguments
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by filling in the blanks.
# Do not change the function names. You can run 'python day6_test.py'
# to check your solutions.

# ======================================================================
# Exercise 1: Product of All Arguments
# ======================================================================
# Task: Complete the function 'multiply_all' that accepts any number of
# numeric arguments (using *args) and returns their product.
# Rules:
# - If no arguments are passed, return 1.
# - Otherwise, multiply all arguments and return the result.
# Example: multiply_all(2, 3, 4) should return 24.

def multiply_all(*args):
    # TODO: Loop over args to calculate product and return
    pass


# ======================================================================
# Exercise 2: Sandwich Maker
# ======================================================================
# Task: Complete the function 'make_sandwich' that accepts:
# 1. 'bread_type' as a keyword argument with a default value of "White".
# 2. An arbitrary list of toppings (*toppings).
#
# It should return a string format as follows:
# - If toppings are specified: "<bread_type> sandwich with: topping1, topping2, ..."
# - If no toppings are specified: "<bread_type> sandwich with no toppings"
#
# Examples:
# - make_sandwich("Wheat", "Ham", "Cheese") -> "Wheat sandwich with: Ham, Cheese"
# - make_sandwich() -> "White sandwich with no toppings"

def make_sandwich(bread_type="White", *toppings):
    # TODO: Build and return the sandwich description string
    pass


# ======================================================================
# Exercise 3: User Profile Builder
# ======================================================================
# Task: Complete the function 'build_user_profile' that takes:
# 1. 'first' (str) - first name
# 2. 'last' (str) - last name
# 3. An arbitrary set of keyword arguments (**kwargs) representing extra profile details.
#
# The function should return a dictionary containing all key-value details,
# with the first name stored under the key 'first_name', and last name under 'last_name'.
#
# Example: build_user_profile("Jane", "Smith", age=28, city="Boston") should return:
# {
#     'first_name': 'Jane',
#     'last_name': 'Smith',
#     'age': 28,
#     'city': 'Boston'
# }

def build_user_profile(first, last, **kwargs):
    # TODO: Build and return the dictionary profile
    pass
