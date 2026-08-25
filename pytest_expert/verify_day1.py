import os
import sys
import subprocess
import ast
import shutil

# Files involved
TARGET_FILE = "test_day1_assignment.py"
FUNCTIONS_FILE = "day1_functions.py"
FUNCTIONS_BACKUP = "day1_functions.py.backup"

# Clean code definition for restoring
CLEAN_CODE = """# Day 1: Target Functions
# These are the functions you need to test in test_day1_assignment.py.

def add(a, b):
    \"\"\"Returns the sum of a and b.\"\"\"
    return a + b

def divide(a, b):
    \"\"\"Returns the division of a by b. Raises ZeroDivisionError if b is 0.\"\"\"
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def get_average(numbers):
    \"\"\"
    Returns the average of numbers in a list.
    Raises ValueError if the list is empty.
    \"\"\"
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)
"""

# Mutants definitions (broken implementations)
MUTANTS = {
    "mutant_add": {
        "desc": "add(a, b) returns a - b (subtraction instead of addition)",
        "code": CLEAN_CODE.replace("return a + b", "return a - b")
    },
    "mutant_divide_zero": {
        "desc": "divide(a, 0) returns 0.0 instead of raising ZeroDivisionError",
        "code": CLEAN_CODE.replace('raise ZeroDivisionError("Cannot divide by zero")', "return 0.0")
    },
    "mutant_divide_calc": {
        "desc": "divide(a, b) returns a * b instead of dividing",
        "code": CLEAN_CODE.replace("return a / b", "return a * b")
    },
    "mutant_average_empty": {
        "desc": "get_average([]) returns 0.0 instead of raising ValueError",
        "code": CLEAN_CODE.replace('raise ValueError("List cannot be empty")', "return 0.0")
    },
    "mutant_average_calc": {
        "desc": "get_average(numbers) returns sum(numbers) (forgot to divide by len)",
        "code": CLEAN_CODE.replace("return sum(numbers) / len(numbers)", "return sum(numbers)")
    }
}

def check_structure():
    """Ensure the target file contains the correct test function names."""
    if not os.path.exists(TARGET_FILE):
        print(f"❌ Error: {TARGET_FILE} not found.")
        return False

    with open(TARGET_FILE, "r") as f:
        tree = ast.parse(f.read())

    required_tests = {
        "test_add_positive_numbers",
        "test_add_negative_numbers",
        "test_divide_normal",
        "test_divide_by_zero",
        "test_get_average_normal",
        "test_get_average_empty"
    }

    found_tests = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_"):
            found_tests.add(node.name)

    missing = required_tests - found_tests
    if missing:
        print(f"❌ Missing required test functions:")
        for m in missing:
            print(f"   - {m}")
        return False
    
    return True

def run_tests():
    """Run pytest on the target file and return (exit_code, output)."""
    # Use sys.executable to ensure we run pytest with the current python virtualenv
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def write_functions_file(content):
    with open(FUNCTIONS_FILE, "w") as f:
        f.write(content)

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 1...")
    print("====================================================")

    # 1. Structural Check
    if not check_structure():
        sys.exit(1)
    print("[OK] File structure and required functions verify OK.")

    # Back up the current functions file
    if os.path.exists(FUNCTIONS_FILE):
        shutil.copyfile(FUNCTIONS_FILE, FUNCTIONS_BACKUP)

    try:
        # 2. Verify on Clean Code (should PASS)
        print("\nTesting against correct code...")
        write_functions_file(CLEAN_CODE)
        code, out = run_tests()
        if code != 0:
            print("[FAIL] Tests failed on correct code! Output:")
            print(out)
            sys.exit(1)
        print("[PASS] All tests passed successfully on correct code.")

        # 3. Verify against Mutants (should FAIL)
        print("\nTesting against broken code (Mutation Testing)...")
        failed_mutants = []
        for name, mutant in MUTANTS.items():
            print(f"Applying mutant: {mutant['desc']}...")
            write_functions_file(mutant["code"])
            code, out = run_tests()

            # If exit code is 0, the test suite didn't catch the bug
            if code == 0:
                print(f"   [FAIL] Your tests did NOT catch this bug! They passed when they should have failed.")
                failed_mutants.append(name)
            else:
                print(f"   [PASS] Your tests successfully caught this bug (tests failed as expected).")

        print("\n----------------------------------------------------")
        if failed_mutants:
            print("[ERROR] Verification Failed!")
            print("Your tests are passing on the correct code, but they did not catch one or more bugs.")
            print("This usually happens if you left 'pass' inside your test functions or didn't write assertions.")
            sys.exit(1)
        else:
            print("[SUCCESS] You have completed Day 1 Assignments successfully.")
            print("Your test suite is comprehensive enough to catch both functional and logic errors!")
            sys.exit(0)

    finally:
        # Restore clean code
        if os.path.exists(FUNCTIONS_BACKUP):
            shutil.copyfile(FUNCTIONS_BACKUP, FUNCTIONS_FILE)
            os.remove(FUNCTIONS_BACKUP)
        else:
            write_functions_file(CLEAN_CODE)

if __name__ == "__main__":
    main()
