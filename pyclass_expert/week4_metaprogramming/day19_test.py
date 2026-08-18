# Day 19 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day19_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week4_metaprogramming.day19_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day19_assignment.py. Error: {e}")
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

print("Starting Day 19 Tests...\n")

# Reset registry before tests
if hasattr(assignment, 'ApiHandler'):
    assignment.ApiHandler.routes = {}

# 1. Metaclass Tests
def test_metaclass():
    assert hasattr(assignment, 'UppercaseAttributesMeta'), "UppercaseAttributesMeta class missing"
    
    # Define a test class using the metaclass
    class TestClass(metaclass=assignment.UppercaseAttributesMeta):
        foo = "bar"
        _internal = "secret"
        
        def hello(self):
            return "world"
            
    # Check that 'foo' got converted to 'FOO'
    assert hasattr(TestClass, 'FOO'), "Public attribute 'foo' was not converted to uppercase class attribute"
    assert not hasattr(TestClass, 'foo'), "Original public attribute 'foo' should not remain lowercase"
    assert TestClass.FOO == "bar"
    
    # Check internal attributes are untouched
    assert hasattr(TestClass, '_internal')
    assert not hasattr(TestClass, '_INTERNAL')
    
    # Check methods (which are functions in attrs dictionary during class creation)
    # Since 'hello' starts with lowercase letter, it gets capitalized to 'HELLO'!
    assert hasattr(TestClass, 'HELLO')
    assert not hasattr(TestClass, 'hello')

run_test("UppercaseAttributesMeta class transformation", test_metaclass)

# 2. __init_subclass__ registry tests
def test_handler_registration():
    assert hasattr(assignment, 'ApiHandler'), "ApiHandler base class missing"
    
    # Declare subclasses
    class HomeHandler(assignment.ApiHandler, route="/"):
        pass
        
    class UsersHandler(assignment.ApiHandler, route="/users"):
        pass
        
    class NonRoutedHandler(assignment.ApiHandler):
        pass
        
    assert assignment.ApiHandler.routes == {
        "/": HomeHandler,
        "/users": UsersHandler
    }, f"Route registry contents incorrect: {assignment.ApiHandler.routes}"

run_test("Subclass auto-registration with __init_subclass__", test_handler_registration)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 19 assignments.")
    print(f"Proceed to Day 20 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day19_assignment.py")
