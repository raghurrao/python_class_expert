# Day 21: Week 3 Review & Retrospective

Fantastic progress! You have completed Week 3 of your Pytest Mastery course. You are now fully capable of writing completely isolated, fast, and deterministic tests that mock databases, patch network requests, write safely to temporary directories, and verify stdout print streams and logger levels.

---

## 1. Week 3 Recap & Concepts Mastered
Here are the core system isolation skills you learned this week:

* **Dependency Mocking**: Replacing third-party services with `Mock` and `MagicMock` instances, stubbing methods using `return_value` and exceptions using `side_effect`, and asserting call counts/parameters using `assert_called_once_with`.
* **Safe State Monkeypatching**: Dynamically patching attributes, configuration values, and environment variables using the `monkeypatch` fixture. It automatically cleans up environment modifications when each test exits.
* **Built-in System Fixtures**:
  * **`tmp_path`**: Safely writing and verifying file inputs/outputs inside unique temporary directories as `pathlib.Path` objects.
  * **`capsys`**: Capturing and checking terminal outputs (`print()` logs).
  * **`caplog`**: Asserting that your application correctly logs warning, info, and error messages via the Python logging library.
* **HTTP Client Mocking**: Stubbing `requests.get` to return mock responses (with custom status codes and JSON payloads) to isolate network components.
* **Database Isolation**: Setting up transactional fixtures that run `begin_transaction()` before and `rollback()` after each test to prevent data pollution across test cases.

---

## 2. Weekly Reflection Questions
Consider these professional unit testing questions:
1. *When should you use `unittest.mock.Mock` to patch dependencies vs. using pytest's built-in `monkeypatch` fixture?*
2. *Why is transactional database rollback preferred over deleting all rows in a teardown function for real database tests?*
3. *If a function prints status text to the terminal and raises a warning log, what is the best way to capture and verify both in a single test case?*

---

## 3. What's Next in Week 4?
Next week, we enter the final **Expert Level** phase:
* Testing asynchronous functions and fixtures using `pytest-asyncio`.
* Measuring and reporting code coverage metrics using `pytest-cov`.
* Developing custom CLI options and registering custom flags using `conftest.py` hooks.
* Writing custom plugins and utilizing advanced pytest hooks (e.g. `pytest_addoption` and `pytest_runtest_setup`).
* Scaling and parallelizing test runs on multiple CPU cores using `pytest-xdist`.
* Setting up testing in GitHub Actions CI/CD pipelines.

You are entering the expert tier! Let's get ready for the final week.
