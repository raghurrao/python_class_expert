# Day 19: Database State & Transactional Fixtures

When testing database repositories, you must ensure that each test runs in a clean, predictable database environment. If one test adds records to a table and does not clean them up, the next test might fail (e.g. unique constraint violations, unexpected row counts). This is called database state pollution.

Today, we will learn how to design database fixtures that seed tables, yield connections, and clean up or roll back changes on teardown.

---

## 1. The Seed & Purge Pattern (Standard Setup/Teardown)
The simplest way to maintain database sanity is to write setup code that populates the database with required test rows, and teardown code that deletes them.

```python
import pytest

@pytest.fixture
def db_session():
    # 1. Setup: Connect to the db and clear any previous state
    session = Database.create_session()
    session.execute("DELETE FROM users")  # Clean start
    
    # 2. Seed: Add common test data
    session.add_user(id=1, name="Alice")
    session.add_user(id=2, name="Bob")
    
    yield session
    
    # 3. Teardown: Clean up the data so we leave the database clean
    session.execute("DELETE FROM users")
    session.close()
```

---

## 2. Transactional Rollback (Advanced Professional Pattern)
An even faster and more robust strategy is to wrap the execution of each test inside a database **Transaction** and roll it back when the test exits. Because the changes are never committed, the database returns to its exact original state automatically!

```python
@pytest.fixture
def transactional_session():
    connection = engine.connect()
    # Start a transaction block
    transaction = connection.begin()
    
    # Bind session to the transaction
    session = Session(bind=connection)
    
    yield session  # Tests make changes inside the transaction
    
    # Roll back everything that happened in the test!
    transaction.rollback()
    connection.close()
```
Since rolling back is extremely fast compared to executing delete statements, this is the preferred pattern for heavy databases.
