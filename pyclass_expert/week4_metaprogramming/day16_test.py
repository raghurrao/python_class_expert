# Day 16 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day16_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week4_metaprogramming.day16_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day16_assignment.py. Error: {e}")
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

print("Starting Day 16 Tests...\n")

# 1. JSONWrapper Tests
def test_json_wrapper():
    assert hasattr(assignment, 'JSONWrapper'), "JSONWrapper class missing"
    
    raw_data = {"name": "Alice", "age": 25, "role": "admin"}
    wrapper = assignment.JSONWrapper(raw_data)
    
    assert wrapper.data is raw_data, "data attribute missing or mismatch"
    assert wrapper.name == "Alice", "Failed to retrieve 'name' attribute"
    assert wrapper.age == 25
    
    # Assert missing attributes raise AttributeError
    try:
        wrapper.nonexistent
        raise AssertionError("Accessing missing attribute should raise AttributeError")
    except AttributeError:
        pass

run_test("JSONWrapper attribute lookup redirection (__getattr__)", test_json_wrapper)

# 2. StrictObject Tests
def test_strict_object():
    assert hasattr(assignment, 'StrictObject'), "StrictObject class missing"
    
    obj = assignment.StrictObject()
    
    # Assign valid numeric values
    try:
        obj.score = 100
        obj.temperature = 98.6
    except TypeError as e:
        raise AssertionError(f"Could not assign numeric values to StrictObject. Error: {e}")
        
    assert obj.score == 100
    assert obj.temperature == 98.6
    
    # Assign invalid types
    try:
        obj.score = "one hundred"
        raise AssertionError("Assigning string to public attribute should raise TypeError")
    except TypeError:
        pass
        
    try:
        obj.username = "alice"
        raise AssertionError("Assigning string to public attribute should raise TypeError")
    except TypeError:
        pass
        
    # Assign protected/private values (should bypass checks)
    try:
        obj._status = "active"
        obj.__checksum = "abc"
    except TypeError as e:
        raise AssertionError(f"Assignment to internal attributes raised unexpected TypeError: {e}")
        
    assert obj._status == "active"
    assert obj._StrictObject__checksum == "abc"

run_test("StrictObject attribute set validation (__setattr__)", test_strict_object)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 16 assignments.")
    print(f"Proceed to Day 17 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day16_assignment.py")
