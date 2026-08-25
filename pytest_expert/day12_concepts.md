# Day 12: Test Parametrization (`@pytest.mark.parametrize`)

Yesterday, we parameterized a fixture. Today, we will learn how to parameterize **test functions** directly using the built-in `@pytest.mark.parametrize` decorator. This lets you run the same test logic against a table of inputs and expected outputs.

---

## 1. Syntax of `@pytest.mark.parametrize`
The decorator takes two main arguments:
1. **Argument Names**: A string of comma-separated argument names (e.g. `"input_val, expected_val"`).
2. **Argument Values**: A list of tuples, where each tuple contains values corresponding to the argument names.

```python
import pytest

def is_even(n):
    return n % 2 == 0

@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, False),
    (0, True),
    (-1, False)
])
def test_is_even(number, expected):
    # This test function runs 4 times!
    assert is_even(number) == expected
```

---

## 2. Naming Test Runs with `ids`
By default, pytest names the parameter test runs using their argument values (e.g. `test_is_even[2-True]`). You can customize these names using the `ids` parameter:

```python
@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, False)
], ids=["even_positive", "odd_positive"])
def test_is_even(number, expected):
    assert is_even(number) == expected
```
This is extremely useful when debugging failures in continuous integration summaries!

---

## 3. Stacking Parametrized Decorators (Cartesian Product)
If you stack multiple `@pytest.mark.parametrize` decorators on a single test function, pytest runs the **Cartesian product** (every combination) of all parameters:

```python
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [10, 20])
def test_combinations(x, y):
    # This runs 4 times: (x=1, y=10), (x=1, y=20), (x=2, y=10), (x=2, y=20)
    assert x + y > 10
```
Use stacking with caution, as adding parameters can cause the number of test runs to grow exponentially!
