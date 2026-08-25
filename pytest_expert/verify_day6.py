import os
import sys
import ast
import subprocess
import shutil
import configparser

TARGET_FILE = "test_day6_assignment.py"
VALIDATOR_FILE = "day6_validator.py"
VALIDATOR_BACKUP = "day6_validator.py.backup"
INI_FILE = "pytest.ini"

CLEAN_CODE = """# Day 6: DataValidator Library to Test

class DataValidator:
    @staticmethod
    def validate_username(username):
        if not isinstance(username, str):
            raise TypeError("Username must be a string")
        if len(username) < 3 or len(username) > 20:
            raise ValueError("Username must be between 3 and 20 characters")
        if not username.isalnum():
            raise ValueError("Username must be alphanumeric")
        return True

    @staticmethod
    def validate_email(email):
        if not isinstance(email, str):
            raise TypeError("Email must be a string")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format")
        return True

    @staticmethod
    def validate_password(password):
        if not isinstance(password, str):
            raise TypeError("Password must be a string")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not any(c.isupper() for c in password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.islower() for c in password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(c.isdigit() for c in password):
            raise ValueError("Password must contain at least one number")
        return True
"""

MUTANTS = {
    "mutant_user_type": {
        "desc": "validate_username() allows non-string inputs without TypeError",
        "code": CLEAN_CODE.replace('raise TypeError("Username must be a string")', "return True")
    },
    "mutant_user_len": {
        "desc": "validate_username() allows length < 3 or > 20 without ValueError",
        "code": CLEAN_CODE.replace('raise ValueError("Username must be between 3 and 20 characters")', "return True")
    },
    "mutant_user_chars": {
        "desc": "validate_username() allows special symbols (e.g. '@') without ValueError",
        "code": CLEAN_CODE.replace('raise ValueError("Username must be alphanumeric")', "return True")
    },
    "mutant_email_format": {
        "desc": "validate_email() accepts email missing '@' or '.' without ValueError",
        "code": CLEAN_CODE.replace('raise ValueError("Invalid email format")', "return True")
    },
    "mutant_password_len": {
        "desc": "validate_password() accepts short passwords without ValueError",
        "code": CLEAN_CODE.replace('raise ValueError("Password must be at least 8 characters")', "return True")
    },
    "mutant_password_upper": {
        "desc": "validate_password() accepts passwords with no uppercase letters",
        "code": CLEAN_CODE.replace('raise ValueError("Password must contain at least one uppercase letter")', "return True")
    },
    "mutant_password_lower": {
        "desc": "validate_password() accepts passwords with no lowercase letters",
        "code": CLEAN_CODE.replace('raise ValueError("Password must contain at least one lowercase letter")', "return True")
    },
    "mutant_password_digit": {
        "desc": "validate_password() accepts passwords with no digits",
        "code": CLEAN_CODE.replace('raise ValueError("Password must contain at least one number")', "return True")
    }
}

REQUIRED_TESTS = {
    "test_username_valid",
    "test_username_invalid_type",
    "test_username_invalid_len",
    "test_username_invalid_chars",
    "test_email_valid",
    "test_email_invalid_type",
    "test_email_invalid_format",
    "test_password_valid",
    "test_password_invalid_type",
    "test_password_too_short",
    "test_password_no_uppercase",
    "test_password_no_lowercase",
    "test_password_no_number"
}

def check_structure_and_markers():
    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        return False

    with open(TARGET_FILE, "r") as f:
        tree = ast.parse(f.read())

    class_found = False
    found_methods = set()
    method_markers = {}

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == "TestDataValidator":
            class_found = True
            for child in node.body:
                if isinstance(child, ast.FunctionDef) and child.name.startswith("test_"):
                    found_methods.add(child.name)
                    # Check decorators
                    markers = []
                    for dec in child.decorator_list:
                        # e.g., @pytest.mark.fast
                        if isinstance(dec, ast.Attribute) and dec.attr:
                            markers.append(dec.attr)
                        # e.g., @pytest.mark.fast()
                        elif isinstance(dec, ast.Call) and isinstance(dec.func, ast.Attribute):
                            markers.append(dec.func.attr)
                    method_markers[child.name] = markers

    if not class_found:
        print("   [FAIL] TestDataValidator class was not found.")
        return False

    missing = REQUIRED_TESTS - found_methods
    if missing:
        print("[FAIL] Missing required test functions inside TestDataValidator:")
        for m in missing:
            print(f"   - {m}")
        return False

    # Check marker configurations
    for method in found_methods:
        markers = method_markers.get(method, [])
        if "password" in method:
            if "security" not in markers:
                print(f"   [FAIL] {method} must be decorated with @pytest.mark.security")
                return False
        else:
            if "fast" not in markers:
                print(f"   [FAIL] {method} must be decorated with @pytest.mark.fast")
                return False

    print("   [PASS] Class structure, method names, and decorators verify OK.")
    return True

def check_ini():
    if not os.path.exists(INI_FILE):
        print(f"   [FAIL] pytest.ini not found in the pytest_expert directory.")
        return False

    config = configparser.ConfigParser()
    try:
        config.read(INI_FILE)
    except Exception as e:
        print(f"   [FAIL] Failed to parse pytest.ini: {e}")
        return False

    if "pytest" not in config.sections() or "markers" not in config["pytest"]:
        print("   [FAIL] pytest.ini missing markers registration.")
        return False

    markers_text = config["pytest"]["markers"].lower()
    for m in ["fast", "database", "security"]:
        if m not in markers_text:
            print(f"   [FAIL] '{m}' marker is not registered in pytest.ini.")
            return False

    print("   [PASS] pytest.ini markers registered OK.")
    return True

def run_tests():
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def write_validator_file(content):
    with open(VALIDATOR_FILE, "w") as f:
        f.write(content)

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 6...")
    print("====================================================")

    if not check_structure_and_markers():
        sys.exit(1)

    if not check_ini():
        sys.exit(1)

    if os.path.exists(VALIDATOR_FILE):
        shutil.copyfile(VALIDATOR_FILE, VALIDATOR_BACKUP)

    try:
        print("\nTesting against correct code...")
        write_validator_file(CLEAN_CODE)
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
            write_validator_file(mutant["code"])
            code, out = run_tests()

            if code == 0:
                print(f"   [FAIL] Your tests did NOT catch this bug! They passed when they should have failed.")
                failed_mutants.append(name)
            else:
                print(f"   [PASS] Your tests successfully caught this bug (tests failed as expected).")

        print("\n----------------------------------------------------")
        if failed_mutants:
            print("[ERROR] Verification Failed!")
            print("Your test suite is missing coverage for some buggy scenarios.")
            print("Ensure your assertions verify correct types, value boundaries, and error messages.")
            sys.exit(1)
        else:
            print("[SUCCESS] You have completed the Week 1 Integration Milestone!")
            sys.exit(0)

    finally:
        if os.path.exists(VALIDATOR_BACKUP):
            shutil.copyfile(VALIDATOR_BACKUP, VALIDATOR_FILE)
            os.remove(VALIDATOR_BACKUP)
        else:
            write_validator_file(CLEAN_CODE)

if __name__ == "__main__":
    main()
