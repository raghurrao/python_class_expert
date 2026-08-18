# Day 16 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day16_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week4_advanced.day16_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day16_assignment.py. Error: {e}")
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

print("Starting Day 16 Tests...\n")

# 1. Test get_squared_odds
def test_get_squared_odds():
    assert hasattr(assignment, 'get_squared_odds'), "get_squared_odds not found"
    
    res = assignment.get_squared_odds([1, 2, 3, 4, 5, 6, 7])
    assert res == [1, 9, 25, 49], f"Expected [1, 9, 25, 49], got {res}"
    
    res2 = assignment.get_squared_odds([2, 4, 6])
    assert res2 == [], f"Expected [], got {res2}"

run_test("Verify squared odd numbers list comprehension", test_get_squared_odds)

# 2. Test invert_dictionary
def test_invert_dictionary():
    assert hasattr(assignment, 'invert_dictionary'), "invert_dictionary not found"
    
    d = {'apple': 'red', 'banana': 'yellow', 'lime': 'green'}
    res = assignment.invert_dictionary(d)
    
    expected = {'red': 'apple', 'yellow': 'banana', 'green': 'lime'}
    assert res == expected, f"Expected {expected}, got {res}"

run_test("Verify dictionary key-value inversion comprehension", test_invert_dictionary)

# 3. Test Countdown iterator
def test_countdown_iterator():
    assert hasattr(assignment, 'Countdown'), "Countdown class not found"
    
    cd = assignment.Countdown(5)
    
    # Try converting to list (forces iteration until StopIteration)
    lst = list(cd)
    assert lst == [5, 4, 3, 2, 1], f"Expected [5, 4, 3, 2, 1], got {lst}"
    
    # Check that it raises StopIteration when empty
    cd2 = assignment.Countdown(1)
    it = iter(cd2)
    assert next(it) == 1
    try:
        next(it)
        raise AssertionError("Did not raise StopIteration after reaching bottom")
    except StopIteration:
        pass

run_test("Verify custom Countdown iterator loop and exception trigger", test_countdown_iterator)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 16 assignments.")
    print(f"Proceed to Day 17 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day16_assignment.py")
