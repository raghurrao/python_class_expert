# Day 6 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day6_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week2_functions_io.day6_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day6_assignment.py. Error: {e}")
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

print("Starting Day 6 Tests...\n")

# 1. Test multiply_all
def test_multiply_all():
    assert hasattr(assignment, 'multiply_all'), "multiply_all not found in day6_assignment.py"
    
    assert assignment.multiply_all() == 1, "Expected 1 when no arguments are passed"
    assert assignment.multiply_all(5) == 5, "Expected 5 for multiply_all(5)"
    assert assignment.multiply_all(2, 3, 4) == 24, "Expected 24 for multiply_all(2, 3, 4)"
    assert assignment.multiply_all(2, -3, 5) == -30, "Expected -30 for multiply_all(2, -3, 5)"

run_test("Verify arbitrary arguments multiplication (*args)", test_multiply_all)

# 2. Test make_sandwich
def test_make_sandwich():
    assert hasattr(assignment, 'make_sandwich'), "make_sandwich not found in day6_assignment.py"
    
    res1 = assignment.make_sandwich("Wheat", "Turkey", "Swiss Cheese")
    assert res1 == "Wheat sandwich with: Turkey, Swiss Cheese", f"Got: '{res1}'"
    
    res2 = assignment.make_sandwich()
    assert res2 == "White sandwich with no toppings", f"Got: '{res2}'"
    
    res3 = assignment.make_sandwich(bread_type="Rye")
    assert res3 == "Rye sandwich with no toppings", f"Got: '{res3}'"

run_test("Verify sandwich description builder and defaults", test_make_sandwich)

# 3. Test build_user_profile
def test_build_user_profile():
    assert hasattr(assignment, 'build_user_profile'), "build_user_profile not found in day6_assignment.py"
    
    profile = assignment.build_user_profile("Alice", "Wonderland", age=22, occupation="Explorer")
    assert isinstance(profile, dict), "Expected a dictionary return type"
    assert profile.get('first_name') == "Alice", "First name should map to 'first_name'"
    assert profile.get('last_name') == "Wonderland", "Last name should map to 'last_name'"
    assert profile.get('age') == 22, "Extra keyword age missing"
    assert profile.get('occupation') == "Explorer", "Extra keyword occupation missing"

run_test("Verify user profile mapping with keyword arguments (**kwargs)", test_build_user_profile)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 6 assignments.")
    print(f"Proceed to Day 7 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day6_assignment.py")
