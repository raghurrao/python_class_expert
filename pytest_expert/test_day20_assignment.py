# Day 20 Assignment: Week 3 Integration Milestone
# -----------------------------------------------------------------
# Task 1: Implement test_sync_success(tmp_path, caplog) to verify success sync execution.
# Task 2: Implement test_sync_api_failure(tmp_path, caplog) to verify exceptions and logs.
# -----------------------------------------------------------------

from unittest.mock import Mock
import pytest
import os
from .day20_app import WeatherSyncEngine, APIError

# Task 1: Test successful synchronization
def test_sync_success(tmp_path, caplog):
    # 1. Set caplog capture level to INFO
    # Your code here:

    # 2. Create a Mock weather_client. Configure get_temperature() to return 25.5.
    # Your code here:

    # 3. Create a Mock db_manager.
    # Your code here:

    # 4. Instantiate WeatherSyncEngine. Inject the mock weather_client, the mock db_manager,
    #    and str(tmp_path) as the backup directory.
    # Your code here:

    # 5. Call sync_weather("Paris") and assert it returns True.
    # Your code here:

    # 6. Assert mock db_manager.add_record was called once with ("Paris", 25.5).
    # Your code here:

    # 7. Assert that backup file "paris_weather.txt" exists in tmp_path and contains
    #    the exact text: "City: Paris, Temp: 25.5C"
    # Your code here:

    # 8. Assert caplog captured the INFO message: "Synced city Paris temperature 25.5C"
    # Your code here:
    pass


# Task 2: Test sync failure handling when API raises exception
def test_sync_api_failure(tmp_path, caplog):
    # 1. Set caplog capture level to WARNING
    # Your code here:

    # 2. Create a Mock weather_client. Configure get_temperature() to raise an APIError("Connection Timeout").
    # Your code here:

    # 3. Create a Mock db_manager.
    # Your code here:

    # 4. Instantiate WeatherSyncEngine injecting the mocks and str(tmp_path).
    # Your code here:

    # 5. Assert calling sync_weather("London") raises a RuntimeError.
    # Your code here:

    # 6. Assert mock db_manager.add_record was NOT called.
    # Your code here:

    # 7. Assert caplog captured the WARNING message: "Failed to sync city London"
    # Your code here:
    pass
