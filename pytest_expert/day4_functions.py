# Day 4: Target Functions for Markers
import sys

def get_windows_path(path):
    """Returns Windows specific path formatting. Raises OSError on other systems."""
    if sys.platform != "win32":
        raise OSError("This function can only be run on Windows systems.")
    return f"C:\\Users\\default\\{path}"

def buggy_feature_under_construction():
    """Known buggy feature that will fail for now by raising NotImplementedError."""
    raise NotImplementedError("Feature is under construction. Expected to fail.")
