# Day 9 Assignment: Abstract Base Classes (ABCs)
# ----------------------------------------------------------------------
# Instructions: Define the ABC and its implementations.
# Run 'python day9_test.py' to verify your solutions.

from abc import ABC, abstractmethod

# ======================================================================
# Exercise 1: StorageSource Abstract Base Class
# ======================================================================
class StorageSource(ABC):
    """
    Requirements:
    1. Must inherit from abc.ABC.
    2. Define abstract method 'read(self, path)' (no implementation).
    3. Define abstract method 'write(self, path, data)' (no implementation).
    """
    # TODO: Implement abstract methods


# ======================================================================
# Exercise 2: LocalStorage implementation
# ======================================================================
class LocalStorage(StorageSource):
    """
    Requirements:
    1. Inherit from StorageSource.
    2. Constructor should initialize an instance attribute 'files' to an empty dictionary.
    3. Implement 'read(self, path)':
       - Return the data corresponding to 'path' in 'self.files'.
       - If 'path' is not in 'self.files', raise a FileNotFoundError.
    4. Implement 'write(self, path, data)':
       - Store 'data' in 'self.files' under the key 'path'.
    """
    # TODO: Implement LocalStorage


# ======================================================================
# Exercise 3: CloudStorage implementation
# ======================================================================
class CloudStorage(StorageSource):
    """
    Requirements:
    1. Inherit from StorageSource.
    2. Constructor should initialize an instance attribute 'bucket' to an empty dictionary.
    3. Implement 'read(self, path)':
       - Return the data corresponding to 'path' in 'self.bucket'.
       - If 'path' is not in 'self.bucket', raise a FileNotFoundError.
    4. Implement 'write(self, path, data)':
       - Store 'data' in 'self.bucket' under the key 'path'.
    """
    # TODO: Implement CloudStorage
