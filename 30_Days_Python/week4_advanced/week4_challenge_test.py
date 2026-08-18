# Week 4 Challenge Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python week4_challenge_test.py
# It will verify if your capstone project code is correct!

import sys
import os
import csv

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week4_advanced.week4_challenge as challenge
except ImportError as e:
    print(f"[FAIL] Could not import week4_challenge.py. Error: {e}")
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

# Temporary path for CSV file testing
test_csv_path = os.path.join(current_dir, "temp_transactions.csv")

def cleanup():
    if os.path.exists(test_csv_path):
        try:
            os.remove(test_csv_path)
        except OSError:
            pass

print("Starting Week 4 Challenge Tests...\n")
cleanup()

# 1. Test Transaction class encapsulation & properties
def test_transaction_class():
    assert hasattr(challenge, 'Transaction'), "Transaction class not found"
    
    t = challenge.Transaction(1, "Groceries", -45.50, "Food")
    assert not hasattr(t, '__amount'), "Amount must be encapsulated private attribute"
    assert t.amount == -45.50
    
    # Update amount
    t.amount = -50.00
    assert t.amount == -50.00
    
    # Try invalid setter (0)
    try:
        t.amount = 0.0
        raise AssertionError("Did not raise ValueError for amount = 0")
    except ValueError as e:
        assert str(e) == "Amount cannot be zero", f"Unexpected error message: {e}"
        
    assert repr(t) == "Transaction(id=1, description='Groceries', amount=-50.0, category='Food')", f"Got: {repr(t)}"

run_test("Verify Transaction class property access and representation", test_transaction_class)

# 2. Test CSV Data Loader
def test_csv_loader():
    assert hasattr(challenge, 'load_transactions_from_csv'), "load_transactions_from_csv not found"
    
    # Try missing file
    res = challenge.load_transactions_from_csv("nonexistent_path.csv")
    assert res == [], f"Expected [] for missing file, got {res}"
    
    # Create test CSV
    with open(test_csv_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "description", "amount", "category"])
        writer.writerow(["1", "Salary", "2500.00", "Income"])
        writer.writerow(["2", "Gas", "-30.25", "Transport"])
        
    loaded = challenge.load_transactions_from_csv(test_csv_path)
    assert len(loaded) == 2, f"Expected 2 transactions, got {len(loaded)}"
    assert isinstance(loaded[0], challenge.Transaction), "List must contain Transaction objects"
    assert loaded[0].amount == 2500.00
    assert loaded[1].description == "Gas"

run_test("Verify CSV Transaction data loader & FileNotFoundError handling", test_csv_loader)

# 3. Test convert_currency
def test_convert_currency():
    assert hasattr(challenge, 'convert_currency'), "convert_currency not found"
    
    transactions = [
        challenge.Transaction(1, "Income", 1000.00, "Salary"),
        challenge.Transaction(2, "Coffee", -4.50, "Food")
    ]
    
    converted = challenge.convert_currency(transactions, 1.2)  # USD to EUR rate e.g.
    assert len(converted) == 2
    assert converted[0].amount == 1200.00, f"Expected 1200.00, got {converted[0].amount}"
    assert converted[1].amount == -5.40, f"Expected -5.40, got {converted[1].amount}"
    assert converted[0] is not transactions[0], "Must return a new Transaction instance, not modify original in-place"

run_test("Verify currency converter using list comprehensions", test_convert_currency)

# 4. Test get_category_summary
def test_category_summary():
    assert hasattr(challenge, 'get_category_summary'), "get_category_summary not found"
    
    transactions = [
        challenge.Transaction(1, "Grocery A", -40.00, "Food"),
        challenge.Transaction(2, "Gas", -30.00, "Transport"),
        challenge.Transaction(3, "Grocery B", -15.50, "Food"),
        challenge.Transaction(4, "Salary", 2000.00, "Income")
    ]
    
    summary = challenge.get_category_summary(transactions)
    assert isinstance(summary, dict), "Expected dictionary return type"
    assert summary.get('Food') == -55.50, f"Expected -55.50 for Food, got {summary.get('Food')}"
    assert summary.get('Transport') == -30.00
    assert summary.get('Income') == 2000.00

run_test("Verify Transaction list category sums aggregation dictionary logic", test_category_summary)

# Cleanup
cleanup()

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed the Week 4 Weekend Challenge and Capstone Project.")
    print(f"You have finished the 1-month learning curriculum and are ready to become a Python Expert!")
else:
    print(f"FAILED: Some challenge tests failed. Check the errors above and fix your code in week4_challenge.py")
