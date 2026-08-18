# Day 2 Assignment: Variables, Operators & Basic Data Types
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by filling in the blanks.
# Do not change the function names. You can run 'python day2_test.py'
# to check your solutions.

# ======================================================================
# Exercise 1: Temperature Converter
# ======================================================================
# Task: Write a function 'fahrenheit_to_celsius' that accepts a temperature
# in Fahrenheit (float) and returns the temperature in Celsius (float).
# The formula is: C = (F - 32) * 5 / 9
# Make sure to round the final result to 2 decimal places.

def fahrenheit_to_celsius(f_temp):
    # TODO: Implement the calculation and return the rounded float
    pass


# ======================================================================
# Exercise 2: Compound Interest Calculator
# ======================================================================
# Task: Complete the function 'calculate_compound_interest' to compute the
# total accumulated value (A) of an investment using the formula:
# A = P * (1 + r/n) ** (n * t)
# Where:
#   P = principal amount (float)
#   r = annual interest rate (float, e.g. 0.05 for 5%)
#   t = time in years (integer)
#   n = number of times interest compounded per year (integer)
# Make sure to round the final result to 2 decimal places.

def calculate_compound_interest(principal, rate, time, n):
    # TODO: Implement the formula and return the rounded float value
    pass


# ======================================================================
# Exercise 3: Profile Card Formatting
# ======================================================================
# Task: Complete the function 'format_profile_card' that takes a user's
# name (str), birth_year (int), and email (str).
# 1. Calculate the user's age assuming the current year is 2026.
# 2. Return a formatted string exactly like this (replace with actual variables):
#
# === PROFILE CARD ===
# Name: John Doe
# Age: 30
# Email: john.doe@example.com
# ====================
#
# Note: Ensure there are no extra leading/trailing whitespace or newlines.

def format_profile_card(name, birth_year, email):
    # TODO: Calculate age and return the formatted profile card string
    pass
