import os
import sqlite3

def test_day_18_interactive():
    db_file = 'blog.db'

    if not os.path.exists(db_file):
        print(f"[ERROR] {db_file} not found.")
        return

    print("--- Running Day 18 Interactive Tests ---\n")

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT version_num FROM alembic_version")
        version = cursor.fetchone()
        
        if not version:
            print("[PENDING] The alembic_version table is empty. Did you run `python -m alembic upgrade head`?")
            return
            
        print(f"[PASS] Alembic Migration applied! Current database version: {version[0]}")
    except sqlite3.OperationalError:
        print("[PENDING] The alembic_version table doesn't exist yet. Did you run the commands in the terminal?")
        return

    print("\n[SUCCESS] YOU DID IT! You have successfully mastered Database Migrations.")
    print("[CONGRATULATIONS] You have officially completed the 30-Day SQL & SQLAlchemy Mastery Plan!")

if __name__ == '__main__':
    test_day_18_interactive()
