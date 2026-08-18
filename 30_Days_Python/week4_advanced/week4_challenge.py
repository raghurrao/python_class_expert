# Week 4 Challenge & Capstone: Personal Finance Tracker CLI
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by implementing the classes and functions.
# You can run 'python week4_challenge_test.py' to verify your solutions.

import csv
import os

# ======================================================================
# Task 1: Transaction Class
# ======================================================================
# Create a class named 'Transaction'.
# 1. Constructor takes 'trans_id' (int), 'description' (str), 'amount' (float),
#    and 'category' (str).
# 2. Encapsulate 'amount' by saving to private instance attribute '__amount'.
# 3. Create getter and setter properties for 'amount'.
#    - Setter must raise a ValueError with message "Amount cannot be zero" if value == 0.
# 4. Implement '__repr__' returning:
#    "Transaction(id=<trans_id>, description='<description>', amount=<amount>, category='<category>')"

class Transaction:
    # TODO: Implement constructor, encapsulated amount, property, and repr
    pass


# ======================================================================
# Task 2: CSV Data Loader
# ======================================================================
# Implement the function 'load_transactions_from_csv' that takes 'filepath' (str).
# 1. Open the CSV file and read transactions.
#    Note: CSV files will have a header row: id,description,amount,category
# 2. Parse each row and create a 'Transaction' object.
#    Hint: Convert row['id'] to int, and row['amount'] to float.
# 3. Return a list of Transaction objects.
# 4. If the CSV file does not exist, catch FileNotFoundError and return [].

def load_transactions_from_csv(filepath):
    # TODO: Load CSV rows, instantiate Transactions, and return list
    pass


# ======================================================================
# Task 3: Currency Converter (using Comprehensions)
# ======================================================================
# Implement the function 'convert_currency' that takes:
# - 'transactions' (list of Transaction objects)
# - 'rate' (float)
#
# Return a NEW list of Transaction objects where each transaction's amount
# is converted (multiplied) by the rate.
# Requirements:
# 1. Use a list comprehension.
# 2. Keep transaction id, description, and category identical. Create new Transaction instances.

def convert_currency(transactions, rate):
    # TODO: Use list comprehension to return new list of Transactions
    pass


# ======================================================================
# Task 4: Category Summary Builder
# ======================================================================
# Implement the function 'get_category_summary' that takes a list of Transaction objects.
# 1. Calculate the total sum of amounts grouped by category.
# 2. Return a dictionary where keys are category names (strings) and values are the total
#    sum of transaction amounts in that category (floats).
#
# Example return: {'Food': 120.50, 'Utilities': 85.00}

def get_category_summary(transactions):
    # TODO: Sum transaction amounts grouped by category and return dictionary
    pass
