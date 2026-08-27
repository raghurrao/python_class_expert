#!/usr/bin/env python3
import sqlite3
import sys

class DatabaseClient:
    def __init__(self, db_path):
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def fetch_all(self, sql, params=()):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            cols = [d[0] for d in cursor.description] if cursor.description else []
            return cols, cursor.fetchall()

    def execute(self, sql, params=()):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount

def main():
    db_path = "/home/raghurao/Learnings/Learn SQL/05_python_sql/modular_app.db"
    db = DatabaseClient(db_path)

    print("==================================================")
    print("    DAY 26: MODULAR PYTHON DB CLIENT PATTERNS     ")
    print("==================================================")

    # Apply Migration
    db.execute("DROP TABLE IF EXISTS audit_logs;")
    db.execute("""
        CREATE TABLE audit_logs (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)

    db.execute("INSERT INTO audit_logs (action) VALUES (?), (?);", ("USER_LOGIN", "DATA_EXPORT"))

    cols, rows = db.fetch_all("SELECT * FROM audit_logs;")

    print(f"[1] Executed Query via DB Client Layer (Cols: {cols}):")
    for r in rows:
        print(f"    - Log #{r[0]}: Action='{r[1]}' | Timestamp={r[2]}")

    print("--------------------------------------------------")
    print("✅ DAY 26 EXERCISE COMPLETED SUCCESSFULLY!")
    print("==================================================")

if __name__ == "__main__":
    main()
