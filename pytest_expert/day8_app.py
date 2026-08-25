# Day 8: Mock Database Connection Client

class SimpleDBClient:
    def __init__(self):
        self.connected = False
        self.data = {}

    def connect(self):
        """Simulates connecting to the database."""
        self.connected = True
        self.data = {"status": "seeded"}

    def disconnect(self):
        """Simulates disconnecting and clearing cached connection memory."""
        self.connected = False
        self.data = {}

    def insert(self, key, value):
        """Inserts a key-value pair. Raises RuntimeError if connection is closed."""
        if not self.connected:
            raise RuntimeError("Database connection is not active")
        self.data[key] = value
        return True
