# Day 1 Assignment: Class, Object, and the Constructor
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by filling in the blanks.
# Do not change the class or method names. You can run 'python day1_test.py'
# to check your solutions.

# ======================================================================
# Exercise 1: Laptop Class
# ======================================================================
# Task: Create a class named 'Laptop' whose constructor (__init__) 
# accepts three attributes: 'brand' (string), 'model' (string), and 'ram' (integer).
# Store these in instance attributes of the same names.

class Laptop:
    # TODO: Implement the constructor (__init__) here
    def __init__(self, brand, model, ram):
        self.brand = brand
        self.model = model
        self.ram = ram


# ======================================================================
# Exercise 2: Book Class
# ======================================================================
# Task: Complete the 'Book' class. 
# 1. The constructor should accept 'title' (string), 'author' (string), and 'pages' (integer).
# 2. Implement an instance method named 'is_long' that returns True if the book
#    has more than 300 pages, and False otherwise.

class Book:
    def __init__(self, title, author, pages):
        # TODO: Initialize instance attributes
        self.title = title
        self.author = author
        self.pages = pages
        

    def is_long(self):
        # TODO: Return True if pages > 300, else False
        if self.pages > 300:
            return True
        else:
            return False

# ======================================================================
# Exercise 3: CartItem Class
# ======================================================================
# Task: Complete the 'CartItem' class.
# 1. The constructor should accept 'name' (string), 'price' (float), and 'quantity' (integer).
# 2. Implement an instance method named 'get_total_price' that calculates and
#    returns the total price of the items (price * quantity).

class CartItem:
    # TODO: Implement constructor and get_total_price method
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price*self.quantity
