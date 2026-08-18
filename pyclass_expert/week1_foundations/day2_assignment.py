# Day 2 Assignment: Attribute Scoping (Instance vs. Class Attributes)
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below. Do not change the class or method names.
# Run 'python day2_test.py' to verify your solutions.

# ======================================================================
# Exercise 1: Employee & Raises
# ======================================================================
# Task: Create an 'Employee' class.
# 1. Add a class attribute 'raise_amount' set to 1.05 (5% raise).
# 2. The constructor should accept 'name' (string) and 'salary' (float).
# 3. Implement an instance method 'apply_raise' that multiplies the employee's 
#    current salary by the employee's 'raise_amount' and updates the salary.
#    Note: Access 'raise_amount' using 'self.raise_amount' (not 'Employee.raise_amount')
#    so that specific employee instances can have custom raise rates.

class Employee:
    # TODO: Implement raise_amount, constructor, and apply_raise method
    raise_amount = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def apply_raise(self):
        self.salary = self.salary * self.raise_amount


# ======================================================================
# Exercise 2: Product Catalog Tracker
# ======================================================================
# Task: Create a 'Product' class that tracks inventory metrics.
# 1. Add a class attribute 'total_products' initialized to 0.
# 2. Add a class attribute 'product_catalog' initialized to an empty list.
# 3. The constructor should take a single argument 'name' (string) and store it 
#    in an instance attribute 'name'.
# 4. Each time a new Product is created:
#    - Increment the 'total_products' count by 1.
#    - Append the product name to the 'product_catalog' list.

class Product:
    # TODO: Implement total_products, product_catalog, and constructor
    total_products = 0
    product_catalog = []

    def __init__(self,name):
        self.name = name
        Product.total_products =self.total_products + 1
        Product.product_catalog.append(self.name)


# ======================================================================
# Exercise 3: Global Configuration Manager
# ======================================================================
# Task: Complete the 'Configuration' class.
# 1. Define a class attribute dictionary named 'settings' with keys:
#    "theme": "light" and "language": "en"
# 2. Implement an instance method 'update_setting(self, key, value)' that updates
#    the setting *globally*. This means changing the dictionary value in the class namespace
#    so that all existing and future instances of 'Configuration' observe the change.

class Configuration:
    # TODO: Define settings dictionary and update_setting method
    settings = {"theme":"light","language":"en"}

    def update_setting(self, key,value):
        Configuration.settings[key] = value

        