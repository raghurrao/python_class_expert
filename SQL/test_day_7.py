import os
import re

def test_day_7_interactive():
    py_file = 'day_7_answers.py'

    if not os.path.exists(py_file):
        print(f"[ERROR] {py_file} not found.")
        return

    with open(py_file, 'r', encoding='utf-8') as f:
        code = f.read()

    print("--- Running Day 7 Interactive Tests ---\n")

    # Step 1 Check
    if not re.search(r'MetaData\(', code):
        print("[PENDING] Step 1: Create an instance of MetaData().")
        return
    print("[PASS] Step 1: MetaData created!")

    # Step 2 Check
    if not re.search(r'Table\(.*autoload_with\s*=\s*engine', code):
        print("[PENDING] Step 2: Use Table() with autoload_with=engine to reflect the 'posts' table.")
        return
    if 'columns.keys' not in code:
        print("[PENDING] Step 2: Don't forget to print the columns.keys()!")
        return
        
    print("[PASS] Step 2: Table reflection successful!")

    print("\n[SUCCESS] AWESOME! SQLAlchemy now knows exactly what your database looks like.")
    print("Try running `python day_7_answers.py` to see the column names printed!")

if __name__ == '__main__':
    test_day_7_interactive()
