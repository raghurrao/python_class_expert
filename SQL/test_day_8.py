import os
import re
import sqlite3

def test_day_8_interactive():
    py_file = 'day_8_answers.py'

    if not os.path.exists(py_file):
        print(f"[ERROR] {py_file} not found.")
        return

    with open(py_file, 'r', encoding='utf-8') as f:
        code = f.read()

    print("--- Running Day 8 Interactive Tests ---\n")

    # Step 1 Check
    if not re.search(r'insert\(', code) or not re.search(r'\.values\(', code):
        print("[PENDING] Step 1: Use insert(authors_table).values(...) to add 'david'.")
        return
    if 'commit' not in code:
        print("[PENDING] Step 1: Don't forget to call conn.commit() after executing your insert!")
        return
    print("[PASS] Step 1: Core insert detected!")

    # Step 2 Check
    if not re.search(r'select\(', code):
        print("[PENDING] Step 2: Use select(authors_table) to fetch authors.")
        return
    print("[PASS] Step 2: Core select detected!")

    # Verify Database state (Did they actually run day_8_answers.py?)
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authors WHERE username = 'david'")
    if not cursor.fetchone():
        print("\n[NOTE] You wrote the correct syntax, but 'david' isn't in the database yet.")
        print("Run `python day_8_answers.py` in your terminal to actually execute your code!")
    else:
        print("\n[SUCCESS] FANTASTIC! You are now writing Pythonic SQL using SQLAlchemy Core!")

if __name__ == '__main__':
    test_day_8_interactive()
