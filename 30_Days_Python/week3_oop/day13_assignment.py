# Day 13 Assignment: Inheritance & Polymorphism
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by filling in the blanks.
# Do not change the class or method names. You can run 'python day13_test.py'
# to check your solutions.

# ======================================================================
# Exercise 1: Vehicle, Car, and ElectricCar Hierarchy
# ======================================================================
# Task: Create a three-level inheritance hierarchy of Vehicle, Car, and ElectricCar.

# 1. Base Class: 'Vehicle'
#    - Constructor takes 'make' (str) and 'model' (str). Save in attributes of same name.
#    - Implement instance method 'describe()' that returns the string:
#      "Vehicle: <make> <model>"
class Vehicle:
    # TODO: Implement constructor and describe method
    pass


# 2. Subclass: 'Car' (inherits from Vehicle)
#    - Constructor takes 'make' (str), 'model' (str), and 'num_doors' (int).
#      Use super() to initialize 'make' and 'model'. Save 'num_doors' as instance attribute.
#    - Override 'describe()' to return the string:
#      "Car: <make> <model> with <num_doors> doors"
class Car(Vehicle):
    # TODO: Implement constructor and override describe
    pass


# 3. Subclass: 'ElectricCar' (inherits from Car)
#    - Constructor takes 'make' (str), 'model' (str), 'num_doors' (int), and 'battery_capacity' (int).
#      Use super() to initialize parent attributes. Save 'battery_capacity' as instance attribute.
#    - Override 'describe()' to return the string:
#      "Electric Car: <make> <model> with <num_doors> doors and <battery_capacity>kWh battery"
class ElectricCar(Car):
    # TODO: Implement constructor and override describe
    pass
