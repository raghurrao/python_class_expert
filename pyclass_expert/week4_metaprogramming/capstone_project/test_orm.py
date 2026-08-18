# Capstone Project Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python test_orm.py
# It will verify if your ORM code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week4_metaprogramming.capstone_project.orm as orm
except ImportError as e:
    print(f"[FAIL] Could not import orm.py. Error: {e}")
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

print("Starting Capstone ORM Tests...\n")

# Reset database simulator before tests
orm.SIMULATED_DB.clear()

# Define test models
if hasattr(orm, 'Model') and hasattr(orm, 'IntegerField') and hasattr(orm, 'StringField'):
    class User(orm.Model):
        username = orm.StringField(min_length=3, max_length=15)
        age = orm.IntegerField(min_value=18, max_value=120)
else:
    User = None

# 1. Metaclass Scanning and Table Setup Tests
def test_metaclass_scaffold():
    assert User is not None, "Model or fields classes missing"
    assert hasattr(User, '_fields'), "Metaclass failed to attach _fields directory"
    assert "username" in User._fields, "username field missing from _fields registry"
    assert "age" in User._fields
    
    assert "User" in orm.SIMULATED_DB, "Metaclass failed to register table in SIMULATED_DB"
    assert orm.SIMULATED_DB["User"] == []

run_test("ORM Metaclass table setup and schema scanning", test_metaclass_scaffold)

# 2. Field Type & Boundaries Validation Tests
def test_field_validation():
    # Valid assignments should succeed
    try:
        u = User(username="alice", age=25)
    except Exception as e:
        raise AssertionError(f"Failed to instantiate valid model. Error: {e}")
        
    assert u.username == "alice"
    assert u.age == 25
    
    # Check default None assignments
    u_partial = User(username="bob")
    assert u_partial.username == "bob"
    assert u_partial.age is None
    
    # Invalid username type
    try:
        User(username=12345, age=20)
        raise AssertionError("Non-string value for StringField should raise TypeError")
    except TypeError:
        pass
        
    # Invalid age type
    try:
        User(username="bob", age="twenty")
        raise AssertionError("Non-integer value for IntegerField should raise TypeError")
    except TypeError:
        pass
        
    # String boundary violations
    try:
        User(username="al", age=20)  # Too short (min is 3)
        raise AssertionError("String below min_length should raise ValueError")
    except ValueError:
        pass
        
    try:
        User(username="a" * 16, age=20)  # Too long (max is 15)
        raise AssertionError("String above max_length should raise ValueError")
    except ValueError:
        pass
        
    # Integer boundary violations
    try:
        User(username="bob", age=17)  # Too young (min is 18)
        raise AssertionError("Integer below min_value should raise ValueError")
    except ValueError:
        pass
        
    try:
        User(username="bob", age=121)  # Too old (max is 120)
        raise AssertionError("Integer above max_value should raise ValueError")
    except ValueError:
        pass
        
    # Unregistered field names
    try:
        User(username="bob", age=20, email="bob@ex.com")
        raise AssertionError("Defining unregistered keywords should raise ValueError")
    except ValueError:
        pass

run_test("ORM Field validation constraints (type and boundary checks)", test_field_validation)

# 3. Model DB operations tests
def test_db_operations():
    orm.SIMULATED_DB["User"].clear()
    
    u1 = User(username="charlie", age=30)
    u2 = User(username="david", age=45)
    
    u1.save()
    u2.save()
    
    # Check database contents
    assert len(orm.SIMULATED_DB["User"]) == 2
    assert orm.SIMULATED_DB["User"][0] is u1
    assert orm.SIMULATED_DB["User"][1] is u2
    
    # Check all() retrieval
    all_users = User.all()
    assert all_users == [u1, u2]

run_test("ORM Database saving and list queries", test_db_operations)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed the Capstone Project!")
    print(f"You have officially mastered Python Classes and OOP!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in orm.py")
