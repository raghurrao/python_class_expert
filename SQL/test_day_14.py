import os
import re

def test_day_14_interactive():
    py_file = 'day_14_answers.py'

    if not os.path.exists(py_file):
        print(f"[ERROR] {py_file} not found.")
        return

    with open(py_file, 'r', encoding='utf-8') as f:
        code = f.read()

    print("--- Running Day 14 Interactive Tests ---\n")

    # Step 1 Check
    if 'relationship' not in code or 'back_populates' not in code:
        print("[PENDING] Task 1: Use relationship(back_populates=...) in both classes.")
        return
    if 'ForeignKey' not in code:
        print("[PENDING] Task 1: Use ForeignKey('authors.id') in the Post class.")
        return
    print("[PASS] Task 1: ORM Relationships mapped correctly!")

    # Step 2 Check
    if not re.search(r'\.posts', code.split('with Session')[-1]):
        print("[PENDING] Task 2: Access the `.posts` attribute on the author object.")
        return
    if 'print(' not in code.split('with Session')[-1]:
        print("[PENDING] Task 2: Remember to print the title of each post!")
        return
    print("[PASS] Task 2: Navigating relationships successfully!")

    print("\n[SUCCESS] INCREDIBLE! You've unlocked the true power of the ORM.")
    print("Run `python day_14_answers.py` in your terminal to see SQLAlchemy automatically fetch Alice's posts!")

if __name__ == '__main__':
    test_day_14_interactive()
