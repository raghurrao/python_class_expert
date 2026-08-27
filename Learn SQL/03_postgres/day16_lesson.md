# Day 16: Common Table Expressions (CTEs) & Recursive SQL

Common Table Expressions (CTEs) define temporary named result sets using the `WITH` clause to simplify modular query logic.

---

## 1. Standard CTE Syntax

```sql
WITH dept_stats AS (
    SELECT dept_id, AVG(salary) AS avg_sal
    FROM employees
    GROUP BY dept_id
)
SELECT e.first_name, e.salary, ds.avg_sal
FROM employees e
JOIN dept_stats ds ON e.dept_id = ds.dept_id
WHERE e.salary > ds.avg_sal;
```

---

## 2. Recursive CTE (`WITH RECURSIVE`)

Generates hierarchical data structures (organisational trees, category trees, graphs).

---

## 3. Hands-On Practical Exercise (Day 16)

Run `03_postgres/day16_run.sh` to run standard and recursive CTEs!
