# Day 18: SQL Aggregations & Grouping

Just like Pandas has `groupby` and `agg`, SQL provides powerful built-in aggregation functions and grouping clauses. This allows you to push computation down to the database level, which is often much faster and more memory-efficient than doing it in Pandas.

---

## 1. Why Push Computation to SQL?
If you have a 100GB table, pulling it all into Pandas to calculate a single average will crash your machine. SQL can calculate the average on the database server and only return the single number to Python.

---

## 2. Core Concepts & Operations

### Aggregate Functions
SQL provides several built-in functions that operate on multiple rows to return a single value.

* **`COUNT()`**: Returns the number of rows.
* **`SUM()`**: Returns the total sum of a numeric column.
* **`AVG()`**: Returns the average value of a numeric column.
* **`MIN()`**: Returns the smallest value.
* **`MAX()`**: Returns the largest value.

```sql
-- Count all rows in the orders table
SELECT COUNT(*) FROM orders;

-- Find the maximum order amount
SELECT MAX(amount) FROM orders;

-- Calculate total revenue
SELECT SUM(amount) AS total_revenue FROM orders;
```

### GROUP BY
The `GROUP BY` statement groups rows that have the same values into summary rows. It is often used with aggregate functions to group the result-set by one or more columns.

```sql
-- Total sales per customer
SELECT customer_id, SUM(amount) AS total_spent
FROM orders
GROUP BY customer_id;

-- Number of employees in each department
SELECT department, COUNT(*) AS num_employees
FROM employees
GROUP BY department;
```

### HAVING
The `WHERE` clause cannot be used with aggregate functions. The `HAVING` clause was added to SQL specifically to filter records *after* they have been grouped and aggregated.

```sql
-- Find customers who have spent more than $1000 in total
SELECT customer_id, SUM(amount) AS total_spent
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 1000;
-- Notice how WHERE wouldn't work here because SUM(amount) is computed AFTER grouping.
```

---

## 3. Reference Documentation
* [SQLite Aggregate Functions](https://www.sqlite.org/lang_aggfunc.html)
* [SQL GROUP BY Statement (W3Schools)](https://www.w3schools.com/sql/sql_groupby.asp)
