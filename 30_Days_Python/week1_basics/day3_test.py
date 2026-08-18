# Day 3 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day3_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week1_basics.day3_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day3_assignment.py. Error: {e}")
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

print("Starting Day 3 Tests...\n")

# 1. Test fizz_buzz
def test_fizz_buzz():
    assert hasattr(assignment, 'fizz_buzz'), "fizz_buzz not found in day3_assignment.py"
    
    val1 = assignment.fizz_buzz(5)
    assert val1 == "1, 2, Fizz, 4, Buzz", f"Expected fizz_buzz(5) to be '1, 2, Fizz, 4, Buzz', got '{val1}'"
    
    val2 = assignment.fizz_buzz(15)
    assert val2.endswith("13, 14, FizzBuzz"), f"Expected fizz_buzz(15) to end with '13, 14, FizzBuzz', got '{val2}'"

run_test("Verify FizzBuzz sequence output formatting", test_fizz_buzz)

# 2. Test is_prime
def test_is_prime():
    assert hasattr(assignment, 'is_prime'), "is_prime not found in day3_assignment.py"
    
    assert assignment.is_prime(2) is True, "2 is prime"
    assert assignment.is_prime(3) is True, "3 is prime"
    assert assignment.is_prime(4) is False, "4 is not prime"
    assert assignment.is_prime(17) is True, "17 is prime"
    assert assignment.is_prime(1) is False, "1 is not prime"
    assert assignment.is_prime(0) is False, "0 is not prime"
    assert assignment.is_prime(-7) is False, "Negative numbers are not prime"

run_test("Verify prime number detection logic", test_is_prime)

# 3. Test sum_even_numbers
def test_sum_even_numbers():
    assert hasattr(assignment, 'sum_even_numbers'), "sum_even_numbers not found in day3_assignment.py"
    
    assert assignment.sum_even_numbers(6) == 12, f"Expected sum_even_numbers(6) to be 12, got {assignment.sum_even_numbers(6)}"
    assert assignment.sum_even_numbers(11) == 30, f"Expected sum_even_numbers(11) to be 30, got {assignment.sum_even_numbers(11)}"
    assert assignment.sum_even_numbers(0) == 0, f"Expected sum_even_numbers(0) to be 0, got {assignment.sum_even_numbers(0)}"

run_test("Verify loop summation logic", test_sum_even_numbers)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 3 assignments.")
    print(f"Proceed to Day 4 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day3_assignment.py")
