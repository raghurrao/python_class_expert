import os
import sys

TARGET_FILE = "day26_assignment.py"

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

    if "auto" not in ans1 or "-n" not in ans1:
        print("   [FAIL] Question 1 answer is incorrect. Command should be: 'pytest -n auto' (or include '-n auto').")
        return False

    if not ans2 or not any(x in ans2 for x in ["lock", "race", "concurrent", "write", "bleed", "overwrite", "thread", "collision"]):
        print("   [FAIL] Question 2 answer is incomplete. Explain that concurrent writes by 4 workers cause race conditions or database locks.")
        return False

    if not ans3 or not any(x in ans3 for x in ["unique", "separate", "isolate", "different", "folder", "directory", "path"]):
        print("   [FAIL] Question 3 answer is incomplete. Explain that tmp_path creates a separate, unique temporary directory for each test run, avoiding conflicts.")
        return False

    print("   [PASS] Conceptual answers verify OK.")
    return True

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 26...")
    print("====================================================")

    ans_ok = check_answers()

    print("\n----------------------------------------------------")
    if not ans_ok:
        print("[ERROR] Verification Failed! Check the errors above.")
        sys.exit(1)
    else:
        print("[SUCCESS] You have completed Day 26 Assignments successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
