# Day 4 Assignment: Encapsulation & Access Modifiers
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below. Do not change the class or method names.
# Run 'python day4_test.py' to verify your solutions.

# ======================================================================
# Exercise 1: Protected GPA with Validation
# ======================================================================
# Task: Complete the 'Student' class.
# 1. Constructor should take 'name' (string) and 'gpa' (float).
# 2. Store 'name' in a public attribute and 'gpa' in a protected attribute '_gpa'.
# 3. Implement 'get_gpa(self)' to return the current GPA.
# 4. Implement 'set_gpa(self, value)' to update the GPA. It must raise a ValueError
#    if the value is not between 0.0 and 4.0 (inclusive).

class Student:
    def __init__(self, name, gpa):
        # TODO: Initialize name and _gpa
        pass

    def get_gpa(self):
        # TODO: Return _gpa
        pass

    def set_gpa(self, value):
        # TODO: Validate and update _gpa, or raise ValueError
        pass


# ======================================================================
# Exercise 2: SecureKey with Name Mangling
# ======================================================================
# Task: Create a 'SecureKey' class.
# 1. Constructor should take a 'secret' (string) and store it in a private
#    instance attribute '__secret'.
# 2. Implement 'verify_secret(self, input_str)' that returns True if 'input_str'
#    matches the private '__secret', and False otherwise.

class SecureKey:
    # TODO: Implement __init__ with private __secret, and verify_secret method
    pass
