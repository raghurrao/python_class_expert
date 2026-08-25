import os
import sys
import subprocess
import ast
import shutil

TARGET_FILE = "test_day2_assignment.py"
FUNCTIONS_FILE = "day2_functions.py"
FUNCTIONS_BACKUP = "day2_functions.py.backup"

CLEAN_CODE = """# Day 2: Target Functions for Exceptions & Dictionary Assertions

def validate_age(age):
    if not isinstance(age, int) or isinstance(age, bool):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 120:
        raise ValueError(f"Age {age} is invalid. Must be between 0 and 120.")
    return True

def parse_user_data(user_dict):
    if "username" not in user_dict:
        raise KeyError("username")
    if "email" not in user_dict:
        raise KeyError("email")
    return f"Username: {user_dict['username']}, Email: {user_dict['email']}"

def merge_configs(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise TypeError("Both inputs must be dictionaries")
    
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_configs(result[key], value)
        else:
            result[key] = value
    return result
"""

MUTANTS = {
    "mutant_age_no_type": {
        "desc": "validate_age() returns True for string instead of raising TypeError",
        "code": CLEAN_CODE.replace('raise TypeError("Age must be an integer")', "return True")
    },
    "mutant_age_wrong_type_msg": {
        "desc": "validate_age() raises TypeError but message does not contain 'Age must be an integer'",
        "code": CLEAN_CODE.replace('raise TypeError("Age must be an integer")', 'raise TypeError("Invalid type")')
    },
    "mutant_age_no_value": {
        "desc": "validate_age() returns True for age out of bounds instead of raising ValueError",
        "code": CLEAN_CODE.replace('raise ValueError(f"Age {age} is invalid. Must be between 0 and 120.")', "return True")
    },
    "mutant_age_wrong_value_msg": {
        "desc": "validate_age() raises ValueError but message lacks the invalid value or 'between 0 and 120'",
        "code": CLEAN_CODE.replace('raise ValueError(f"Age {age} is invalid. Must be between 0 and 120.")', 'raise ValueError("Age out of bounds")')
    },
    "mutant_parse_no_key_error": {
        "desc": "parse_user_data() does not raise KeyError when keys are missing",
        "code": CLEAN_CODE.replace('raise KeyError("username")', "pass").replace('raise KeyError("email")', "pass")
    },
    "mutant_parse_wrong_key": {
        "desc": "parse_user_data() raises KeyError but specifies a different key name",
        "code": CLEAN_CODE.replace('raise KeyError("username")', 'raise KeyError("missing_key")')
    },
    "mutant_merge_no_type": {
        "desc": "merge_configs() does not raise TypeError for invalid argument types",
        "code": CLEAN_CODE.replace('raise TypeError("Both inputs must be dictionaries")', "return {}")
    },
    "mutant_merge_wrong_msg": {
        "desc": "merge_configs() raises TypeError but message does not contain 'must be dictionaries'",
        "code": CLEAN_CODE.replace('raise TypeError("Both inputs must be dictionaries")', 'raise TypeError("Wrong input type")')
    },
    "mutant_merge_no_recurse": {
        "desc": "merge_configs() does not recursively merge nested dictionaries (overwrites them)",
        "code": CLEAN_CODE.replace("result[key] = merge_configs(result[key], value)", "result[key] = value")
    }
}

def check_structure():
    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        return False

    with open(TARGET_FILE, "r") as f:
        tree = ast.parse(f.read())

    required_tests = {
        "test_validate_age_valid",
        "test_validate_age_invalid_type",
        "test_validate_age_out_of_bounds",
        "test_parse_user_data_valid",
        "test_parse_user_data_missing_key",
        "test_merge_configs_flat",
        "test_merge_configs_nested",
        "test_merge_configs_invalid_type"
    }

    found_tests = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_"):
            found_tests.add(node.name)

    missing = required_tests - found_tests
    if missing:
        print(f"[ERROR] Missing required test functions:")
        for m in missing:
            print(f"   - {m}")
        return False
    return True

def run_tests():
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def write_functions_file(content):
    with open(FUNCTIONS_FILE, "w") as f:
        f.write(content)

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 2...")
    print("====================================================")

    if not check_structure():
        sys.exit(1)
    print("[OK] File structure and required functions verify OK.")

    if os.path.exists(FUNCTIONS_FILE):
        shutil.copyfile(FUNCTIONS_FILE, FUNCTIONS_BACKUP)

    try:
        print("\nTesting against correct code...")
        write_functions_file(CLEAN_CODE)
        code, out = run_tests()
        if code != 0:
            print("[FAIL] Tests failed on correct code! Output:")
            print(out)
            sys.exit(1)
        print("[PASS] All tests passed successfully on correct code.")

        print("\nTesting against broken code (Mutation Testing)...")
        failed_mutants = []
        for name, mutant in MUTANTS.items():
            print(f"Applying mutant: {mutant['desc']}...")
            write_functions_file(mutant["code"])
            code, out = run_tests()

            if code == 0:
                print(f"   [FAIL] Your tests did NOT catch this bug! They passed when they should have failed.")
                failed_mutants.append(name)
            else:
                print(f"   [PASS] Your tests successfully caught this bug (tests failed as expected).")

        print("\n----------------------------------------------------")
        if failed_mutants:
            print("[ERROR] Verification Failed!")
            print("Your tests did not catch one or more mutated bugs.")
            print("Check that you assert exception types, check error messages with 'match' or 'excinfo', and test nesting.")
            sys.exit(1)
        else:
            print("[SUCCESS] You have completed Day 2 Assignments successfully.")
            sys.exit(0)

    finally:
        if os.path.exists(FUNCTIONS_BACKUP):
            shutil.copyfile(FUNCTIONS_BACKUP, FUNCTIONS_FILE)
            os.remove(FUNCTIONS_BACKUP)
        else:
            write_functions_file(CLEAN_CODE)

if __name__ == "__main__":
    main()
