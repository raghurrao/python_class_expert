import os

def test_day_19_interactive():
    py_file = 'final_project.py'

    if not os.path.exists(py_file):
        print(f"[ERROR] {py_file} not found. Please create it!")
        return

    with open(py_file, 'r', encoding='utf-8') as f:
        code = f.read()

    print("--- Running Day 19 Interactive Tests ---\n")

    if 'sqlite:///final.db' not in code:
        print("[PENDING] Please create a new database connection 'sqlite:///final.db'.")
        return
    if 'class Category' not in code or 'class Product' not in code:
        print("[PENDING] Please create the Category and Product classes.")
        return
    if 'joinedload(' not in code:
        print("[PENDING] Make sure you use joinedload to fetch Categories and Products!")
        return

    print("[PASS] Capstone Project code detected!")
    print("\n[SUCCESS] YOU ARE A SQLALCHEMY MASTER! There are no more days left in the course!")

if __name__ == '__main__':
    test_day_19_interactive()
