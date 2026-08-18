# Day 6 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day6_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week2_relationships.day6_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day6_assignment.py. Error: {e}")
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

print("Starting Day 6 Tests...\n")

# 1. Vehicle Tests
def test_vehicle():
    assert hasattr(assignment, 'Vehicle'), "Vehicle class missing"
    v = assignment.Vehicle("Toyota", 120)
    assert v.brand == "Toyota"
    assert v.speed == 120
    assert v.describe() == "Brand: Toyota, Speed: 120 km/h"

run_test("Vehicle base class implementation", test_vehicle)

# 2. Car Tests
def test_car():
    assert hasattr(assignment, 'Car'), "Car class missing"
    assert issubclass(assignment.Car, assignment.Vehicle), "Car must inherit from Vehicle"
    
    c = assignment.Car("Honda", 180, "Gasoline")
    assert c.brand == "Honda"
    assert c.speed == 180
    assert c.fuel_type == "Gasoline"
    assert c.describe() == "Brand: Honda, Speed: 180 km/h, Fuel Type: Gasoline"

run_test("Car subclass (Single Inheritance & overrides)", test_car)

# 3. ElectricCar Tests
def test_electric_car():
    assert hasattr(assignment, 'ElectricCar'), "ElectricCar class missing"
    assert issubclass(assignment.ElectricCar, assignment.Car), "ElectricCar must inherit from Car"
    assert issubclass(assignment.ElectricCar, assignment.Vehicle), "ElectricCar must inherit from Vehicle"
    
    ec = assignment.ElectricCar("Tesla", 250, 85)
    assert ec.brand == "Tesla"
    assert ec.speed == 250
    assert ec.fuel_type == "Electric"
    assert ec.battery_capacity == 85
    assert ec.describe() == "Brand: Tesla, Speed: 250 km/h, Fuel Type: Electric, Battery: 85 kWh"

run_test("ElectricCar sub-subclass (Multi-level constructor chaining)", test_electric_car)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 6 assignments.")
    print(f"Proceed to Day 7 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day6_assignment.py")
