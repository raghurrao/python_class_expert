# Day 12 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day12_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week3_dunder_methods.day12_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day12_assignment.py. Error: {e}")
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

print("Starting Day 12 Tests...\n")

# 1. Money Math & Comparison Tests
def test_money_operators():
    assert hasattr(assignment, 'Money'), "Money class missing"
    
    m1 = assignment.Money(10.50, "USD")
    m2 = assignment.Money(5.25, "USD")
    m_eur = assignment.Money(10.50, "EUR")
    
    # Add
    m3 = m1 + m2
    assert m3.amount == 15.75
    assert m3.currency == "USD"
    
    # Sub
    m4 = m1 - m2
    assert m4.amount == 5.25
    
    # Error on currency mismatch
    try:
        m1 + m_eur
        raise AssertionError("Adding different currencies should raise ValueError")
    except ValueError:
        pass
        
    try:
        m1 - m_eur
        raise AssertionError("Subtracting different currencies should raise ValueError")
    except ValueError:
        pass
        
    # Compare
    assert m2 < m1
    assert m1 > m2  # inferred
    try:
        m2 < m_eur
        raise AssertionError("Comparing different currencies should raise ValueError")
    except ValueError:
        pass

run_test("Money addition, subtraction, and comparison rules", test_money_operators)

# 2. Scalar Multiplication Tests
def test_money_multiplication():
    m = assignment.Money(10.0, "USD")
    
    # Mul
    m_double = m * 2
    assert m_double.amount == 20.0
    assert m_double.currency == "USD"
    
    # Rmul
    m_triple = 3.5 * m
    assert m_triple.amount == 35.0
    
    # Invalid multiplier
    try:
        m * "two"
        raise AssertionError("Multiplying by string should raise TypeError or return NotImplemented")
    except TypeError:
        pass

run_test("Money scalar and reflected multiplication", test_money_multiplication)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 12 assignments.")
    print(f"Proceed to Day 13 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day12_assignment.py")
