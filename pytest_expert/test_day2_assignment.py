# Day 2 Assignment: Exception and Structure Assertions
# -----------------------------------------------------------------
# Write tests for functions in day2_functions.py.
# Follow the docstring instructions.
# Run 'pytest' to test and check your progress!
# -----------------------------------------------------------------

import pytest
from .day2_functions import validate_age, parse_user_data, merge_configs

# ==========================================
# Task 1: Testing Age Validation
# ==========================================

def test_validate_age_valid():
    """Assert validate_age returns True for a valid age (e.g. 25)."""
    # Your code here:
    pass

def test_validate_age_invalid_type():
    """
    Assert validate_age raises TypeError if age is not an integer.
    Verify the exception message contains 'Age must be an integer'.
    Hint: Use 'with pytest.raises(TypeError, match="..."):' or excinfo.
    """
    # Your code here:
    pass

def test_validate_age_out_of_bounds():
    """
    Assert validate_age raises ValueError if age is out of bounds (< 0 or > 120).
    Verify that the message contains 'between 0 and 120' and the invalid age value.
    Example: validate_age(-5) -> ValueError containing "-5" and "between 0 and 120".
    """
    # Your code here:
    pass


# ==========================================
# Task 2: Testing User Data Parsing
# ==========================================

def test_parse_user_data_valid():
    """Assert parse_user_data returns the correct string for a valid dictionary."""
    # Your code here:
    pass

def test_parse_user_data_missing_key():
    """
    Assert parse_user_data raises KeyError when a key is missing.
    Specifically assert that the missing key name (e.g. 'username') is part of the exception.
    """
    # Your code here:
    pass


# ==========================================
# Task 3: Testing Config Merging
# ==========================================

def test_merge_configs_flat():
    """
    Assert merge_configs successfully merges two flat dictionaries.
    Ensure values from the second dict overwrite values from the first dict if keys overlap.
    """
    # Your code here:
    pass

def test_merge_configs_nested():
    """
    Assert merge_configs successfully merges nested dictionaries.
    Example:
    dict1 = {"database": {"host": "localhost", "port": 5432}}
    dict2 = {"database": {"port": 9999, "user": "admin"}}
    Merged result should have "host" = "localhost", "port" = 9999, and "user" = "admin".
    """
    # Your code here:
    pass

def test_merge_configs_invalid_type():
    """Assert merge_configs raises TypeError with message 'must be dictionaries' if inputs are invalid."""
    # Your code here:
    pass
