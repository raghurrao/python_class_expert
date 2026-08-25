# Day 18: Weather API Client App
import requests

class APIError(Exception):
    """Custom exception raised when weather client API fails."""
    pass

class WeatherClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.weather.com/v1"

    def get_temperature(self, city):
        """Fetches the current temperature for a city. Raises APIError on failure."""
        url = f"{self.base_url}/current?city={city}&key={self.api_key}"
        try:
            response = requests.get(url)
        except Exception as e:
            raise APIError(f"Network error connecting to weather service: {e}")

        if response.status_code != 200:
            raise APIError(f"API returned error status: {response.status_code}")

        data = response.json()
        if "temp_c" not in data:
            raise APIError("Malformed API response: temp_c key missing")
            
        return data["temp_c"]
