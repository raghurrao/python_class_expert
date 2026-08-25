# Day 20: Week 3 Integration Assignment

Today is your third weekly milestone! We will consolidate everything you have learned this week (mocking external gateways, monkeypatching modules and env vars, writing to tmp files, capturing outputs, and database state rollbacks) to test a complete data synchronization engine called `WeatherSyncEngine`.

---

## The Challenge: Testing `WeatherSyncEngine`
You are provided with a package containing `day20_app.py`. It contains:
1. **`WeatherSyncEngine`**: A class initialized with a `weather_client`, a `db_manager`, and a `backup_dir` path.
2. **`sync_weather(city)`**:
   * Fetches the temperature for a city using `weather_client.get_temperature(city)`.
   * Adds the city and temperature as a record inside the database `db_manager.add_record(city, temp)`.
   * Writes a backup text file named `<city>_weather.txt` inside `backup_dir` containing `"City: <city>, Temp: <temp>C"`.
   * Logs an info event: `"Synced city <city> temperature <temp>C"`.

Your job is to write a complete test suite inside `test_day20_assignment.py` following these specifications:

### 1. Test Architecture
* Inject pytest system fixtures `tmp_path` and `caplog` into your tests.
* Create a Mock object for the `weather_client` dependency, stubbing `get_temperature` to return `25.5` on the first test, and to raise `APIError` on another.
* Create a Mock object or real transactional setup for `db_manager` (stubbing `add_record` or using our transactional DB client).

### 2. Assertions to Implement
* **Success Path**:
  * Assert `sync_weather` returns `True`.
  * Assert the mock database `add_record` was called with correct city and temperature.
  * Assert that a backup file was written in `tmp_path` and contains the exact string `"City: Paris, Temp: 25.5C"`.
  * Assert that an INFO log was generated containing `"Synced city Paris temperature 25.5C"`.
* **API Failure Path**:
  * If the weather client raises `APIError`, assert that the sync engine catches it, logs a warning `"Failed to sync city London"`, and raises a `RuntimeError`.

---

## Verification Commands
Verify your test coverage using:
```powershell
.venv\Scripts\python pytest_expert/verify_day20.py
```
This runs mutation testing to check that your tests can detect logic bugs, file path errors, missing databases, and missing logs.
