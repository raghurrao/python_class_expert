# Day 6: SQLite CLI & DDL (Data Definition Language)

Welcome to **Module 2: SQLite & Relational Core**!

SQLite is an embedded, serverless, self-contained relational database engine. In Linux environments, database files (`.db`) can be queried using the `sqlite3` CLI tool.

---

## 1. SQLite Data Types

SQLite uses **Dynamic Type Affinity**:
- `INTEGER`: Signed integer (1, 2, 4, 8 bytes).
- `REAL`: 8-byte floating point numbers.
- `TEXT`: UTF-8 encoded text string.
- `BLOB`: Binary Large Object (stored exactly as input).
- `NULL`: Represents missing or unknown data.

---

## 2. Key DDL Statements

### Create Table with Constraints:
```sql
CREATE TABLE IF NOT EXISTS departments (
    dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dept_name TEXT NOT NULL UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    salary REAL CHECK (salary > 0),
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

---

## 3. Hands-On Practical Exercise (Day 6)

Run `02_sqlite/day6_run.sh` to initialize your first database `company.db`!
