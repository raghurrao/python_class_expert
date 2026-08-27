-- Day 16: CTEs and Recursive Sequences

-- 1. Standard CTE: Employees earning more than their department average
WITH dept_averages AS (
    SELECT 
        dept_id,
        AVG(salary) AS avg_dept_salary
    FROM employees
    WHERE dept_id IS NOT NULL
    GROUP BY dept_id
)
SELECT 
    e.first_name,
    e.salary,
    ROUND(da.avg_dept_salary, 2) AS dept_avg
FROM employees e
JOIN dept_averages da ON e.dept_id = da.dept_id
WHERE e.salary > da.avg_dept_salary;

-- 2. Recursive CTE: Generate a sequence of numbers (1 to 5)
WITH RECURSIVE cnt(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM cnt WHERE n < 5
)
SELECT n, n * 100 AS milestone FROM cnt;
