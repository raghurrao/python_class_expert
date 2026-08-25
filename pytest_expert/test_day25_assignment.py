# Day 25 Assignment: Pytest Hooks & Plugin Development
# -----------------------------------------------------------------
# Task 4: Implement the two test functions below.
#         - 'test_documented' must contain a docstring (e.g. """Documented.""").
#           It should assert True.
#         - 'test_undocumented' must NOT contain any docstring at all.
#           It should assert True, but will be intercepted and skipped!
# -----------------------------------------------------------------

import pytest

def test_documented():
    """This test has documentation. It should run and pass."""
    assert True

def test_undocumented():
    # Write a simple passing assertion here.
    # Note: Do NOT add a docstring to this function!
    assert True
