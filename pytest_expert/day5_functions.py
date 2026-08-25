# Day 5: Target Functions for Custom Markers
import time

def fast_login(username):
    """A fast operation representing username check."""
    if not username:
        return False
    return True

def slow_sync_database():
    """A slow operation representing database sync."""
    time.sleep(0.05)
    return "Synced"
