# Day 15 Assignment: Context Managers (with blocks)
# ----------------------------------------------------------------------
# Instructions: Complete the Transaction class context manager.
# Run 'python day15_test.py' to verify your solutions.

class Transaction:
    """
    Simulates a database transaction.
    Requirements:
    1. Constructor accepts a dictionary 'database' (e.g. {"Alice": 100, "Bob": 50}).
    2. Store it in 'self.database'.
    3. Implement '__enter__(self)':
       - Create a deep copy or flat copy of the database and save it in 'self.backup'
         (e.g., self.backup = self.database.copy()).
       - Return the database dictionary so the code inside the 'with' block can modify it.
    4. Implement '__exit__(self, exc_type, exc_val, exc_tb)':
       - If 'exc_type' is not None (an exception occurred inside the 'with' block):
         - Perform rollback: revert the 'database' dictionary back to 'self.backup' content.
           (Hint: use self.database.clear() then self.database.update(self.backup) so you modify
           the original dictionary in-place rather than reassigning variables).
         - Return False to allow the exception to propagate out of the context manager.
       - If no exception occurred, keep the changes (do nothing).
    """
    def __init__(self, database):
        # TODO: Initialize attributes
        pass

    def __enter__(self):
        # TODO: Backup database state and return database dictionary
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Revert database on error (exc_type is not None), return False
        pass
