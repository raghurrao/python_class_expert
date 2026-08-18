# Day 18 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day18_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week4_advanced.day18_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day18_assignment.py. Error: {e}")
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

# Setup capture stdout helpers to check printing output
from io import StringIO

print("Starting Day 18 Tests...\n")

# 1. Test log_execution
def test_log_execution():
    assert hasattr(assignment, 'log_execution'), "log_execution not found"
    
    # Define a decorated test function
    @assignment.log_execution
    def add(a, b):
        """Add two numbers."""
        return a + b
        
    assert add.__name__ == "add", "Decorator did not preserve function name. Ensure @functools.wraps is used."
    assert add.__doc__ == "Add two numbers.", "Decorator did not preserve function docstring."
    
    # Capture print output
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        res = add(10, 20)
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
        
    assert res == 30, f"Expected output 30, got {res}"
    assert "[LOG] Executing add..." in output, f"Expected print log prefix, got: {repr(output)}"

run_test("Verify execution logger decorator outputs and wraps metadata", test_log_execution)

# 2. Test validate_ints
def test_validate_ints():
    assert hasattr(assignment, 'validate_ints'), "validate_ints not found"
    
    @assignment.validate_ints
    def multiply(a, b):
        return a * b
        
    assert multiply(5, 5) == 25, "Expected 25"
    
    # Try calling with invalid types
    try:
        multiply(5, "five")
        raise AssertionError("Did not raise TypeError for invalid float/string arguments")
    except TypeError as e:
        assert str(e) == "All arguments must be integers", f"Unexpected error message: {e}"

run_test("Verify arguments type-checking decorator (validate_ints)", test_validate_ints)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 18 assignments.")
    print(f"Proceed to Day 19 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day18_assignment.py")
