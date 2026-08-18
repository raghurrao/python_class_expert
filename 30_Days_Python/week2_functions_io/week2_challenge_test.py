# Week 2 Challenge Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python week2_challenge_test.py
# It will verify if your task manager challenge code works!

import sys
import os
import json

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week2_functions_io.week2_challenge as challenge
except ImportError as e:
    print(f"[FAIL] Could not import week2_challenge.py. Error: {e}")
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

# Temporary path for testing file IO
test_tasks_json = os.path.join(current_dir, "temp_tasks.json")

def cleanup():
    if os.path.exists(test_tasks_json):
        try:
            os.remove(test_tasks_json)
        except OSError:
            pass

print("Starting Week 2 Challenge Tests...\n")
cleanup()

# 1. Test load_tasks (missing file)
def test_load_tasks_missing():
    assert hasattr(challenge, 'load_tasks'), "load_tasks not found"
    
    res = challenge.load_tasks(test_tasks_json)
    assert res == [], f"Expected empty list [] for missing file, got {res}"

run_test("Load tasks from missing file", test_load_tasks_missing)

# 2. Test add_task
def test_add_task():
    assert hasattr(challenge, 'add_task'), "add_task not found"
    
    tasks = []
    tasks = challenge.add_task(tasks, "Buy milk")
    assert len(tasks) == 1, "Expected task count to be 1"
    assert tasks[0]['id'] == 1, "First task ID should be 1"
    assert tasks[0]['title'] == "Buy milk", "Task title incorrect"
    assert tasks[0]['completed'] is False, "Task should start as incomplete"
    
    tasks = challenge.add_task(tasks, "Read Book")
    assert len(tasks) == 2, "Expected task count to be 2"
    assert tasks[1]['id'] == 2, "Second task ID should be 2"

run_test("Add tasks to list and check autoincrement ID", test_add_task)

# 3. Test complete_task
def test_complete_task():
    assert hasattr(challenge, 'complete_task'), "complete_task not found"
    
    tasks = [
        {'id': 1, 'title': 'Task A', 'completed': False},
        {'id': 2, 'title': 'Task B', 'completed': False}
    ]
    
    tasks = challenge.complete_task(tasks, 1)
    assert tasks[0]['completed'] is True, "Expected Task A completed to be True"
    assert tasks[1]['completed'] is False, "Expected Task B completed to be False"
    
    # Check invalid task ID
    tasks = challenge.complete_task(tasks, 99)
    assert len(tasks) == 2, "List should not change size for invalid IDs"

run_test("Mark task completed by ID", test_complete_task)

# 4. Test save_tasks and load_tasks (existing file)
def test_save_and_load_tasks():
    assert hasattr(challenge, 'save_tasks'), "save_tasks not found"
    
    tasks = [
        {'id': 1, 'title': 'First', 'completed': True},
        {'id': 2, 'title': 'Second', 'completed': False}
    ]
    
    challenge.save_tasks(test_tasks_json, tasks)
    assert os.path.exists(test_tasks_json), "JSON task file was not created"
    
    loaded = challenge.load_tasks(test_tasks_json)
    assert loaded == tasks, f"Expected loaded list to match saved list: {tasks}, got: {loaded}"

run_test("Serialize and deserialize tasks checklist to JSON file", test_save_and_load_tasks)

# Cleanup
cleanup()

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed the Week 2 Weekend Challenge.")
    print(f"You are now ready to progress to Week 3 (OOP)!")
else:
    print(f"FAILED: Some challenge tests failed. Check the errors above and fix your code in week2_challenge.py")
