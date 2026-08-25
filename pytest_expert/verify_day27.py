import os
import sys
import ast
import subprocess
import shutil

CONFTEST_FILE = "conftest.py"
TARGET_FILE = "test_day27_assignment.py"
APP_FILE = "day27_app.py"
APP_BACKUP = "day27_app.py.backup"

CLEAN_CODE = """# Day 27: SecureDataManager Capstone App
import os
import logging
import asyncio

logger = logging.getLogger("SecureData")

def os_encrypt(raw_data, key):
    raise NotImplementedError("Encryption hardware API is offline in this environment!")

class SecureDataManager:
    def __init__(self, db_client, backup_dir):
        self.db_client = db_client
        self.backup_dir = backup_dir
        self.connected = False

    async def connect(self):
        await asyncio.sleep(0.01)
        self.connected = True

    async def disconnect(self):
        await asyncio.sleep(0.01)
        self.connected = False

    async def encrypt_and_save(self, user_id, raw_data, key, skip_encryption=False):
        if not self.connected:
            raise RuntimeError("Database connection is not active")
        
        if not isinstance(raw_data, str) or len(raw_data) < 5:
            logger.warning(f"Short payload rejected for user {user_id}")
            raise ValueError("Payload must be at least 5 characters")

        if skip_encryption:
            encrypted_data = raw_data
        else:
            encrypted_data = os_encrypt(raw_data, key)

        await self.db_client.save_record(user_id, encrypted_data)

        meta_file = os.path.join(self.backup_dir, f"meta_{user_id}.json")
        with open(meta_file, "w") as f:
            f.write(f'{{"size": {len(raw_data)}}}')

        logger.info(f"Successfully saved encrypted record for user {user_id}")
        return True
"""

MUTANTS = {
    "mutant_no_meta": {
        "desc": "SecureDataManager skips writing local metadata backup JSON",
        "code": CLEAN_CODE.replace("with open(meta_file, \"w\") as f:\n            f.write(f'{{\"size\": {len(raw_data)}}}')", "pass")
    },
    "mutant_short_payload": {
        "desc": "SecureDataManager allows short payloads (< 5 chars) without ValueError",
        "code": CLEAN_CODE.replace("raise ValueError(\"Payload must be at least 5 characters\")", "pass")
    },
    "mutant_ignore_skip_flag": {
        "desc": "SecureDataManager ignores the skip_encryption flag (always encrypts)",
        "code": CLEAN_CODE.replace("if skip_encryption:\n            encrypted_data = raw_data\n        else:", "if False:\n            pass\n        else:")
    }
}

REQUIRED_TESTS = {
    "test_encrypt_and_save_success",
    "test_payload_too_short",
    "test_skip_encryption_flag"
}

def check_ast():
    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        return False

    with open(TARGET_FILE, "r") as f:
        tree = ast.parse(f.read())

    async_fixture = False
    async_tests_count = 0
    async_mock_used = False

    for node in ast.walk(tree):
        if isinstance(node, ast.AsyncFunctionDef):
            if node.name == "manager":
                async_fixture = True
            elif node.name in REQUIRED_TESTS:
                async_tests_count += 1
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "AsyncMock":
                async_mock_used = True

    if not async_fixture:
        print("   [FAIL] 'manager' fixture must be declared as 'async def manager()'.")
        return False
    if async_tests_count < len(REQUIRED_TESTS):
        print(f"   [FAIL] All capstone tests inside TestSecureDataManager must be asynchronous 'async def' test functions.")
        return False
    if not async_mock_used:
        print("   [FAIL] You must use 'AsyncMock' to mock the async database client save_record method.")
        return False

    # Check conftest.py
    if not os.path.exists(CONFTEST_FILE):
        print(f"[ERROR] {CONFTEST_FILE} not found.")
        return False
    with open(CONFTEST_FILE, "r") as f:
        conftest_tree = ast.parse(f.read())

    flag_registered = False
    for node in ast.walk(conftest_tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "addoption":
            for arg in node.args:
                if isinstance(arg, ast.Constant) and arg.value == "--skip-encryption":
                    flag_registered = True

    if not flag_registered:
        print("   [FAIL] --skip-encryption flag must be registered in conftest.py")
        return False

    print("   [PASS] AST async setups and conftest flag registration verify OK.")
    return True

def run_test_cmd(args):
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def write_app_file(content):
    with open(APP_FILE, "w") as f:
        f.write(content)

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 27...")
    print("====================================================")

    if not check_ast():
        sys.exit(1)

    if os.path.exists(APP_FILE):
        shutil.copyfile(APP_FILE, APP_BACKUP)

    try:
        # 1. Verify success path on clean code (WITHOUT flag)
        print("\nTesting against correct code (without --skip-encryption)...")
        write_app_file(CLEAN_CODE)
        code, out = run_test_cmd([])
        if code != 0 or "3 passed" not in out:
            print("[FAIL] Test run failed on correct code without flag. Output:")
            print(out)
            sys.exit(1)
        print("   [PASS] Clean code execution passes.")

        # 2. Verify success path on clean code (WITH flag)
        print("\nTesting against correct code (with --skip-encryption)...")
        code, out = run_test_cmd(["--skip-encryption"])
        if code != 0 or "3 passed" not in out:
            print("[FAIL] Test run failed on correct code with flag. Output:")
            print(out)
            sys.exit(1)
        print("   [PASS] Clean code execution passes with skip flag enabled.")

        # 3. Mutation testing
        print("\nTesting against broken code (Mutation Testing)...")
        failed_mutants = []
        for name, mutant in MUTANTS.items():
            print(f"Applying mutant: {mutant['desc']}...")
            write_app_file(mutant["code"])
            # Run without flag (and also with flag for ignore_skip)
            code, out = run_test_cmd([])
            code_flag, out_flag = run_test_cmd(["--skip-encryption"])

            # If both pass, the test suite is blind to this mutant
            if code == 0 and code_flag == 0:
                print(f"   [FAIL] Your tests did NOT catch this bug! They passed when they should have failed.")
                failed_mutants.append(name)
            else:
                print(f"   [PASS] Your tests successfully caught this bug (tests failed as expected).")

        print("\n----------------------------------------------------")
        if failed_mutants:
            print("[ERROR] Verification Failed!")
            print("Your capstone test suite is missing assertions or validation checks.")
            print("Ensure you verify database async calls, file backups, exception boundaries, and skip configurations.")
            sys.exit(1)
        else:
            print("[SUCCESS] You have successfully passed the Professional Capstone Project!")
            sys.exit(0)

    finally:
        if os.path.exists(APP_BACKUP):
            shutil.copyfile(APP_BACKUP, APP_FILE)
            os.remove(APP_BACKUP)
        else:
            write_app_file(CLEAN_CODE)

if __name__ == "__main__":
    main()
