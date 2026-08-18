# Day 19 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day19_test.py
# It will verify if your API connection code is correct!

import sys
import os
from unittest.mock import patch, Mock
import requests

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week4_advanced.day19_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day19_assignment.py. Error: {e}")
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

print("Starting Day 19 Tests...\n")

# 1. Test fetch_github_user
@patch('week4_advanced.day19_assignment.requests.get')
def test_fetch_github_user(mock_get):
    assert hasattr(assignment, 'fetch_github_user'), "fetch_github_user not found"
    
    # Mock successful response
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_type = None
    mock_resp.json.return_value = {
        "name": "Octocat",
        "public_repos": 15,
        "followers": 100,
        "company": "GitHub"
    }
    mock_get.return_value = mock_resp
    
    res1 = assignment.fetch_github_user("octocat")
    assert isinstance(res1, dict), f"Expected dict, got {type(res1).__name__}"
    assert res1.get('name') == "Octocat"
    assert res1.get('public_repos') == 15
    assert res1.get('followers') == 100
    assert 'company' not in res1, "Dictionary should only contain 'name', 'public_repos', and 'followers'"
    
    # Mock 404 response
    mock_resp_404 = Mock()
    mock_resp_404.status_code = 404
    mock_get.return_value = mock_resp_404
    
    res2 = assignment.fetch_github_user("invaliduser123")
    assert res2 == "User not found", f"Expected 'User not found', got '{res2}'"
    
    # Mock 500 response
    mock_resp_500 = Mock()
    mock_resp_500.status_code = 500
    mock_get.return_value = mock_resp_500
    res3 = assignment.fetch_github_user("any")
    assert res3 == "Error: 500", f"Expected 'Error: 500', got '{res3}'"

run_test("Verify GitHub user fetch states & data dictionary filters", lambda: test_fetch_github_user())

# 2. Test get_http_status_message
@patch('week4_advanced.day19_assignment.requests.get')
def test_get_http_status_message(mock_get):
    assert hasattr(assignment, 'get_http_status_message'), "get_http_status_message not found"
    
    # Success 2xx
    mock_resp = Mock()
    mock_resp.status_code = 201
    mock_get.return_value = mock_resp
    res1 = assignment.get_http_status_message("https://example.com")
    assert res1 == "Success: 201", f"Got: {res1}"
    
    # Failure 4xx
    mock_resp_400 = Mock()
    mock_resp_400.status_code = 400
    mock_get.return_value = mock_resp_400
    res2 = assignment.get_http_status_message("https://example.com")
    assert res2 == "Failure: 400", f"Got: {res2}"
    
    # Exception (network error)
    mock_get.side_effect = requests.RequestException("Connection timed out")
    res3 = assignment.get_http_status_message("https://badurl.com")
    assert res3 == "Network error", f"Expected 'Network error', got '{res3}'"

run_test("Verify URL status checker and HTTP network exception handling", lambda: test_get_http_status_message())

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 19 assignments.")
    print(f"Proceed to Day 20 when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day19_assignment.py")
