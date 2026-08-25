# Day 5: Custom Markers & Pytest Configuration

As test suites grow, you need to group tests logically (e.g. running only fast unit tests in a git commit hook, and slow integration tests only in a nightly CI run). Custom markers are pytest's way of grouping tests.

---

## 1. Defining Custom Markers
You can name a marker whatever you want by decorating a test with `@pytest.mark.your_marker_name`:

```python
import pytest

@pytest.mark.database
def test_user_insertion():
    assert save_to_db() is True

@pytest.mark.fast
def test_simple_addition():
    assert 1 + 1 == 2
```

---

## 2. Running Marked Tests via CLI
You can filter tests based on custom markers using the `-m` flag:

* Run only tests marked with `database`:
  ```bash
  pytest -m database
  ```
* Run tests that are NOT marked with `slow`:
  ```bash
  pytest -m "not slow"
  ```
* Run tests that are marked with `database` AND are `fast`:
  ```bash
  pytest -m "database and fast"
  ```

---

## 3. Registering Markers in Configuration Files
If you run custom markers without registering them, pytest will execute them, but it will raise a warning:
`PytestUnknownMarkWarning: Unknown pytest.mark.database - is this a typo?`

To register custom markers, you define them in a configuration file:

### Option A: `pytest.ini` (Recommended for standalone folders)
Create a file named `pytest.ini` in your test folder and add:

```ini
[pytest]
markers =
    fast: marks tests as fast unit tests
    database: marks tests that interact with the database
```

### Option B: `pyproject.toml`
If you are using `pyproject.toml`, you can register them under the `tool.pytest.ini_options` section:

```toml
[tool.pytest.ini_options]
markers = [
    "fast: marks tests as fast unit tests",
    "database: marks tests that interact with the database"
]
```

---

## 4. Other Useful Configuration Options
In `pytest.ini`, you can configure other behaviors, such as:
* **`addopts`**: Set default command line options so you don't have to type them every time:
  ```ini
  [pytest]
  addopts = -v --tb=short
  ```
* **`testpaths`**: Specify directories where pytest should look for tests:
  ```ini
  [pytest]
  testpaths = tests
  ```
