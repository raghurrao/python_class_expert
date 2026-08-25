# Day 22: Asynchronous User Repository App
import asyncio

class AsyncUserRepository:
    def __init__(self):
        self.connected = False
        self.users = {}

    async def connect(self):
        """Simulates establishing async database connection."""
        await asyncio.sleep(0.01)
        self.connected = True
        self.users = {1: "Alice", 2: "Bob"}

    async def disconnect(self):
        """Simulates closing async database connection."""
        await asyncio.sleep(0.01)
        self.connected = False
        self.users = {}

    async def fetch_user_name(self, user_id):
        """Fetches username asynchronously. Raises RuntimeError if disconnected."""
        if not self.connected:
            raise RuntimeError("Repository connection is offline")
        await asyncio.sleep(0.01)
        return self.users.get(user_id)

    async def save_user_name(self, user_id, name):
        """Saves username asynchronously. Raises RuntimeError if disconnected."""
        if not self.connected:
            raise RuntimeError("Repository connection is offline")
        await asyncio.sleep(0.01)
        self.users[user_id] = name
        return True
