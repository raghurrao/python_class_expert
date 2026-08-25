import os
import sys
import ast
import subprocess
import shutil

TARGET_FILE = "test_day20_assignment.py"
APP_FILE = "day20_app.py"
APP_BACKUP = "day20_app.py.backup"

CLEAN_CODE = """# Day 20: Weather Sync Engine Library
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
"""

MUTANTS = {
    "mutant_no_backup": {
        "desc": "WeatherSyncEngine.sync_weather() skips writing the backup file",
        "code": CLEAN_CODE.replace("with open(backup_file, \"w\") as f:\n            f.write(f\"City: {city}, Temp: {temp}C\")", "pass")
    },
    "mutant_bad_backup_content": {
        "desc": "WeatherSyncEngine.sync_weather() writes wrong text inside the backup file",
        "code": CLEAN_CODE.replace("f.write(f\"City: {city}, Temp: {temp}C\")", "f.write(\"Wrong Format\")")
    },
    "mutant_no_db_record": {
        "desc": "WeatherSyncEngine.sync_weather() does not call db_manager.add_record()",
        "code": CLEAN_CODE.replace("self.db_manager.add_record(city, temp)", "pass")
    },
    "mutant_no_warning_log": {
        "desc": "WeatherSyncEngine.sync_weather() does not log warning on API failure",
        "code": CLEAN_CODE.replace("logger.warning(f\"Failed to sync city {city}\")", "pass")
    },
    "mutant_no_runtime_err": {
        "desc": "WeatherSyncEngine.sync_weather() does not raise RuntimeError on API failure",
        "code": CLEAN_CODE.replace("raise RuntimeError(f\"Sync failed due to API error: {e}\")", "return False")
    }
}

REQUIRED_TESTS = {
    "test_sync_success",
    "test_sync_api_failure"
}

def check_ast():
    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        return False

    with open(TARGET_FILE, "r") as f:
        tree = ast.parse(f.read())

    mock_imported = False
    mock_instantiated = False
    tmp_path_requested = False
    caplog_requested = False
    found_methods = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if "mock" in node.module or "unittest.mock" in node.module:
                mock_imported = True
        elif isinstance(node, ast.FunctionDef):
            if node.name in REQUIRED_TESTS:
                found_methods.add(node.name)
                args = [arg.arg for arg in node.args.args]
                if "tmp_path" in args:
                    tmp_path_requested = True
                if "caplog" in args:
                    caplog_requested = True
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in ("Mock", "MagicMock"):
                mock_instantiated = True

    if not mock_imported:
        print("   [FAIL] unittest.mock.Mock was not imported.")
        return False
    if not mock_instantiated:
        print("   [FAIL] You must instantiate Mock objects for WeatherClient and DatabaseManager.")
        return False
    if not tmp_path_requested:
        print("   [FAIL] Test functions must request the 'tmp_path' fixture to map directories.")
        return False
    if not caplog_requested:
        print("   [FAIL] Test functions must request the 'caplog' fixture to check logger events.")
        return False

    missing = REQUIRED_TESTS - found_methods
    if missing:
        print(f"   [FAIL] Missing required test functions: {missing}")
        return False

    print("   [PASS] AST checks for Day 20 verify OK.")
    return True

def run_tests():
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def write_app_file(content):
    with open(APP_FILE, "w") as f:
        f.write(content)

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 20...")
    print("====================================================")

    if not check_ast():
        sys.exit(1)

    if os.path.exists(APP_FILE):
        shutil.copyfile(APP_FILE, APP_BACKUP)

    try:
        print("\nTesting against correct code...")
        write_app_file(CLEAN_CODE)
        code, out = run_tests()
        if code != 0:
            print("[FAIL] Tests failed on correct code! Output:")
            print(out)
            sys.exit(1)
        print("[PASS] All tests passed successfully on correct code.")

        print("\nTesting against broken code (Mutation Testing)...")
        failed_mutants = []
        for name, mutant in MUTANTS.items():
            print(f"Applying mutant: {mutant['desc']}...")
            write_app_file(mutant["code"])
            code, out = run_tests()

            if code == 0:
                print(f"   [FAIL] Your tests did NOT catch this bug! They passed when they should have failed.")
                failed_mutants.append(name)
            else:
                print(f"   [PASS] Your tests successfully caught this bug (tests failed as expected).")

        print("\n----------------------------------------------------")
        if failed_mutants:
            print("[ERROR] Verification Failed!")
            print("Your test suite is missing assertions for some sync operations.")
            print("Ensure you verify database writes, log content, exception scopes, and file cache templates.")
            sys.exit(1)
        else:
            print("[SUCCESS] You have completed the Week 3 Integration Milestone!")
            sys.exit(0)

    finally:
        if os.path.exists(APP_BACKUP):
            shutil.copyfile(APP_BACKUP, APP_FILE)
            os.remove(APP_BACKUP)
        else:
            write_app_file(CLEAN_CODE)

if __name__ == "__main__":
    main()
