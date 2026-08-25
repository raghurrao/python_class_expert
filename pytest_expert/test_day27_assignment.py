# Day 27 Assignment: Professional Capstone Project
# -----------------------------------------------------------------
# Task 1: Write an async fixture 'manager' that returns a tuple (manager_instance, mock_db_client).
#         - Mock db_client's save_record async method using AsyncMock.
#         - Instantiate SecureDataManager, await connect(), yield, and await disconnect().
# Task 2: Implement three async test functions inside the class 'TestSecureDataManager'.
#         - test_encrypt_and_save_success
#         - test_payload_too_short
#         - test_skip_encryption_flag
# -----------------------------------------------------------------

from unittest.mock import Mock, AsyncMock
import pytest
import os
import json
from .day27_app import SecureDataManager, os_encrypt
from . import day27_app

# Task 1: Implement the async fixture 'manager'.
# 1. Inject 'tmp_path' into the fixture.
# 2. Instantiate mock_db = AsyncMock() (it must represent the db_client).
# 3. Instantiate manager_instance = SecureDataManager(mock_db, str(tmp_path)).
# 4. Await manager_instance.connect()
# 5. YIELD the tuple (manager_instance, mock_db)
# 6. Await manager_instance.disconnect() in teardown.
@pytest.fixture
async def manager(tmp_path):
    # Replace pass with your implementation:
    pass


class TestSecureDataManager:
    # Task 2a: Test successful encryption and storage.
    # 1. Destructure the manager fixture: manager_instance, mock_db = manager.
    # 2. Set caplog level to INFO.
    # 3. Use monkeypatch to patch "os_encrypt" inside day27_app to return "ENC_DATA".
    #    Hint: monkeypatch.setattr(day27_app, "os_encrypt", lambda data, key: "ENC_DATA")
    # 4. Await manager_instance.encrypt_and_save("usr_1", "my_secret_payload", "key_abc").
    #    Assert it returns True.
    # 5. Assert mock_db.save_record was awaited once with arguments ("usr_1", "ENC_DATA").
    #    Hint: mock_db.save_record.assert_awaited_once_with("usr_1", "ENC_DATA")
    # 6. Assert local metadata file "meta_usr_1.json" exists inside the manager's backup directory,
    #    and contains the text '{"size": 17}'.
    # 7. Assert caplog has info log message: "Successfully saved encrypted record for user usr_1"
    async def test_encrypt_and_save_success(self, manager, monkeypatch, caplog):
        # Replace pass with your assertions:
        pass

    # Task 2b: Test short payload rejection.
    # 1. Destructure: manager_instance, mock_db = manager.
    # 2. Set caplog level to WARNING.
    # 3. Assert calling manager_instance.encrypt_and_save("usr_1", "abc", "key") raises ValueError.
    # 4. Assert mock_db.save_record was NOT called.
    # 5. Assert caplog has warning log message: "Short payload rejected for user usr_1"
    async def test_payload_too_short(self, manager, caplog):
        # Replace pass with your assertions:
        pass

    # Task 2c: Test skip encryption flag.
    # 1. Destructure: manager_instance, mock_db = manager.
    # 2. Fetch the '--skip-encryption' flag value from the request fixture:
    #    skip_flag = request.config.getoption("--skip-encryption")
    # 3. Use monkeypatch to patch "os_encrypt" to return "ENC_DATA".
    # 4. Await manager_instance.encrypt_and_save("usr_1", "my_secret_payload", "key_abc", skip_encryption=skip_flag).
    # 5. If skip_flag is True, assert mock_db.save_record was called with raw data: ("usr_1", "my_secret_payload").
    #    If skip_flag is False, assert mock_db.save_record was called with encrypted data: ("usr_1", "ENC_DATA").
    async def test_skip_encryption_flag(self, manager, monkeypatch, request):
        # Replace pass with your assertions:
        pass
