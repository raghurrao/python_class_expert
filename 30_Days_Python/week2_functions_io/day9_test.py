# Day 9 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day9_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week2_functions_io.day9_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day9_assignment.py. Error: {e}")
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

print("Starting Day 9 Tests...\n")

# 1. Test safe_divide
def test_safe_divide():
    assert hasattr(assignment, 'safe_divide'), "safe_divide not found in day9_assignment.py"
    
    assert assignment.safe_divide(10, 2) == 5.0, "Expected 5.0"
    assert assignment.safe_divide(10, 0) == "Error: Division by zero", "Zero division failed"
    assert assignment.safe_divide(10, "two") == "Error: Invalid types", "Type error failed"

run_test("Verify division calculations and error handling", test_safe_divide)

# 2. Test read_number_file
def test_read_number_file():
    assert hasattr(assignment, 'read_number_file'), "read_number_file not found in day9_assignment.py"
    
    # Missing file
    res = assignment.read_number_file("nonexistent_file_path.txt")
    assert res == "Error: File not found", f"Expected 'Error: File not found', got {repr(res)}"
    
    # File with invalid format
    temp_invalid = os.path.join(current_dir, "invalid_num.txt")
    with open(temp_invalid, "w") as f:
        f.write("abc")
    try:
        res2 = assignment.read_number_file(temp_invalid)
        assert res2 == "Error: Invalid number format", f"Expected 'Error: Invalid number format', got {repr(res2)}"
    finally:
        if os.path.exists(temp_invalid):
            os.remove(temp_invalid)
            
    # File with valid format
    temp_valid = os.path.join(current_dir, "valid_num.txt")
    with open(temp_valid, "w") as f:
        f.write("  42  ")
    try:
        res3 = assignment.read_number_file(temp_valid)
        assert res3 == 42, f"Expected 42, got {res3}"
    finally:
        if os.path.exists(temp_valid):
            os.remove(temp_valid)

run_test("Verify file input parsing and error logging", test_read_number_file)

# 3. Test validate_age
def test_validate_age():
    assert hasattr(assignment, 'validate_age'), "validate_age not found in day9_assignment.py"
    assert hasattr(assignment, 'InvalidAgeError'), "InvalidAgeError exception not found in day9_assignment.py"
    
    # Valid ages
    assert assignment.validate_age(0) == 0
    assert assignment.validate_age(25) == 25
    assert assignment.validate_age(120) == 120
    
    # Invalid too low
    try:
        assignment.validate_age(-5)
        raise AssertionError("Did not raise InvalidAgeError for negative age")
    except assignment.InvalidAgeError as e:
        assert str(e) == "Age must be between 0 and 120", f"Unexpected exception message: {e}"
        
    # Invalid too high
    try:
        assignment.validate_age(121)
        raise AssertionError("Did not raise InvalidAgeError for age > 120")
    except assignment.InvalidAgeError as e:
        assert str(e) == "Age must be between 0 and 120", f"Unexpected exception message: {e}"

run_test("Verify age validator and custom exception triggers", test_validate_age)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 9 assignments.")
    print(f"Proceed to Day 10 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day9_assignment.py")
