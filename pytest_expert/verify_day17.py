import os
import sys
import ast
import subprocess

TARGET_FILE = "test_day17_assignment.py"

def check_ast():
    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        return False

    with open(TARGET_FILE, "r") as f:
        tree = ast.parse(f.read())

    tmp_path_requested = False
    capsys_requested = False
    caplog_requested = False
    readouterr_called = False
    set_level_called = False

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            args = [arg.arg for arg in node.args.args]
            if node.name == "test_process_success":
                if "tmp_path" in args:
                    tmp_path_requested = True
                if "capsys" in args:
                    capsys_requested = True
                if "caplog" in args:
                    caplog_requested = True
            elif node.name == "test_process_empty":
                if "capsys" in args:
                    capsys_requested = True
                if "caplog" in args:
                    caplog_requested = True
        
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "readouterr":
                readouterr_called = True
            elif node.func.attr == "set_level":
                set_level_called = True

    if not tmp_path_requested:
        print("   [FAIL] test_process_success is missing the 'tmp_path' fixture argument.")
        return False
    if not capsys_requested:
        print("   [FAIL] test functions are missing the 'capsys' fixture argument.")
        return False
    if not caplog_requested:
        print("   [FAIL] test functions are missing the 'caplog' fixture argument.")
        return False
    if not readouterr_called:
        print("   [FAIL] capsys.readouterr() was never called to fetch stdout.")
        return False
    if not set_level_called:
        print("   [FAIL] caplog.set_level() was never called to set the capture threshold.")
        return False

    print("   [PASS] AST checks for Day 17 verify OK.")
    return True

def run_tests():
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 17...")
    print("====================================================")

    if not check_ast():
        sys.exit(1)

    print("\nRunning pytest on your system fixture tests...")
    code, out = run_tests()
    if code != 0:
        print("[FAIL] Test suite execution failed! Output:")
        print(out)
        sys.exit(1)
        
    print("[PASS] System fixture tests executed successfully.")
    print(out)
    
    print("\n----------------------------------------------------")
    print("[SUCCESS] You have completed Day 17 Assignments successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()
