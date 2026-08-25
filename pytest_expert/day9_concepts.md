# Day 9: Fixture Scopes & Autouse

Yesterday you created a function-scoped fixture. Function scope is the safest choice because it isolates tests from each other, but it can be slow if setup takes time. Pytest allows you to control the lifecycle of a fixture using **Scopes**.

---

## 1. Fixture Scopes
Pytest supports 5 scope levels:

| Scope | Lifetime | Useful For |
| :--- | :--- | :--- |
| **`function`** (default) | Setup/Teardown run once for **each test function**. | Fast tests requiring high isolation. |
| **`class`** | Setup/Teardown run once for **each test class**. | Grouping tests sharing expensive class states. |
| **`module`** | Setup/Teardown run once for **each `.py` file**. | Local module mocks, read-only cache loading. |
| **`package`** | Setup/Teardown run once for **each package folder**. | Package-level config verification. |
| **`session`** | Setup/Teardown run **only once** for the entire test run. | Starting microservices, connecting to real heavy databases. |

### Declaring Scope
```python
import pytest

@pytest.fixture(scope="session")
def database_connection():
    conn = connect_heavy_db()
    yield conn
    conn.close()  # Only runs once at the very end of the pytest run
```

---

## 2. Autouse Fixtures (`autouse=True`)
Sometimes you want a fixture to run automatically for every test, even if the test does not request it as an argument. Examples include:
* Clearing a database table before every test.
* Measuring elapsed time for every test.
* Setting environment variables.

You enable this by setting `autouse=True` in the decorator:

```python
import time
import pytest

@pytest.fixture(autouse=True)
def print_test_timer():
    # Setup
    start_time = time.time()
    yield
    # Teardown
    duration = time.time() - start_time
    print(f"\nTest duration: {duration:.4f} seconds")
```
Now, `print_test_timer` runs for **every single test** in the folder/module automatically.
