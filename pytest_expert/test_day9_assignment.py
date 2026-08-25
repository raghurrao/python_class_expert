# Day 9 Assignment: Fixture Scopes & Autouse
# -----------------------------------------------------------------
# Task 1: Create a session-scoped fixture named 'logger' that returns a TelemetryLogger.
#         It must start_session() before tests, yield, and end_session() after.
# Task 2: Create a function-scoped autouse fixture named 'auto_log_test'.
#         It must inject 'logger', log "test_run" before, yield, and log "test_done" after.
# -----------------------------------------------------------------

import pytest
from .day9_app import TelemetryLogger

# Task 1: Create the session-scoped fixture named 'logger'.
# 1. Set scope="session" in the fixture decorator.
# 2. Instantiate TelemetryLogger()
# 3. Call start_session() on the instance
# 4. YIELD the logger object
# 5. Call end_session() on the instance in teardown
# Your code here:
@pytest.fixture
def logger():
    # Replace pass with your implementation:
    pass


# Task 2: Create the autouse function-scoped fixture named 'auto_log_test'.
# 1. Set autouse=True in the decorator.
# 2. Inject the 'logger' fixture as an argument.
# 3. Call logger.log_event("test_run") before the yield.
# 4. YIELD
# 5. Call logger.log_event("test_done") after the yield.
# Your code here:
@pytest.fixture
def auto_log_test():
    # Replace pass with your implementation:
    pass


# Test cases that use the logger to verify setup
def test_feature_alpha(logger):
    logger.log_event("alpha_click")
    assert "alpha_click" in logger.events

def test_feature_beta(logger):
    logger.log_event("beta_hover")
    assert "beta_hover" in logger.events
