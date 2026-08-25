# Day 11 Assignment: Dynamic Fixtures & the request Object
# -----------------------------------------------------------------
# Task 1: Write a parameterized fixture named 'db_client'.
#         - Parameters must be: ["sqlite", "postgres", "mysql"]
#         - Inject 'request' and use request.param to yield the client.
# Task 2: Write a test function 'test_client_queries' that uses 'db_client'.
#         - Assert that client.query() returns a string ending with "Result".
# -----------------------------------------------------------------

import pytest
from .day11_app import get_client

# Task 1: Implement the parameterized fixture 'db_client'.
# 1. Set the decorator @pytest.fixture with params=["sqlite", "postgres", "mysql"]
# 2. Inject 'request' as an argument to the fixture.
# 3. Fetch the engine name using request.param.
# 4. Call get_client(engine_name) and yield the client.
@pytest.fixture
def db_client():
    # Replace pass with your implementation:
    pass


# Task 2: Write the test 'test_client_queries' that requests the 'db_client' fixture.
# Assert that:
# 1. client.name is in the list ["sqlite", "postgres", "mysql"]
# 2. client.query() returns a string ending in "Result" (or containing "Result").
def test_client_queries(db_client):
    # Replace pass with your assertions:
    pass
