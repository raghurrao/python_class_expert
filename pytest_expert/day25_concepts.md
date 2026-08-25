# Day 25: Pytest Hooks & Plugin Development

Pytest is built on a modular architecture powered by hooks. A hook is a callback function defined in `conftest.py` (or a packaged plugin) that pytest calls at specific stages of the testing lifecycle:
1. **Initialization**: Loading options, configuring settings.
2. **Collection**: Discovering test files and test functions.
3. **Execution**: Running setups, calling test functions, reporting failures.
4. **Teardown**: Capturing logs, cleaning environments.

Today, we will learn how to write a custom hook to intercept test execution.

---

## 1. Popular Pytest Hooks

### `pytest_runtest_setup(item)`
Called before executing each test function (`item`). You can inspect the test function name, docstring, or markers, and decide to run or skip it.

```python
# conftest.py
import pytest

def pytest_runtest_setup(item):
    # Retrieve the function object
    func = item.obj
    
    # If the function name starts with "test_admin_", verify we have permissions
    if func.__name__.startswith("test_admin_"):
        if not check_admin_rights():
            pytest.skip("Skipping admin test: No admin privileges detected.")
```

### `pytest_collection_modifyitems(session, config, items)`
Called after pytest has discovered all tests. You can reorder them (e.g. running fast tests first) or add custom markers dynamically.

```python
# conftest.py
import pytest

def pytest_collection_modifyitems(config, items):
    for item in items:
        # Dynamically add the 'slow' marker to any test containing 'indexing'
        if "indexing" in item.name:
            item.add_marker(pytest.mark.slow)
```

---

## 2. Accessing Test Metadata in Hooks
The `item` parameter passed to execution hooks represents the test node. You can access:
* **`item.name`**: The test function name (e.g. `test_login`).
* **`item.nodeid`**: The full path identifier (e.g. `tests/test_auth.py::test_login`).
* **`item.obj`**: The actual underlying Python function object.
* **`item.obj.__doc__`**: The docstring defined inside the test function!
* **`item.parent`**: The parent class or module.
