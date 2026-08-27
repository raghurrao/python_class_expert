# Day 25: High-Performance Bulk Insertions (`executemany`)

Inserting records one-by-one with separate transaction commits is extremely slow ($O(N)$ disk I/O overhead). Data Engineers use batch insertions and single-transaction commits.

---

## 1. Batch Insertion Pattern

```python
records = [
    ("emp_101", 85000),
    ("emp_102", 92000),
    ("emp_103", 78000),
]

# Use executemany inside single transaction context
with conn:
    conn.executemany("INSERT INTO employees (name, salary) VALUES (?, ?)", records)
```

---

## 2. Hands-On Practical Exercise (Day 25)

Run `05_python_sql/day25_run.sh` to benchmark 10,000 row bulk insertion performance!
