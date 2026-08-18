# Week 3 Challenge: Inventory Management System
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by implementing the classes.
# You can run 'python week3_challenge_test.py' to verify your solutions.

# ======================================================================
# Task 1: Product Base Class
# ======================================================================
# Create a base class named 'Product'.
# 1. Constructor takes 'product_id' (str), 'name' (str), and 'price' (float).
# 2. Encapsulate 'price' by saving it to a private attribute '__price'.
# 3. Create getter and setter properties for 'price'.
#    - The setter must raise a ValueError with message "Price must be positive" if value <= 0.
# 4. Implement a method 'get_details()' that returns:
#    "Product: <name> (ID: <product_id>) - $<price>"

class Product:
    # TODO: Implement constructor, private price, properties, and get_details
    pass


# ======================================================================
# Task 2: DigitalProduct Subclass
# ======================================================================
# Create a class named 'DigitalProduct' that inherits from Product.
# 1. Constructor takes 'product_id' (str), 'name' (str), 'price' (float), and
#    'file_size_mb' (float). Use super() to initialize parent attributes.
# 2. Save 'file_size_mb' as an instance attribute.
# 3. Override 'get_details()' to return:
#    "Digital Product: <name> (ID: <product_id>) - $<price> [File Size: <file_size_mb>MB]"

class DigitalProduct(Product):
    # TODO: Implement constructor and override get_details
    pass


# ======================================================================
# Task 3: Inventory Tracker
# ======================================================================
# Create a class named 'Inventory' to store products.
# 1. Constructor initializes an empty dictionary self.products (product_id -> product object).
# 2. Implement method 'add_product(product)': adds product object to self.products dictionary.
# 3. Implement method 'get_product(product_id)': returns product matching product_id.
#    If the ID is not found, return None.
# 4. Implement method 'remove_product(product_id)': removes product from dictionary.
#    If not found, do nothing.

class Inventory:
    # TODO: Implement constructor, add_product, get_product, and remove_product
    pass
