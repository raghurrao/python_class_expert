# Day 8 Assignment: File Handling & Serialization
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by filling in the blanks.
# Do not change the function names. You can run 'python day8_test.py'
# to check your solutions.

import json

# ======================================================================
# Exercise 1: Write a Text File
# ======================================================================
# Task: Complete the function 'write_text_file' that takes:
# 1. 'filepath' (str) - the target path where the file should be written.
# 2. 'content' (str) - the string content to write.
#
# Use a context manager ('with open') to open the file in write mode and write
# the content to it.

def write_text_file(filepath, content):
    # TODO: Write content to filepath using context manager
    pass


# ======================================================================
# Exercise 2: Append to a File
# ======================================================================
# Task: Complete the function 'append_to_file' that takes:
# 1. 'filepath' (str) - the target path of the file.
# 2. 'content' (str) - the content string to append.
#
# Write the content string followed by a newline character ('\n') to the file
# using append mode, so subsequent calls append content on new lines.

def append_to_file(filepath, content):
    # TODO: Append content followed by a newline to filepath
    pass


# ======================================================================
# Exercise 3: Read and Parse JSON
# ======================================================================
# Task: Complete the function 'read_and_parse_json' that takes:
# 1. 'filepath' (str) - path to a JSON file.
#
# It should open the file in read mode, parse (deserialize) the JSON data,
# and return the resulting Python dictionary or list.

def read_and_parse_json(filepath):
    # TODO: Load JSON from file and return it
    pass
