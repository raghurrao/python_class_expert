# Day 17 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day17_test.py
# It will verify if your assignment code is correct!

import sys
import os
import types

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week4_advanced.day17_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day17_assignment.py. Error: {e}")
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

print("Starting Day 17 Tests...\n")

# 1. Test fibonacci generator
def test_fibonacci_generator():
    assert hasattr(assignment, 'fibonacci'), "fibonacci function not found"
    
    gen = assignment.fibonacci(10)
    assert isinstance(gen, types.GeneratorType), "Expected a Generator object to be returned"
    
    lst = list(gen)
    assert lst == [0, 1, 1, 2, 3, 5, 8], f"Expected [0, 1, 1, 2, 3, 5, 8], got {lst}"
    
    lst2 = list(assignment.fibonacci(0))
    assert lst2 == [0], f"Expected [0], got {lst2}"

run_test("Verify Fibonacci lazy generator logic", test_fibonacci_generator)

# 2. Test TemporaryFileMock context manager
def test_temporary_file_mock():
    assert hasattr(assignment, 'TemporaryFileMock'), "TemporaryFileMock class not found"
    
    mock = assignment.TemporaryFileMock("test.txt")
    assert mock.is_open is False, "File should start closed"
    
    with mock as handle:
        assert mock.is_open is True, "File should be marked open inside block"
        assert handle == "FILE_HANDLE:test.txt", f"Expected 'FILE_HANDLE:test.txt', got '{handle}'"
        
    assert mock.is_open is False, "File should be marked closed after exiting block"

run_test("Verify TemporaryFileMock context manager enter/exit states", test_temporary_file_mock)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 17 assignments.")
    print(f"Proceed to Day 18 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day17_assignment.py")
