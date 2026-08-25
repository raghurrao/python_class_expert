import os
import sys
import ast
import subprocess

TARGET_FILE = "test_day19_assignment.py"

def check_ast():
    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        return False

    with open(TARGET_FILE, "r") as f:
        tree = ast.parse(f.read())

    engine_session_ok = False
    session_yield_ok = False
    begin_transaction_called = False
    rollback_called = False

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if node.name == "db_engine":
                # Check scope="session"
                for dec in node.decorator_list:
                    if isinstance(dec, ast.Call) and isinstance(dec.func, ast.Attribute) and dec.func.attr == "fixture":
                        for kw in dec.keywords:
                            if kw.arg == "scope" and isinstance(kw.value, ast.Constant) and kw.value.value == "session":
                                engine_session_ok = True
                            elif kw.arg == "scope" and isinstance(kw.value, ast.Name) and kw.value.id == "session":
                                engine_session_ok = True
            elif node.name == "db_session":
                # Check yield
                for child in ast.walk(node):
                    if isinstance(child, ast.Yield):
                        session_yield_ok = True
                    elif isinstance(child, ast.Call) and isinstance(child.func, ast.Attribute):
                        if child.func.attr == "begin_transaction":
                            begin_transaction_called = True
                        elif child.func.attr == "rollback":
                            rollback_called = True

    if not engine_session_ok:
        print("   [FAIL] db_engine fixture must be scope='session'")
        return False
    if not session_yield_ok:
        print("   [FAIL] db_session fixture must use yield for setup/teardown")
        return False
    if not begin_transaction_called:
        print("   [FAIL] db_session fixture is missing the call to client.begin_transaction() in setup")
        return False
    if not rollback_called:
        print("   [FAIL] db_session fixture is missing the call to client.rollback() in teardown")
        return False

    print("   [PASS] AST checks for Day 19 verify OK.")
    return True

def run_tests():
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 19...")
    print("====================================================")

    if not check_ast():
        sys.exit(1)

    print("\nRunning pytest on your database isolation tests...")
    code, out = run_tests()
    if code != 0:
        print("[FAIL] Test suite execution failed! Output:")
        print(out)
        sys.exit(1)
        
    print("[PASS] Database transactional isolation tests executed successfully.")
    print(out)
    
    print("\n----------------------------------------------------")
    print("[SUCCESS] You have completed Day 19 Assignments successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()
