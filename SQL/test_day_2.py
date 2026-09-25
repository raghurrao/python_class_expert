import sqlite3
import os
import re

def test_day_2_interactive():
    schema_file = 'day_1_answers.sql'
    dml_file = 'day_2_answers.sql'

    if not os.path.exists(schema_file) or not os.path.exists(dml_file):
        print(f"[ERROR] Ensure both {schema_file} and {dml_file} exist in this directory.")
        return

    with open(schema_file, 'r', encoding='utf-8') as f:
        schema_sql = f.read()
    with open(dml_file, 'r', encoding='utf-8') as f:
        dml_sql = f.read()

    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Step 0: Build schema from Day 1
    try:
        cursor.executescript(schema_sql)
    except sqlite3.Error as e:
        print(f"[ERROR] Could not build schema from Day 1. Did you change {schema_file}?\nError: {e}")
        return

    print("--- Running Day 2 Interactive Tests ---\n")
    
    try:
        cursor.executescript(dml_sql)
    except sqlite3.Error as e:
        print(f"[ERROR] SQL Execution Error in {dml_file}:\n{e}")
        print("Check your syntax and try again.")
        return

    # Check Step 1 (INSERT)
    cursor.execute("SELECT COUNT(*) FROM authors")
    author_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM posts")
    post_count = cursor.fetchone()[0]

    if author_count < 2 or post_count < 1:
        print("[PENDING] Step 1: Use INSERT to add at least 2 authors and 2 posts.")
        return
    print("[PASS] Step 1: Authors and Posts inserted (and tracked) successfully!")

    # Check Step 2 (SELECT)
    # Since executescript consumes SELECTs silently, we evaluate the text loosely.
    if not re.search(r'SELECT', dml_sql, re.IGNORECASE):
        print("[PENDING] Step 2: Write a SELECT statement.")
        return
    if 'title' not in dml_sql.lower() or 'author_id' not in dml_sql.lower() or '1' not in dml_sql:
        print("[PENDING] Step 2: Your SELECT statement should get 'title' where 'author_id = 1'.")
        return
    print("[PASS] Step 2: SELECT statement looks good!")

    # Check Step 3 (UPDATE)
    cursor.execute("SELECT email FROM authors WHERE id = 2")
    row = cursor.fetchone()
    if not row or row[0] != 'new_email@example.com':
        print("[PENDING] Step 3: Update the email of author with id=2 to 'new_email@example.com'.")
        return
    print("[PASS] Step 3: Author email updated!")

    # Check Step 4 (DELETE)
    cursor.execute("SELECT * FROM posts WHERE id = 1")
    if cursor.fetchone() is not None:
         print("[PENDING] Step 4: Delete the post with id = 1.")
         return
    print("[PASS] Step 4: Post deleted!")

    print("\n[SUCCESS] AMAZING! You completed Day 2's CRUD operations!")

if __name__ == '__main__':
    test_day_2_interactive()
