# Day 10: Sharing Fixtures via `conftest.py`

When building a large test suite, you don't want to redefine the same fixtures (like database connections or mock clients) in every single test file. You also want to avoid manual imports. Pytest solves this using a special configuration file named **`conftest.py`**.

---

## 1. What is `conftest.py`?
`conftest.py` is a file where you define shared fixtures, hooks, and plugins. Pytest automatically discovers this file during startup and injects its fixtures into any test function running in the same directory or its subdirectories.
* **No Imports Required**: You do **NOT** import fixtures from `conftest.py`. If a test requests a fixture name, pytest resolves it automatically from `conftest.py`.

---

## 2. Directory Hierarchy and Discovery
Pytest looks for `conftest.py` recursively starting from the directory of the test file being executed, up to the root folder.

```text
tests/
│
├── conftest.py          # Fixtures defined here are available globally
│
├── auth/
│   ├── conftest.py      # Fixtures defined here are available ONLY in auth/
│   └── test_login.py
│
└── payment/
    └── test_checkout.py
```

* **Global Fixtures**: Defined in the root `conftest.py`.
* **Scoped/Local Fixtures**: Defined in subfolders' `conftest.py`.

---

## 3. Today's Assignment
You will work in a new directory named `day10_tests/` inside your `pytest_expert` folder:
1. Open [day10_tests/conftest.py](file:///g:/Backup%20Fdrive/Python/pytest_expert/day10_tests/conftest.py) and implement a session-scoped fixture named `app_version` returning `"2.0.1"`.
2. Open [day10_tests/test_auth.py](file:///g:/Backup%20Fdrive/Python/pytest_expert/day10_tests/test_auth.py) and write a test function requesting `app_version`.
3. Open [day10_tests/test_payment.py](file:///g:/Backup%20Fdrive/Python/pytest_expert/day10_tests/test_payment.py) and write another test function requesting `app_version`.

Notice that neither test file will import `conftest.py`!
