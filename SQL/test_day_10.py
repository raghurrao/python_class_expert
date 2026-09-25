import os
import re

def test_day_10_interactive():
    py_file = 'day_10_answers.py'

    if not os.path.exists(py_file):
        print(f"[ERROR] {py_file} not found.")
        return

    with open(py_file, 'r', encoding='utf-8') as f:
        code = f.read()

    print("--- Running Day 10 Interactive Tests ---\n")

    # Step 1 Check
    if not re.search(r'\.select_from\(', code):
        print("[PENDING] Task 1: Use .select_from() to apply your join.")
        return
    if not re.search(r'\.join\(', code):
        print("[PENDING] Task 1: Use the .join() method (e.g. authors_table.join(posts_table)).")
        return
        
    print("[PASS] Task 1: Core Join detected!")
    print("\n[SUCCESS] FANTASTIC! You are linking tables via pure Python!")

if __name__ == '__main__':
    test_day_10_interactive()
