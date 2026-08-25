# Day 22 Assignment: Testing Async Code
# -----------------------------------------------------------------
# Task 1: Create an async fixture 'repo' that instantiates, connects,
#         yields, and disconnects AsyncUserRepository.
# Task 2: Write async test functions to verify fetch and save operations.
# -----------------------------------------------------------------

import pytest
from .day22_app import AsyncUserRepository

# Task 1: Implement the async fixture 'repo'.
# Note: Declare the fixture using standard @pytest.fixture, but make the function 'async def'.
@pytest.fixture
async def repo():
    # Replace pass with your implementation:
    pass


# Task 2a: Write the async test 'test_fetch_user' requesting the 'repo' fixture.
# Await repo.fetch_user_name(1) and assert it is "Alice".
# Await repo.fetch_user_name(99) and assert it is None.
async def test_fetch_user(repo):
    # Replace pass with your assertions:
    pass


# Task 2b: Write the async test 'test_save_user' requesting the 'repo' fixture.
# Await repo.save_user_name(3, "Charlie") and assert it returns True.
# Await repo.fetch_user_name(3) and assert it is "Charlie".
async def test_save_user(repo):
    # Replace pass with your assertions:
    pass
