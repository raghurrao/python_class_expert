import sqlite3
import os
import re

def test_day_4_interactive():
    dml_file = 'day_4_answers.sql'
    db_file = 'blog.db'

    if not os.path.exists(dml_file) or not os.path.exists(db_file):
        print(f"[ERROR] Ensure both {dml_file} and {db_file} exist.")
        return

    with open(dml_file, 'r', encoding='utf-8') as f:
        dml_sql = f.read()

    print("--- Running Day 4 Interactive Tests ---\n")

    # Step 1 Check
    if not re.search(r'INNER\s+JOIN\s+authors', dml_sql, re.IGNORECASE) and not re.search(r'JOIN\s+authors', dml_sql, re.IGNORECASE):
        print("[PENDING] Step 1: Use INNER JOIN to link posts and authors.")
        return
    print("[PASS] Step 1: INNER JOIN syntax detected!")

    # Step 2 Check
    if not re.search(r'LEFT\s+(OUTER\s+)?JOIN\s+posts', dml_sql, re.IGNORECASE):
        print("[PENDING] Step 2: Use LEFT JOIN starting from authors to link posts.")
        return
    print("[PASS] Step 2: LEFT JOIN syntax detected!")

    print("\n[SUCCESS] FANTASTIC! You are linking tables like a pro!")

if __name__ == '__main__':
    test_day_4_interactive()
