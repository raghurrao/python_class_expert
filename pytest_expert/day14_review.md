# Day 14: Week 2 Review & Retrospective

Incredible job! You have conquered Week 2. You have moved past simple assertions and markers into pytest's dependency injection system, lifecycle management, and data-driven testing configurations.

---

## 1. Week 2 Recap & Concepts Mastered
Here are the powerful tools you added to your test toolbox this week:

* **Fixtures & Dependency Injection**: Declaring `@pytest.fixture` functions and requesting them as arguments.
* **Yield Setup & Teardown**: Splitting execution into setup (before `yield`) and teardown (after `yield`) to clean up files or database states automatically.
* **Fixture Lifecycles (Scopes)**: Managing resource lifetimes at the `function` (default), `class`, `module`, or `session` level to optimize execution speed.
* **Autouse Fixtures**: Running background tasks automatically for every test using `autouse=True`.
* **Shared conftest.py Configurations**: Storing fixtures in `conftest.py` so they are automatically discovered by pytest without explicit imports.
* **The `request` Fixture**: Accessing test execution context and dynamic parameters using `request.param`.
* **Test Parametrization**: Running the same test function against tables of values using `@pytest.mark.parametrize` with custom test run `ids`.

---

## 2. Weekly Reflection Questions
Reflect on these design decisions:
1. *If a fixture opens a browser window and navigates to a login page, why should it be scope="session" or scope="module" instead of the default function scope? What are the tradeoffs?*
2. *When sharing fixtures in `conftest.py`, how does pytest decide which fixture to use if you have two fixtures with the exact same name in your root folder's `conftest.py` and a subfolder's `conftest.py`?*
3. *How do you test the Cartesian product of two lists of variables using `@pytest.mark.parametrize`?*

---

## 3. What's Next in Week 3?
Next week, we enter the world of **Mocking, Monkeypatching, and System Testing**.
We will learn:
* Mocking basics using `unittest.mock` and `MagicMock`.
* Patching environment variables, global attributes, and external modules using pytest's built-in `monkeypatch` fixture.
* Safely writing to disk without directory collisions using the built-in `tmp_path` fixture.
* Capturing standard terminal output and checking logs using `capsys` and `caplog`.
* Mocking HTTP clients and testing API integrations.

Keep up the momentum! You are halfway to becoming a true Pytest Expert!
