# Day 18: Performance & Indexing Strategies

Indexes are B-tree data structures that accelerate table lookups from $O(N)$ full table scans to $O(\log N)$ index searches.

---

## 1. Index Types & Trade-Offs

- **B-Tree Index**: Default index for equality (`=`) and range comparison (`>`, `<`, `BETWEEN`).
- **Composite Index**: Multi-column index on `(col1, col2)`.
- **Unique Index**: Enforces uniqueness constraint while indexing.

> [!WARNING]
> Indexes accelerate reads (`SELECT`) but add overhead to writes (`INSERT`, `UPDATE`, `DELETE`) because index structures must be maintained.

---

## 2. Analyzing Query Plans (`EXPLAIN QUERY PLAN`)

```sql
EXPLAIN QUERY PLAN
SELECT * FROM employees WHERE email = 'alice@company.com';
```

---

## 3. Hands-On Practical Exercise (Day 18)

Run `03_postgres/day18_run.sh` to measure the difference before and after indexing!
