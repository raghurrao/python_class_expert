# Day 19: Working with Web APIs

Modern applications rarely run in isolation; they talk to databases, external services, and remote servers. Today, we will learn how Python communicates over the web using the HTTP protocol and the third-party **`requests`** library.

---

## 1. HTTP and Web Requests

**HTTP** (HyperText Transfer Protocol) is the foundation of data exchange on the World Wide Web.
*   **Request**: Sent by the client (your Python script) to a server.
*   **Response**: Returned by the server back to your script.

### Common HTTP Methods
*   **`GET`**: Retrieve data from a server.
*   **`POST`**: Submit new data to a server.

### HTTP Status Codes
*   **`200 OK`**: Request succeeded.
*   **`404 Not Found`**: The requested resource does not exist.
*   **`500 Internal Server Error`**: Something went wrong on the server.

---

## 2. Using the `requests` Library

While Python has built-in HTTP tools (`urllib`), they are verbose and complex. The community standard is **`requests`**, which is extremely user-friendly.

> [!NOTE]
> `requests` is a third-party library. To install it, run:
> ```powershell
> pip install requests
> ```

### Sending a GET Request
```python
import requests

url = "https://api.github.com/users/octocat"
response = requests.get(url)

# Check status code
print(response.status_code)  # Output: 200

# Parse JSON response body directly into a Python dictionary
user_data = response.json()
print(user_data["name"])  # Output: The Octocat
```

### Passing Query Parameters
Some API endpoints accept search terms or options as query parameters (e.g., `?q=python`). You can pass them as a dictionary:
```python
params = {"q": "python", "sort": "stars"}
response = requests.get("https://api.github.com/search/repositories", params=params)
```

---

Now, proceed to the Day 19 Assignment: [day19_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week4_advanced/day19_assignment.py).
