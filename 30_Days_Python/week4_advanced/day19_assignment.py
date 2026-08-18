# Day 19 Assignment: Working with Web APIs
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below by filling in the blanks.
# Do not change the function names. You can run 'python day19_test.py'
# to check your solutions.

import requests

# ======================================================================
# Exercise 1: Fetch GitHub User Details
# ======================================================================
# Task: Complete the function 'fetch_github_user' that takes a 'username' (str).
# 1. Send an HTTP GET request to: "https://api.github.com/users/<username>"
# 2. Check the response status code:
#    - If it is 200, parse the JSON body and return a dictionary with keys:
#      'name' (str/None), 'public_repos' (int), 'followers' (int).
#    - If it is 404, return the string "User not found".
#    - For any other status code, return string "Error: <status_code>"

def fetch_github_user(username):
    # TODO: Perform GET, parse output or handle status error messages
    pass


# ======================================================================
# Exercise 2: HTTP Status Checker with Exceptions
# ======================================================================
# Task: Complete the function 'get_http_status_message' that accepts a 'url' (str).
# 1. Send an HTTP GET request to the URL.
# 2. If the request is successful and returns a 2xx status code (e.g. 200 to 299),
#    return string: "Success: <status_code>"
# 3. Otherwise (e.g. 3xx, 4xx, 5xx), return string: "Failure: <status_code>"
# 4. Use a try-except block to catch 'requests.RequestException' (which catches timeouts,
#    connection errors, etc.) and return the string: "Network error"

def get_http_status_message(url):
    # TODO: Implement request sending and exception handling
    pass
