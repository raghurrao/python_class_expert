import os
import sys
import ast
import subprocess

TARGET_FILE = "test_day18_assignment.py"

def check_ast():
    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        return False

    with open(TARGET_FILE, "r") as f:
        tree = ast.parse(f.read())

    monkeypatch_count = 0
    setattr_count = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            args = [arg.arg for arg in node.args.args]
            if node.name in ("test_get_temperature_success", "test_get_temperature_api_failure", "test_get_temperature_malformed_response"):
                if "monkeypatch" in args:
                    monkeypatch_count += 1
        
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name) and node.func.value.id == "monkeypatch":
                if node.func.attr == "setattr":
                    setattr_count += 1

    if monkeypatch_count < 3:
        print("   [FAIL] All 3 test functions must request the 'monkeypatch' fixture.")
        return False
    if setattr_count < 3:
        print("   [FAIL] You must call monkeypatch.setattr inside all 3 test functions.")
        return False

    print("   [PASS] AST checks for Day 18 verify OK.")
    return True

def run_tests():
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 18...")
    print("====================================================")

    if not check_ast():
        sys.exit(1)

    print("\nRunning pytest on your mock HTTP client tests...")
    code, out = run_tests()
    if code != 0:
        print("[FAIL] Test suite execution failed! Output:")
        print(out)
        sys.exit(1)
        
    print("[PASS] HTTP Client mock tests executed successfully.")
    print(out)
    
    print("\n----------------------------------------------------")
    print("[SUCCESS] You have completed Day 18 Assignments successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()
