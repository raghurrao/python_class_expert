# Day 4 Assignment: Built-in Markers (Skip, SkipIf, XFail)
# -----------------------------------------------------------------
# Add built-in pytest markers to the test functions below.
# Refer to the instructions inside each test function docstring.
# Run 'pytest' to check your progress.
# -----------------------------------------------------------------

import sys
import pytest
from .day4_functions import get_windows_path, buggy_feature_under_construction

# Task 1: Unconditional Skip
# Decorate this test to skip it unconditionally.
# Set the reason parameter to: "Feature is deprecated".
def test_deprecated_feature():
    # If this test is executed, it will fail:
    assert False


# Task 2: Conditional Skip
# Decorate this test to skip if the OS is NOT Windows.
# Hint: Use sys.platform != "win32" as the condition.
# Set the reason parameter to: "Requires Windows OS".
def test_windows_only_path():
    path = get_windows_path("documents")
    assert path.startswith("C:\\")


# Task 3: Expected Failure (XFail)
# Decorate this test to expect a failure because the feature is broken.
# 1. Set the reason parameter to: "Work in progress".
# 2. Set strict=True so that if the test unexpectedly passes, it is marked as FAILED.
def test_buggy_feature():
    result = buggy_feature_under_construction()
    assert result == "Completed"
