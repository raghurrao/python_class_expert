import os
import re
import sqlite3

def test_day_9_interactive():
    py_file = 'day_9_answers.py'

    if not os.path.exists(py_file):
        print(f"[ERROR] {py_file} not found.")
        return

    with open(py_file, 'r', encoding='utf-8') as f:
        code = f.read()

    print("--- Running Day 9 Interactive Tests ---\n")

    # Step 1 Check
    if '.where(' not in code or '.order_by(' not in code:
        print("[PENDING] Step 1: Use .where() and .order_by() on your select statement.")
        return
    if '.c.' not in code:
        print("[PENDING] Step 1: Use .c. to access columns on the reflected table (e.g. authors_table.c.username).")
        return
    print("[PASS] Step 1: Filtering and Ordering detected!")

    # Step 2 Check
    if not re.search(r'update\(', code) or '.where(' not in code.split('update(')[-1]:
        print("[PENDING] Step 2: Use update(authors_table).where(...) to update charlie.")
        return
    print("[PASS] Step 2: Update statement detected!")

    # Verify Database state
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM authors WHERE id = 3")
    row = cursor.fetchone()
    if not row or row[0] != 'charlie_new@test.com':
        print("\n[NOTE] You wrote the correct syntax, but the database wasn't updated.")
        print("Run `python day_9_answers.py` in your terminal to actually execute your code!")
    else:
        print("\n[SUCCESS] FANTASTIC! You've mastered SQLAlchemy Core querying and modifications!")

if __name__ == '__main__':
    test_day_9_interactive()
