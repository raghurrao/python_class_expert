# Day 16: Environment Configuration Loader App
import os

class ConfigLoader:
    def __init__(self):
        self.db_url = None
        self.api_key = None

    def load_from_env(self):
        """Loads configuration from environment variables."""
        self.db_url = os.getenv("DB_URL")
        if not self.db_url:
            raise ValueError("DB_URL environment variable is missing")
        self.api_key = os.getenv("API_KEY", "default_key")

def get_system_uptime():
    """Simulates query to OS utilities. Raises NotImplementedError in testing."""
    raise NotImplementedError("Requires Windows API access!")
