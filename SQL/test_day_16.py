import os
import re

def test_day_16_interactive():
    ini_file = 'alembic.ini'

    if not os.path.exists(ini_file):
        print(f"[ERROR] {ini_file} not found. Did Alembic initialize correctly?")
        return

    with open(ini_file, 'r', encoding='utf-8') as f:
        code = f.read()

    print("--- Running Day 16 Interactive Tests ---\n")

    if not re.search(r'sqlalchemy\.url\s*=\s*sqlite:///blog\.db', code):
        print("[PENDING] Task 1: Update sqlalchemy.url in alembic.ini to point to sqlite:///blog.db")
        return
    
    print("[PASS] Task 1: Alembic is now configured to talk to blog.db!")
    print("\n[SUCCESS] AWESOME! You are ready to start writing database migrations!")

if __name__ == '__main__':
    test_day_16_interactive()
