# Day 18 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day18_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week4_metaprogramming.day18_assignment as assignment
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

print("Starting Day 18 Tests...\n")

# Reset singleton before tests
if hasattr(assignment, 'LoggerPool'):
    assignment.LoggerPool._instance = None

# 1. LoggerPool Singleton Tests
def test_singleton_logger():
    assert hasattr(assignment, 'LoggerPool'), "LoggerPool class missing"
    
    log1 = assignment.LoggerPool()
    log2 = assignment.LoggerPool()
    
    assert log1 is log2, "LoggerPool failed to implement Singleton pattern (instances differ)"
    
    # Verify initialization guard
    log1.log("First log entry")
    log2.log("Second log entry")
    
    # Total logs should be 2. If __init__ was run again it would have wiped the list!
    assert len(log1.logs) == 2, f"Logs list was reinitialized or wiped. Length: {len(log1.logs)}"
    assert log1.logs == ["First log entry", "Second log entry"]

run_test("LoggerPool Singleton pattern and reinitialization protection", test_singleton_logger)

# 2. UppercaseString Tests
def test_uppercase_string():
    assert hasattr(assignment, 'UppercaseString'), "UppercaseString class missing"
    assert issubclass(assignment.UppercaseString, str), "UppercaseString must inherit from str"
    
    s = assignment.UppercaseString("hello world")
    
    assert isinstance(s, assignment.UppercaseString)
    assert s == "HELLO WORLD", f"String was not capitalized. Expected 'HELLO WORLD', got '{s}'"
    assert s.lower() == "hello world"

run_test("UppercaseString immutable subclass creation (__new__)", test_uppercase_string)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 18 assignments.")
    print(f"Proceed to Day 19 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day18_assignment.py")
