# Day 26: Building Modular Database Access Layers & Schema Migrations

Production applications use decoupled Database Access Objects (DAO) / Clients to encapsulate connections, query execution, logging, and automated migrations.

---

## 1. Modular Database Client Pattern

```python
class DatabaseClient:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def execute_query(self, sql, params=()):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            if cursor.description:
                return cursor.fetchall()
            return cursor.rowcount
```

---

## 2. Hands-On Practical Exercise (Day 26)

Run `05_python_sql/day26_run.sh` to run the modular database client and migration runner!
