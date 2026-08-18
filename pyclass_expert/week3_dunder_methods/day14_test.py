# Day 14 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day14_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week3_dunder_methods.day14_assignment as assignment
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

# 1. Fibonacci Iterator Tests
def test_fibonacci_iterator():
    assert hasattr(assignment, 'Fibonacci'), "Fibonacci class missing"
    
    # Generate 6 terms
    fib = assignment.Fibonacci(6)
    terms = list(fib)
    
    expected_terms = [0, 1, 1, 2, 3, 5]
    assert terms == expected_terms, f"Expected {expected_terms}, got {terms}"
    
    # Check limit of 0
    terms_empty = list(assignment.Fibonacci(0))
    assert terms_empty == []

run_test("Fibonacci class iterator protocol implementation", test_fibonacci_iterator)

# 2. Callable Accumulator Tests
def test_callable_accumulator():
    assert hasattr(assignment, 'CallableAccumulator'), "CallableAccumulator class missing"
    
    acc = assignment.CallableAccumulator(10)
    assert acc.value == 10
    
    # Check call
    r1 = acc(5)
    assert r1 == 15, f"Expected 15, got {r1}"
    assert acc.value == 15
    
    r2 = acc(10)
    assert r2 == 25
    assert acc.value == 25
    
    # Check default initial value
    acc_default = assignment.CallableAccumulator()
    assert acc_default.value == 0
    assert acc_default(5) == 5

run_test("CallableAccumulator function-like call interface", test_callable_accumulator)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 14 assignments.")
    print(f"Proceed to Day 15 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day14_assignment.py")
