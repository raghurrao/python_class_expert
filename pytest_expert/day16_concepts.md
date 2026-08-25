# Day 16: Monkeypatching (`monkeypatch` Fixture)

In Python, you can modify classes, modules, and environment variables dynamically at runtime. This is called "monkeypatching". Pytest provides a built-in fixture named **`monkeypatch`** to do this safely.

---

## 1. Why Use `monkeypatch`?
If you modify global objects or environment variables manually in a test, they will stay modified for the rest of your test suite. This leads to leaky tests that depend on the order of execution. 

The `monkeypatch` fixture automatically **restores** all modified attributes, dictionary values, and environment variables when the test finishes!

---

## 2. Common `monkeypatch` Methods

### A. Modifying Environment Variables (`setenv` / `delenv`)
Often, configuration managers read values from environment variables (e.g. database credentials or API keys).

```python
def test_config_with_env(monkeypatch):
    # Set an environment variable for the duration of this test
    monkeypatch.setenv("DATABASE_URL", "sqlite:///:memory:")
    
    # Execute code that reads os.environ["DATABASE_URL"]
    config = load_config()
    assert config.db_url == "sqlite:///:memory:"
    
    # Once this test exits, DATABASE_URL is automatically restored to its original value!
```

### B. Patching Object/Module Attributes (`setattr`)
If you want to mock a single function inside another module without mocking the entire class, use `setattr`:

```python
import os
import pytest

def test_custom_home_directory(monkeypatch):
    # Temporarily mock os.path.expanduser to return a dummy path
    monkeypatch.setattr(os.path, "expanduser", lambda x: "/mock/home")
    
    assert os.path.expanduser("~") == "/mock/home"
```

### C. Modifying Dictionaries (`setitem` / `delitem`)
Use `setitem` to temporarily inject or change keys inside dictionaries (like `os.environ` or settings dicts):

```python
def test_settings(monkeypatch):
    my_settings = {"debug": False}
    # Set setting 'debug' to True
    monkeypatch.setitem(my_settings, "debug", True)
    assert my_settings["debug"] is True
```
