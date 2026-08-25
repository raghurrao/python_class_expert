# Day 19: Database Manager App

class DatabaseManager:
    def __init__(self):
        self.users = {}  # In-memory dictionary acting as users table: {id: name}
        self.in_transaction = False
        self.transaction_backup = {}

    def begin_transaction(self):
        """Starts a transaction, backing up the current state."""
        self.in_transaction = True
        self.transaction_backup = self.users.copy()

    def commit(self):
        """Commits changes, finalizing database state."""
        self.in_transaction = False
        self.transaction_backup = {}

    def rollback(self):
        """Discards all modifications since begin_transaction() was called."""
        if not self.in_transaction:
            raise RuntimeError("No active transaction to rollback")
        self.users = self.transaction_backup.copy()
        self.in_transaction = False
        self.transaction_backup = {}

    def add_user(self, user_id, name):
        """Inserts a user record. Raises ValueError if ID already exists."""
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists")
        self.users[user_id] = name

    def get_user(self, user_id):
        """Fetches a user record by ID."""
        return self.users.get(user_id)
