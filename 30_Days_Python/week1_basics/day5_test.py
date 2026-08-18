# Day 5 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day5_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week1_basics.day5_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day5_assignment.py. Error: {e}")
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

print("Starting Day 5 Tests...\n")

# 1. Test count_words
def test_count_words():
    assert hasattr(assignment, 'count_words'), "count_words not found in day5_assignment.py"
    
    text = "The quick brown fox jumps, over the lazy dog. The dog was lazy."
    counts = assignment.count_words(text)
    
    assert isinstance(counts, dict), f"Expected dict, got {type(counts).__name__}"
    assert counts.get('the') == 3, f"Expected count for 'the' to be 3, got {counts.get('the')}"
    assert counts.get('lazy') == 2, f"Expected count for 'lazy' to be 2, got {counts.get('lazy')}"
    assert counts.get('dog') == 2, f"Expected count for 'dog' to be 2, got {counts.get('dog')}"
    assert counts.get('fox') == 1, f"Expected count for 'fox' to be 1, got {counts.get('fox')}"

run_test("Verify word count cleaning and frequency dict", test_count_words)

# 2. Test find_common_and_unique
def test_find_common_and_unique():
    assert hasattr(assignment, 'find_common_and_unique'), "find_common_and_unique not found in day5_assignment.py"
    
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    res = assignment.find_common_and_unique(set1, set2)
    
    assert isinstance(res, dict), f"Expected dict, got {type(res).__name__}"
    assert res.get('common') == {3, 4}, f"Expected common to be {{3, 4}}, got {res.get('common')}"
    assert res.get('only_a') == {1, 2}, f"Expected only_a to be {{1, 2}}, got {res.get('only_a')}"

run_test("Verify set operations (intersection and difference)", test_find_common_and_unique)

# 3. Test get_student_grade
def test_get_student_grade():
    assert hasattr(assignment, 'get_student_grade'), "get_student_grade not found in day5_assignment.py"
    
    grades = {"Alice": "A", "Bob": "B", "Charlie": "A+"}
    
    assert assignment.get_student_grade(grades, "Alice") == "A", "Alice should have an A"
    assert assignment.get_student_grade(grades, "Bob") == "B", "Bob should have a B"
    assert assignment.get_student_grade(grades, "David") == "Student not found", "David is missing, should return 'Student not found'"

run_test("Verify safe dictionary grade lookup", test_get_student_grade)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 5 assignments.")
    print(f"Proceed to the Week 1 Weekend Challenge when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day5_assignment.py")
