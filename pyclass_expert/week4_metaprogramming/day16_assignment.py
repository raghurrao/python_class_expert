# Day 16 Assignment: Attribute Hooking (__getattr__ vs. __getattribute__)
# ----------------------------------------------------------------------
# Instructions: Complete the classes to customize attribute access.
# Run 'python day16_test.py' to verify your solutions.

# ======================================================================
# Exercise 1: JSONWrapper (Dynamic Attribute Access)
# ======================================================================
class JSONWrapper:
    """
    Wraps a dictionary so its keys can be accessed as attributes.
    Requirements:
    1. Constructor accepts a dictionary 'data' and stores it in 'self.data'.
    2. Implement '__getattr__(self, name)':
       - If 'name' exists in 'self.data' dictionary, return it.
       - Otherwise, raise AttributeError.
    """
    def __init__(self, data):
        # TODO: Initialize dictionary
        pass

    def __getattr__(self, name):
        # TODO: Lookup attribute in self.data dictionary
        pass


# ======================================================================
# Exercise 2: StrictObject (Attribute Write Validation)
# ======================================================================
class StrictObject:
    """
    A class that strictly validates attribute values upon assignment.
    Requirements:
    1. Implement '__setattr__(self, name, value)':
       - If 'name' starts with an underscore (e.g., '_gpa' or '__secret'), allow
         the assignment without validation (using super().__setattr__).
       - Otherwise, if 'name' is public, validate that 'value' is numeric (int or float).
         If not, raise TypeError("Value must be numeric").
       - If validation passes, set the attribute using super().__setattr__.
    """
    def __setattr__(self, name, value):
        # TODO: Implement strict validation on public attributes
        pass
