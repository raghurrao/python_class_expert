# Day 23: Python `sqlite3` & Parameterized Queries

Python provides native database connectivity through DB-API 2.0 (`sqlite3`, `psycopg2`, `sqlite-utils`).

---

## 1. Preventing SQL Injection with Parameterized Queries

> [!CAUTION]
> **NEVER** format SQL strings using f-strings or string concatenation with untrusted input!
> `cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")` -> **SQL INJECTION RISK!**

### Safe Parameterized Pattern:
```python
# Pass tuple or list of values as second argument
cursor.execute("SELECT * FROM users WHERE username = ? AND status = ?", (username, status))
```

---

## 2. Hands-On Practical Exercise (Day 23)

Run `05_python_sql/day23_run.sh` to run parameterized queries in Python!
