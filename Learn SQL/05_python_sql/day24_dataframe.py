#!/usr/bin/env python3
import sqlite3

def main():
    db_path = "/home/raghurao/Learnings/Learn SQL/02_sqlite/company.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("==================================================")
    print("    DAY 24: PYTHON DATAFRAME & SQL INTEGRATION    ")
    print("==================================================")

    # Fetch records and perform tabular aggregation in Python
    query = """
        SELECT e.first_name, e.last_name, e.salary, COALESCE(d.dept_name, 'Unassigned') AS department
        FROM employees e
        LEFT JOIN departments d ON e.dept_id = d.dept_id;
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    cols = [desc[0] for desc in cursor.description]

    print(f"[1] Loaded {len(rows)} records from SQL Database.")
    print(f"    Columns: {cols}")

    dept_salaries = {}
    for r in rows:
        dept = r[3]
        sal = r[2]
        dept_salaries[dept] = dept_salaries.get(dept, 0) + sal

    print("\n[2] Department Total Payroll Aggregated in Python:")
    for dept, total in dept_salaries.items():
        print(f"    - {dept:<15}: ${total:,.2f}")

    conn.close()
    print("--------------------------------------------------")
    print("✅ DAY 24 EXERCISE COMPLETED SUCCESSFULLY!")
    print("==================================================")

if __name__ == "__main__":
    main()
