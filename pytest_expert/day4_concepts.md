# Day 4: Built-in Markers (Skip, SkipIf, XFail)

In production software, some tests cannot run on all platforms, require specific Python versions, or fail because of known bugs that are not yet fixed. Pytest provides built-in decorators (called **markers**) to handle these scenarios gracefully without breaking the build.

---

## 1. What are Markers?
Markers are decorators applied to test functions or classes to configure their behavior. Pytest has several built-in markers:
* `@pytest.mark.skip`
* `@pytest.mark.skipif`
* `@pytest.mark.xfail`
* `@pytest.mark.parametrize` (which we will cover next week!)

---

## 2. Unconditional Skipping (`@pytest.mark.skip`)
If a feature is deprecated, temporarily broken, or slow, you can tell pytest to ignore the test entirely:

```python
import pytest

@pytest.mark.skip(reason="Legacy API is currently offline")
def test_legacy_connection():
    # This code will not be run
    assert connect_legacy() == True
```

---

## 3. Conditional Skipping (`@pytest.mark.skipif`)
If a test should only run under certain conditions (e.g., specific Operating System, Python version, database type), use `skipif`. It takes a boolean condition and a reason string:

```python
import sys
import pytest

@pytest.mark.skipif(sys.platform != "win32", reason="Requires Windows OS")
def test_windows_registry():
    assert read_windows_registry() is not None

@pytest.mark.skipif(sys.version_info < (3, 11), reason="Requires Python 3.11 or higher")
def test_new_match_syntax():
    # Code that uses features introduced in Python 3.11
    pass
```

---

## 4. Expected Failures (`@pytest.mark.xfail`)
If you write a test for a known bug before it is fixed (a practice in test-driven development), you don't want that test to fail your entire continuous integration (CI) pipeline. 
The `@pytest.mark.xfail` marker tells pytest that we *expect* this test to fail:

* If the test **fails** (as expected): reported as **XFAIL** (Expected Failure). The overall test suite passes.
* If the test **passes** (unexpectedly): reported as **XPASS** (Unexpected Pass). By default, the overall test suite still passes, but warning logs are shown.

```python
@pytest.mark.xfail(reason="Bug #1043: Timeout on heavy loads")
def test_heavy_load_query():
    assert run_heavy_query() == "success"
```

### Strict Mode (`strict=True`)
To force the test suite to fail if an `xfail` test unexpectedly passes (for example, to make sure you remember to clean up the marker when a bug is fixed), set `strict=True`:

```python
@pytest.mark.xfail(strict=True, reason="Bug #1043: Timeout on heavy loads")
def test_heavy_load_query():
    # If this passes, pytest will report a test FAILURE!
    pass
```
* If it fails: reported as XFAIL (Passed/Green run).
* If it passes: reported as FAILED (Failed/Red run).
