# Day 22: Testing Async Code (`pytest-asyncio`)

Modern Python utilizes asynchronous programming (`async`/`await`) for high-performance I/O bound operations (like fetching web pages, querying databases, or reading files). Standard testing frameworks cannot run coroutines because they must be executed inside an event loop. 

Pytest solves this with the **`pytest-asyncio`** plugin.

---

## 1. Async Test Functions
To test an asynchronous function (declared with `async def`), you must declare your test function as `async def` as well.

With `pytest-asyncio` installed, you can configure it to automatically handle these functions using `asyncio_mode = auto` in your configuration.

```python
import asyncio
import pytest

async def fetch_api_data():
    await asyncio.sleep(0.01)  # Simulates network call
    return "API Data"

# Declare the test as async!
async def test_api_data():
    # You can now use the await keyword inside your test cases!
    result = await fetch_api_data()
    assert result == "API Data"
```

---

## 2. Async Fixtures
You can also write fixtures that are asynchronous. This is essential if your setup or teardown code needs to `await` database sessions, web requests, or connection cleanups:

```python
import pytest
from my_app import AsyncDatabaseClient

@pytest.fixture
async def async_db():
    # Setup: await connection
    db = AsyncDatabaseClient()
    await db.connect()
    
    yield db  # Provide client to test
    
    # Teardown: await disconnection
    await db.disconnect()
```

---

## 3. Configuration: `asyncio_mode`
To run async tests without getting warnings or needing to manually decorate every test function with `@pytest.mark.asyncio`, you should configure `asyncio_mode` in your `pytest.ini` or `pyproject.toml` file:

### In `pytest.ini`:
```ini
[pytest]
asyncio_mode = auto
```

This tells pytest to automatically treat all `async def` test functions and fixtures in the suite as asyncio tests.
