# Day 6 Assignment: Week 1 Integration Milestone
# -----------------------------------------------------------------
# Task 1: Group all tests inside a class named 'TestDataValidator'.
# Task 2: Implement test methods validating username, email, and password.
# Task 3: Apply '@pytest.mark.fast' (for usernames & emails) 
#         and '@pytest.mark.security' (for passwords) markers.
# Task 4: Register all custom markers (including 'security') in pytest.ini.
# -----------------------------------------------------------------

import pytest
from .day6_validator import DataValidator

# Implement your TestDataValidator class below:
class TestDataValidator:
    # Write your tests here.
    # Required test functions to implement (do not change names):
    # - test_username_valid
    # - test_username_invalid_type (assert TypeError + message check)
    # - test_username_invalid_len (assert ValueError + message check)
    # - test_username_invalid_chars (assert ValueError + message check)
    # - test_email_valid
    # - test_email_invalid_type (assert TypeError + message check)
    # - test_email_invalid_format (assert ValueError + message check)
    # - test_password_valid
    # - test_password_invalid_type (assert TypeError + message check)
    # - test_password_too_short (assert ValueError + message check)
    # - test_password_no_uppercase (assert ValueError + message check)
    # - test_password_no_lowercase (assert ValueError + message check)
    # - test_password_no_number (assert ValueError + message check)
    
    pass
