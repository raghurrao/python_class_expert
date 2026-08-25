import os
import sys
import ast
import subprocess

TARGET_FILE = "test_day15_assignment.py"

def check_ast():
    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        return False

    with open(TARGET_FILE, "r") as f:
        tree = ast.parse(f.read())

    mock_imported = False
    mock_used = False
    assert_called_used = False

    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if "mock" in node.module or "unittest.mock" in node.module:
                mock_imported = True
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in ("Mock", "MagicMock"):
                mock_used = True
            elif isinstance(node.func, ast.Attribute) and "assert_called" in node.func.attr:
                assert_called_used = True

    if not mock_imported:
        print("   [FAIL] unittest.mock.Mock was not imported.")
        return False
    if not mock_used:
        print("   [FAIL] No Mock object was instantiated in your test file.")
        return False
    if not assert_called_used:
        print("   [FAIL] You must verify that your mock was called using mock_gateway.charge.assert_called_once_with(...) or similar.")
        return False

    print("   [PASS] AST checks for Day 15 verify OK.")
    return True

def run_tests():
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 15...")
    print("====================================================")

    if not check_ast():
        sys.exit(1)

    print("\nRunning pytest on your mock tests...")
    code, out = run_tests()
    if code != 0:
        print("[FAIL] Test suite execution failed! Output:")
        print(out)
        sys.exit(1)
        
    print("[PASS] Mock tests executed successfully.")
    print(out)
    
    print("\n----------------------------------------------------")
    print("[SUCCESS] You have completed Day 15 Assignments successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()
