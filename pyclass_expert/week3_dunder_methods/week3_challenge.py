# Week 3 Challenge: Custom Queryable Dataset Class
# ----------------------------------------------------------------------
# Instructions: Integrate magic methods and protocols to build a custom
# queryable data structure ('Dataset') containing records (dictionaries).
# Run 'python week3_challenge_test.py' to verify your solutions.

class Dataset:
    """
    Represents a list of dictionary records.
    Example:
        records = [
            {"id": 1, "name": "Alice", "role": "admin"},
            {"id": 2, "name": "Bob", "role": "user"}
        ]
        data = Dataset(records)

    Requirements:
    1. Constructor accepts a list of dictionaries 'records' and stores in 'self._records'.
    2. Implement '__len__(self)' returning the count of records.
    3. Implement '__getitem__(self, index)' to support record index retrieval (e.g. data[0])
       and slicing (e.g. data[0:2], which should return a NEW Dataset object).
    4. Implement '__contains__(self, item)':
       - Return True if any record has a value matching 'item' (in any field).
       - Return False otherwise.
    5. Implement '__iter__(self)' returning an iterator over self._records.
    6. Implement '__str__(self)' returning: "Dataset with <num> records"
    7. Implement '__repr__(self)' returning: "Dataset(<self._records>)"
    8. Implement '__add__(self, other)':
       - If 'other' is not an instance of Dataset, raise TypeError.
       - Return a NEW Dataset containing records from both self and other combined.
    9. Implement '__eq__(self, other)':
       - If 'other' is not an instance of Dataset, return False.
       - Return True if self._records is equal to other._records.
    10. Implement '__call__(self, **kwargs)':
        - Filter records where keys and values match the kwargs arguments.
        - Return a NEW Dataset containing the matched records.
        - Example: data(role="admin") returns a new Dataset with Alice's record.
    11. Implement Context Manager Protocol (__enter__ and __exit__):
        - Entering: Backup self._records. Return the list self._records so it can be edited.
        - Exiting: If an exception occurs, revert self._records back to the backup.
          Return False so the exception propagates.
    """
    def __init__(self, records):
        self._records = list(records)

    # TODO: Implement the magic methods listed above
