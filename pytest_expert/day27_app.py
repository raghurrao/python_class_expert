# Day 27: SecureDataManager Capstone App
import os
import logging
import asyncio

logger = logging.getLogger("SecureData")

def os_encrypt(raw_data, key):
    """Simulates system level hardware encryption. Raises NotImplementedError in tests."""
    raise NotImplementedError("Encryption hardware API is offline in this environment!")

class SecureDataManager:
    def __init__(self, db_client, backup_dir):
        self.db_client = db_client
        self.backup_dir = backup_dir
        self.connected = False

    async def connect(self):
        """Simulates establishing async database connection."""
        await asyncio.sleep(0.01)
        self.connected = True

    async def disconnect(self):
        """Simulates closing async database connection."""
        await asyncio.sleep(0.01)
        self.connected = False

    async def encrypt_and_save(self, user_id, raw_data, key, skip_encryption=False):
        """Processes, encrypts (optional), and saves data records."""
        if not self.connected:
            raise RuntimeError("Database connection is not active")
        
        if not isinstance(raw_data, str) or len(raw_data) < 5:
            logger.warning(f"Short payload rejected for user {user_id}")
            raise ValueError("Payload must be at least 5 characters")

        if skip_encryption:
            encrypted_data = raw_data
        else:
            encrypted_data = os_encrypt(raw_data, key)

        # Save to database (async call)
        await self.db_client.save_record(user_id, encrypted_data)

        # Write local metadata file
        meta_file = os.path.join(self.backup_dir, f"meta_{user_id}.json")
        with open(meta_file, "w") as f:
            f.write(f'{{"size": {len(raw_data)}}}')

        logger.info(f"Successfully saved encrypted record for user {user_id}")
        return True
