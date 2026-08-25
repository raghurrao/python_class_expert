import os
import sys
import ast
import subprocess

TARGET_FILE = "test_day9_assignment.py"

def check_ast():
    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        return False

    with open(TARGET_FILE, "r") as f:
        tree = ast.parse(f.read())

    logger_scope_ok = False
    autouse_ok = False
    logger_yield = False
    autouse_yield = False

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if node.name == "logger":
                # Check decorator arguments for scope="session"
                for dec in node.decorator_list:
                    if isinstance(dec, ast.Call) and isinstance(dec.func, ast.Attribute) and dec.func.attr == "fixture":
                        for kw in dec.keywords:
                            if kw.arg == "scope" and isinstance(kw.value, ast.Constant) and kw.value.value == "session":
                                logger_scope_ok = True
                            # Handle older python ast
                            elif kw.arg == "scope" and isinstance(kw.value, ast.Name) and kw.value.id == "session":
                                logger_scope_ok = True

                for child in ast.walk(node):
                    if isinstance(child, ast.Yield):
                        logger_yield = True

            elif node.name == "auto_log_test":
                # Check decorator arguments for autouse=True
                for dec in node.decorator_list:
                    if isinstance(dec, ast.Call) and isinstance(dec.func, ast.Attribute) and dec.func.attr == "fixture":
                        for kw in dec.keywords:
                            if kw.arg == "autouse" and isinstance(kw.value, ast.Constant) and kw.value.value is True:
                                autouse_ok = True
                            elif kw.arg == "autouse" and isinstance(kw.value, ast.Name) and kw.value.id == "True":
                                autouse_ok = True

                for child in ast.walk(node):
                    if isinstance(child, ast.Yield):
                        autouse_yield = True

    if not logger_scope_ok:
        print("   [FAIL] logger fixture is not declared with scope='session'.")
        return False
    if not logger_yield:
        print("   [FAIL] logger fixture is missing the 'yield' statement.")
        return False
    if not autouse_ok:
        print("   [FAIL] auto_log_test fixture is not configured with autouse=True.")
        return False
    if not autouse_yield:
        print("   [FAIL] auto_log_test fixture is missing the 'yield' statement.")
        return False

    print("   [PASS] AST checks for Day 9 verify OK.")
    return True

def run_tests():
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 9...")
    print("====================================================")

    if not check_ast():
        sys.exit(1)

    print("\nRunning pytest on your scoped fixture tests...")
    code, out = run_tests()
    if code != 0:
        print("[FAIL] Test suite execution failed! Output:")
        print(out)
        sys.exit(1)
    
    print("[PASS] Scoped and autouse fixtures executed correctly.")
    print(out)
    
    print("\n----------------------------------------------------")
    print("[SUCCESS] You have completed Day 9 Assignments successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()
