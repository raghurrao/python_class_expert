# Day 5 Assignment: Pythonic Getters & Setters with Properties
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below. Do not change the class or method names.
# Run 'python day5_test.py' to verify your solutions.

# ======================================================================
# Exercise 1: Circle Properties (Read/Write & Read-Only)
# ======================================================================
# Task: Complete the 'Circle' class.
# 1. Constructor should take 'radius' (float) and store it in an internal attribute '_radius'.
# 2. Implement 'radius' as a property (getter and setter). The setter must raise a
#    ValueError if the value is negative.
# 3. Implement 'diameter' as a read-only property (no setter) that returns radius * 2.
# 4. Implement 'area' as a read-only property (no setter) that returns 3.14159 * radius^2.

class Circle:
    def __init__(self, radius):
        # TODO: Initialize _radius via property setter (so it gets validated)
        pass

    # TODO: Implement getter & setter for 'radius'

    # TODO: Implement read-only 'diameter'

    # TODO: Implement read-only 'area'


# ======================================================================
# Exercise 2: Temperature Converter (Dual-sync Properties)
# ======================================================================
# Task: Create a 'Temperature' class.
# 1. Constructor should take a 'celsius' (float) and store it in '_celsius'.
# 2. Implement 'celsius' as a property (getter and setter).
# 3. Implement 'fahrenheit' as a property (getter and setter).
#    - Reading fahrenheit should compute: celsius * 1.8 + 32
#    - Writing fahrenheit should convert the value to Celsius and update '_celsius'.
#      Formula to Celsius: (fahrenheit - 32) / 1.8

class Temperature:
    # TODO: Implement constructor and property getters/setters for 'celsius' and 'fahrenheit'
    pass
