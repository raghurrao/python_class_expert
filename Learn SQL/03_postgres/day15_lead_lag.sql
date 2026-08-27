-- Day 15: Value Window Functions (LAG & Running Total)

SELECT 
    emp_id,
    first_name,
    salary,
    LAG(salary, 1, 0) OVER (ORDER BY salary ASC) AS prev_lower_salary,
    salary - LAG(salary, 1, salary) OVER (ORDER BY salary ASC) AS salary_diff,
    SUM(salary) OVER (ORDER BY salary ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_payroll
FROM employees;
