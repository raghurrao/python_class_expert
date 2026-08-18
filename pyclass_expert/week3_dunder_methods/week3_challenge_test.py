# Week 3 Challenge Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python week3_challenge_test.py
# It will verify if your challenge code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week3_dunder_methods.week3_challenge as challenge
except ImportError as e:
    print(f"[FAIL] Could not import week3_challenge.py. Error: {e}")
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

print("Starting Week 3 Challenge Tests...\n")

records = [
    {"id": 1, "name": "Alice", "role": "admin"},
    {"id": 2, "name": "Bob", "role": "user"},
    {"id": 3, "name": "Charlie", "role": "user"}
]

# 1. Container & Sequence tests
def test_dataset_container():
    assert hasattr(challenge, 'Dataset'), "Dataset class missing"
    
    data = challenge.Dataset(records)
    
    # len
    assert len(data) == 3, f"Expected length 3, got {len(data)}"
    
    # getitem index
    assert data[0] == {"id": 1, "name": "Alice", "role": "admin"}
    
    # getitem slice (returns Dataset)
    slice_data = data[0:2]
    assert isinstance(slice_data, challenge.Dataset), "Slices must return a new Dataset instance"
    assert len(slice_data) == 2
    assert slice_data[1] == {"id": 2, "name": "Bob", "role": "user"}
    
    # contains check
    assert "Alice" in data
    assert "user" in data
    assert "nonexistent" not in data
    
    # iteration check
    items = list(data)
    assert items == records

run_test("Challenge - Container & Sequence protocols", test_dataset_container)

# 2. Representations and Math Operators tests
def test_dataset_math():
    data1 = challenge.Dataset(records[0:2])
    data2 = challenge.Dataset(records[2:3])
    
    # representation
    assert str(data1) == "Dataset with 2 records", f"Str representation mismatch: '{str(data1)}'"
    assert repr(data1) == f"Dataset({records[0:2]})"
    
    # add operator
    combined = data1 + data2
    assert isinstance(combined, challenge.Dataset)
    assert len(combined) == 3
    assert combined[2] == {"id": 3, "name": "Charlie", "role": "user"}
    
    # equality
    data3 = challenge.Dataset(records[0:2])
    assert data1 == data3
    assert data1 != data2

run_test("Challenge - Presentation and math operators", test_dataset_math)

# 3. Query (Callable) and Context Manager tests
def test_dataset_query_context():
    data = challenge.Dataset(records)
    
    # call queries
    users = data(role="user")
    assert isinstance(users, challenge.Dataset)
    assert len(users) == 2
    assert users[0]["name"] == "Bob"
    assert users[1]["name"] == "Charlie"
    
    user_alice = data(role="admin", name="Alice")
    assert len(user_alice) == 1
    
    empty_res = data(role="manager")
    assert len(empty_res) == 0
    
    # context manager successful
    with data as mutable_list:
        mutable_list.append({"id": 4, "name": "David", "role": "guest"})
        
    assert len(data) == 4
    assert data[3]["name"] == "David"
    
    # context manager failing (triggers rollback)
    try:
        with data as mutable_list:
            mutable_list.append({"id": 5, "name": "Eve", "role": "admin"})
            raise RuntimeError("Failure occurred inside block!")
    except RuntimeError:
        pass
        
    # Check that Eve is not in dataset
    assert len(data) == 4, f"Dataset did not roll back! Current length: {len(data)}"
    assert "Eve" not in data

run_test("Challenge - Callable queries and transactional context management", test_dataset_query_context)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed the Week 3 Challenge.")
    print(f"You have fully mastered Python's Magic/Dunder Methods!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in week3_challenge.py")
