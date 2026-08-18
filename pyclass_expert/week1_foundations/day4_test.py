# Day 4 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day4_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week1_foundations.day4_assignment as assignment
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

# 1. Student Tests
def test_student_encapsulation():
    assert hasattr(assignment, 'Student'), "Student class not found"
    
    try:
        s = assignment.Student("John Doe", 3.5)
    except TypeError as e:
        raise AssertionError(f"Could not instantiate Student. Error: {e}")
        
    assert s.name == "John Doe", "Public name attribute missing or incorrect"
    assert hasattr(s, '_gpa'), "Protected _gpa attribute missing"
    assert s._gpa == 3.5, "Protected _gpa value mismatch"
    
    # Check getters and setters
    assert s.get_gpa() == 3.5, "get_gpa did not return correct value"
    
    # Valid set
    s.set_gpa(3.8)
    assert s.get_gpa() == 3.8, "set_gpa did not update the GPA value"
    
    # Invalid sets (ValueError expected)
    try:
        s.set_gpa(4.5)
        raise AssertionError("set_gpa(4.5) should have raised ValueError but did not")
    except ValueError:
        pass  # Success
        
    try:
        s.set_gpa(-0.1)
        raise AssertionError("set_gpa(-0.1) should have raised ValueError but did not")
    except ValueError:
        pass  # Success

run_test("Student class encapsulation and validation limits", test_student_encapsulation)

# 2. SecureKey Tests
def test_secure_key():
    assert hasattr(assignment, 'SecureKey'), "SecureKey class not found"
    
    try:
        key = assignment.SecureKey("secret123")
    except TypeError as e:
        raise AssertionError(f"Could not instantiate SecureKey. Error: {e}")
        
    # Verify private field doesn't exist under raw name
    assert not hasattr(key, '__secret'), "SecureKey instance should not expose raw '__secret' attribute"
    
    # Verify Name Mangling occurred
    assert hasattr(key, '_SecureKey__secret'), "SecureKey instance should name-mangle '__secret' to '_SecureKey__secret'"
    assert getattr(key, '_SecureKey__secret') == "secret123", "Mangled attribute value mismatch"
    
    # Verify verify_secret works
    assert key.verify_secret("wrong_secret") is False, "verify_secret returned True for wrong secret"
    assert key.verify_secret("secret123") is True, "verify_secret returned False for correct secret"

run_test("SecureKey name mangling and verification utility", test_secure_key)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 4 assignments.")
    print(f"Proceed to Day 5 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day4_assignment.py")
