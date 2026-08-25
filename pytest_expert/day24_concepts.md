# Day 24: Custom Command-Line Options

When developing enterprise test suites, you often need to adapt execution dynamically. For example, pointing tests to different server environments (`--env=staging` vs `--env=dev`) or choosing to run slow tests only on demand (`--run-slow`). 

Pytest allows you to register custom command-line options inside **`conftest.py`**.

---

## 1. Registering Flags: `pytest_addoption`
To add a command-line flag, implement the built-in hook `pytest_addoption(parser)` inside your local `conftest.py` file:

```python
# conftest.py

def pytest_addoption(parser):
    # Register the --env option
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="environment to run tests against: dev or staging"
    )
```

---

## 2. Accessing Custom Flags in Fixtures
To read the flag inside your tests, inject the standard `request` fixture and call `request.config.getoption()`:

```python
# conftest.py (or any test file)
import pytest

@pytest.fixture
def api_base_url(request):
    # Fetch the command-line argument value
    env_name = request.config.getoption("--env")
    
    if env_name == "staging":
        return "https://staging-api.example.com"
    return "https://dev-api.example.com"
```

Now, when you run pytest, you can pass your custom flag:
```bash
pytest --env=staging -s
```

---

## 3. Dynamically Skipping Tests
If you want to define a flag like `--run-slow` to toggle slow tests, you can check the flag and call `pytest.skip` dynamically:

```python
# test_suite.py
import pytest
import time

def test_slow_database_indexing(request):
    # If the user did not specify the --run-slow flag, skip the test
    if not request.config.getoption("--run-slow"):
        pytest.skip("Skipping slow test. Use --run-slow flag to execute.")
        
    time.sleep(5)  # Heavy operation
    assert True
```
This is a standard pattern to keep your local feedback loop fast while allowing full sweeps in nightly builds.
