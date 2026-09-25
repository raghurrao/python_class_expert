import os
import re

def test_day_17_interactive():
    env_file = os.path.join('alembic', 'env.py')

    if not os.path.exists(env_file):
        print(f"[ERROR] {env_file} not found.")
        return

    with open(env_file, 'r', encoding='utf-8') as f:
        code = f.read()

    print("--- Running Day 17 Interactive Tests ---\n")

    if not re.search(r'from\s+models\s+import\s+Base', code):
        print("[PENDING] Task 1: Make sure to import Base from models in env.py.")
        return
    if not re.search(r'target_metadata\s*=\s*Base\.metadata', code):
        print("[PENDING] Task 1: Set target_metadata = Base.metadata in env.py.")
        return
        
    print("[PASS] Task 1: Alembic env.py configured to read your SQLAlchemy classes!")
    print("\n[SUCCESS] PERFECT! Alembic is now fully wired up to your code.")
    print("In the next lesson, we will actually run the migration!")

if __name__ == '__main__':
    test_day_17_interactive()
