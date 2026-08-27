# Day 24: Python DataFrames & SQL Integration

Data Engineers use DataFrames (`pandas`, `polars`) to bridge relational database tables with analytical processing libraries.

---

## 1. Reading & Writing SQL Data with Python DataFrames

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect("company.db")

# Read SQL query directly into DataFrame
df = pd.read_sql_query("SELECT * FROM employees WHERE salary > 80000", conn)

# Write DataFrame directly to a database table
df.to_sql("high_earners_summary", conn, if_exists="replace", index=False)
```

---

## 2. Hands-On Practical Exercise (Day 24)

Run `05_python_sql/day24_run.sh` to extract SQL records and transform them in Python!
