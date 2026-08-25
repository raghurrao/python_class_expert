import os
import sys
import ast
import subprocess

CONFTEST_FILE = "conftest.py"
TARGET_FILE = "test_day24_assignment.py"

def check_ast():
    if not os.path.exists(CONFTEST_FILE):
        print(f"[ERROR] {CONFTEST_FILE} not found.")
        return False
        
    with open(CONFTEST_FILE, "r") as f:
        conftest_tree = ast.parse(f.read())

    hook_found = False
    addoption_called = False

    for node in ast.walk(conftest_tree):
        if isinstance(node, ast.FunctionDef) and node.name == "pytest_addoption":
            hook_found = True
            for child in ast.walk(node):
                if isinstance(child, ast.Call) and isinstance(child.func, ast.Attribute):
                    if child.func.attr == "addoption":
                        for arg in child.args:
                            if isinstance(arg, ast.Constant) and arg.value == "--run-slow":
                                addoption_called = True
                            elif isinstance(arg, ast.Name) and arg.id == "--run-slow":
                                addoption_called = True
                        for kw in child.keywords:
                            if kw.arg == "action" and isinstance(kw.value, ast.Constant) and kw.value.value == "store_true":
                                pass # option verified

    if not hook_found:
        print("   [FAIL] pytest_addoption hook was not implemented in conftest.py")
        return False
    if not addoption_called:
        print("   [FAIL] parser.addoption('--run-slow') was not called inside pytest_addoption.")
        return False

    with open(TARGET_FILE, "r") as f:
        test_tree = ast.parse(f.read())

    skip_called = False
    getoption_called = False

    for node in ast.walk(test_tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "skip":
                skip_called = True
            elif node.func.attr == "getoption":
                getoption_called = True

    if not getoption_called:
        print("   [FAIL] test_slow_task does not fetch flag using request.config.getoption('--run-slow')")
        return False
    if not skip_called:
        print("   [FAIL] test_slow_task does not call pytest.skip(...) when flag is False")
        return False

    print("   [PASS] AST checks for Day 24 verify OK.")
    return True

def run_test_cmd(args):
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 24...")
    print("====================================================")

    if not check_ast():
        sys.exit(1)

    # 1. Run without flag (Should show SKIPPED)
    print("\nRunning test suite WITHOUT --run-slow flag...")
    code, out = run_test_cmd([])
    if code != 0 or "1 skipped" not in out:
        print("[FAIL] Expected 1 skipped test when running without the flag. Output:")
        print(out)
        sys.exit(1)
    print("   [PASS] Test skipped successfully as expected.")

    # 2. Run with flag (Should show PASSED)
    print("\nRunning test suite WITH --run-slow flag...")
    code, out = run_test_cmd(["--run-slow"])
    if code != 0 or "1 passed" not in out or "skipped" in out:
        print("[FAIL] Expected 1 passed (and 0 skipped) test when running with --run-slow. Output:")
        print(out)
        sys.exit(1)
    print("   [PASS] Test ran and passed successfully.")

    print("\n----------------------------------------------------")
    print("[SUCCESS] You have completed Day 24 Assignments successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()
