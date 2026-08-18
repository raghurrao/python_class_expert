# Day 7 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day7_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week2_functions_io.day7_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day7_assignment.py. Error: {e}")
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

print("Starting Day 7 Tests...\n")

# 1. Test square_even_numbers
def test_square_even_numbers():
    assert hasattr(assignment, 'square_even_numbers'), "square_even_numbers not found in day7_assignment.py"
    
    res = assignment.square_even_numbers([1, 2, 3, 4, 5, 6])
    assert res == [4, 16, 36], f"Expected [4, 16, 36], got {res}"
    
    res2 = assignment.square_even_numbers([1, 3, 5])
    assert res2 == [], f"Expected [], got {res2}"

run_test("Verify square even numbers logic (map, filter, lambda)", test_square_even_numbers)

# 2. Test combine_names_and_ages
def test_combine_names_and_ages():
    assert hasattr(assignment, 'combine_names_and_ages'), "combine_names_and_ages not found in day7_assignment.py"
    
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    res = assignment.combine_names_and_ages(names, ages)
    
    expected = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 35}
    ]
    assert res == expected, f"Expected {expected}, got {res}"

run_test("Verify parallel lists combination (zip)", test_combine_names_and_ages)

# 3. Test index_words
def test_index_words():
    assert hasattr(assignment, 'index_words'), "index_words not found in day7_assignment.py"
    
    words = ["hello", "world", "python"]
    res = assignment.index_words(words)
    
    expected = ["0: hello", "1: world", "2: python"]
    assert res == expected, f"Expected {expected}, got {res}"

run_test("Verify indexed word strings format (enumerate)", test_index_words)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 7 assignments.")
    print(f"Proceed to Day 8 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day7_assignment.py")
