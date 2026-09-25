import os
import re

def test_day_13_interactive():
    py_file = 'day_13_answers.py'

    if not os.path.exists(py_file):
        print(f"[ERROR] {py_file} not found.")
        return

    with open(py_file, 'r', encoding='utf-8') as f:
        code = f.read()

    print("--- Running Day 13 Interactive Tests ---\n")

    # Step 1 Check
    if not re.search(r'select\(Author\)', code):
        print("[PENDING] Task 1: Use select(Author) to query the class.")
        return
    if 'scalars()' not in code:
        print("[PENDING] Task 1: Remember to use .scalars() when executing the statement to get the objects!")
        return
    print("[PASS] Task 1: ORM Select syntax is correct!")

    # Step 2 Check
    if not re.search(r'\.username\s*=\s*[\'"]bob_the_builder[\'"]', code):
        print("[PENDING] Task 2: Update the author\'s username attribute directly in Python.")
        return
    if 'session.commit()' not in code.split('bob_the_builder')[-1]:
        print("[PENDING] Task 2: Don\'t forget to commit() the session after modifying the object!")
        return
    print("[PASS] Task 2: ORM Update syntax is correct!")

    print("\n[SUCCESS] FANTASTIC! You are doing CRUD operations with pure Python Objects!")

if __name__ == '__main__':
    test_day_13_interactive()
