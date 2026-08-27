-- Day 9: Aggregations and Grouping Queries

-- Overall Salary Metrics
SELECT 
    COUNT(*) AS total_staff,
    SUM(salary) AS total_payroll,
    ROUND(AVG(salary), 2) AS avg_salary,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary
FROM employees;

-- Department Payroll & Headcount Summary
SELECT 
    dept_id,
    COUNT(*) AS emp_count,
    ROUND(AVG(salary), 2) AS dept_avg_salary
FROM employees
WHERE dept_id IS NOT NULL
GROUP BY dept_id
HAVING emp_count >= 2
ORDER BY dept_avg_salary DESC;
