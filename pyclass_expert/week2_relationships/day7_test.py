# Day 7 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day7_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week2_relationships.day7_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day7_assignment.py. Error: {e}")
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

print("Starting Day 7 Tests...\n")

# 1. Cooperative SmartDoc Tests
def test_smart_doc():
    assert hasattr(assignment, 'SmartDoc'), "SmartDoc class missing"
    assert issubclass(assignment.SmartDoc, assignment.Loggable), "SmartDoc must inherit Loggable"
    assert issubclass(assignment.SmartDoc, assignment.Storable), "SmartDoc must inherit Storable"
    
    try:
        doc = assignment.SmartDoc("report.txt", log_format="*** {} ***", storage_dir="/var/log")
    except TypeError as e:
        raise AssertionError(f"Could not instantiate SmartDoc. Ensure all classes pass **kwargs to super().__init__. Error: {e}")
        
    assert doc.filename == "report.txt", "Filename attribute incorrect"
    assert doc.log_format == "*** {} ***", "Log format was not successfully initialized"
    assert doc.storage_dir == "/var/log", "Storage dir was not successfully initialized"
    
    assert doc.log("Hello") == "*** Hello ***", f"Expected '*** Hello ***', got '{doc.log('Hello')}'"
    assert doc.save("raw data") == "Saving data to /var/log", f"Expected 'Saving data to /var/log', got '{doc.save('raw data')}'"

run_test("Cooperative multi-inheritance (SmartDoc)", test_smart_doc)

# 2. Diamond Problem Chaining Tests
def test_diamond_mro():
    assert hasattr(assignment, 'Bottom'), "Bottom class missing"
    
    # Check MRO order
    mro_names = [cls.__name__ for cls in assignment.Bottom.mro()]
    expected_mro = ["Bottom", "Left", "Right", "Top", "object"]
    assert mro_names == expected_mro, f"Incorrect MRO list. Expected {expected_mro}, got {mro_names}"
    
    # Check Diamond method lookup resolution
    b = assignment.Bottom()
    expected_msg = "Bottom -> Left -> Right -> Top"
    msg = b.message()
    assert msg == expected_msg, f"Method chain resolved incorrectly.\nExpected: '{expected_msg}'\nGot: '{msg}'"

run_test("Diamond inheritance resolution and MRO method chaining", test_diamond_mro)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 7 assignments.")
    print(f"Proceed to Day 8 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day7_assignment.py")
