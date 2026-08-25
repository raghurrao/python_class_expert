import os
import sys
import ast
import subprocess

CONFTEST_FILE = os.path.join("day10_tests", "conftest.py")
AUTH_FILE = os.path.join("day10_tests", "test_auth.py")
PAYMENT_FILE = os.path.join("day10_tests", "test_payment.py")

def check_ast():
    # 1. Check conftest.py
    if not os.path.exists(CONFTEST_FILE):
        print(f"[ERROR] {CONFTEST_FILE} not found.")
        return False
        
    with open(CONFTEST_FILE, "r") as f:
        conftest_tree = ast.parse(f.read())

    app_version_found = False
    scope_session = False
    for node in ast.walk(conftest_tree):
        if isinstance(node, ast.FunctionDef) and node.name == "app_version":
            app_version_found = True
            for dec in node.decorator_list:
                if isinstance(dec, ast.Call) and isinstance(dec.func, ast.Attribute) and dec.func.attr == "fixture":
                    for kw in dec.keywords:
                        if kw.arg == "scope" and isinstance(kw.value, ast.Constant) and kw.value.value == "session":
                            scope_session = True
                        elif kw.arg == "scope" and isinstance(kw.value, ast.Name) and kw.value.id == "session":
                            scope_session = True

    if not app_version_found:
        print("   [FAIL] app_version fixture was not found in day10_tests/conftest.py")
        return False
    if not scope_session:
        print("   [FAIL] app_version fixture in conftest.py is missing scope='session'")
        return False

    # 2. Check test files for imports and params
    for path, test_name in [(AUTH_FILE, "test_auth_version_check"), (PAYMENT_FILE, "test_payment_version_check")]:
        if not os.path.exists(path):
            print(f"[ERROR] {path} not found.")
            return False

        with open(path, "r") as f:
            code_text = f.read()
            tree = ast.parse(code_text)

        # Check that there are no imports of conftest or app_version
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for name in node.names:
                    if "conftest" in name.name or "app_version" in name.name:
                        print(f"   [FAIL] {path} contains explicit imports of conftest/app_version. Do not import them!")
                        return False
            elif isinstance(node, ast.ImportFrom):
                if node.module and ("conftest" in node.module or "app_version" in node.module):
                    print(f"   [FAIL] {path} contains explicit imports of conftest/app_version. Do not import them!")
                    return False
                for name in node.names:
                    if "app_version" in name.name:
                        print(f"   [FAIL] {path} contains explicit imports of app_version. Do not import them!")
                        return False

        # Check parameter
        param_ok = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == test_name:
                args = [arg.arg for arg in node.args.args]
                if "app_version" in args:
                    param_ok = True

        if not param_ok:
            print(f"   [FAIL] {test_name} in {path} must request the 'app_version' fixture as an argument.")
            return False

    print("   [PASS] conftest.py structural and import checks verify OK.")
    return True

def run_tests():
    cmd = [sys.executable, "-m", "pytest", "day10_tests", "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 10...")
    print("====================================================")

    if not check_ast():
        sys.exit(1)

    print("\nRunning pytest on your day10_tests directory...")
    code, out = run_tests()
    if code != 0:
        print("[FAIL] Test suite execution failed! Output:")
        print(out)
        sys.exit(1)
    
    print("[PASS] Multi-file shared fixture tests ran and passed successfully.")
    print(out)
    
    print("\n----------------------------------------------------")
    print("[SUCCESS] You have completed Day 10 Assignments successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()
