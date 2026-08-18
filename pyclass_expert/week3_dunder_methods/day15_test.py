# Day 15 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day15_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week3_dunder_methods.day15_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day15_assignment.py. Error: {e}")
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

print("Starting Day 15 Tests...\n")

# 1. Transaction Context Manager Tests
def test_transaction():
    assert hasattr(assignment, 'Transaction'), "Transaction class missing"
    
    db = {"Alice": 100, "Bob": 50}
    
    # Test successful transaction
    try:
        with assignment.Transaction(db) as tx:
            tx["Alice"] -= 20
            tx["Bob"] += 20
    except Exception as e:
        raise AssertionError(f"Transaction raised unexpected error: {e}")
        
    assert db["Alice"] == 80, "Successful transaction was not saved"
    assert db["Bob"] == 70
    
    # Test failing transaction (triggers rollback)
    try:
        with assignment.Transaction(db) as tx:
            tx["Alice"] -= 50  # 80 -> 30
            tx["Bob"] += 50    # 70 -> 120
            raise RuntimeError("Database connection lost midway!")
        raise AssertionError("Exception inside Transaction was suppressed; it should propagate (return False)")
    except RuntimeError as e:
        assert str(e) == "Database connection lost midway!"
        
    # Check that database rolled back to previous state (80 and 70)
    assert db["Alice"] == 80, f"Expected 80 after rollback, got {db['Alice']}"
    assert db["Bob"] == 70, f"Expected 70 after rollback, got {db['Bob']}"

run_test("Transaction manager commit and rollback mechanics", test_transaction)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 15 assignments.")
    print(f"Proceed to the Week 3 Challenge when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day15_assignment.py")
