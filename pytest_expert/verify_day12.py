import os
import sys
import ast
import subprocess

TARGET_FILE = "test_day12_assignment.py"

def check_ast():
    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        return False

    with open(TARGET_FILE, "r") as f:
        tree = ast.parse(f.read())

    prime_param_ok = False
    prime_ids_ok = False
    type_param_ok = False

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if node.name == "test_is_prime":
                for dec in node.decorator_list:
                    if isinstance(dec, ast.Call) and isinstance(dec.func, ast.Attribute) and dec.func.attr == "parametrize":
                        prime_param_ok = True
                        for kw in dec.keywords:
                            if kw.arg == "ids":
                                prime_ids_ok = True

            elif node.name == "test_is_prime_type_error":
                for dec in node.decorator_list:
                    if isinstance(dec, ast.Call) and isinstance(dec.func, ast.Attribute) and dec.func.attr == "parametrize":
                        type_param_ok = True

    if not prime_param_ok:
        print("   [FAIL] test_is_prime is not decorated with @pytest.mark.parametrize")
        return False
    if not prime_ids_ok:
        print("   [FAIL] test_is_prime is missing the custom 'ids' parameter in its parametrization.")
        return False
    if not type_param_ok:
        print("   [FAIL] test_is_prime_type_error is not decorated with @pytest.mark.parametrize")
        return False

    print("   [PASS] AST checks for Day 12 verify OK.")
    return True

def run_tests():
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 12...")
    print("====================================================")

    if not check_ast():
        sys.exit(1)

    print("\nRunning pytest on your test-parameterized suite...")
    code, out = run_tests()
    if code != 0:
        print("[FAIL] Test suite execution failed! Output:")
        print(out)
        sys.exit(1)
        
    # Check that 11 tests ran (7 from is_prime, 4 from is_prime_type_error)
    if "11 passed" not in out:
        print("[FAIL] Expected exactly 11 passed tests to run, check output:")
        print(out)
        sys.exit(1)
        
    print("[PASS] Parametrized test suite executed successfully (11 runs generated).")
    print(out)
    
    print("\n----------------------------------------------------")
    print("[SUCCESS] You have completed Day 12 Assignments successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()
