# Day 8: File Handling & Serialization

Data in variables resides in volatile memory (RAM) and is lost when the program ends. Today we learn how to read and write data to persistent storage (files) and serialize structures to JSON.

---

## 1. File Handling & Context Managers

In Python, the safest way to work with files is using the `with` statement, which acts as a **context manager**. It automatically closes the file after the block of code executes, even if errors occur.

### Opening a File: `open(filepath, mode)`
The `mode` parameter defines how the file is accessed:
*   `'r'`: **Read** (default). Fails if the file does not exist.
*   `'w'`: **Write**. Overwrites the file if it exists, or creates it if it doesn't.
*   `'a'`: **Append**. Adds content to the end of the file without deleting existing data.

### Writing to a File
```python
# 'w' mode will create or overwrite the file
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Writing another line.")
```

### Reading from a File
*   `file.read()`: Reads the entire file content as a single string.
*   `file.readlines()`: Reads the file line by line and returns a list of strings.

```python
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
```

---

## 2. JSON Serialization & Deserialization

**JSON** (JavaScript Object Notation) is a standard, text-based data format widely used for storing and exchanging data. Python provides the built-in `json` module to handle it.

*   **Serialization** (Encoding): Converting Python objects (like dicts/lists) into a JSON string.
    *   `json.dumps(obj)`: Serializes object to a JSON formatted **string**.
    *   `json.dump(obj, file_obj)`: Serializes object and writes it to a **file**.
*   **Deserialization** (Decoding): Converting JSON strings or files back into Python objects.
    *   `json.loads(json_str)`: Parses a JSON **string**.
    *   `json.load(file_obj)`: Parses a JSON **file**.

### Example: Writing JSON to a File
```python
import json

data = {
    "name": "Bob",
    "skills": ["Python", "SQL"],
    "is_active": True
}

with open("user.json", "w") as file:
    json.dump(data, file, indent=4)  # writes formatted JSON to user.json
```

### Example: Reading JSON from a File
```python
with open("user.json", "r") as file:
    user_dict = json.load(file)
    print(user_dict["skills"])  # Output: ['Python', 'SQL']
```

---

Now, proceed to the Day 8 Assignment: [day8_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week2_functions_io/day8_assignment.py).
