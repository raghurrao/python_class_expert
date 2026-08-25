# Day 17 Assignment: Standard System Fixtures
# -----------------------------------------------------------------
# Task 1: Test successful text processing (file save, print stdout, info logs).
# Task 2: Test empty text warning logs and warning print capture.
# -----------------------------------------------------------------

import logging
import pytest
from .day17_app import TextProcessor

def test_process_success(tmp_path, capsys, caplog):
    # 1. Create a temporary filepath using tmp_path (e.g. tmp_path / "out.txt")
    # Your code here:

    # 2. Set caplog capture level to INFO
    # Your code here:

    # 3. Instantiate TextProcessor with your temporary filepath, 
    #    and call process_and_save("hello world")
    # Your code here:

    # 4. Assert the file exists and contains "HELLO WORLD" (uppercase/trimmed)
    # Your code here:

    # 5. Assert capsys captures stdout containing the string "File saved"
    # Your code here:

    # 6. Assert caplog captures an INFO log message containing "Successfully processed 11 characters"
    # Your code here:
    pass


def test_process_empty(capsys, caplog):
    # 1. Set caplog capture level to WARNING
    # Your code here:

    # 2. Instantiate TextProcessor with a dummy path (e.g., "dummy.txt"),
    #    and call process_and_save("")
    # Your code here:

    # 3. Assert capsys captures stdout containing "Warning: Received empty text"
    # Your code here:

    # 4. Assert caplog captures a WARNING log message "Empty string passed to processor"
    # Your code here:
    pass
