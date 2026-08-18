# Day 20 Verifier (Mutation Testing Checker)
# ----------------------------------------------------------------------
# Run this file in your terminal: python day20_verifier.py
# It will check if your unit tests in day20_test.py are correctly written
# and actually asserting the behaviors!

import sys
import os
import subprocess

# Ensure the parent directory is in sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Paths
assignment_path = os.path.join(current_dir, "day20_assignment.py")
test_runner_path = os.path.join(current_dir, "day20_test.py")

def run_tests():
    """Runs day20_test.py and returns (passed, output)."""
    res = subprocess.run(
        [sys.executable, test_runner_path],
        capture_output=True,
        text=True,
        cwd=current_dir
    )
    return res.returncode == 0, res.stderr + res.stdout

def read_file(path):
    with open(path, "r") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)

print("Starting Day 20 Test Verifier (Mutation Checker)...\n")

# 1. Run unmodified test suite
passed, output = run_tests()
if not passed:
    print("[FAIL] Your tests failed even with the correct code! Check your assertions in day20_test.py.")
    print("Test Runner Output:")
    print(output)
    sys.exit(1)

# Check if user actually wrote tests (if they kept pass, they'll pass, but won't catch mutations)
original_code = read_file(assignment_path)

# Mutation 1: Change sum calculation in statistics
mutated_sum = original_code.replace("'sum': sum(numbers)", "'sum': sum(numbers) + 1")
write_file(assignment_path, mutated_sum)
try:
    passed, output = run_tests()
    if passed:
        print("[FAIL] Mutation Test: We broke the 'sum' calculation, but your test suite still passed!")
        print("Ensure you are asserting the sum value in test_valid_numbers().")
        sys.exit(1)
finally:
    write_file(assignment_path, original_code)  # Restore

# Mutation 2: Change empty list error handling
mutated_empty = original_code.replace("raise ValueError(\"List cannot be empty\")", "pass")
write_file(assignment_path, mutated_empty)
try:
    passed, output = run_tests()
    if passed:
        print("[FAIL] Mutation Test: We removed the ValueError on empty list, but your test suite still passed!")
        print("Ensure you are checking for ValueError in test_empty_list_raises_error().")
        sys.exit(1)
finally:
    write_file(assignment_path, original_code)  # Restore

# Mutation 3: Break palindrome check
mutated_pal = original_code.replace("return cleaned == cleaned[::-1]", "return True")
write_file(assignment_path, mutated_pal)
try:
    passed, output = run_tests()
    if passed:
        print("[FAIL] Mutation Test: We made is_palindrome() always return True, but your test suite still passed!")
        print("Ensure you are asserting False on non-palindromes in test_non_palindrome().")
        sys.exit(1)
finally:
    write_file(assignment_path, original_code)  # Restore

print("[PASS] Mutation Testing Successful!")
print("SUCCESS: Your unit tests are robust and successfully catch code mutations! Day 20 completed.")
