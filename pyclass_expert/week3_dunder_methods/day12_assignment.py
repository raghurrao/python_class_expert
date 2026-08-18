# Day 12 Assignment: Operator Overloading
# ----------------------------------------------------------------------
# Instructions: Complete the Money class to support mathematical operators.
# Run 'python day12_test.py' to verify your solutions.

class Money:
    """
    Requirements:
    1. Constructor accepts 'amount' (float/int) and 'currency' (str, e.g., "USD").
    2. Implement '__repr__(self)' returning: Money(amount=<amount>, currency='<currency>')
    3. Implement '__add__(self, other)' to add amounts of the same currency:
       - If 'other' is not an instance of Money, or currency does not match, raise ValueError.
       - Return a new Money object.
    4. Implement '__sub__(self, other)' to subtract amounts of the same currency:
       - If 'other' is not an instance of Money, or currency does not match, raise ValueError.
       - Return a new Money object.
    5. Implement '__lt__(self, other)' to compare amounts:
       - If 'other' is not an instance of Money, or currency does not match, raise ValueError.
       - Return boolean.
    6. Implement '__mul__(self, factor)' to multiply amount by a numeric scalar (int/float):
       - If 'factor' is not an int or float, return NotImplemented.
       - Return a new Money object.
    7. Implement '__rmul__(self, factor)' (reflected multiplication) to support factor * money:
       - Redirect to '__mul__'.
    """
    def __init__(self, amount, currency):
        # TODO: Initialize attributes (force amount to float or keep as is)
        pass

    def __repr__(self):
        # TODO: Return representation
        pass

    def __add__(self, other):
        # TODO: Check currency and add
        pass

    def __sub__(self, other):
        # TODO: Check currency and subtract
        pass

    def __lt__(self, other):
        # TODO: Check currency and compare
        pass

    def __mul__(self, factor):
        # TODO: Multiply amount by factor
        pass

    def __rmul__(self, factor):
        # TODO: Redirect to __mul__
        pass
