# Day 2 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day2_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week1_basics.day2_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day2_assignment.py. Error: {e}")
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

print("Starting Day 2 Tests...\n")

# 1. Test fahrenheit_to_celsius
def test_fahrenheit_to_celsius():
    assert hasattr(assignment, 'fahrenheit_to_celsius'), "fahrenheit_to_celsius not found in day2_assignment.py"
    
    val1 = assignment.fahrenheit_to_celsius(32)
    assert val1 == 0.0, f"Expected 32°F to be 0.0°C, got {val1}"
    
    val2 = assignment.fahrenheit_to_celsius(100)
    assert val2 == 37.78, f"Expected 100°F to be 37.78°C, got {val2}"
    
    val3 = assignment.fahrenheit_to_celsius(-40)
    assert val3 == -40.0, f"Expected -40°F to be -40.0°C, got {val3}"
    
    # Ensure float return type
    assert isinstance(val1, float), "Expected return value to be a float"

run_test("Verify temperature converter logic", test_fahrenheit_to_celsius)

# 2. Test calculate_compound_interest
def test_calculate_compound_interest():
    assert hasattr(assignment, 'calculate_compound_interest'), "calculate_compound_interest not found in day2_assignment.py"
    
    # P=1000, r=0.05, t=5, n=12 (compounded monthly)
    val1 = assignment.calculate_compound_interest(1000, 0.05, 5, 12)
    assert val1 == 1283.36, f"Expected compound interest total to be 1283.36, got {val1}"
    
    # P=5000, r=0.08, t=10, n=4 (compounded quarterly)
    val2 = assignment.calculate_compound_interest(5000, 0.08, 10, 4)
    assert val2 == 11040.20, f"Expected compound interest total to be 11040.20, got {val2}"

run_test("Verify compound interest calculator logic", test_calculate_compound_interest)

# 3. Test format_profile_card
def test_format_profile_card():
    assert hasattr(assignment, 'format_profile_card'), "format_profile_card not found in day2_assignment.py"
    
    card1 = assignment.format_profile_card("John Doe", 1996, "john.doe@example.com")
    expected1 = (
        "=== PROFILE CARD ===\n"
        "Name: John Doe\n"
        "Age: 30\n"
        "Email: john.doe@example.com\n"
        "===================="
    )
    assert card1 == expected1, f"Profile card formatting mismatch:\nExpected:\n{expected1}\n\nGot:\n{card1}"

run_test("Verify profile card formatting", test_format_profile_card)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 2 assignments.")
    print(f"Proceed to Day 3 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day2_assignment.py")
