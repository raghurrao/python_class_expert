import os
import re

def test_day_6_interactive():
    py_file = 'day_6_answers.py'

    if not os.path.exists(py_file):
        print(f"[ERROR] {py_file} not found.")
        return

    with open(py_file, 'r', encoding='utf-8') as f:
        code = f.read()

    print("--- Running Day 6 Interactive Tests ---\n")

    # Step 1 Check
    if not re.search(r'create_engine\(.*sqlite:///blog\.db', code, re.IGNORECASE):
        print("[PENDING] Step 1: Make sure you imported create_engine and connected to 'sqlite:///blog.db'.")
        return
    print("[PASS] Step 1: Engine created successfully!")

    # Step 2 Check
    if not re.search(r'text\(', code) or not re.search(r'\.execute\(', code):
        print("[PENDING] Step 2: Make sure you import text(), open a connection, and execute a SELECT statement.")
        return
    if 'fetchall' not in code and 'print' not in code:
        print("[PENDING] Step 2: Don't forget to fetchall() and print the results!")
        return
        
    print("[PASS] Step 2: Connection and raw SQL execution detected!")

    print("\n[SUCCESS] INCREDIBLE! You've officially written your first SQLAlchemy code in Python!")
    print("Run `python day_6_answers.py` in your terminal to actually see the authors print out!")

if __name__ == '__main__':
    test_day_6_interactive()
