import os
import re

def test_day_15_interactive():
    py_file = 'day_15_answers.py'

    if not os.path.exists(py_file):
        print(f"[ERROR] {py_file} not found.")
        return

    with open(py_file, 'r', encoding='utf-8') as f:
        code = f.read()

    print("--- Running Day 15 Interactive Tests ---\n")

    if 'joinedload(Author.posts)' not in code:
        print("[PENDING] Task 1: Use .options(joinedload(Author.posts)) on your select statement.")
        return
    print("[PASS] Task 1: joinedload syntax detected!")

    if 'unique().all()' not in code:
        print("[PENDING] Task 2: You must use .unique() before .all() when using joinedload on a one-to-many relationship.")
        return
    print("[PASS] Task 2: Execution and unique() detected!")

    print("\n[SUCCESS] FANTASTIC! You've learned how to optimize ORM queries to prevent the N+1 problem!")

if __name__ == '__main__':
    test_day_15_interactive()
