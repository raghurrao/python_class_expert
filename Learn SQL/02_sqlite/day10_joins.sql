-- Day 10: Relational Joins Queries

-- 1. INNER JOIN (Matching Employees and Departments)
SELECT 
    e.emp_id,
    e.first_name || ' ' || e.last_name AS employee_name,
    d.dept_name,
    d.location
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- 2. LEFT JOIN (Includes unassigned employees like George)
SELECT 
    e.first_name || ' ' || e.last_name AS employee_name,
    COALESCE(d.dept_name, 'Unassigned') AS department_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;
