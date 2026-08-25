# Day 20: Weather Sync Engine Library
import os
import logging

logger = logging.getLogger("SyncEngine")

class APIError(Exception):
    pass

class WeatherSyncEngine:
    def __init__(self, weather_client, db_manager, backup_dir):
        self.weather_client = weather_client
        self.db_manager = db_manager
        self.backup_dir = backup_dir

    def sync_weather(self, city):
        """
        Synchronizes temperature data for a city.
        Gets temp, saves to database, writes a backup file, and logs events.
        Raises RuntimeError on API failures.
        """
        try:
            temp = self.weather_client.get_temperature(city)
        except Exception as e:
            logger.warning(f"Failed to sync city {city}")
            raise RuntimeError(f"Sync failed due to API error: {e}")

        # Save to database
        self.db_manager.add_record(city, temp)

        # Write local backup cache
        filename = f"{city.lower()}_weather.txt"
        backup_file = os.path.join(self.backup_dir, filename)
        with open(backup_file, "w") as f:
            f.write(f"City: {city}, Temp: {temp}C")

        # Log completion
        logger.info(f"Synced city {city} temperature {temp}C")
        return True
