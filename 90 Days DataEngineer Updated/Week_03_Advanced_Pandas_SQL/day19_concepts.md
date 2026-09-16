# Day 19: Advanced SQL CTEs & Windows

Today we cover advanced SQL features that are crucial for modern data engineering and analytics: Common Table Expressions (CTEs) and Window Functions.

---

## 1. Why Advanced SQL?
While simple `SELECT` and `GROUP BY` queries can take you far, complex analytical logic (like calculating a running total, or finding the top 3 selling products per category) becomes extremely messy if written with nested subqueries. CTEs and Window Functions make complex logic readable, modular, and performant.

---

## 2. Core Concepts & Operations

### Common Table Expressions (CTEs)
A CTE is a temporary, named result set that you can reference within a `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement. It acts like a temporary view that only exists for the duration of that query.

**Syntax:** `WITH cte_name AS ( query )`

```sql
-- Without CTE (Nested subquery - hard to read)
SELECT * FROM (
    SELECT customer_id, SUM(amount) as total 
    FROM orders 
    GROUP BY customer_id
) WHERE total > 1000;

-- With CTE (Clean and modular)
WITH CustomerTotals AS (
    SELECT customer_id, SUM(amount) as total
    FROM orders
    GROUP BY customer_id
)
SELECT * FROM CustomerTotals WHERE total > 1000;
```

### Window Functions
Window functions perform calculations across a set of table rows that are somehow related to the current row. **Crucially, unlike aggregate functions (`GROUP BY`), window functions do NOT cause rows to become grouped into a single output row.** The rows retain their separate identities.

**Syntax:** `function_name() OVER (PARTITION BY col1 ORDER BY col2)`

```sql
-- 1. Running Total
-- Calculates the cumulative sum of sales ordered by date
SELECT 
    date,
    daily_sales,
    SUM(daily_sales) OVER (ORDER BY date) as running_total
FROM sales;

-- 2. Ranking within Categories
-- Assigns a rank to employees based on salary, resetting for each department
SELECT 
    name,
    department,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dept_rank
FROM employees;

-- 3. Getting the "Previous" Row's Value
-- LAG() fetches the value from the previous row (useful for week-over-week growth)
SELECT
    date,
    revenue,
    LAG(revenue, 1) OVER (ORDER BY date) as previous_day_revenue
FROM daily_metrics;
```

---

## 3. Reference Documentation
* [SQLite Window Functions](https://www.sqlite.org/windowfunctions.html)
* [SQLite CTEs (WITH clause)](https://www.sqlite.org/lang_with.html)
