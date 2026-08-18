# Day 12 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day12_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week3_oop.day12_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day12_assignment.py. Error: {e}")
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

print("Starting Day 12 Tests...\n")

# 1. Test Employee encapsulation
def test_employee_properties():
    assert hasattr(assignment, 'Employee'), "Employee class not found in day12_assignment.py"
    
    emp = assignment.Employee("Jane", 50000.0)
    assert not hasattr(emp, '__salary'), "Salary attribute must be private (double underscore)"
    assert hasattr(emp, 'salary'), "Getter property for salary not found"
    
    assert emp.salary == 50000.0, f"Expected 50000.0, got {emp.salary}"
    
    emp.salary = 60000.0
    assert emp.salary == 60000.0, "Salary setter did not update the value"
    
    # Try invalid salary
    try:
        emp.salary = -100
        raise AssertionError("Did not raise ValueError for negative salary setter")
    except ValueError as e:
        assert str(e) == "Salary cannot be negative", f"Unexpected error message: {e}"

run_test("Verify Employee private attributes and validation properties", test_employee_properties)

# 2. Test Temperature features
def test_temperature_features():
    assert hasattr(assignment, 'Temperature'), "Temperature class not found in day12_assignment.py"
    
    temp = assignment.Temperature(0.0)
    assert hasattr(temp, '_celsius'), "Celsius attribute should be protected (_celsius)"
    assert temp._celsius == 0.0
    
    # Get Fahrenheit: 0 C should be 32 F
    assert temp.fahrenheit == 32.0, f"Expected 32.0, got {temp.fahrenheit}"
    
    # Set Fahrenheit: 212 F should change Celsius to 100
    temp.fahrenheit = 212.0
    assert temp._celsius == 100.0, f"Expected Celsius to update to 100.0, got {temp._celsius}"
    
    # Check classmethod factory
    temp2 = assignment.Temperature.from_fahrenheit(50.0)  # (50-32)/1.8 = 10 C
    assert isinstance(temp2, assignment.Temperature), "from_fahrenheit did not return a Temperature instance"
    assert temp2._celsius == 10.0, f"Expected Celsius of factory object to be 10.0, got {temp2._celsius}"
    
    # Check staticmethod
    k = assignment.Temperature.celsius_to_kelvin(0.0)
    assert k == 273.15, f"Expected Kelvin to be 273.15, got {k}"

run_test("Verify Temperature converter property, classmethod, and staticmethod", test_temperature_features)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 12 assignments.")
    print(f"Proceed to Day 13 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day12_assignment.py")
