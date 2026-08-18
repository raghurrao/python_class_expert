# Day 20 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day20_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week4_metaprogramming.day20_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day20_assignment.py. Error: {e}")
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

print("Starting Day 20 Tests...\n")

# 1. EmployeeRecord Dataclass Tests
def test_employee_record():
    assert hasattr(assignment, 'EmployeeRecord'), "EmployeeRecord class missing"
    
    # Try successful instantiation
    try:
        rec1 = assignment.EmployeeRecord("John", 50000.0)
        rec2 = assignment.EmployeeRecord("Bob", 60000.0, 5000.0, ["remote", "tech"])
    except Exception as e:
        raise AssertionError(f"Could not instantiate EmployeeRecord dataclass. Error: {e}")
        
    # Check default arguments
    assert rec1.bonus == 0.0
    assert rec1.tags == []
    assert rec1.total_pay == 50000.0, f"Expected total_pay 50000.0, got {rec1.total_pay}"
    
    # Check custom arguments and post_init
    assert rec2.bonus == 5000.0
    assert rec2.tags == ["remote", "tech"]
    assert rec2.total_pay == 65000.0, f"Expected total_pay 65000.0, got {rec2.total_pay}"
    
    # Ensure tags lists are independent instances (default_factory verification)
    assert rec1.tags is not rec2.tags, "Tags lists are shared (default_factory was not used correctly)"

run_test("EmployeeRecord dataclass parameters and post_init hook", test_employee_record)

# 2. Pixel Slots Tests
def test_pixel_slots():
    assert hasattr(assignment, 'Pixel'), "Pixel class missing"
    
    try:
        p = assignment.Pixel(10, 20, "red")
    except Exception as e:
        raise AssertionError(f"Could not instantiate Pixel. Error: {e}")
        
    assert p.x == 10
    assert p.y == 20
    assert p.color == "red"
    
    # Check that __dict__ does not exist (verifying slots are active)
    assert not hasattr(p, '__dict__'), "Pixel should not have __dict__ attribute (verify __slots__ is defined)"
    
    # Check that assigning unregistered attributes fails
    try:
        p.z = 30
        raise AssertionError("Adding unregistered attribute to slot-based class should raise AttributeError")
    except AttributeError:
        pass

run_test("Pixel memory-optimized slot validation", test_pixel_slots)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 20 assignments.")
    print(f"Proceed to the Capstone Project when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day20_assignment.py")
