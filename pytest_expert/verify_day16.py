import os
import sys
import ast
import subprocess

TARGET_FILE = "test_day16_assignment.py"

def check_ast():
    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        return False

    with open(TARGET_FILE, "r") as f:
        tree = ast.parse(f.read())

    setenv_used = False
    delenv_used = False
    setattr_used = False

    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name) and node.func.value.id == "monkeypatch":
                if node.func.attr == "setenv":
                    setenv_used = True
                elif node.func.attr == "delenv":
                    delenv_used = True
                elif node.func.attr == "setattr":
                    setattr_used = True

    if not setenv_used:
        print("   [FAIL] monkeypatch.setenv was not called.")
        return False
    if not delenv_used:
        print("   [FAIL] monkeypatch.delenv was not called.")
        return False
    if not setattr_used:
        print("   [FAIL] monkeypatch.setattr was not called.")
        return False

    print("   [PASS] AST checks for Day 16 verify OK.")
    return True

def run_tests():
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 16...")
    print("====================================================")

    if not check_ast():
        sys.exit(1)

    print("\nRunning pytest on your monkeypatch tests...")
    code, out = run_tests()
    if code != 0:
        print("[FAIL] Test suite execution failed! Output:")
        print(out)
        sys.exit(1)
        
    print("[PASS] Monkeypatch tests executed successfully.")
    print(out)
    
    print("\n----------------------------------------------------")
    print("[SUCCESS] You have completed Day 16 Assignments successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()
