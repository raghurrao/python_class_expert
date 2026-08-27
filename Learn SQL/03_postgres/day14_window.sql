-- Day 14: Window Ranking Queries

SELECT 
    e.first_name || ' ' || e.last_name AS employee_name,
    COALESCE(d.dept_name, 'Unassigned') AS dept_name,
    e.salary,
    ROW_NUMBER() OVER (PARTITION BY e.dept_id ORDER BY e.salary DESC) AS row_num,
    DENSE_RANK() OVER (ORDER BY e.salary DESC) AS global_salary_rank
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;
