# Day 15 Assignment: Abstract Base Classes (ABCs)
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by filling in the blanks.
# Do not change the class or method names. You can run 'python day15_test.py'
# to check your solutions.

from abc import ABC, abstractmethod

# ======================================================================
# Exercise 1: PaymentProcessor Interface
# ======================================================================
# Task: Create an abstract base class 'PaymentProcessor' and concrete subclasses.

# 1. Abstract Class: 'PaymentProcessor'
#    - Inherits from ABC.
#    - Define abstract method 'process_payment(amount)' (amount: float).
#    - Define abstract method 'refund_payment(transaction_id)' (transaction_id: str).
class PaymentProcessor(ABC):
    # TODO: Define abstract methods process_payment and refund_payment
    pass


# 2. Concrete Subclass: 'StripeProcessor'
#    - Inherits from PaymentProcessor.
#    - Implement 'process_payment(amount)' to return string:
#      "Stripe: Processed transaction of $<amount>"
#    - Implement 'refund_payment(transaction_id)' to return string:
#      "Stripe: Refunded transaction <transaction_id>"
class StripeProcessor(PaymentProcessor):
    # TODO: Implement concrete payment and refund logic
    pass


# 3. Concrete Subclass: 'PayPalProcessor'
#    - Inherits from PaymentProcessor.
#    - Implement 'process_payment(amount)' to return string:
#      "PayPal: Processed transaction of $<amount>"
#    - Implement 'refund_payment(transaction_id)' to return string:
#      "PayPal: Refunded transaction <transaction_id>"
class PayPalProcessor(PaymentProcessor):
    # TODO: Implement concrete payment and refund logic
    pass
