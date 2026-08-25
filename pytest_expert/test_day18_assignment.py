# Day 18 Assignment: Testing External HTTP Clients
# -----------------------------------------------------------------
# Task 1: Test successful temperature retrieval.
# Task 2: Test API error code handling (status code 500).
# Task 3: Test API returning malformed JSON schemas.
# -----------------------------------------------------------------

from unittest.mock import Mock
import pytest
import requests
from .day18_app import WeatherClient, APIError

# Task 1: Test successful temperature retrieval
def test_get_temperature_success(monkeypatch):
    # 1. Create a mock response with status_code 200 and json returning {"temp_c": 22.5}
    # Your code here:

    # 2. Patch requests.get using monkeypatch to inject the mock response
    # Your code here:

    # 3. Instantiate WeatherClient("test_key") and assert get_temperature("London") returns 22.5
    # Your code here:
    pass


# Task 2: Test API failure handling (500 Server Error)
def test_get_temperature_api_failure(monkeypatch):
    # 1. Create a mock response with status_code 500
    # Your code here:

    # 2. Patch requests.get using monkeypatch to inject the mock response
    # Your code here:

    # 3. Assert calling get_temperature("Paris") raises an APIError containing "API returned error status: 500"
    # Your code here:
    pass


# Task 3: Test API returning malformed JSON structure (missing temp_c key)
def test_get_temperature_malformed_response(monkeypatch):
    # 1. Create a mock response with status_code 200 and json returning {"humidity": 80} (missing "temp_c")
    # Your code here:

    # 2. Patch requests.get using monkeypatch to inject the mock response
    # Your code here:

    # 3. Assert calling get_temperature("Tokyo") raises APIError containing "Malformed API response"
    # Your code here:
    pass
