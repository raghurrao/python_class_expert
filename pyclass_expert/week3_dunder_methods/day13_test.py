# Day 13 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day13_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week3_dunder_methods.day13_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day13_assignment.py. Error: {e}")
    sys.exit(1)

passed_tests = 0
total_tests = 0

def run_test(test_name, test_fn):
    global passed_tests, total_tests
    total_tests += 1
    try:
        test_fn()
        print(f"[PASS] {test_name}")
        passed_tests += 1
    except AssertionError as e:
        print(f"[FAIL] {test_name}")
        print(f"   AssertionError: {e}\n")
    except Exception as e:
        print(f"[FAIL] {test_name}")
        print(f"   Unexpected Error: {type(e).__name__}: {e}\n")

print("Starting Day 13 Tests...\n")

# 1. Playlist Sequence & Container Protocol Tests
def test_playlist_protocol():
    assert hasattr(assignment, 'Playlist'), "Playlist class missing"
    
    pl = assignment.Playlist("My Rock List")
    assert len(pl) == 0, "Initial length should be 0"
    
    # Populate songs
    pl._songs.extend(["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"])
    
    # Check len
    assert len(pl) == 3
    
    # Check getitem
    assert pl[0] == "Bohemian Rhapsody"
    assert pl[-1] == "Hotel California"
    
    # Check slice
    assert pl[0:2] == ["Bohemian Rhapsody", "Stairway to Heaven"], f"Slicing mismatch: {pl[0:2]}"
    
    # Check setitem
    pl[1] = "Back in Black"
    assert pl[1] == "Back in Black"
    
    # Type validation in setitem
    try:
        pl[2] = 12345
        raise AssertionError("Setting song to non-string should raise TypeError")
    except TypeError:
        pass
        
    # Check delitem
    del pl[0]
    assert len(pl) == 2
    assert pl[0] == "Back in Black"
    
    # Check case-insensitive contains
    assert "back in black" in pl, "Membership check should be case-insensitive"
    assert "BACK IN BLACK" in pl
    assert "Hotel California" in pl
    assert "Bohemian Rhapsody" not in pl, "Bohemian Rhapsody should have been deleted"

run_test("Playlist container and sequence protocol validation", test_playlist_protocol)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 13 assignments.")
    print(f"Proceed to Day 14 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day13_assignment.py")
