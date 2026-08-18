# Day 4 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day4_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week1_basics.day4_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day4_assignment.py. Error: {e}")
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

print("Starting Day 4 Tests...\n")

# 1. Test get_first_and_last
def test_get_first_and_last():
    assert hasattr(assignment, 'get_first_and_last'), "get_first_and_last not found in day4_assignment.py"
    
    # Check normal sequence
    res1 = assignment.get_first_and_last([1, 2, 3, 4, 5])
    assert res1 == (1, 5), f"Expected (1, 5), got {res1}"
    
    # Check one item
    res2 = assignment.get_first_and_last(["apple"])
    assert res2 == ("apple", "apple"), f"Expected ('apple', 'apple'), got {res2}"
    
    # Check empty list
    res3 = assignment.get_first_and_last([])
    assert res3 == (None, None), f"Expected (None, None), got {res3}"
    
    # Check tuple
    res4 = assignment.get_first_and_last((10, 20, 30))
    assert res4 == (10, 30), f"Expected (10, 30), got {res4}"

run_test("Verify first and last elements retrieval logic", test_get_first_and_last)

# 2. Test list_slicing_magic
def test_list_slicing_magic():
    assert hasattr(assignment, 'list_slicing_magic'), "list_slicing_magic not found in day4_assignment.py"
    
    lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    res1 = assignment.list_slicing_magic(lst)
    assert res1 == [20, 40, 60], f"Expected [20, 40, 60], got {res1}"
    
    lst2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    res2 = assignment.list_slicing_magic(lst2)
    assert res2 == ['b', 'd', 'f'], f"Expected ['b', 'd', 'f'], got {res2}"

run_test("Verify list slicing index calculations", test_list_slicing_magic)

# 3. Test manage_shopping_list
def test_manage_shopping_list():
    assert hasattr(assignment, 'manage_shopping_list'), "manage_shopping_list not found in day4_assignment.py"
    
    # List: ['milk', 'bread', 'eggs']. Add: 'butter', Remove: 'bread'
    # Result should be sorted: ['butter', 'eggs', 'milk']
    res1 = assignment.manage_shopping_list(['milk', 'bread', 'eggs'], 'butter', 'bread')
    assert res1 == ['butter', 'eggs', 'milk'], f"Expected ['butter', 'eggs', 'milk'], got {res1}"
    
    # Check safe removal when item does not exist
    # List: ['apples', 'oranges']. Add: 'bananas', Remove: 'peaches' (doesn't exist)
    # Result should be sorted: ['apples', 'bananas', 'oranges']
    res2 = assignment.manage_shopping_list(['apples', 'oranges'], 'bananas', 'peaches')
    assert res2 == ['apples', 'bananas', 'oranges'], f"Expected ['apples', 'bananas', 'oranges'], got {res2}"

run_test("Verify shopping list management, safe removal, and sorting", test_manage_shopping_list)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 4 assignments.")
    print(f"Proceed to Day 5 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day4_assignment.py")
