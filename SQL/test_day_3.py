import sqlite3
import os
import re

def test_day_3_interactive():
    schema_file = 'day_1_answers.sql'
    dml_file = 'day_3_answers.sql'

    if not os.path.exists(schema_file) or not os.path.exists(dml_file):
        print(f"[ERROR] Ensure both {schema_file} and {dml_file} exist.")
        return

    with open(schema_file, 'r', encoding='utf-8') as f:
        schema_sql = f.read()
    with open(dml_file, 'r', encoding='utf-8') as f:
        dml_sql = f.read()

    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    try:
        cursor.executescript(schema_sql)
    except sqlite3.Error as e:
        print(f"[ERROR] Could not build schema from Day 1.\nError: {e}")
        return

    # Seed data specifically for Day 3 so we have reliable numbers to aggregate
    cursor.executescript("""
        INSERT INTO authors (id, username, email) VALUES (1, 'alice', 'alice@test.com');
        INSERT INTO authors (id, username, email) VALUES (2, 'bob', 'bob@test.com');
        INSERT INTO authors (id, username, email) VALUES (3, 'charlie', 'charlie@test.com');
        
        INSERT INTO posts (id, title, author_id) VALUES (1, 'A1', 1);
        INSERT INTO posts (id, title, author_id) VALUES (2, 'A2', 1);
        INSERT INTO posts (id, title, author_id) VALUES (3, 'A3', 1);
        INSERT INTO posts (id, title, author_id) VALUES (4, 'B1', 2);
        INSERT INTO posts (id, title, author_id) VALUES (5, 'B2', 2);
    """)

    print("--- Running Day 3 Interactive Tests ---\n")

    # Step 1 Check
    if not re.search(r'COUNT\s*\(\s*\*\s*\)', dml_sql, re.IGNORECASE) and not re.search(r'COUNT\s*\(\s*(id|title|author_id)\s*\)', dml_sql, re.IGNORECASE):
        print("[PENDING] Step 1: Write a SELECT statement using COUNT() on the posts table.")
        return
    print("[PASS] Step 1: COUNT function used!")

    # Step 2 Check
    if not re.search(r'GROUP\s+BY\s+author_id', dml_sql, re.IGNORECASE):
        print("[PENDING] Step 2: Use GROUP BY author_id to count posts per author.")
        return
    print("[PASS] Step 2: GROUP BY applied correctly!")

    # Step 3 Check
    if not re.search(r'HAVING\s+COUNT', dml_sql, re.IGNORECASE):
        print("[PENDING] Step 3: Use the HAVING clause to filter authors with > 1 post.")
        return
    print("[PASS] Step 3: HAVING clause applied correctly!")

    print("\n[SUCCESS] EXCELLENT! You've mastered Aggregations and Grouping!")

if __name__ == '__main__':
    test_day_3_interactive()
