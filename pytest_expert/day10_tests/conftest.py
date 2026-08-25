# Day 10: Shared conftest.py Configuration
import pytest

# Task 1: Create a session-scoped fixture named 'app_version'.
# It should simply return the string "2.0.1".
# Your code here:
@pytest.fixture(scope="session")
def app_version():
    # Replace pass with your implementation:
    pass
