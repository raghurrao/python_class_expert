-- Day 8: Data Retrieval Queries

-- Query 1: Filter high earners (salary >= 90000) sorted descending
SELECT emp_id, first_name || ' ' || last_name AS full_name, salary
FROM employees
WHERE salary >= 90000
ORDER BY salary DESC;

-- Query 2: Wildcard pattern matching (email ending with '@company.com')
SELECT first_name, email
FROM employees
WHERE email LIKE '%company.com';

-- Query 3: Handling NULL values with COALESCE
SELECT first_name, last_name, COALESCE(dept_id, 0) AS department_code
FROM employees;

-- Query 4: Pagination (Top 3 highest salaries)
SELECT first_name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3 OFFSET 0;
