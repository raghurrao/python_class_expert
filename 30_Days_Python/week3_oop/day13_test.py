# Day 13 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day13_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week3_oop.day13_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day13_assignment.py. Error: {e}")
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

print("Starting Day 13 Tests...\n")

# 1. Test Vehicle
def test_vehicle():
    assert hasattr(assignment, 'Vehicle'), "Vehicle class not found"
    
    v = assignment.Vehicle("Toyota", "Corolla")
    assert v.make == "Toyota"
    assert v.model == "Corolla"
    assert v.describe() == "Vehicle: Toyota Corolla", f"Got: '{v.describe()}'"

run_test("Verify Vehicle base class", test_vehicle)

# 2. Test Car
def test_car():
    assert hasattr(assignment, 'Car'), "Car class not found"
    assert issubclass(assignment.Car, assignment.Vehicle), "Car must inherit from Vehicle"
    
    c = assignment.Car("Honda", "Civic", 4)
    assert c.make == "Honda"
    assert c.num_doors == 4
    assert c.describe() == "Car: Honda Civic with 4 doors", f"Got: '{c.describe()}'"

run_test("Verify Car subclass overriding and attributes", test_car)

# 3. Test ElectricCar
def test_electric_car():
    assert hasattr(assignment, 'ElectricCar'), "ElectricCar class not found"
    assert issubclass(assignment.ElectricCar, assignment.Car), "ElectricCar must inherit from Car"
    
    ec = assignment.ElectricCar("Tesla", "Model 3", 4, 75)
    assert ec.make == "Tesla"
    assert ec.battery_capacity == 75
    assert ec.describe() == "Electric Car: Tesla Model 3 with 4 doors and 75kWh battery", f"Got: '{ec.describe()}'"

run_test("Verify ElectricCar multi-level subclass overriding", test_electric_car)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 13 assignments.")
    print(f"Proceed to Day 14 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day13_assignment.py")
