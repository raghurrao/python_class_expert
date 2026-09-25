import os
import re

def test_day_11_interactive():
    py_file = 'day_11_answers.py'

    if not os.path.exists(py_file):
        print(f"[ERROR] {py_file} not found.")
        return

    with open(py_file, 'r', encoding='utf-8') as f:
        code = f.read()

    print("--- Running Day 11 Interactive Tests ---\n")

    if not re.search(r'engine\.begin\(\)', code):
        print("[PENDING] Task 1: Use engine.begin() to manage the transaction automatically.")
        return
    if re.search(r'\.commit\(\)', code):
        print("[PENDING] Task 1: You don't need to call .commit() manually when using engine.begin()!")
        return
        
    print("[PASS] Task 1: Transaction block detected!")
    print("\n[SUCCESS] GREAT! You now know how to safely run multiple queries as a single transaction.")
    print("This concludes SQLAlchemy Core! We are ready for the ORM.")

if __name__ == '__main__':
    test_day_11_interactive()
