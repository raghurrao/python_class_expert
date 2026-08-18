# Day 8 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day8_test.py
# It will verify if your assignment code is correct!

import sys
import os
import json

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week2_functions_io.day8_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day8_assignment.py. Error: {e}")
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

# Temporary files for testing
test_txt_path = os.path.join(current_dir, "temp_test.txt")
test_json_path = os.path.join(current_dir, "temp_test.json")

def cleanup():
    for path in [test_txt_path, test_json_path]:
        if os.path.exists(path):
            try:
                os.remove(path)
            except OSError:
                pass

print("Starting Day 8 Tests...\n")
cleanup()

# 1. Test write_text_file
def test_write_text_file():
    assert hasattr(assignment, 'write_text_file'), "write_text_file not found in day8_assignment.py"
    
    content = "Hello testing!\nLine 2 of test."
    assignment.write_text_file(test_txt_path, content)
    
    assert os.path.exists(test_txt_path), "File was not created"
    with open(test_txt_path, "r") as f:
        read_content = f.read()
    assert read_content == content, f"Expected '{content}', got '{read_content}'"

run_test("Verify text writing capabilities", test_write_text_file)

# 2. Test append_to_file
def test_append_to_file():
    assert hasattr(assignment, 'append_to_file'), "append_to_file not found in day8_assignment.py"
    
    # Start fresh
    if os.path.exists(test_txt_path):
        os.remove(test_txt_path)
        
    assignment.append_to_file(test_txt_path, "Line A")
    assignment.append_to_file(test_txt_path, "Line B")
    
    with open(test_txt_path, "r") as f:
        lines = f.readlines()
        
    assert len(lines) == 2, f"Expected 2 lines, got {len(lines)}"
    assert lines[0] == "Line A\n", f"Expected 'Line A\\n', got {repr(lines[0])}"
    assert lines[1] == "Line B\n", f"Expected 'Line B\\n', got {repr(lines[1])}"

run_test("Verify text appending on new lines", test_append_to_file)

# 3. Test read_and_parse_json
def test_read_and_parse_json():
    assert hasattr(assignment, 'read_and_parse_json'), "read_and_parse_json not found in day8_assignment.py"
    
    data = {"project": "Python Study", "completed": False, "days": 30}
    with open(test_json_path, "w") as f:
        json.dump(data, f)
        
    parsed = assignment.read_and_parse_json(test_json_path)
    assert parsed == data, f"Expected parsed JSON to be {data}, got {parsed}"

run_test("Verify JSON parsing", test_read_and_parse_json)

# Cleanup after testing
cleanup()

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 8 assignments.")
    print(f"Proceed to Day 9 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day8_assignment.py")
