# Day 16 Assignment: Monkeypatching
# -----------------------------------------------------------------
# Task 1: Test config loader with mocked environment variables.
# Task 2: Test config loader error when DB_URL is missing.
# Task 3: Mock OS utility function using monkeypatch.setattr.
# -----------------------------------------------------------------

import pytest
from .day16_app import ConfigLoader, get_system_uptime
from . import day16_app  # Imported for attribute patching in Task 3

# Task 1: Test successful config load
def test_config_load_success(monkeypatch):
    # 1. Use monkeypatch.setenv to set environment variables "DB_URL" to "sqlite:///test.db"
    #    and "API_KEY" to "secret123".
    # Your code here:

    # 2. Instantiate ConfigLoader(), call load_from_env()
    # Your code here:

    # 3. Assert loader.db_url is "sqlite:///test.db" and loader.api_key is "secret123".
    # Your code here:
    pass


# Task 2: Test missing DB URL raises ValueError
def test_config_load_missing_db(monkeypatch):
    # 1. Use monkeypatch.delenv to delete "DB_URL" from environment (use raising=False to prevent crashes)
    # Your code here:

    # 2. Assert load_from_env() raises a ValueError containing the message "DB_URL environment variable is missing"
    # Your code here:
    pass


# Task 3: Mock the OS utility function using monkeypatch.setattr
def test_system_uptime(monkeypatch):
    # 1. Use monkeypatch.setattr to patch "get_system_uptime" inside day16_app module.
    #    Hint: monkeypatch.setattr(day16_app, "get_system_uptime", lambda: 3600)
    # Your code here:

    # 2. Call get_system_uptime() and assert it returns 3600.
    # Your code here:
    pass
