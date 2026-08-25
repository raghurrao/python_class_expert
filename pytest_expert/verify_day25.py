import os
import sys
import ast
import subprocess

CONFTEST_FILE = "conftest.py"
TARGET_FILE = "test_day25_assignment.py"

def check_ast():
    if not os.path.exists(CONFTEST_FILE):
        print(f"[ERROR] {CONFTEST_FILE} not found.")
        return False
        
    with open(CONFTEST_FILE, "r") as f:
        conftest_tree = ast.parse(f.read())

    hook_found = False
    for node in ast.walk(conftest_tree):
        if isinstance(node, ast.FunctionDef) and node.name == "pytest_runtest_setup":
            hook_found = True
            
    if not hook_found:
        print("   [FAIL] pytest_runtest_setup hook was not implemented in conftest.py")
        return False

    with open(TARGET_FILE, "r") as f:
        test_tree = ast.parse(f.read())

    doc_ok = False
    undoc_ok = False

    for node in ast.walk(test_tree):
        if isinstance(node, ast.FunctionDef):
            if node.name == "test_documented":
                # Check for docstring
                docstring = ast.get_docstring(node)
                if docstring:
                    doc_ok = True
            elif node.name == "test_undocumented":
                docstring = ast.get_docstring(node)
                if not docstring:
                    undoc_ok = True

    if not doc_ok:
        print("   [FAIL] test_documented is missing a docstring.")
        return False
    if not undoc_ok:
        print("   [FAIL] test_undocumented should NOT have a docstring.")
        return False

    print("   [PASS] AST checks for Day 25 verify OK.")
    return True

def run_tests():
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 25...")
    print("====================================================")

    if not check_ast():
        sys.exit(1)

    print("\nRunning pytest on your hooked test suite...")
    code, out = run_tests()
    
    # In pytest, if tests pass or skip, returncode is 0. If it fails, it's 1.
    if code != 0:
        print("[FAIL] Test run failed! Output:")
        print(out)
        sys.exit(1)

    if "1 passed, 1 skipped" not in out:
        print("[FAIL] Expected exactly 1 passed test and 1 skipped test (undocumented one). Output:")
        print(out)
        sys.exit(1)

    print("   [PASS] Documented test passed, undocumented test was successfully skipped.")
    print(out)
    
    print("\n----------------------------------------------------")
    print("[SUCCESS] You have completed Day 25 Assignments successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()
