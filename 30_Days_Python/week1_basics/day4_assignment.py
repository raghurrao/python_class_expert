# Day 4 Assignment: Sequences (Lists & Tuples)
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by filling in the blanks.
# Do not change the function names. You can run 'python day4_test.py'
# to check your solutions.

# ======================================================================
# Exercise 1: First and Last Elements
# ======================================================================
# Task: Complete the function 'get_first_and_last' that accepts a sequence
# (like a list or tuple) and returns a tuple containing:
# 1. The first element of the sequence.
# 2. The last element of the sequence.
#
# If the sequence is empty, return (None, None).
# If the sequence contains only one item, that item is both first and last.

def get_first_and_last(sequence):
    # TODO: Check length of sequence and return tuple (first, last)
    pass


# ======================================================================
# Exercise 2: List Slicing Magic
# ======================================================================
# Task: Complete the function 'list_slicing_magic' that accepts a list 'lst'.
# Return a slice of the list containing every second element from index 1
# up to, but not including, index 7.
#
# Example: If input is [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Elements between index 1 and 7 are: [20, 30, 40, 50, 60, 70]
# Taking every second element starting at index 1: [20, 40, 60]

def list_slicing_magic(lst):
    # TODO: Return the sliced sublist
    pass


# ======================================================================
# Exercise 3: Manage Shopping List
# ======================================================================
# Task: Complete the function 'manage_shopping_list' which:
# 1. Appends 'item_to_add' to 'shopping_list'.
# 2. Removes 'item_to_remove' from 'shopping_list' if it exists in the list.
#    (Hint: Use the 'in' operator to check before calling list.remove() to avoid an error).
# 3. Sorts the list alphabetically.
# 4. Returns the modified list.

def manage_shopping_list(shopping_list, item_to_add, item_to_remove):
    # TODO: Add item, conditionally remove item, sort list, and return
    pass
