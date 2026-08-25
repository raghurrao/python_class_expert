# Day 18: Testing External HTTP Clients

When writing software that consumes REST APIs, your unit tests should never make real HTTP network requests. Real calls are slow, can hit rate limits, require an internet connection, and might change the database state of the external service.

Today, we will learn how to mock the python `requests` library to return custom status codes and JSON payloads without leaving the local machine.

---

## 1. Mocking the HTTP Response
To mock a `requests.get` or `requests.post` call, we need to return a mock object that mimics a `requests.Response` object. The methods/attributes we usually need to stub are:
* **`status_code`** (integer like 200, 404, 500)
* **`json()`** (a method returning a dictionary of the parsed response)
* **`text`** (string response body)

```python
from unittest.mock import Mock

# 1. Create a fake response
mock_response = Mock()
mock_response.status_code = 200
mock_response.json.return_value = {"status": "active", "id": 42}
```

---

## 2. Patching `requests.get` using `monkeypatch`
We can use the `monkeypatch` fixture to temporarily replace `requests.get` with a function that returns our mock response.

```python
import requests
import pytest

def test_fetch_user(monkeypatch):
    # 1. Setup mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"username": "alice"}
    
    # 2. Patch requests.get to return our mock response
    # We pass a lambda that accepts the URL argument and returns our mock_response
    monkeypatch.setattr(requests, "get", lambda url, headers=None: mock_response)
    
    # 3. Call your application code
    user = my_api_client.fetch_user(42)
    assert user == "alice"
```

---

## 3. Testing HTTP Failures
Mocking makes it trivial to test how your code behaves when remote servers crash (500 Internal Server Error) or endpoints are missing (404 Not Found):

```python
def test_fetch_user_server_error(monkeypatch):
    mock_response = Mock()
    mock_response.status_code = 500
    
    monkeypatch.setattr(requests, "get", lambda url, headers=None: mock_response)
    
    # Assert your application code raises a custom exception when it gets a 500 error
    with pytest.raises(RuntimeError, match="API Server Error"):
        my_api_client.fetch_user(42)
```
