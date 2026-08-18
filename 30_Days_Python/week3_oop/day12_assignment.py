# Day 12 Assignment: Encapsulation & Class/Static Methods
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by filling in the blanks.
# Do not change the class or method names. You can run 'python day12_test.py'
# to check your solutions.

# ======================================================================
# Exercise 1: Employee Class with Private Attributes & Property
# ======================================================================
# Task: Complete the class 'Employee'.
# 1. The constructor should accept 'name' (str) and 'salary' (float).
#    Store the salary in a private instance attribute named '__salary'.
# 2. Implement a getter property named 'salary' that returns the private '__salary'.
# 3. Implement a setter property named 'salary' that validates:
#    - If value is negative, raise a ValueError with message: "Salary cannot be negative"
#    - Otherwise, set the private '__salary' to the new value.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        # TODO: Initialize private salary attribute
        pass

    # TODO: Implement getter property for salary
    
    # TODO: Implement setter property for salary
    pass


# ======================================================================
# Exercise 2: Temperature Class with Custom Constructors
# ======================================================================
# Task: Complete the class 'Temperature'.
# 1. The constructor accepts 'celsius' (float) and stores it in a protected
#    attribute '_celsius'.
# 2. Implement getter and setter properties for 'fahrenheit'.
#    - Formula: F = C * 1.8 + 32
#    - Formula: C = (F - 32) / 1.8
# 3. Implement a class method 'from_fahrenheit' that accepts a fahrenheit value (float),
#    calculates the Celsius value, and returns a new Temperature instance.
# 4. Implement a static method 'celsius_to_kelvin' that accepts a celsius value (float)
#    and returns the Kelvin temperature (Celsius + 273.15).

class Temperature:
    def __init__(self, celsius):
        # TODO: Set protected _celsius
        pass

    # TODO: Implement fahrenheit property getter & setter

    # TODO: Implement classmethod from_fahrenheit

    # TODO: Implement staticmethod celsius_to_kelvin
    pass
