# Day 5 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day5_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week1_foundations.day5_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day5_assignment.py. Error: {e}")
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

print("Starting Day 5 Tests...\n")

# 1. Circle Tests
def test_circle_properties():
    assert hasattr(assignment, 'Circle'), "Circle class not found"
    
    try:
        c = assignment.Circle(5)
    except TypeError as e:
        raise AssertionError(f"Could not instantiate Circle. Error: {e}")
        
    assert c.radius == 5, f"Expected radius 5, got {c.radius}"
    assert c.diameter == 10, f"Expected diameter 10, got {c.diameter}"
    assert abs(c.area - 78.53975) < 0.001, f"Expected area ~78.54, got {c.area}"
    
    # Update radius
    c.radius = 10
    assert c.radius == 10
    assert c.diameter == 20
    assert abs(c.area - 314.159) < 0.001
    
    # Try invalid radius setter value
    try:
        c.radius = -1
        raise AssertionError("c.radius = -1 should have raised ValueError but did not")
    except ValueError:
        pass  # Success
        
    # Verify diameter and area are read-only
    try:
        c.diameter = 15
        raise AssertionError("c.diameter setter should raise AttributeError (read-only) but did not")
    except AttributeError:
        pass  # Success
        
    try:
        c.area = 100
        raise AssertionError("c.area setter should raise AttributeError (read-only) but did not")
    except AttributeError:
        pass  # Success

run_test("Circle class properties (getter, setter, and read-only attributes)", test_circle_properties)

# 2. Temperature Tests
def test_temperature_sync():
    assert hasattr(assignment, 'Temperature'), "Temperature class not found"
    
    try:
        t = assignment.Temperature(25.0)
    except TypeError as e:
        raise AssertionError(f"Could not instantiate Temperature. Error: {e}")
        
    assert t.celsius == 25.0, f"Expected celsius 25.0, got {t.celsius}"
    # 25 * 1.8 + 32 = 45 + 32 = 77.0
    assert abs(t.fahrenheit - 77.0) < 0.001, f"Expected fahrenheit 77.0, got {t.fahrenheit}"
    
    # Set fahrenheit
    t.fahrenheit = 32.0
    assert abs(t.celsius - 0.0) < 0.001, f"Expected celsius 0.0 after setting fahrenheit 32.0, got {t.celsius}"
    
    # Set celsius
    t.celsius = 100.0
    assert abs(t.fahrenheit - 212.0) < 0.001, f"Expected fahrenheit 212.0, got {t.fahrenheit}"

run_test("Temperature synchronization between Celsius and Fahrenheit", test_temperature_sync)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 5 assignments.")
    print(f"Proceed to the Week 1 Challenge when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day5_assignment.py")
