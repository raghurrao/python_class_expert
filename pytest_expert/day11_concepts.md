# Day 11: Dynamic Fixtures & the `request` Object

Today, we will learn how to make fixtures dynamic by parameterizing them, and how to inspect the calling test context using pytest's built-in **`request`** fixture.

---

## 1. The Built-in `request` Fixture
The `request` fixture is a special, built-in system fixture. You can inject it into your custom fixtures to inspect information about the test function that is currently running:
* **`request.node.name`**: The name of the running test function.
* **`request.module.__name__`**: The name of the test module.
* **`request.param`**: The specific parameter value currently being injected (used in parameterized fixtures).

```python
import pytest

@pytest.fixture
def log_test_context(request):
    # Retrieve the name of the test that called this fixture
    test_name = request.node.name
    print(f"\nRunning fixture setup for test: {test_name}")
    yield
```

---

## 2. Fixture Parametrization
You can specify a list of values in the fixture decorator using the `params` keyword. Pytest will run **every test function that requests this fixture once for each parameter value**. 

Inside the fixture, you retrieve the current parameter value using `request.param`:

```python
import pytest

@pytest.fixture(params=["sqlite", "postgresql"])
def db_engine(request):
    # request.param holds the current value ("sqlite" or "postgresql")
    engine_name = request.param
    db = DatabaseClient(engine=engine_name)
    db.connect()
    
    yield db
    
    db.disconnect()

def test_insertion(db_engine):
    # This test runs TWICE:
    # 1st run: db_engine is sqlite
    # 2nd run: db_engine is postgresql
    assert db_engine.is_healthy() is True
```

**Why is this powerful?**
If you have 10 tests that request `db_engine`, pytest runs all 10 tests twice, generating a matrix of 20 runs. This is the foundation of cross-compatibility testing!
