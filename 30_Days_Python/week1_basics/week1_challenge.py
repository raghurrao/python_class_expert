# Week 1 Challenge: CLI Text Analyzer & Advanced Calculator
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by implementing the functions.
# You can run 'python week1_challenge_test.py' to verify your solutions.

# ======================================================================
# Task 1: Text Metrics Analyzer
# ======================================================================
# Implement the function 'analyze_text' that takes a string of text and returns
# a dictionary containing metrics about the text:
# 1. 'char_count': The total number of characters in the text (including spaces and punctuation).
# 2. 'word_count': The total number of words. Words are separated by whitespace.
# 3. 'sentence_count': The total number of sentences. A sentence is defined as ending with
#    a period ('.'), exclamation mark ('!'), or question mark ('?').
#    Hint: Count the occurrences of '.', '!', and '?' in the text.
# 4. 'unique_word_count': The total number of unique words (case-insensitive).
#    E.g. "Apple apple" has 1 unique word ('apple'). Make sure to remove punctuation
#    ('.', ',', '!', '?') from words before counting unique ones.
#
# Example input: "Hello world! Hello Python."
# Expected return:
# {
#     'char_count': 26,
#     'word_count': 4,
#     'sentence_count': 2,
#     'unique_word_count': 3
# }

def analyze_text(text):
    # TODO: Implement the metrics calculations and return the dictionary
    pass


# ======================================================================
# Task 2: Advanced Operations Calculator
# ======================================================================
# Implement the function 'calculate' that takes:
# - 'num1' (float or int)
# - 'num2' (float or int)
# - 'operation' (string: '+', '-', '*', '/', '//', '%', '**')
#
# Rules:
# 1. Perform the math operation: num1 <operation> num2.
# 2. If 'operation' is division ('/'), floor division ('//'), or modulo ('%'),
#    and num2 is 0, return the string: "Error: Division by zero"
# 3. If the operation is not one of the supported operators listed above,
#    return the string: "Error: Invalid operator"
# 4. Otherwise, return the numeric result.

def calculate(num1, num2, operation):
    # TODO: Implement the calculator operations and return the output
    pass
