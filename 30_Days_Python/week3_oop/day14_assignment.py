# Day 14 Assignment: Special (Dunder) Methods
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by filling in the blanks.
# Do not change the class or method names. You can run 'python day14_test.py'
# to check your solutions.

# ======================================================================
# Exercise 1: Custom Book Class with Dunder Hooks
# ======================================================================
# Task: Complete the class 'Book' by implementing special dunder methods.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # 1. Implement '__str__'
    #    Return format: "'<title>' by <author>"
    #    Example: 'The Hobbit' by J.R.R. Tolkien
    def __str__(self):
        # TODO: Implement string representation
        pass

    # 2. Implement '__repr__'
    #    Return format: "Book(title='<title>', author='<author>', pages=<pages>)"
    #    Example: Book(title='The Hobbit', author='J.R.R. Tolkien', pages=310)
    def __repr__(self):
        # TODO: Implement debugging representation
        pass

    # 3. Implement '__eq__'
    #    Compare two Book objects. Return True if BOTH 'title' and 'author' match.
    #    Otherwise, return False. Protect against non-Book comparisons.
    def __eq__(self, other):
        # TODO: Implement equality checking
        pass

    # 4. Implement '__add__'
    #    Allow adding pages (int) to a Book using the '+' operator.
    #    It should return a NEW Book instance with the same title and author,
    #    but with its pages set to: (original pages) + (integer pages).
    #    If 'other' is not an integer, return 'NotImplemented'.
    def __add__(self, other):
        # TODO: Implement pages addition
        pass
