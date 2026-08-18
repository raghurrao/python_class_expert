# Day 15 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day15_test.py
# It will verify if your assignment code is correct!

import sys
import os
from abc import ABC

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week3_oop.day15_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day15_assignment.py. Error: {e}")
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

print("Starting Day 15 Tests...\n")

# 1. Test PaymentProcessor ABC
def test_payment_processor_abc():
    assert hasattr(assignment, 'PaymentProcessor'), "PaymentProcessor class not found"
    assert issubclass(assignment.PaymentProcessor, ABC), "PaymentProcessor must inherit from ABC"
    
    # Try instantiating PaymentProcessor directly
    try:
        assignment.PaymentProcessor()
        raise AssertionError("Instantiated abstract PaymentProcessor class successfully (it should error)")
    except TypeError:
        pass

run_test("Verify PaymentProcessor is an Abstract Base Class (ABC)", test_payment_processor_abc)

# 2. Test StripeProcessor
def test_stripe_processor():
    assert hasattr(assignment, 'StripeProcessor'), "StripeProcessor not found"
    assert issubclass(assignment.StripeProcessor, assignment.PaymentProcessor), "StripeProcessor must inherit from PaymentProcessor"
    
    stripe = assignment.StripeProcessor()
    
    res1 = stripe.process_payment(99.95)
    assert res1 == "Stripe: Processed transaction of $99.95", f"Got: '{res1}'"
    
    res2 = stripe.refund_payment("tx_abc123")
    assert res2 == "Stripe: Refunded transaction tx_abc123", f"Got: '{res2}'"

run_test("Verify StripeProcessor concrete implementation", test_stripe_processor)

# 3. Test PayPalProcessor
def test_paypal_processor():
    assert hasattr(assignment, 'PayPalProcessor'), "PayPalProcessor not found"
    assert issubclass(assignment.PayPalProcessor, assignment.PaymentProcessor), "PayPalProcessor must inherit from PaymentProcessor"
    
    paypal = assignment.PayPalProcessor()
    
    res1 = paypal.process_payment(45.00)
    assert res1 == "PayPal: Processed transaction of $45.0", f"Got: '{res1}'"
    
    res2 = paypal.refund_payment("tx_pay999")
    assert res2 == "PayPal: Refunded transaction tx_pay999", f"Got: '{res2}'"

run_test("Verify PayPalProcessor concrete implementation", test_paypal_processor)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 15 assignments.")
    print(f"Proceed to the Week 3 Weekend Challenge when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day15_assignment.py")
