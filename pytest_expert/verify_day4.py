import os
import sys
import ast
import subprocess

TARGET_FILE = "test_day4_assignment.py"

def check_ast():
    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        return False

    with open(TARGET_FILE, "r") as f:
        tree = ast.parse(f.read())

    # Flags to check
    skip_found = False
    skipif_found = False
    xfail_found = False
    strict_found = False

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if node.name == "test_deprecated_feature":
                # Check for @pytest.mark.skip
                for dec in node.decorator_list:
                    if isinstance(dec, ast.Call) and isinstance(dec.func, ast.Attribute):
                        if dec.func.attr == "skip":
                            skip_found = True
            
            elif node.name == "test_windows_only_path":
                # Check for @pytest.mark.skipif
                for dec in node.decorator_list:
                    if isinstance(dec, ast.Call) and isinstance(dec.func, ast.Attribute):
                        if dec.func.attr == "skipif":
                            skipif_found = True

            elif node.name == "test_buggy_feature":
                # Check for @pytest.mark.xfail(strict=True)
                for dec in node.decorator_list:
                    if isinstance(dec, ast.Call) and isinstance(dec.func, ast.Attribute):
                        if dec.func.attr == "xfail":
                            xfail_found = True
                            # Check strict=True argument
                            for kw in dec.keywords:
                                if kw.arg == "strict":
                                    if isinstance(kw.value, ast.Constant) and kw.value.value is True:
                                        strict_found = True
                                    # Handle older python ast where it was ast.Name Constant
                                    elif isinstance(kw.value, ast.Name) and kw.value.id == "True":
                                        strict_found = True

    if not skip_found:
        print("   [FAIL] test_deprecated_feature is not decorated with @pytest.mark.skip")
        return False
    if not skipif_found:
        print("   [FAIL] test_windows_only_path is not decorated with @pytest.mark.skipif")
        return False
    if not xfail_found:
        print("   [FAIL] test_buggy_feature is not decorated with @pytest.mark.xfail")
        return False
    if not strict_found:
        print("   [FAIL] test_buggy_feature xfail marker is missing strict=True")
        return False

    print("   [PASS] AST markers and parameters verify OK.")
    return True

def run_tests():
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 4...")
    print("====================================================")

    if not check_ast():
        sys.exit(1)

    print("\nRunning pytest on your marked suite...")
    code, out = run_tests()
    if code != 0:
        print("[FAIL] Test suite execution failed! Output:")
        print(out)
        sys.exit(1)
    
    print("[PASS] Test suite ran successfully (skipped and xfailed as configured).")
    print(out)
    
    print("\n----------------------------------------------------")
    print("[SUCCESS] You have completed Day 4 Assignments successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()
