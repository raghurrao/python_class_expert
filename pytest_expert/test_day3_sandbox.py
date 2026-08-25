# Day 3: Sandbox Test Suite
# Use this file to practice running different pytest CLI commands!

import time

def test_user_login_success():
    print("\n[DEBUG] Login success print output.")
    assert True

def test_user_login_fail():
    print("\n[DEBUG] Login failed print output.")
    assert 1 == 2  # Fails!

def test_user_logout():
    assert True

def test_payment_stripe_charge():
    assert True

def test_payment_paypal_charge():
    assert True

def test_payment_refund():
    assert True

def test_admin_dashboard_view():
    assert True

def test_slow_database_query():
    time.sleep(0.1)  # Simulates a slow test
    assert True

def test_slow_api_connection():
    time.sleep(0.05)  # Simulates another slow test
    assert True
