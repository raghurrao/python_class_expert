# Day 14: Window Functions (Part 1: Ranking Functions)

Unlike `GROUP BY` which collapses rows, **Window Functions** compute values across a set of table rows while preserving individual row details.

---

## 1. Ranking Window Functions

- `ROW_NUMBER()`: Unique sequential integer assigned to each row within partition.
- `RANK()`: Rank assigned with gaps for tied values (e.g. 1, 2, 2, 4).
- `DENSE_RANK()`: Rank assigned without gaps for tied values (e.g. 1, 2, 2, 3).

### Syntax:
```sql
SELECT 
    emp_id,
    dept_id,
    salary,
    ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS dept_rank
FROM employees;
```

---

## 2. Hands-On Practical Exercise (Day 14)

Run `03_postgres/day14_run.sh` to rank employees within departments!
