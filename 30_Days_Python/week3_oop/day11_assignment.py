# Day 11 Assignment: Classes & Object Basics
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by filling in the blanks.
# Do not change the class or method names. You can run 'python day11_test.py'
# to check your solutions.

# ======================================================================
# Exercise 1: Laptop Class
# ======================================================================
# Task: Create a class named 'Laptop'.
# 1. Its constructor should accept 'brand' (str), 'model' (str), and 'ram' (int).
#    Store these in instance attributes of the same name.
# 2. Implement an instance method named 'upgrade_ram' that takes an 'additional_ram'
#    integer value and adds it to the laptop's existing 'ram' attribute.

class Laptop:
    # TODO: Implement the constructor and upgrade_ram method
    pass


# ======================================================================
# Exercise 2: BankAccount Class
# ======================================================================
# Task: Complete the class 'BankAccount'.
# 1. The constructor should accept 'owner' (str) and 'balance' (float, default value of 0.0).
# 2. Implement an instance method 'deposit' that takes 'amount' (float), adds it
#    to 'balance', and returns the new balance.
# 3. Implement an instance method 'withdraw' that takes 'amount' (float).
#    - If balance is greater than or equal to amount, subtract amount from balance and return the new balance.
#    - Otherwise, do not modify balance and return string "Insufficient funds".

class BankAccount:
    # TODO: Implement constructor, deposit, and withdraw methods
    pass
