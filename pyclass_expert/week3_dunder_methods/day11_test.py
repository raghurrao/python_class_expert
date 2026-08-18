# Day 11 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day11_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week3_dunder_methods.day11_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day11_assignment.py. Error: {e}")
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

print("Starting Day 11 Tests...\n")

# 1. Book Tests
def test_book_presentation():
    assert hasattr(assignment, 'Book'), "Book class missing"
    
    b = assignment.Book("1984", "George Orwell")
    
    assert str(b) == "'1984' by George Orwell", f"Expected \"'1984' by George Orwell\", got \"{str(b)}\""
    assert repr(b) == "Book(title='1984', author='George Orwell')", f"Expected \"Book(title='1984', author='George Orwell')\", got \"{repr(b)}\""

run_test("Book class presentation dunders (__str__ and __repr__)", test_book_presentation)

# 2. Color equality & Hashing Tests
def test_color_hash():
    assert hasattr(assignment, 'Color'), "Color class missing"
    
    c1 = assignment.Color(255, 0, 0)
    c2 = assignment.Color(255, 0, 0)
    c3 = assignment.Color(0, 0, 255)
    
    # Assert equality
    assert c1 == c2, "Colors with identical components should be equal"
    assert c1 != c3, "Colors with different components should not be equal"
    assert c1 != "not a color", "Color should not be equal to a string"
    
    # Assert hashing
    color_set = {c1, c2, c3}
    assert len(color_set) == 2, f"Expected set size 2 (c1 and c2 are identical), got {len(color_set)}"
    assert c1 in color_set
    assert assignment.Color(0, 0, 255) in color_set

run_test("Color equality and hashability implementation", test_color_hash)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 11 assignments.")
    print(f"Proceed to Day 12 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day11_assignment.py")
