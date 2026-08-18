# Day 9 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day9_test.py
# It will verify if your assignment code is correct!

import sys
import os
from abc import ABC

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week2_relationships.day9_assignment as assignment
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

# 1. Base Class Tests
def test_abstract_base():
    assert hasattr(assignment, 'StorageSource'), "StorageSource class missing"
    assert issubclass(assignment.StorageSource, ABC), "StorageSource must inherit from abc.ABC"
    
    # Assert that StorageSource cannot be instantiated
    try:
        assignment.StorageSource()
        raise AssertionError("StorageSource should be an abstract class and not instantiable!")
    except TypeError:
        pass  # Success

run_test("StorageSource Abstract Base Class enforcement", test_abstract_base)

# 2. LocalStorage Tests
def test_local_storage():
    assert hasattr(assignment, 'LocalStorage'), "LocalStorage class missing"
    assert issubclass(assignment.LocalStorage, assignment.StorageSource), "LocalStorage must inherit StorageSource"
    
    try:
        local = assignment.LocalStorage()
    except TypeError as e:
        raise AssertionError(f"LocalStorage could not be instantiated. Did you implement all abstract methods? Error: {e}")
        
    local.write("configs.json", "{'theme': 'dark'}")
    assert local.read("configs.json") == "{'theme': 'dark'}"
    
    try:
        local.read("nonexistent.txt")
        raise AssertionError("Reading nonexistent path should raise FileNotFoundError")
    except FileNotFoundError:
        pass

run_test("LocalStorage concrete implementation", test_local_storage)

# 3. CloudStorage Tests
def test_cloud_storage():
    assert hasattr(assignment, 'CloudStorage'), "CloudStorage class missing"
    assert issubclass(assignment.CloudStorage, assignment.StorageSource), "CloudStorage must inherit StorageSource"
    
    try:
        cloud = assignment.CloudStorage()
    except TypeError as e:
        raise AssertionError(f"CloudStorage could not be instantiated. Did you implement all abstract methods? Error: {e}")
        
    cloud.write("image.png", "binary_data_here")
    assert cloud.read("image.png") == "binary_data_here"
    
    try:
        cloud.read("missing_key")
        raise AssertionError("Reading nonexistent path should raise FileNotFoundError")
    except FileNotFoundError:
        pass

run_test("CloudStorage concrete implementation", test_cloud_storage)

# 4. Partial Implementation test
def test_partial_implementation():
    # Make sure a class that doesn't implement read is not instantiable
    class BadStorage(assignment.StorageSource):
        def write(self, path, data):
            pass
            
    try:
        BadStorage()
        raise AssertionError("A class missing read() implementation should not be instantiable")
    except TypeError:
        pass  # Success

run_test("Incomplete subclass non-instantiability contract", test_partial_implementation)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 9 assignments.")
    print(f"Proceed to Day 10 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day9_assignment.py")
