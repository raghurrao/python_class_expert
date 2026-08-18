# Day 3 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day3_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week1_foundations.day3_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day3_assignment.py. Error: {e}")
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

print("Starting Day 3 Tests...\n")

# 1. User Tests
def test_user_factory():
    assert hasattr(assignment, 'User'), "User class not found"
    
    # Check standard constructor
    try:
        u = assignment.User("john_doe", "john@example.com")
    except TypeError as e:
        raise AssertionError(f"Could not instantiate User with (username, email). Error: {e}")
        
    assert u.username == "john_doe", f"Expected username 'john_doe', got '{u.username}'"
    assert u.email == "john_doe@example.com" or u.email == "john@example.com", f"Expected email 'john@example.com', got '{u.email}'"
    
    # Check classmethod factory
    assert hasattr(assignment.User, 'from_string'), "User class has no 'from_string' method"
    
    # Check that from_string is a bound classmethod
    # In Python, calling a classmethod on the class returns a bound method
    method = assignment.User.from_string
    assert method.__self__ is assignment.User, "from_string must be a classmethod (decorated with @classmethod)"
    
    try:
        u2 = assignment.User.from_string("alice,alice@example.com")
    except Exception as e:
        raise AssertionError(f"from_string failed with error: {e}")
        
    assert isinstance(u2, assignment.User), "from_string did not return a User instance"
    assert u2.username == "alice", f"Expected username 'alice', got '{u2.username}'"
    assert u2.email == "alice@example.com", f"Expected email 'alice@example.com', got '{u2.email}'"

run_test("User class constructor and @classmethod factory", test_user_factory)

# 2. MathHelper Tests
def test_math_helper():
    assert hasattr(assignment, 'MathHelper'), "MathHelper class not found"
    assert hasattr(assignment.MathHelper, 'is_prime'), "MathHelper class has no 'is_prime' method"
    
    # Check is_prime is a staticmethod
    # A staticmethod accessed on the class doesn't bind to self or class
    assert not hasattr(assignment.MathHelper.is_prime, '__self__'), "is_prime must be a staticmethod (decorated with @staticmethod)"
    
    # Test prime values
    assert assignment.MathHelper.is_prime(1) is False, "1 is not prime"
    assert assignment.MathHelper.is_prime(2) is True, "2 is prime"
    assert assignment.MathHelper.is_prime(4) is False, "4 is not prime"
    assert assignment.MathHelper.is_prime(17) is True, "17 is prime"
    assert assignment.MathHelper.is_prime(-5) is False, "Negative numbers cannot be prime"
    
    # Test history logging instance method
    try:
        mh = assignment.MathHelper()
    except TypeError as e:
        raise AssertionError(f"Could not instantiate MathHelper. Error: {e}")
        
    assert hasattr(mh, 'history'), "MathHelper instance lacks 'history' attribute"
    assert mh.history == [], "history list should start empty"
    
    res1 = mh.check_and_log(7)
    assert res1 is True, "check_and_log(7) should return True"
    assert len(mh.history) == 1, "history should contain 1 log entry"
    assert mh.history[0] == "7 is prime", f"Expected log '7 is prime', got '{mh.history[0]}'"
    
    res2 = mh.check_and_log(10)
    assert res2 is False, "check_and_log(10) should return False"
    assert len(mh.history) == 2, "history should contain 2 entries"
    assert mh.history[1] == "10 is composite", f"Expected log '10 is composite', got '{mh.history[1]}'"

run_test("MathHelper static utility and instance log validation", test_math_helper)

# 3. Booking Tests
def test_booking():
    assert hasattr(assignment, 'Booking'), "Booking class not found"
    assert hasattr(assignment.Booking, 'tax_rate'), "Booking class should have class attribute 'tax_rate'"
    
    # Reset default tax rate
    assignment.Booking.tax_rate = 0.12
    
    try:
        b1 = assignment.Booking(150.0, 4)
    except TypeError as e:
        raise AssertionError(f"Could not instantiate Booking. Error: {e}")
        
    cost1 = b1.get_total_cost()
    # 150 * 4 * 1.12 = 600 * 1.12 = 672.0
    assert abs(cost1 - 672.0) < 0.001, f"Expected total cost 672.0, got {cost1}"
    
    # Change tax rate using classmethod
    assert hasattr(assignment.Booking, 'set_tax_rate'), "Booking class has no 'set_tax_rate' method"
    assert assignment.Booking.set_tax_rate.__self__ is assignment.Booking, "set_tax_rate must be a classmethod (decorated with @classmethod)"
    
    assignment.Booking.set_tax_rate(0.18)
    assert assignment.Booking.tax_rate == 0.18, "tax_rate class attribute not updated"
    
    # Check cost under new rate
    cost2 = b1.get_total_cost()
    # 150 * 4 * 1.18 = 600 * 1.18 = 708.0
    assert abs(cost2 - 708.0) < 0.001, f"Expected total cost 708.0, got {cost2}"

run_test("Booking tax rate updates and cost calculation", test_booking)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 3 assignments.")
    print(f"Proceed to Day 4 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day3_assignment.py")
