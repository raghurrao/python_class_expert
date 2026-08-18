# Day 1 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day1_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week1_basics.day1_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day1_assignment.py. Error: {e}")
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

print("Starting Day 1 Tests...\n")

# 1. Test get_system_info
def test_get_system_info():
    assert hasattr(assignment, 'get_system_info'), "get_system_info function not found in day1_assignment.py"
    
    info = assignment.get_system_info()
    assert isinstance(info, dict), f"Expected get_system_info to return a dict, got {type(info).__name__}"
    assert 'python_version' in info, "Dictionary missing 'python_version' key"
    assert 'workspace_path' in info, "Dictionary missing 'workspace_path' key"
    
    # Check values
    assert isinstance(info['python_version'], str), "python_version must be a string"
    assert sys.version in info['python_version'], f"Expected python_version to contain '{sys.version}'"
    assert isinstance(info['workspace_path'], str), "workspace_path must be a string"
    assert os.path.abspath(current_dir) == os.path.abspath(info['workspace_path']), "workspace_path does not match this file's folder path"

run_test("Verify get_system_info dictionary structures", test_get_system_info)

# 2. Test verify_setup
def test_verify_setup():
    assert hasattr(assignment, 'verify_setup'), "verify_setup function not found in day1_assignment.py"
    
    msg_alice = assignment.verify_setup("Alice")
    assert isinstance(msg_alice, str), f"Expected verify_setup to return a string, got {type(msg_alice).__name__}"
    expected_alice = "Hello Alice! Your Python environment in VS Code is successfully configured."
    assert msg_alice == expected_alice, f"Expected output: '{expected_alice}', got: '{msg_alice}'"
    
    msg_bob = assignment.verify_setup("Bob")
    expected_bob = "Hello Bob! Your Python environment in VS Code is successfully configured."
    assert msg_bob == expected_bob, f"Expected output: '{expected_bob}', got: '{msg_bob}'"

run_test("Verify welcome setup message format", test_verify_setup)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 1 assignments.")
    print(f"Proceed to Day 2 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day1_assignment.py")
