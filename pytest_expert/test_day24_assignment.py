# Day 24 Assignment: Custom Command-Line Options
# -----------------------------------------------------------------
# Task 2: Implement test_slow_task to skip itself if '--run-slow' flag is absent.
# -----------------------------------------------------------------

import pytest

# Task 2: Implement test_slow_task checking for custom option --run-slow
def test_slow_task(request):
    # 1. Fetch the value of the custom command line option "--run-slow" using request.config.getoption.
    # Your code here:

    # 2. If the option is False (flag was not passed), call pytest.skip with the message "Requires --run-slow flag".
    # Your code here:

    # 3. Otherwise, assert True.
    # Your code here:
    pass
