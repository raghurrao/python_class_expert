# Day 8 Assignment: Intro to Fixtures & Setup/Teardown
# -----------------------------------------------------------------
# Task 1: Write a pytest fixture named 'db_client' using 'yield'.
# Task 2: Implement test functions that request the 'db_client' fixture.
# -----------------------------------------------------------------

import pytest
from .day8_app import SimpleDBClient

# Task 1: Create a fixture named 'db_client'.
# Inside the fixture:
# 1. Instantiate SimpleDBClient()
# 2. Call connect()
# 3. YIELD the client object to the tests
# 4. Call disconnect() after the yield to clean up the connection
# Your code here:
@pytest.fixture
def db_client():
    # Replace pass with your implementation:
    pass


# Task 2a: Write a test that accepts the db_client fixture.
# Assert that the client's 'connected' attribute is True, and the 'status' 
# key inside 'data' dictionary contains "seeded".
def test_db_connection_status(db_client):
    pass


# Task 2b: Write a test that accepts the db_client fixture.
# Call insert("key1", "val1") and assert it returns True.
# Also assert that "key1" in the client's data dictionary is mapped to "val1".
def test_db_insert(db_client):
    pass
