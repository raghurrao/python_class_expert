import sys
import os
import shlex

TARGET_FILE = "day3_assignment.py"

def print_fail(msg):
    print(f"   [FAIL] {msg}")

def verify_command(name, command, required_flags, forbidden_flags, k_contains=None, k_not_contains=None):
    if not command:
        print_fail(f"{name} is empty! Please write the pytest command.")
        return False

    parts = shlex.split(command)
    if parts[0] != "pytest":
        print_fail(f"{name} must start with 'pytest'. Got: '{parts[0]}'")
        return False

    if "test_day3_sandbox.py" not in parts:
        print_fail(f"{name} must target 'test_day3_sandbox.py'.")
        return False

    # Check required flags
    for flag in required_flags:
        if isinstance(flag, tuple):
            # One of the flags in the tuple must be present
            if not any(f in parts for f in flag):
                print_fail(f"{name} is missing a required flag. Expected one of: {flag}")
                return False
        else:
            if flag not in parts:
                print_fail(f"{name} is missing required flag: '{flag}'")
                return False

    # Check forbidden flags
    for flag in forbidden_flags:
        if flag in parts:
            print_fail(f"{name} contains forbidden flag: '{flag}'")
            return False

    # Special check for -k parameter
    if k_contains or k_not_contains:
        # Find -k value
        k_val = None
        for i, part in enumerate(parts):
            if part == "-k" and i + 1 < len(parts):
                k_val = parts[i + 1]
                break
        
        if not k_val:
            print_fail(f"{name} must use the '-k' flag to filter tests.")
            return False

        k_lower = k_val.lower()
        if k_contains:
            for item in k_contains:
                if item.lower() not in k_lower:
                    print_fail(f"{name} filter '-k' value '{k_val}' is missing expected term: '{item}'")
                    return False
        if k_not_contains:
            for item in k_not_contains:
                if item.lower() in k_lower:
                    print_fail(f"{name} filter '-k' value '{k_val}' contains unexpected term: '{item}'")
                    return False
                if "not" not in k_lower:
                    print_fail(f"{name} filter '-k' value '{k_val}' should use 'not' logic.")
                    return False

    print(f"   [PASS] {name} is correct.")
    return True

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 3...")
    print("====================================================")

    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        sys.exit(1)

    # Load assignment variables
    namespace = {}
    try:
        with open(TARGET_FILE, "r") as f:
            exec(f.read(), namespace)
    except Exception as e:
        print(f"[ERROR] Failed to execute {TARGET_FILE}: {e}")
        sys.exit(1)

    commands = {
        "COMMAND_PAYMENT_ONLY": (
            namespace.get("COMMAND_PAYMENT_ONLY", ""),
            ["-k"],
            [],
            ["payment"],
            []
        ),
        "COMMAND_LOGIN_NOT_SUCCESS": (
            namespace.get("COMMAND_LOGIN_NOT_SUCCESS", ""),
            ["-k"],
            [],
            ["login"],
            ["success"]
        ),
        "COMMAND_DISABLE_CAPTURE": (
            namespace.get("COMMAND_DISABLE_CAPTURE", ""),
            [("-s", "--capture=no")],
            [],
            None,
            None
        ),
        "COMMAND_EXIT_ON_FIRST_FAIL": (
            namespace.get("COMMAND_EXIT_ON_FIRST_FAIL", ""),
            [("-x", "--maxfail=1")],
            [],
            None,
            None
        ),
        "COMMAND_RUN_LAST_FAILED": (
            namespace.get("COMMAND_RUN_LAST_FAILED", ""),
            [("--lf", "--last-failed")],
            [],
            None,
            None
        ),
        "COMMAND_SHOW_SLOWEST_TESTS": (
            namespace.get("COMMAND_SHOW_SLOWEST_TESTS", ""),
            ["--durations=2"],
            [],
            None,
            None
        )
    }

    all_passed = True
    for name, (cmd, req, forbidden, k_inc, k_dec) in commands.items():
        if not verify_command(name, cmd.strip(), req, forbidden, k_inc, k_dec):
            all_passed = False

    print("\n----------------------------------------------------")
    if not all_passed:
        print("[ERROR] Verification Failed! Check the errors above.")
        sys.exit(1)
    else:
        print("[SUCCESS] You have completed Day 3 Assignments successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
