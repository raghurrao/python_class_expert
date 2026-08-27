-- Day 11: Subqueries & Set Operations

-- 1. Employees earning above company average salary
SELECT first_name, last_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- 2. Departments that currently have assigned employees (EXISTS)
SELECT dept_id, dept_name
FROM departments d
WHERE EXISTS (
    SELECT 1 FROM employees e WHERE e.dept_id = d.dept_id
);

-- 3. EXCEPT: Departments with NO assigned employees
SELECT dept_id, dept_name FROM departments
EXCEPT
SELECT d.dept_id, d.dept_name FROM departments d JOIN employees e ON d.dept_id = e.dept_id;
