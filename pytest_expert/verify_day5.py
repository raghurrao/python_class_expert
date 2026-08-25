import os
import sys
import ast
import configparser

TARGET_FILE = "test_day5_assignment.py"
INI_FILE = "pytest.ini"

def check_ast():
    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        return False

    with open(TARGET_FILE, "r") as f:
        tree = ast.parse(f.read())

    fast_found = False
    database_found = False

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if node.name == "test_fast_login":
                for dec in node.decorator_list:
                    if isinstance(dec, ast.Attribute) and dec.attr == "fast":
                        fast_found = True
            elif node.name == "test_db_sync":
                for dec in node.decorator_list:
                    if isinstance(dec, ast.Attribute) and dec.attr == "database":
                        database_found = True

    if not fast_found:
        print("   [FAIL] test_fast_login is not decorated with @pytest.mark.fast")
        return False
    if not database_found:
        print("   [FAIL] test_db_sync is not decorated with @pytest.mark.database")
        return False

    print("   [PASS] AST markers verify OK.")
    return True

def check_ini():
    if not os.path.exists(INI_FILE):
        print(f"   [FAIL] pytest.ini not found in the pytest_expert directory.")
        return False

    # Read the INI file
    config = configparser.ConfigParser()
    try:
        config.read(INI_FILE)
    except Exception as e:
        print(f"   [FAIL] Failed to parse pytest.ini: {e}")
        return False

    if "pytest" not in config.sections():
        print("   [FAIL] pytest.ini is missing the [pytest] section.")
        return False

    if "markers" not in config["pytest"]:
        print("   [FAIL] pytest.ini has a [pytest] section but is missing the 'markers' setting.")
        return False

    markers_text = config["pytest"]["markers"].lower()
    if "fast" not in markers_text:
        print("   [FAIL] 'fast' marker is not registered in pytest.ini.")
        return False
    if "database" not in markers_text:
        print("   [FAIL] 'database' marker is not registered in pytest.ini.")
        return False

    print("   [PASS] pytest.ini configuration verify OK.")
    return True

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 5...")
    print("====================================================")

    ast_ok = check_ast()
    ini_ok = check_ini()

    print("\n----------------------------------------------------")
    if not (ast_ok and ini_ok):
        print("[ERROR] Verification Failed! Check the errors above.")
        sys.exit(1)
    else:
        print("[SUCCESS] You have completed Day 5 Assignments successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
