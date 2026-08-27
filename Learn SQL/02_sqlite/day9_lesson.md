# Day 9: Grouping & Aggregations (`GROUP BY`, `HAVING`)

SQL Aggregate functions operate across multiple rows to return a single summary value.

---

## 1. Aggregate Functions & Syntax

- `COUNT(*)`: Total row count.
- `COUNT(col)`: Non-null count of column values.
- `SUM(col)`, `AVG(col)`: Total sum and arithmetic mean.
- `MIN(col)`, `MAX(col)`: Minimum and maximum values.

### The SQL Logical Order of Operations:
1. `FROM`
2. `WHERE` (filters individual rows *before* grouping)
3. `GROUP BY` (groups rows sharing identical column values)
4. `HAVING` (filters summary groups *after* aggregation)
5. `SELECT`
6. `ORDER BY`

---

## 2. Hands-On Practical Exercise (Day 9)

Run `02_sqlite/day9_run.sh` to run summary metrics and group queries!
