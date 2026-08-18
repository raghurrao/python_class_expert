# Week 3 Challenge Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python week3_challenge_test.py
# It will verify if your inventory management system classes work!

import sys
import os

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week3_oop.week3_challenge as challenge
except ImportError as e:
    print(f"[FAIL] Could not import week3_challenge.py. Error: {e}")
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

print("Starting Week 3 Challenge Tests...\n")

# 1. Test Product class properties and validations
def test_product_class():
    assert hasattr(challenge, 'Product'), "Product class not found"
    
    p = challenge.Product("P100", "Mechanical Keyboard", 89.99)
    assert not hasattr(p, '__price'), "Price attribute must be private"
    assert p.price == 89.99
    
    # Test valid setter
    p.price = 79.99
    assert p.price == 79.99
    
    # Test invalid setter (<= 0)
    try:
        p.price = 0
        raise AssertionError("Did not raise ValueError for price = 0")
    except ValueError as e:
        assert str(e) == "Price must be positive", f"Unexpected error message: {e}"
        
    try:
        p.price = -10.0
        raise AssertionError("Did not raise ValueError for negative price")
    except ValueError as e:
        assert str(e) == "Price must be positive"
        
    assert p.get_details() == "Product: Mechanical Keyboard (ID: P100) - $79.99", f"Got: '{p.get_details()}'"

run_test("Verify Product base class encapsulation & properties", test_product_class)

# 2. Test DigitalProduct subclass
def test_digital_product_class():
    assert hasattr(challenge, 'DigitalProduct'), "DigitalProduct class not found"
    assert issubclass(challenge.DigitalProduct, challenge.Product), "DigitalProduct must inherit from Product"
    
    dp = challenge.DigitalProduct("D200", "Python eBook", 19.99, 4.5)
    assert dp.price == 19.99
    assert dp.file_size_mb == 4.5
    
    assert dp.get_details() == "Digital Product: Python eBook (ID: D200) - $19.99 [File Size: 4.5MB]", f"Got: '{dp.get_details()}'"

run_test("Verify DigitalProduct inheritance and method overriding", test_digital_product_class)

# 3. Test Inventory tracker class
def test_inventory_class():
    assert hasattr(challenge, 'Inventory'), "Inventory class not found"
    
    inv = challenge.Inventory()
    assert hasattr(inv, 'products') and isinstance(inv.products, dict), "Inventory must have 'products' dictionary"
    
    p1 = challenge.Product("P1", "Mouse", 10.00)
    dp2 = challenge.DigitalProduct("DP2", "E-Music", 5.00, 15.0)
    
    # Add products
    inv.add_product(p1)
    inv.add_product(dp2)
    assert len(inv.products) == 2
    
    # Retrieve product
    assert inv.get_product("P1") == p1
    assert inv.get_product("DP2") == dp2
    assert inv.get_product("NONEXISTENT") is None
    
    # Remove product
    inv.remove_product("P1")
    assert len(inv.products) == 1
    assert inv.get_product("P1") is None
    
    # Safe remove nonexistent
    inv.remove_product("NONEXISTENT") # Should not error

run_test("Verify Inventory product tracking operations", test_inventory_class)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed the Week 3 Weekend Challenge.")
    print(f"You are now ready to progress to Week 4 (Advanced Python)!")
else:
    print(f"FAILED: Some challenge tests failed. Check the errors above and fix your code in week3_challenge.py")
