import sqlite3
import os

def test_day_1_interactive():
    sql_file = 'day_1_answers.sql'
    if not os.path.exists(sql_file):
        print(f"[ERROR] {sql_file} not found.")
        return

    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_script = f.read()

    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    try:
        cursor.executescript(sql_script)
    except sqlite3.Error as e:
        print(f"[ERROR] SQL Execution Error: {e}")
        print("Check your SQL syntax and try again.")
        return

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cursor.fetchall()]

    print("--- Running Interactive Tests ---\n")

    # Step 1 & 2 Checks (authors table)
    if 'authors' not in tables:
        print("[PENDING] Step 1: Create the 'authors' table.")
        return
        
    cursor.execute("PRAGMA table_info(authors)")
    authors_columns = {row[1]: row for row in cursor.fetchall()}
    
    if 'email' not in authors_columns:
        print("[ERROR] Step 1: 'authors' table missing the 'email' column.")
        return
        
    print("[PASS] Step 1: 'authors' table created!")

    if authors_columns.get('id', [0]*6)[5] == 0:
        print("[PENDING] Step 2: Make 'id' the PRIMARY KEY in 'authors'.")
        return
    if authors_columns.get('username', [0]*6)[3] == 0:
        print("[PENDING] Step 2: Add NOT NULL to 'username' in 'authors'.")
        return

    print("[PASS] Step 2: Constraints applied to 'authors'!")

    # Step 3 Checks (posts table)
    if 'posts' not in tables:
        print("\n[PENDING] Step 3: Create the 'posts' table with a foreign key.")
        return
        
    cursor.execute("PRAGMA table_info(posts)")
    posts_columns = {row[1]: row for row in cursor.fetchall()}
    if 'author_id' not in posts_columns:
        print("[ERROR] Step 3: 'posts' table missing 'author_id'.")
        return
        
    print("[PASS] Step 3: 'posts' table created!")

    # Step 4 Checks (comments table)
    if 'comments' not in tables:
        print("\n[PENDING] Step 4: Create the 'comments' table with a CHECK constraint.")
        return
        
    print("[PASS] Step 4: 'comments' table created!")
    
    print("\n[SUCCESS] AMAZING! You have completed Day 1's Interactive Lesson! Let me know in the chat when you are ready for Day 2.")

if __name__ == '__main__':
    test_day_1_interactive()
