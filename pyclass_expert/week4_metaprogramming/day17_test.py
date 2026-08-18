# Day 17 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day17_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week4_metaprogramming.day17_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day17_assignment.py. Error: {e}")
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

print("Starting Day 17 Tests...\n")

# 1. Descriptor Class Tests
def test_descriptor_logic():
    assert hasattr(assignment, 'NonEmptyString'), "NonEmptyString class missing"
    assert hasattr(assignment, 'User'), "User class missing"
    
    # Check that username and email on User class are descriptors
    assert isinstance(assignment.User.username, assignment.NonEmptyString), "User.username must be a NonEmptyString descriptor"
    assert isinstance(assignment.User.email, assignment.NonEmptyString), "User.email must be a NonEmptyString descriptor"
    
    # Try successful instantiation
    try:
        u1 = assignment.User("john_doe", "john@example.com")
        u2 = assignment.User("alice_w", "alice@example.com")
    except Exception as e:
        raise AssertionError(f"Could not instantiate User with valid strings. Error: {e}")
        
    assert u1.username == "john_doe"
    assert u2.username == "alice_w"
    
    # Check that values are stored in instance __dict__ under private names
    assert "_username" in u1.__dict__, "Value should be stored in instance.__dict__ under private name '_username'"
    assert u1._username == "john_doe"
    
    # Check that values are trimmed (stripped)
    u3 = assignment.User("   bob   ", "bob@ex.com")
    assert u3.username == "bob", f"Descriptor should strip whitespace, got '{u3.username}'"
    
    # Check type validation
    try:
        assignment.User(1234, "test@example.com")
        raise AssertionError("Non-string username should raise TypeError")
    except TypeError:
        pass
        
    # Check emptiness validation
    try:
        assignment.User("alice", "    ")
        raise AssertionError("Empty string email should raise ValueError")
    except ValueError:
        pass

run_test("NonEmptyString validation descriptor and User application", test_descriptor_logic)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 17 assignments.")
    print(f"Proceed to Day 18 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day17_assignment.py")
