# Day 10 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day10_test.py
# It will verify if your assignment code is correct!

import sys
import os
import datetime
import math

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week2_functions_io.day10_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day10_assignment.py. Error: {e}")
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

print("Starting Day 10 Tests...\n")

# 1. Test get_random_element
def test_get_random_element():
    assert hasattr(assignment, 'get_random_element'), "get_random_element not found in day10_assignment.py"
    
    lst = [10, 20, 30, 40, 50]
    # Call it multiple times to verify it picks from the list
    for _ in range(5):
        choice = assignment.get_random_element(lst)
        assert choice in lst, f"Selected value {choice} not present in list {lst}"

run_test("Verify random selection logic", test_get_random_element)

# 2. Test format_date_now
def test_format_date_now():
    assert hasattr(assignment, 'format_date_now'), "format_date_now not found in day10_assignment.py"
    
    formatted = assignment.format_date_now()
    assert isinstance(formatted, str), "Expected string return type"
    
    # Check shape: "YYYY-MM-DD HH:MM:SS" length is 19 characters
    assert len(formatted) == 19, f"Expected length 19, got {len(formatted)} ('{formatted}')"
    assert formatted[4] == '-' and formatted[7] == '-', "Dash formatting character missing in date"
    assert formatted[10] == ' ', "Space separation missing between date and time"
    assert formatted[13] == ':' and formatted[16] == ':', "Colon formatting characters missing in time"

run_test("Verify datetime formatting string format", test_format_date_now)

# 3. Test calculate_hypotenuse
def test_calculate_hypotenuse():
    assert hasattr(assignment, 'calculate_hypotenuse'), "calculate_hypotenuse not found in day10_assignment.py"
    
    res1 = assignment.calculate_hypotenuse(3.0, 4.0)
    assert res1 == 5.0, f"Expected 5.0, got {res1}"
    
    res2 = assignment.calculate_hypotenuse(5.0, 12.0)
    assert res2 == 13.0, f"Expected 13.0, got {res2}"

run_test("Verify Pythagorean calculation logic", test_calculate_hypotenuse)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 10 assignments.")
    print(f"Proceed to the Week 2 Weekend Challenge when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day10_assignment.py")
