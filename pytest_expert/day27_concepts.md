# Day 27: Professional Capstone Project

Congratulations! You have reached the Capstone Project of the Pytest Mastery course. Today, you will combine all the skills you've developed over the past 4 weeks to write a production-ready, enterprise-grade test suite.

---

## The Capstone Challenge: Testing `SecureDataManager`
You are provided with a package containing `day27_app.py`. It implements a class `SecureDataManager` that processes sensitive customer records:
1. **Async Connection**: Requires async `connect()` and `disconnect()` calls.
2. **Encryption Boundary**: Calls a low-level sync function `os_encrypt(data, key)` which is offline during testing.
3. **Data Verification**: Checks input length. If length is under 5 characters, logs a warning and raises a `ValueError`.
4. **Database Storage**: Calls `self.db_client.save_record(user_id, encrypted_data)` asynchronously.
5. **Metadata Backup**: Writes a local file named `meta_<user_id>.json` inside a backup directory.

---

## Test Suite Specifications
Your test suite inside `test_day27_assignment.py` must fulfill these criteria:

### 1. Fixture Design
* **Async Fixture `manager`**: Instantiates `SecureDataManager(db_client, backup_dir)`, calls `await manager.connect()`, yields the manager, and calls `await manager.disconnect()` in teardown.
* **Mock Database Client**: Use `Mock` to mock `db_client` and its async method `save_record`.
* **Path Mapping**: Use `tmp_path` to provide the backup directory.

### 2. Mocking & Monkeypatching
* Use `monkeypatch.setattr` to mock the low-level sync function `os_encrypt` in `day27_app.py` so it simply returns `"ENC_" + raw_data`.

### 3. Custom CLI Integration
* In `conftest.py`, register a new custom CLI option: `--skip-encryption`.
* Inside your test suite, if the `--skip-encryption` flag is passed, verify that your synchronization logic bypasses the `os_encrypt` function entirely.

### 4. Logging & System Auditing
* Inject `caplog` to assert that correct warning and info logs are captured during success and failure runs.

---

## Verification Commands
Verify your capstone project using:
```powershell
.venv\Scripts\python pytest_expert/verify_day27.py
```
This script will execute full mutation sweeps, CLI flag toggling, and AST structure audits to verify your test suite.
