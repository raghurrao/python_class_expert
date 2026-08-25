# Day 2: Target Functions for Exceptions & Dictionary Assertions

def validate_age(age):
    """
    Validates age parameter.
    Raises ValueError if age is not an integer or is outside [0, 120].
    """
    if not isinstance(age, int) or isinstance(age, bool):  # Note: bool is a subclass of int in Python
        raise TypeError("Age must be an integer")
    if age < 0 or age > 120:
        raise ValueError(f"Age {age} is invalid. Must be between 0 and 120.")
    return True

def parse_user_data(user_dict):
    """
    Parses a user dictionary.
    Requires 'username' and 'email' keys.
    Returns a formatted string 'Username: <username>, Email: <email>'.
    Raises KeyError if any required key is missing.
    """
    if "username" not in user_dict:
        raise KeyError("username")
    if "email" not in user_dict:
        raise KeyError("email")
    return f"Username: {user_dict['username']}, Email: {user_dict['email']}"

def merge_configs(dict1, dict2):
    """
    Merges dict2 into dict1.
    If a key exists in both and both values are dictionaries, it merges them recursively.
    Raises TypeError if either input is not a dictionary.
    """
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise TypeError("Both inputs must be dictionaries")
    
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_configs(result[key], value)
        else:
            result[key] = value
    return result
