import os
import re

def test_day_12_interactive():
    py_file = 'day_12_answers.py'

    if not os.path.exists(py_file):
        print(f"[ERROR] {py_file} not found.")
        return

    with open(py_file, 'r', encoding='utf-8') as f:
        code = f.read()

    print("--- Running Day 12 Interactive Tests ---\n")

    if not re.search(r'class\s+Author\(Base\):', code):
        print("[PENDING] Task 1: Create a class named Author that inherits from Base.")
        return
    if '__tablename__' not in code:
        print("[PENDING] Task 1: Don't forget __tablename__ = 'authors'.")
        return
    if 'Mapped[int]' not in code or 'mapped_column(primary_key=True)' not in code:
        print("[PENDING] Task 1: Define the id column using Mapped and mapped_column.")
        return
    print("[PASS] Task 1: Declarative class Author created!")

    if 'Session(engine)' not in code:
        print("[PENDING] Task 2: Open a with Session(engine) as session: block.")
        return
    if 'session.add(' not in code:
        print("[PENDING] Task 2: Use session.add() to add your new Author object.")
        return
    print("[PASS] Task 2: Session created and object added!")

    print("\n[SUCCESS] FANTASTIC! You are now using the SQLAlchemy ORM!")

if __name__ == '__main__':
    test_day_12_interactive()
