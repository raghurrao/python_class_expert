# Day 1 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day1_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week1_foundations.day1_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day1_assignment.py. Error: {e}")
    sys.exit(1)

passed_tests = 0
total_tests = 0

def run_test(test_name, test_fn):
    global passed_tests, total_tests
    total_tests += 1
    try:
        test_fn()
        print(f"[PASS] {test_name}")
        passed_tests += 1
    except AssertionError as e:
        print(f"[FAIL] {test_name}")
        print(f"   AssertionError: {e}\n")
    except Exception as e:
        print(f"[FAIL] {test_name}")
        print(f"   Unexpected Error: {type(e).__name__}: {e}\n")

print("Starting Day 1 Tests...\n")

# 1. Laptop Class Tests
def test_laptop():
    assert hasattr(assignment, 'Laptop'), "Laptop class not found in day1_assignment.py"
    
    # Try creating a laptop
    try:
        macbook = assignment.Laptop("Apple", "MacBook Pro", 16)
    except TypeError as e:
        raise AssertionError(f"Could not instantiate Laptop. Ensure constructor takes brand, model, and ram. Error: {e}")
    
    assert hasattr(macbook, 'brand'), "Laptop instance has no 'brand' attribute"
    assert hasattr(macbook, 'model'), "Laptop instance has no 'model' attribute"
    assert hasattr(macbook, 'ram'), "Laptop instance has no 'ram' attribute"
    
    assert macbook.brand == "Apple", f"Expected brand to be 'Apple', got '{macbook.brand}'"
    assert macbook.model == "MacBook Pro", f"Expected model to be 'MacBook Pro', got '{macbook.model}'"
    assert macbook.ram == 16, f"Expected ram to be 16, got {macbook.ram}"

run_test("Laptop class constructor and attributes", test_laptop)

# 2. Book Class Tests
def test_book():
    assert hasattr(assignment, 'Book'), "Book class not found in day1_assignment.py"
    
    try:
        short_book = assignment.Book("The Old Man and the Sea", "Ernest Hemingway", 127)
        long_book = assignment.Book("War and Peace", "Leo Tolstoy", 1225)
    except TypeError as e:
        raise AssertionError(f"Could not instantiate Book. Ensure constructor takes title, author, and pages. Error: {e}")
        
    assert hasattr(short_book, 'title'), "Book instance has no 'title' attribute"
    assert hasattr(short_book, 'author'), "Book instance has no 'author' attribute"
    assert hasattr(short_book, 'pages'), "Book instance has no 'pages' attribute"
    
    assert short_book.title == "The Old Man and the Sea"
    assert short_book.pages == 127
    
    # Check is_long method
    assert hasattr(short_book, 'is_long'), "Book instance does not have 'is_long' method"
    assert short_book.is_long() is False, "is_long() should return False for 127 pages"
    assert long_book.is_long() is True, "is_long() should return True for 1225 pages"

run_test("Book class constructor, attributes, and is_long method", test_book)

# 3. CartItem Class Tests
def test_cart_item():
    assert hasattr(assignment, 'CartItem'), "CartItem class not found in day1_assignment.py"
    
    try:
        item = assignment.CartItem("Wireless Mouse", 29.99, 3)
    except TypeError as e:
        raise AssertionError(f"Could not instantiate CartItem. Ensure constructor takes name, price, and quantity. Error: {e}")
        
    assert hasattr(item, 'name'), "CartItem instance has no 'name' attribute"
    assert hasattr(item, 'price'), "CartItem instance has no 'price' attribute"
    assert hasattr(item, 'quantity'), "CartItem instance has no 'quantity' attribute"
    
    assert item.name == "Wireless Mouse"
    assert item.price == 29.99
    assert item.quantity == 3
    
    # Check get_total_price method
    assert hasattr(item, 'get_total_price'), "CartItem instance has no 'get_total_price' method"
    total_price = item.get_total_price()
    assert abs(total_price - 89.97) < 0.001, f"Expected total price to be 89.97, got {total_price}"

run_test("CartItem class constructor, attributes, and get_total_price method", test_cart_item)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 1 assignments.")
    print(f"Proceed to Day 2 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day1_assignment.py")
