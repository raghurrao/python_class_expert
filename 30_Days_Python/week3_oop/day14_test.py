# Day 14 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day14_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week3_oop.day14_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day14_assignment.py. Error: {e}")
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

print("Starting Day 14 Tests...\n")

# 1. Test Book str and repr
def test_book_presentation():
    assert hasattr(assignment, 'Book'), "Book class not found"
    
    b = assignment.Book("1984", "George Orwell", 328)
    
    # Check str
    assert str(b) == "'1984' by George Orwell", f"Expected \"'1984' by George Orwell\", got \"{str(b)}\""
    
    # Check repr
    assert repr(b) == "Book(title='1984', author='George Orwell', pages=328)", f"Got: \"{repr(b)}\""

run_test("Verify Book __str__ and __repr__ string formatting", test_book_presentation)

# 2. Test Book equality __eq__
def test_book_equality():
    assert hasattr(assignment, 'Book'), "Book class not found"
    
    b1 = assignment.Book("1984", "George Orwell", 328)
    b2 = assignment.Book("1984", "George Orwell", 400)  # Different pages, same title/author
    b3 = assignment.Book("Animal Farm", "George Orwell", 112)
    
    assert b1 == b2, "Books with same title and author should be equal"
    assert b1 != b3, "Books with different titles should not be equal"
    assert b1 != "1984 by George Orwell", "Book compared to string should return False, not crash"

run_test("Verify Book __eq__ equality check logic", test_book_equality)

# 3. Test Book addition __add__
def test_book_addition():
    assert hasattr(assignment, 'Book'), "Book class not found"
    
    b = assignment.Book("1984", "George Orwell", 320)
    b_new = b + 8
    
    assert isinstance(b_new, assignment.Book), "Addition must return a new Book instance"
    assert b_new.pages == 328, f"Expected 328 pages, got {b_new.pages}"
    assert b_new.title == "1984", "Title should remain unchanged"
    assert b.pages == 320, "Original Book instance pages should remain unchanged (immutable addition)"
    
    # Try invalid addition
    try:
        b + "eight"
        raise AssertionError("Did not raise TypeError / return NotImplemented for invalid addition")
    except TypeError:
        pass

run_test("Verify Book operator overloading (__add__)", test_book_addition)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 14 assignments.")
    print(f"Proceed to Day 15 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day14_assignment.py")
