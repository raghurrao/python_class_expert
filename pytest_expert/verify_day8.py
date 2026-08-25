import os
import sys
import ast
import subprocess

TARGET_FILE = "test_day8_assignment.py"

def check_ast():
    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        return False

    with open(TARGET_FILE, "r") as f:
        tree = ast.parse(f.read())

    fixture_found = False
    yield_found = False
    disconnect_found = False

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "db_client":
            # Check decorator
            for dec in node.decorator_list:
                if isinstance(dec, ast.Attribute) and dec.attr == "fixture":
                    fixture_found = True
                elif isinstance(dec, ast.Call) and isinstance(dec.func, ast.Attribute) and dec.func.attr == "fixture":
                    fixture_found = True

            # Check inside function body
            for child in ast.walk(node):
                if isinstance(child, ast.Yield):
                    yield_found = True
                elif isinstance(child, ast.Call):
                    if isinstance(child.func, ast.Attribute) and child.func.attr == "disconnect":
                        disconnect_found = True

    if not fixture_found:
        print("   [FAIL] db_client is not decorated with @pytest.fixture")
        return False
    if not yield_found:
        print("   [FAIL] db_client fixture must use the 'yield' keyword to return its client resource.")
        return False
    if not disconnect_found:
        print("   [FAIL] db_client fixture is missing the cleanup step calling client.disconnect() after yield.")
        return False

    # Check that tests accept the fixture as parameter
    required_tests = ["test_db_connection_status", "test_db_insert"]
    found_tests = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in required_tests:
            found_tests[node.name] = [arg.arg for arg in node.args.args]

    for name in required_tests:
        if name not in found_tests:
            print(f"   [FAIL] Missing required test function: {name}")
            return False
        if "db_client" not in found_tests[name]:
            print(f"   [FAIL] Test function {name} must request the 'db_client' fixture as an argument.")
            return False

    print("   [PASS] AST checks for Day 8 verify OK.")
    return True

def run_tests():
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 8...")
    print("====================================================")

    if not check_ast():
        sys.exit(1)

    print("\nRunning pytest on your fixture tests...")
    code, out = run_tests()
    if code != 0:
        print("[FAIL] Test suite failed on your fixture tests! Output:")
        print(out)
        sys.exit(1)
    
    print("[PASS] Fixtures ran and all tests passed successfully.")
    print(out)
    
    print("\n----------------------------------------------------")
    print("[SUCCESS] You have completed Day 8 Assignments successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()
