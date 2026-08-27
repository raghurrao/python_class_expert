#!/usr/bin/env python3
import sqlite3
import sys

def main():
    db_path = "/home/raghurao/Learnings/Learn SQL/02_sqlite/company.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("==================================================")
    print("    DAY 23: PYTHON SQLITE PARAMETERIZED QUERIES   ")
    print("==================================================")

    # 1. Parameterized Query (Safe against SQL Injection)
    search_dept_id = 1
    min_sal = 80000.0

    query = """
        SELECT emp_id, first_name, last_name, salary
        FROM employees
        WHERE dept_id = ? AND salary >= ?
        ORDER BY salary DESC;
    """

    cursor.execute(query, (search_dept_id, min_sal))
    rows = cursor.fetchall()

    print(f"[1] Query Results for Dept {search_dept_id} (Salary >= ${min_sal}):")
    for r in rows:
        print(f"    - ID: {r[0]} | {r[1]} {r[2]} | Salary: ${r[3]:,.2f}")

    conn.close()
    print("--------------------------------------------------")
    print("✅ DAY 23 EXERCISE COMPLETED SUCCESSFULLY!")
    print("==================================================")

if __name__ == "__main__":
    main()
