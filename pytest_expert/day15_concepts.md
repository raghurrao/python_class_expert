# Day 15: Mocking Basics with `unittest.mock`

When testing a component, it often depends on external services (like payment gateways, mail servers, or third-party APIs). If these services are down or slow, your tests will fail or become sluggish. **Mocking** solves this by replacing these external dependencies with fake objects that mimic the real ones.

In Python, we use the standard library's `unittest.mock` module (specifically `Mock` and `MagicMock`), which integrates perfectly with pytest.

---

## 1. What is a Mock?
A Mock is a flexible object that can replace any Python object. You can configure it to:
* Return specific values when its methods are called.
* Raise specific exceptions.
* Record how many times it was called and with what arguments.

```python
from unittest.mock import Mock

# Create a mock object
mock_client = Mock()

# Configure a return value for a method
mock_client.get_user_name.return_value = "Bob"

# When you call it, it returns the configured value
name = mock_client.get_user_name(102)
assert name == "Bob"

# Verify how it was called
mock_client.get_user_name.assert_called_once_with(102)
```

---

## 2. Using `MagicMock`
`MagicMock` is a subclass of `Mock` that implements Python's magic methods (double underscore methods like `__len__`, `__str__`, `__iter__`, etc.) by default. It is the default mock type you should use.

```python
from unittest.mock import MagicMock

mock_list = MagicMock()
mock_list.__len__.return_value = 5

assert len(mock_list) == 5
```

---

## 3. Mocking Exceptions
If you want to test how your application handles errors from external services, you can configure a mock method to raise an exception using `side_effect`:

```python
mock_gateway = Mock()
# Configure to raise an exception
mock_gateway.charge_card.side_effect = ConnectionError("Gateway timeout")

import pytest

with pytest.raises(ConnectionError, match="Gateway timeout"):
    mock_gateway.charge_card()
```
