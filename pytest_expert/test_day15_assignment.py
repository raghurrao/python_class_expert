# Day 15 Assignment: Mocking Basics
# -----------------------------------------------------------------
# Task 1: Test successful payment processing using a mock client.
# Task 2: Test declined payment processing.
# Task 3: Test connection timeouts and exception wrapper.
# -----------------------------------------------------------------

from unittest.mock import Mock
import pytest
from .day15_app import PaymentProcessor, GatewayClient

def test_payment_success():
    # 1. Create a Mock of GatewayClient:
    mock_gateway = Mock(spec=GatewayClient)
    
    # 2. Configure mock_gateway.charge to return "SUCCESS":
    # Your code here (set return_value):

    # 3. Instantiate PaymentProcessor and inject the mock_gateway:
    # Your code here:

    # 4. Call process_payment(100.0, "tok_123") and assert it returns True:
    # Your code here:

    # 5. Assert mock_gateway.charge was called once with (100.0, "tok_123"):
    # Hint: Use assert_called_once_with()
    # Your code here:
    pass


def test_payment_failure_status():
    # 1. Create mock of GatewayClient and configure charge() to return "DECLINED"
    # Your code here:

    # 2. Assert process_payment(50.0, "tok_declined") returns False
    # Your code here:
    pass


def test_payment_gateway_exception():
    # 1. Create mock of GatewayClient and configure charge() to raise a ConnectionError("Gateway timeout")
    # Hint: Use mock.charge.side_effect = ConnectionError("Gateway timeout")
    # Your code here:

    # 2. Assert process_payment(200.0, "tok_timeout") raises a RuntimeError
    # Verify that the message contains "Payment failed due to gateway error" and "Gateway timeout".
    # Your code here:
    pass
