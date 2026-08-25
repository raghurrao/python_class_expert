# Day 17: Standard System Fixtures (`tmp_path`, `capsys`, `caplog`)

Pytest provides built-in fixtures to interact with the operating system, terminal outputs, and logger records. Today we cover the three most common: **`tmp_path`**, **`capsys`**, and **`caplog`**.

---

## 1. File System Mocks: `tmp_path`
The `tmp_path` fixture provides a unique temporary directory for each test function. It returns a **`pathlib.Path`** object. Pytest manages the directories and deletes old ones automatically.

```python
def test_file_writer(tmp_path):
    # tmp_path is a unique Path object
    my_file = tmp_path / "settings.json"
    
    # Write text to the temporary file
    my_file.write_text('{"theme": "dark"}')
    
    # Assertions
    assert my_file.exists() is True
    assert my_file.read_text() == '{"theme": "dark"}'
```

---

## 2. Capturing Terminal Output: `capsys`
When functions print status messages using `print()`, they write to standard output (`stdout`). Pytest captures this. The `capsys` fixture lets you inspect it:

```python
def test_console_logs(capsys):
    print("Initializing engine...")
    
    # Capture all stdout and stderr since the start of the test
    captured = capsys.readouterr()
    
    # captured.out contains stdout, captured.err contains stderr
    assert captured.out == "Initializing engine...\n"
```
> [!NOTE]
> `capsys.readouterr()` clears the buffer. Calling it twice in the same test will return empty output for the second call.

---

## 3. Capturing Log Messages: `caplog`
If your application uses Python's standard `logging` library, you can assert that specific warning or error messages are recorded using `caplog`:

```python
import logging
import pytest

def process_transaction(amount):
    if amount < 0:
        logging.warning(f"Negative transaction skipped: {amount}")

def test_transaction_warning(caplog):
    # Temporarily set log capture level to WARNING
    caplog.set_level(logging.WARNING)
    
    process_transaction(-50)
    
    # Verify the log message was captured
    assert "Negative transaction skipped: -50" in caplog.text
    
    # You can also inspect the structured records list
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "WARNING"
```
