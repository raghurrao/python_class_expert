# Day 8: Introduction to Fixtures & Setup/Teardown

In unit testing, tests often require preparatory state—such as instantiating database connections, loading config files, seeding test data, or starting background servers. In other frameworks, this is done in `setUp()` and `tearDown()` methods, which can become bloated. Pytest uses **Fixtures** to handle setup and teardown cleanly.

---

## 1. What is a Fixture?
A fixture is a function decorated with `@pytest.fixture` that returns or yields a resource. Test functions request this resource by declaring the fixture name as an **argument** in their signature. This is a form of dependency injection.

```python
import pytest

@pytest.fixture
def sample_user():
    # Setup phase
    return {"username": "john_doe", "is_admin": False}

def test_user_properties(sample_user):
    # The sample_user argument receives the return value of the fixture
    assert sample_user["username"] == "john_doe"
    assert sample_user["is_admin"] is False
```

---

## 2. Setup and Teardown using `yield`
When you need to clean up resources after a test completes (e.g. closing files, shutting down DB connections, deleting temp directories), replace `return` with the `yield` keyword:

1. **Before `yield`**: Code executed **before** the test runs (Setup).
2. **`yield` value**: The object injected into the test function.
3. **After `yield`**: Code executed **after** the test runs (Teardown/Cleanup).

```python
@pytest.fixture
def temp_database():
    # 1. Setup: initialize DB connection
    db = DatabaseClient()
    db.connect()
    db.seed_data()
    
    # 2. Yield: Provide the DB client to the test
    yield db
    
    # 3. Teardown: Clean up state after the test exits (even if the test failed!)
    db.clear_data()
    db.disconnect()
```

> [!IMPORTANT]
> The teardown code (after `yield`) is guaranteed to run, even if the test function fails, crashes, or raises an unexpected exception.
