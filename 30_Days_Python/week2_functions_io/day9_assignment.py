# Day 9 Assignment: Error & Exception Handling
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by filling in the blanks.
# Do not change the function/class names. You can run 'python day9_test.py'
# to check your solutions.

# ======================================================================
# Exercise 1: Safe Division
# ======================================================================
# Task: Complete the function 'safe_divide' that performs division (a / b).
# Use a try-except block to handle:
# 1. ZeroDivisionError: If b is 0, return string "Error: Division by zero"
# 2. TypeError: If parameters are not numbers, return string "Error: Invalid types"
#
# If no errors occur, return the result of a / b.

def safe_divide(a, b):
    # TODO: Implement the division and exception handling
    pass


# ======================================================================
# Exercise 2: Read Number from File
# ======================================================================
# Task: Complete the function 'read_number_file' that:
# 1. Opens the file at 'filepath' and reads its content.
# 2. Converts the trimmed contents to an integer and returns it.
#
# Handle these exceptions specifically:
# - FileNotFoundError: Return the string "Error: File not found"
# - ValueError: Return the string "Error: Invalid number format"

def read_number_file(filepath):
    # TODO: Implement try-except for file reading and parsing
    pass


# ======================================================================
# Exercise 3: Custom Age Exception
# ======================================================================
# Task: Complete the custom exception 'InvalidAgeError' and the function
# 'validate_age'.
# 1. Define 'InvalidAgeError' as a subclass of Exception.
# 2. Implement 'validate_age(age)' to check if age is between 0 and 120 (inclusive).
# 3. If age is not in that range, raise InvalidAgeError with the message:
#    "Age must be between 0 and 120"
# 4. Otherwise, return the age.

# TODO: Define InvalidAgeError exception class here
class InvalidAgeError(Exception):
    pass

def validate_age(age):
    # TODO: Raise InvalidAgeError if age is invalid, else return age
    pass
