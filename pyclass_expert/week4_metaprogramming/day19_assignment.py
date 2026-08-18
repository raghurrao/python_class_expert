# Day 19 Assignment: Metaclasses & __init_subclass__
# ----------------------------------------------------------------------
# Instructions: Complete the UppercaseAttributesMeta metaclass and the
# ApiHandler route auto-registration system.
# Run 'python day19_test.py' to verify your solutions.

# ======================================================================
# Exercise 1: UppercaseAttributesMeta Metaclass
# ======================================================================
class UppercaseAttributesMeta(type):
    """
    A metaclass that automatically converts all public attributes to UPPERCASE.
    Requirements:
    1. Inherit from 'type'.
    2. Implement '__new__(mcs, name, bases, attrs)':
       - Create a new dictionary for modified attributes.
       - Iterate over 'attrs'. If a key is public (does not start with '_'),
         save it in uppercase (key.upper()) with the same value.
         Otherwise, save key and value unchanged.
       - Call super().__new__(mcs, name, bases, modified_attrs) and return the class.
    """
    # TODO: Implement UppercaseAttributesMeta


# ======================================================================
# Exercise 2: ApiHandler route auto-registration using __init_subclass__
# ======================================================================
class ApiHandler:
    """
    A base handler class that automatically registers routes of its subclasses.
    Requirements:
    1. Define class attribute 'routes' as an empty dictionary.
    2. Implement class method '__init_subclass__(cls, route=None, **kwargs)':
       - Call super().__init_subclass__(**kwargs).
       - If 'route' (str) is provided, store the subclass in 'ApiHandler.routes' dictionary
         under the key 'route'.
    """
    # TODO: Implement routes attribute and __init_subclass__ method
    pass
