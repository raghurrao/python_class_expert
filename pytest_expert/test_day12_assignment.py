# Day 12 Assignment: Test Parametrization
# -----------------------------------------------------------------
# Task 1: Write a parameterized test function 'test_is_prime'.
#         - Parameters: "number, expected"
#         - Test values: 2 (True), 3 (True), 4 (False), 11 (True), 15 (False), 1 (False), -5 (False).
#         - Customize names using the 'ids' argument.
# Task 2: Write a parameterized test 'test_is_prime_type_error'.
#         - Parameters: "invalid_input"
#         - Verify they raise TypeError.
# -----------------------------------------------------------------

import pytest
from .day12_math import is_prime

# Task 1: Parameterize and implement test_is_prime.
# Remember to decorate with @pytest.mark.parametrize and provide custom 'ids' for each tuple.
# Your code here:
def test_is_prime(number, expected):
    # Replace pass with assertions calling is_prime(number) == expected:
    pass


# Task 2: Parameterize and implement test_is_prime_type_error.
# Inputs to test: "three", 3.14, [7], None.
# Assert that each input raises TypeError.
# Your code here:
def test_is_prime_type_error(invalid_input):
    # Replace pass with assertions checking for TypeError:
    pass
