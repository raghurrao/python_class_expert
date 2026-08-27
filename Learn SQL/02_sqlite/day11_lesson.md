# Day 11: Subqueries & Set Operations

Subqueries embed queries within queries. Set operations combine query result sets vertically.

---

## 1. Subquery Types

- **Scalar Subquery**: Returns single value (e.g. `salary > (SELECT AVG(salary) FROM employees)`).
- **Correlated Subquery**: References outer query columns per row iteration.
- **`EXISTS` / `NOT EXISTS`**: Tests for existence of matching rows.

---

## 2. Set Operations

- `UNION`: Combines results, removing duplicates.
- `UNION ALL`: Combines results including duplicates (fastest).
- `INTERSECT`: Returns rows present in both queries.
- `EXCEPT`: Returns rows in first query but absent in second query.

---

## 3. Hands-On Practical Exercise (Day 11)

Run `02_sqlite/day11_run.sh` to run advanced subqueries and set operations!
