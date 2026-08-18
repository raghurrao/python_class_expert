# Day 5 Assignment: Dictionaries & Sets
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by filling in the blanks.
# Do not change the function names. You can run 'python day5_test.py'
# to check your solutions.

# ======================================================================
# Exercise 1: Word Counter
# ======================================================================
# Task: Complete the function 'count_words' that takes a string of text.
# 1. Clean the text by replacing commas (',') and periods ('.') with empty strings.
# 2. Convert all text to lowercase.
# 3. Split the text into individual words by whitespace.
# 4. Count the occurrences of each word and store them in a dictionary.
# 5. Return the counts dictionary.
#
# E.g. count_words("Apple, apple. Orange") should return {'apple': 2, 'orange': 1}

def count_words(text):
    # TODO: Clean, lowercase, split, and count into a dictionary
    pass


# ======================================================================
# Exercise 2: Common & Unique Sets
# ======================================================================
# Task: Complete the function 'find_common_and_unique' that accepts two sets: 'set_a' and 'set_b'.
# It should return a dictionary with exactly two keys:
# - 'common': A set containing elements present in both sets.
# - 'only_a': A set containing elements present only in 'set_a' and not 'set_b'.

def find_common_and_unique(set_a, set_b):
    # TODO: Implement set operations and return dict
    pass


# ======================================================================
# Exercise 3: Safe Grade Lookup
# ======================================================================
# Task: Complete the function 'get_student_grade' that accepts a dictionary 'grades_dict'
# (where keys are student names and values are their letter grades) and a 'student_name' (str).
# 1. Return the student's grade if they are in the dictionary.
# 2. If the student is not in the dictionary, return the string: "Student not found"
# Note: Use a dictionary method to handle this lookup safely without raising a KeyError.

def get_student_grade(grades_dict, student_name):
    # TODO: Use a safe dictionary lookup method and return the value
    pass
