# Day 20 Assignment: Dataclasses & Slots Optimization
# ----------------------------------------------------------------------
# Instructions: Complete the EmployeeRecord dataclass and the Pixel slot class.
# Run 'python day20_test.py' to verify your solutions.

from dataclasses import dataclass, field

# ======================================================================
# Exercise 1: EmployeeRecord Dataclass
# ======================================================================
# Requirements:
# 1. Use the @dataclass decorator.
# 2. Define attributes:
#    - 'name' (str)
#    - 'base_salary' (float)
#    - 'bonus' (float, default value 0.0)
#    - 'tags' (list of strings, use default_factory=list to prevent mutability issues)
#    - 'total_pay' (float, exclude from __init__ constructor using field(init=False))
# 3. Implement '__post_init__(self)' to calculate 'total_pay' as base_salary + bonus.

# TODO: Implement EmployeeRecord dataclass


# ======================================================================
# Exercise 2: Memory-Optimized Pixel Class
# ======================================================================
class Pixel:
    """
    A memory-optimized representation of a screen pixel.
    Requirements:
    1. Define '__slots__' containing exactly: "x", "y", and "color".
    2. Implement constructor taking 'x' (int), 'y' (int), and 'color' (str)
       and store them in attributes of the same names.
    """
    # TODO: Implement slots and constructor
    pass
