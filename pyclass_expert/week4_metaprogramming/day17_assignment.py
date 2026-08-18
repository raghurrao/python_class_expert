# Day 17 Assignment: The Descriptor Protocol
# ----------------------------------------------------------------------
# Instructions: Complete the NonEmptyString descriptor and User class.
# Run 'python day17_test.py' to verify your solutions.

class NonEmptyString:
    """
    A validation descriptor that forces string types of non-zero length.
    Requirements:
    1. Implement '__set_name__(self, owner, name)':
       - Save the private variable name as self.private_name = "_" + name.
    2. Implement '__get__(self, instance, owner)':
       - If 'instance' is None, return 'self'.
       - Otherwise, return the value from 'instance.__dict__' using 'self.private_name'.
    3. Implement '__set__(self, instance, value)':
       - If 'value' is not a string (isinstance(value, str)), raise TypeError("Value must be a string").
       - If 'value' is empty or only whitespace (len(value.strip()) == 0), raise ValueError("String cannot be empty").
       - Otherwise, store 'value.strip()' in 'instance.__dict__' under 'self.private_name'.
    """
    # TODO: Implement NonEmptyString descriptor


class User:
    """
    Requirements:
    1. Define class attributes 'username' and 'email' as instances of NonEmptyString.
    2. Constructor should accept 'username' (str) and 'email' (str) and assign them.
    """
    # TODO: Implement User class using NonEmptyString descriptors
    pass
