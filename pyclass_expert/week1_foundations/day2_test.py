# Day 2 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day2_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week1_foundations.day2_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day2_assignment.py. Error: {e}")
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

print("Starting Day 2 Tests...\n")

# Reset class variables for Product between runs if needed (just in case)
if hasattr(assignment, 'Product'):
    assignment.Product.total_products = 0
    assignment.Product.product_catalog = []

# 1. Employee Tests
def test_employee():
    assert hasattr(assignment, 'Employee'), "Employee class not found"
    assert hasattr(assignment.Employee, 'raise_amount'), "Employee class should have a 'raise_amount' class attribute"
    assert assignment.Employee.raise_amount == 1.05, "Default raise_amount should be 1.05"
    
    try:
        emp1 = assignment.Employee("Alice", 50000.0)
        emp2 = assignment.Employee("Bob", 60000.0)
    except TypeError as e:
        raise AssertionError(f"Could not instantiate Employee. Error: {e}")
        
    # Check default raise application
    emp1.apply_raise()
    assert abs(emp1.salary - 52500.0) < 0.001, f"Expected salary of 52500.0, got {emp1.salary}"
    
    # Check instance override behavior
    emp2.raise_amount = 1.10
    emp2.apply_raise()
    assert abs(emp2.salary - 66000.0) < 0.001, f"Expected custom raise salary of 66000.0, got {emp2.salary}"
    
    # Ensure Employee class attribute was not altered
    assert assignment.Employee.raise_amount == 1.05, "Modifying instance raise_amount should not modify class raise_amount"
    assert 'raise_amount' not in emp1.__dict__, "emp1 should not have 'raise_amount' in its instance namespace"
    assert 'raise_amount' in emp2.__dict__, "emp2 should have overridden 'raise_amount' in its instance namespace"

run_test("Employee raise_amount (Class vs Instance attribute lookup)", test_employee)

# 2. Product Tests
def test_product():
    assert hasattr(assignment, 'Product'), "Product class not found"
    assert hasattr(assignment.Product, 'total_products'), "Product class should have 'total_products'"
    assert hasattr(assignment.Product, 'product_catalog'), "Product class should have 'product_catalog'"
    
    try:
        p1 = assignment.Product("Banana")
        p2 = assignment.Product("Apple")
    except TypeError as e:
        raise AssertionError(f"Could not instantiate Product. Error: {e}")
        
    assert p1.name == "Banana"
    assert assignment.Product.total_products == 2, f"Expected 2 total products, got {assignment.Product.total_products}"
    assert "Banana" in assignment.Product.product_catalog, "Banana missing from catalog"
    assert "Apple" in assignment.Product.product_catalog, "Apple missing from catalog"
    assert assignment.Product.product_catalog == ["Banana", "Apple"], f"Catalog contents mismatch: {assignment.Product.product_catalog}"

run_test("Product class counters and list trackers", test_product)

# 3. Configuration Tests
def test_configuration():
    assert hasattr(assignment, 'Configuration'), "Configuration class not found"
    assert hasattr(assignment.Configuration, 'settings'), "Configuration class must have 'settings' dict"
    
    # Reset config settings default
    assignment.Configuration.settings = {"theme": "light", "language": "en"}
    
    try:
        c1 = assignment.Configuration()
        c2 = assignment.Configuration()
    except TypeError as e:
        raise AssertionError(f"Could not instantiate Configuration. Error: {e}")
        
    assert c1.settings["theme"] == "light"
    
    # Modify globally
    c1.update_setting("theme", "dark")
    
    # Both instances and the class itself should reflect this update
    assert c2.settings["theme"] == "dark", "Theme not updated on separate instance"
    assert assignment.Configuration.settings["theme"] == "dark", "Theme not updated on class level"

run_test("Configuration global settings updater", test_configuration)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 2 assignments.")
    print(f"Proceed to Day 3 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day2_assignment.py")
