# Day 3: Pytest CLI Execution & Filters

Today, we will master pytest's command-line interface (CLI). In professional development, test suites can grow to thousands of tests. Knowing how to run a single test, filter tests, capture standard output, debug failures, and profile execution speed is a superpower.

---

## 1. Running Specific Tests
You don't have to run the entire suite. Pytest lets you target specific components:

* **By File Path**:
  ```bash
  pytest tests/test_auth.py
  ```
* **By Test Class**:
  ```bash
  pytest tests/test_auth.py::TestLogin
  ```
* **By Specific Test Function**:
  ```bash
  pytest tests/test_auth.py::TestLogin::test_success
  ```

---

## 2. Filtering with `-k` (Expression Matching)
The `-k` flag is extremely powerful. It allows you to run tests whose names match a string expression. It supports boolean operators like `and`, `or`, and `not`.

* Run only tests with `login` in their name:
  ```bash
  pytest -k "login"
  ```
* Run tests with `login` or `register` in their name:
  ```bash
  pytest -k "login or register"
  ```
* Run all database tests but skip any that involve Oracle:
  ```bash
  pytest -k "db and not oracle"
  ```
> [!NOTE]
> Substring matching is case-insensitive. It checks the name of the file, class, and test function.

---

## 3. Print Output Capturing (`-s` / `--capture`)
By default, pytest captures all standard output (`stdout`) and standard error (`stderr`). If a test passes, you won't see any `print()` statements in your terminal.
* To disable capturing and force print statements to output immediately, use the `-s` flag (short for `--capture=no`):
  ```bash
  pytest -s
  ```

---

## 4. Execution Flow Control (`-x`, `--lf`, `--ff`, `--maxfail`)
When fixing broken code, you want quick iterations.

* **Exit on first failure (`-x`)**: Stops running tests the moment any test fails.
  ```bash
  pytest -x
  ```
* **Exit after N failures (`--maxfail`)**:
  ```bash
  pytest --maxfail=3
  ```
* **Run last failed only (`--lf` / `--last-failed`)**: Pytest remembers which tests failed in its cache. This flag runs *only* the tests that failed in the last run.
  ```bash
  pytest --lf
  ```
* **Failed first (`--ff` / `--failed-first`)**: Runs previously failed tests first, then runs the rest of the passing suite.
  ```bash
  pytest --ff
  ```

---

## 5. Performance and Debugging (`--durations`, `--tb`)
* **Profile slow tests (`--durations=N`)**: Show the top `N` slowest setup, test call, or teardown phases.
  ```bash
  pytest --durations=5
  ```
* **Control Stack Traces (`--tb`)**: Controls the verbosity of test failures. Options include `auto`, `long`, `short`, `line`, `native`, and `no`.
  ```bash
  pytest --tb=short
  ```
