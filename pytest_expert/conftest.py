# Day 24: Global conftest.py Configuration
import pytest

# Task 1: Register the custom command-line option '--run-slow'.
# 1. Implement pytest_addoption(parser).
# 2. Call parser.addoption("--run-slow", action="store_true", default=False, help="Run slow tests")
# Your code here:
def pytest_addoption(parser):
    parser.addoption("--run-slow", action="store_true", default=False, help="Run slow tests")
    # Task 5: Register the custom command-line option '--skip-encryption'.
    # 1. Action must be 'store_true'.
    # 2. Default must be False.
    # Your code here:
    pass


# Task 3: Implement the hook 'pytest_runtest_setup(item)'.
# 1. Inspect item.obj.__doc__ (the docstring of the test function).
# 2. If it is None or empty/whitespace-only, call pytest.skip("Test missing docstring documentation").
# Your code here:
def pytest_runtest_setup(item):
    # Replace pass with your implementation:
    pass

