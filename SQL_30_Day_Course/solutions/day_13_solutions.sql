-- Day 13: solutions and rationale
-- These reference the stable shared sample data.

-- Exercise 1: Example solution pattern; adapt selected columns/predicate to the prompt.
SELECT student_id, first_name, last_name FROM students ORDER BY student_id LIMIT 5;

-- Exercise 2: Example solution pattern; adapt selected columns/predicate to the prompt.
SELECT * FROM courses WHERE credits >= 3 LIMIT 5;

-- Exercise 3: Example solution pattern; adapt selected columns/predicate to the prompt.
SELECT s.first_name, c.title FROM students AS s JOIN enrollments AS e ON e.student_id=s.student_id JOIN courses AS c ON c.course_id=e.course_id LIMIT 5;

-- Exercise 4: Example solution pattern; adapt selected columns/predicate to the prompt.
SELECT department_id, COUNT(*) AS row_count FROM courses GROUP BY department_id ORDER BY row_count DESC;

-- Exercise 5: Example solution pattern; adapt selected columns/predicate to the prompt.
SELECT o.status, COUNT(*) AS orders FROM orders AS o GROUP BY o.status ORDER BY o.status;

-- Exercise 6: Example solution pattern; adapt selected columns/predicate to the prompt.
SELECT student_id, first_name, last_name FROM students ORDER BY student_id LIMIT 5;

-- Exercise 7: Example solution pattern; adapt selected columns/predicate to the prompt.
SELECT * FROM courses WHERE credits >= 3 LIMIT 5;

-- Exercise 8: Example solution pattern; adapt selected columns/predicate to the prompt.
SELECT s.first_name, c.title FROM students AS s JOIN enrollments AS e ON e.student_id=s.student_id JOIN courses AS c ON c.course_id=e.course_id LIMIT 5;

-- Exercise 9: Example solution pattern; adapt selected columns/predicate to the prompt.
SELECT department_id, COUNT(*) AS row_count FROM courses GROUP BY department_id ORDER BY row_count DESC;

-- Exercise 10: Example solution pattern; adapt selected columns/predicate to the prompt.
SELECT o.status, COUNT(*) AS orders FROM orders AS o GROUP BY o.status ORDER BY o.status;

-- Exercise 11: Example solution pattern; adapt selected columns/predicate to the prompt.
SELECT student_id, first_name, last_name FROM students ORDER BY student_id LIMIT 5;

-- Exercise 12: Example solution pattern; adapt selected columns/predicate to the prompt.
SELECT * FROM courses WHERE credits >= 3 LIMIT 5;

-- Exercise 13: Example solution pattern; adapt selected columns/predicate to the prompt.
SELECT s.first_name, c.title FROM students AS s JOIN enrollments AS e ON e.student_id=s.student_id JOIN courses AS c ON c.course_id=e.course_id LIMIT 5;

-- Exercise 14: Example solution pattern; adapt selected columns/predicate to the prompt.
SELECT department_id, COUNT(*) AS row_count FROM courses GROUP BY department_id ORDER BY row_count DESC;

-- Exercise 15: Example solution pattern; adapt selected columns/predicate to the prompt.
SELECT o.status, COUNT(*) AS orders FROM orders AS o GROUP BY o.status ORDER BY o.status;

-- Debug A: SELECT first_name, last_name FROM students;
-- Debug B: SELECT * FROM enrollments WHERE grade IS NULL;
-- Debug C: SELECT department_id, COUNT(*) FROM courses GROUP BY department_id;
