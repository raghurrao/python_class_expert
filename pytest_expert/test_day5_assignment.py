# Day 5 Assignment: Custom Markers & Configuration
# -----------------------------------------------------------------
# Task 1: Decorate the tests below with custom markers "fast" and "database".
# Task 2: Create a 'pytest.ini' file inside 'pytest_expert' directory
#         and register both custom markers inside it.
# -----------------------------------------------------------------

import pytest
from .day5_functions import fast_login, slow_sync_database

# Task 1a: Decorate this function with your custom @pytest.mark.fast marker.
def test_fast_login():
    assert fast_login("admin") is True

# Task 1b: Decorate this function with your custom @pytest.mark.database marker.
def test_db_sync():
    assert slow_sync_database() == "Synced"
