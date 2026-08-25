import os
import sys
import configparser

TARGET_FILE = "day23_assignment.py"
INI_FILE = "pytest.ini"

def check_answers():
    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        return False

    namespace = {}
    try:
        with open(TARGET_FILE, "r") as f:
            exec(f.read(), namespace)
    except Exception as e:
        print(f"[ERROR] Failed to execute {TARGET_FILE}: {e}")
        return False

    ans1 = namespace.get("ANSWER_QUESTION_1", "").lower()
    ans2 = namespace.get("ANSWER_QUESTION_2", "").lower()
    ans3 = namespace.get("ANSWER_QUESTION_3", "").lower()

    if not ans1 or not any(x in ans1 for x in ["branch", "condition", "path", "decision", "if", "else"]):
        print("   [FAIL] Question 1 answer is incomplete or missing. Explain how branch coverage tracks both True/False paths of conditionals.")
        return False

    if "html" not in ans2 or "report" not in ans2 or "--cov" not in ans2:
        print("   [FAIL] Question 2 answer is incorrect. Command should look like: 'pytest --cov=module --cov-report=html'")
        return False

    if "htmlcov" not in ans3:
        print("   [FAIL] Question 3 answer is incorrect. The default directory is 'htmlcov'.")
        return False

    print("   [PASS] Conceptual answers verify OK.")
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

    if "pytest" not in config.sections() or "addopts" not in config["pytest"]:
        print("   [FAIL] pytest.ini is missing the 'addopts' setting in the [pytest] section.")
        return False

    opts = config["pytest"]["addopts"]
    if "--cov=day6_validator" not in opts:
        print("   [FAIL] pytest.ini addopts is missing the '--cov=day6_validator' coverage trigger.")
        return False

    if "--cov-fail-under=" not in opts:
        print("   [FAIL] pytest.ini addopts is missing the '--cov-fail-under=90' check.")
        return False

    # Extract threshold
    try:
        parts = opts.split()
        threshold = None
        for part in parts:
            if part.startswith("--cov-fail-under="):
                threshold = int(part.split("=")[1])
                break
        if not threshold or threshold < 90:
            print(f"   [FAIL] Coverage threshold must be at least 90%. Got: {threshold}")
            return False
    except Exception:
        print("   [FAIL] Failed to parse coverage threshold from addopts.")
        return False

    print("   [PASS] pytest.ini coverage configuration verify OK.")
    return True

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 23...")
    print("====================================================")

    ans_ok = check_answers()
    ini_ok = check_ini()

    print("\n----------------------------------------------------")
    if not (ans_ok and ini_ok):
        print("[ERROR] Verification Failed! Check the errors above.")
        sys.exit(1)
    else:
        print("[SUCCESS] You have completed Day 23 Assignments successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
