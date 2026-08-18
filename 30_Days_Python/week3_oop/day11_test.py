# Day 11 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day11_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week3_oop.day11_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day11_assignment.py. Error: {e}")
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

print("Starting Day 11 Tests...\n")

# 1. Test Laptop class
def test_laptop():
    assert hasattr(assignment, 'Laptop'), "Laptop class not found in day11_assignment.py"
    
    laptop = assignment.Laptop("Dell", "XPS", 8)
    assert hasattr(laptop, 'brand'), "Missing brand attribute"
    assert hasattr(laptop, 'model'), "Missing model attribute"
    assert hasattr(laptop, 'ram'), "Missing ram attribute"
    
    assert laptop.brand == "Dell"
    assert laptop.ram == 8
    
    # Test method
    assert hasattr(laptop, 'upgrade_ram'), "Missing upgrade_ram method"
    laptop.upgrade_ram(8)
    assert laptop.ram == 16, f"Expected ram to be upgraded to 16, got {laptop.ram}"

run_test("Verify Laptop definition and RAM upgrade method", test_laptop)

# 2. Test BankAccount class
def test_bank_account():
    assert hasattr(assignment, 'BankAccount'), "BankAccount class not found in day11_assignment.py"
    
    # Check default balance
    acct = assignment.BankAccount("Bob")
    assert acct.owner == "Bob"
    assert acct.balance == 0.0, f"Expected default balance to be 0.0, got {acct.balance}"
    
    acct2 = assignment.BankAccount("Alice", 1000.0)
    assert acct2.balance == 1000.0
    
    # Check deposit
    new_bal = acct2.deposit(250.0)
    assert acct2.balance == 1250.0, "Balance not updated on deposit"
    assert new_bal == 1250.0, "Deposit method should return new balance"
    
    # Check withdrawal
    new_bal2 = acct2.withdraw(300.0)
    assert acct2.balance == 950.0, "Balance not updated on withdrawal"
    assert new_bal2 == 950.0, "Withdraw method should return new balance"
    
    # Check insufficient withdrawal
    err_msg = acct2.withdraw(2000.0)
    assert acct2.balance == 950.0, "Balance should not change on insufficient funds"
    assert err_msg == "Insufficient funds", f"Expected 'Insufficient funds', got {repr(err_msg)}"

run_test("Verify BankAccount constructor, deposits, and withdrawals", test_bank_account)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 11 assignments.")
    print(f"Proceed to Day 12 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day11_assignment.py")
