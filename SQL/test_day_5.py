import sqlite3
import os
import re

def test_day_5_interactive():
    dml_file = 'day_5_answers.sql'
    db_file = 'blog.db'

    if not os.path.exists(dml_file) or not os.path.exists(db_file):
        print(f"[ERROR] Ensure both {dml_file} and {db_file} exist.")
        return

    with open(dml_file, 'r', encoding='utf-8') as f:
        dml_sql = f.read()

    print("--- Running Day 5 Interactive Tests ---\n")

    # Step 1 Check
    if not re.search(r'WHERE\s+author_id\s+IN\s*\(', dml_sql, re.IGNORECASE) and not re.search(r'WHERE\s+author_id\s*=\s*\(', dml_sql, re.IGNORECASE):
        print("[PENDING] Step 1: Use a subquery inside parentheses () in the WHERE clause.")
        return
    print("[PASS] Step 1: Subquery detected!")

    # Step 2 Check
    if not re.search(r'WITH\s+\w+\s+AS\s*\(', dml_sql, re.IGNORECASE):
        print("[PENDING] Step 2: Use the WITH clause to create a CTE.")
        return
    print("[PASS] Step 2: CTE (WITH clause) detected!")

    print("\n[SUCCESS] INCREDIBLE! You've mastered Subqueries and CTEs.")
    print("You are officially done with the raw SQL section! We are ready for SQLAlchemy!")

if __name__ == '__main__':
    test_day_5_interactive()
