# Day 11 Assignment: Object Presentation and Hashing
# ----------------------------------------------------------------------
# Instructions: Implement the dunder methods below.
# Run 'python day11_test.py' to verify your solutions.

# ======================================================================
# Exercise 1: Book Presentation Dunders
# ======================================================================
class Book:
    """
    Requirements:
    1. Constructor accepts 'title' (str) and 'author' (str).
    2. Implement '__str__(self)' returning: "'<title>' by <author>"
       Example: "'Hamlet' by William Shakespeare"
    3. Implement '__repr__(self)' returning: "Book(title='<title>', author='<author>')"
       Example: "Book(title='Hamlet', author='William Shakespeare')"
    """
    def __init__(self, title, author):
        # TODO: Initialize title and author
        pass

    def __str__(self):
        # TODO: Return user-friendly string
        pass

    def __repr__(self):
        # TODO: Return unambiguous developer representation
        pass


# ======================================================================
# Exercise 2: Equal & Hashable Colors
# ======================================================================
class Color:
    """
    Requirements:
    1. Constructor accepts RGB values: 'r' (int), 'g' (int), and 'b' (int).
    2. Implement '__eq__(self, other)' to compare two Color objects based on r, g, b.
       - Safely return NotImplemented if 'other' is not an instance of Color.
    3. Implement '__hash__(self)' to return the hash of the tuple (r, g, b)
       so that Color instances can be added to sets and keys in dicts.
    """
    def __init__(self, r, g, b):
        # TODO: Initialize values
        pass

    def __eq__(self, other):
        # TODO: Check equality
        pass

    def __hash__(self):
        # TODO: Return hash of color channels
        pass
