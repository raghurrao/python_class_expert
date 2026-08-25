import os
import sys
import ast
import subprocess
import configparser

TARGET_FILE = "test_day22_assignment.py"
INI_FILE = "pytest.ini"

def check_ast():
    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        return False

    with open(TARGET_FILE, "r") as f:
        tree = ast.parse(f.read())

    repo_async = False
    fetch_async = False
    save_async = False

    for node in ast.walk(tree):
        if isinstance(node, ast.AsyncFunctionDef):
            if node.name == "repo":
                repo_async = True
            elif node.name == "test_fetch_user":
                fetch_async = True
            elif node.name == "test_save_user":
                save_async = True

    if not repo_async:
        print("   [FAIL] repo fixture must be defined as an asynchronous function ('async def repo()').")
        return False
    if not fetch_async:
        print("   [FAIL] test_fetch_user must be defined as 'async def test_fetch_user()'.")
        return False
    if not save_async:
        print("   [FAIL] test_save_user must be defined as 'async def test_save_user()'.")
        return False

    print("   [PASS] AST async declarations verify OK.")
    return True

def check_ini():
    if not os.path.exists(INI_FILE):
        print(f"   [FAIL] pytest.ini not found in the pytest_expert directory.")
        return False

    config = configparser.ConfigParser()
    try:
        config.read(INI_FILE)
    except Exception as e:
        print(f"   [FAIL] Failed to parse pytest.ini: {e}")
        return False

    if "pytest" not in config.sections() or "asyncio_mode" not in config["pytest"]:
        print("   [FAIL] pytest.ini is missing the 'asyncio_mode' setting in the [pytest] section.")
        return False

    mode = config["pytest"]["asyncio_mode"].lower()
    if mode != "auto":
        print(f"   [FAIL] 'asyncio_mode' must be set to 'auto'. Got: '{mode}'")
        return False

    print("   [PASS] pytest.ini asyncio_mode config verify OK.")
    return True

def run_tests():
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 22...")
    print("====================================================")

    if not check_ast():
        sys.exit(1)

    if not check_ini():
        sys.exit(1)

    print("\nRunning pytest on your async tests...")
    code, out = run_tests()
    if code != 0:
        print("[FAIL] Test suite execution failed! Output:")
        print(out)
        sys.exit(1)
        
    print("[PASS] Async tests and async fixtures executed successfully.")
    print(out)
    
    print("\n----------------------------------------------------")
    print("[SUCCESS] You have completed Day 22 Assignments successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()
