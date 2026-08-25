# Day 19 Assignment: Database State & Transactional Fixtures
# -----------------------------------------------------------------
# Task 1: Create a session-scoped fixture 'db_engine' that instantiates a single DatabaseManager.
# Task 2: Create a function-scoped fixture 'db_session' that:
#         - Starts a transaction (db_engine.begin_transaction()).
#         - Seeds a default user: db_engine.add_user(1, "Alice").
#         - Yields the db_engine.
#         - Rolls back the transaction on teardown (db_engine.rollback()).
# -----------------------------------------------------------------

import pytest
from .day19_db import DatabaseManager

# Task 1: Declare the session-scoped fixture 'db_engine'.
# It should return a single DatabaseManager instance.
@pytest.fixture(scope="session")
def db_engine():
    # Replace pass with your implementation:
    pass


# Task 2: Declare the function-scoped fixture 'db_session'.
# 1. Inject the 'db_engine' fixture.
# 2. Call db_engine.begin_transaction()
# 3. Call db_engine.add_user(1, "Alice") (seed data)
# 4. Yield db_engine
# 5. Call db_engine.rollback() in teardown.
@pytest.fixture
def db_session(db_engine):
    # Replace pass with your implementation:
    pass


# Test cases verifying database transaction isolation:

def test_read_seeded_user(db_session):
    # This test should see the seeded user Alice
    assert db_session.get_user(1) == "Alice"

def test_add_new_user(db_session):
    # This test adds a new user Bob
    db_session.add_user(2, "Bob")
    assert db_session.get_user(2) == "Bob"
    assert db_session.get_user(1) == "Alice"

def test_user_isolation(db_session):
    # Because test_add_new_user was rolled back, user ID 2 (Bob) should NOT exist in this test!
    # If the database was not isolated, this test would fail!
    assert db_session.get_user(2) is None
    assert db_session.get_user(1) == "Alice"
