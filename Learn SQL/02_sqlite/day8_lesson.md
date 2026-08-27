# Day 8: Querying & Filtering Fundamentals (DQL)

Data Query Language (DQL) allows retrieving and filtering database records.

---

## 1. Key Filtering Clauses

- `WHERE`: Filter rows based on conditions.
- `LIKE`: Pattern matching (`%` = 0 or more chars, `_` = 1 char).
- `BETWEEN a AND b`: Inclusive range comparison.
- `IN (val1, val2)`: Value list inclusion.
- `IS NULL` / `IS NOT NULL`: Null value check.
- `COALESCE(val1, val2)`: Return first non-null argument.
- `ORDER BY col [ASC|DESC]`: Sorting results.
- `LIMIT n OFFSET m`: Pagination.

---

## 2. Hands-On Practical Exercise (Day 8)

Run `02_sqlite/day8_run.sh` to run DQL query suites!
