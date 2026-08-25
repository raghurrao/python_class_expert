# Day 7: Week 1 Review & Retrospective

Congratulations! You have completed Week 1 of your Pytest Mastery journey. You've gone from writing basic assert statements to building a robust, configured test suite that handles exceptions, maps platform dependencies, and runs selective categories of tests.

---

## 1. Week 1 Recap & Concepts Mastered
Here is a summary of the core building blocks you have acquired:

* **Testing Philosophy**: Why we test, and how `pytest` simplifies testing by eliminating Java-style OOP boilerplate (no more `self.assertEqual`).
* **Naming Conventions**: Why files must be `test_*.py` / `*_test.py`, test classes must be `Test*`, and test functions must be `test_*` for auto-discovery.
* **Assertion Magic**: How pytest rewrites assertions behind the scenes to show rich diff comparisons for lists, sets, and nested dicts.
* **Exception Verification**: Testing code boundary cases using `with pytest.raises(...)` and inspecting details via `excinfo` or the `match` regex parameter.
* **CLI Command Filters**: Running individual test cases, filtering with `-k` using `and`, `or`, `not` boolean strings, capturing print stdout with `-s`, and debugging failed suites with `--lf` and `-x`.
* **Built-in Markers**: Controlling test conditions with `@pytest.mark.skip`, `@pytest.mark.skipif`, and managing known bugs with `@pytest.mark.xfail(strict=True)`.
* **Custom Markers & Configs**: Creating markers like `fast` and `security`, registering them in `pytest.ini` to prevent warnings, and filtering execution with `pytest -m <marker>`.

---

## 2. Weekly Reflection Questions
Take a moment to write down or think about the answers to these:
1. *When should you use `with pytest.raises(..., match="...")` instead of just checking the exception class type?*
2. *Why is registering custom markers in `pytest.ini` or `pyproject.toml` considered a best practice in professional settings?*
3. *If you have 100 tests and 5 of them are failing, what is the fastest CLI sequence of commands to run and debug ONLY those 5 failing tests, showing print statements immediately?*

---

## 3. What's Next in Week 2?
Next week, we unlock pytest's most powerful and distinctive feature: **Fixtures**.
We will learn:
* Dependency injection basics.
* Setup and teardown patterns using `yield`.
* Controlling fixture lifetime scopes (`function`, `class`, `module`, `session`).
* Sharing fixtures seamlessly using `conftest.py`.
* Writing data-driven test suites using `@pytest.mark.parametrize` to run a single test function against dozens of input scenarios.

Get ready for an exciting week!
