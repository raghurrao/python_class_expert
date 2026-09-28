-- Representative answer key: adapt predicates to stated conditions.
SELECT s.student_id,s.first_name,d.name FROM students s LEFT JOIN departments d USING(department_id);
SELECT * FROM enrollments WHERE grade IS NULL;
SELECT status,COUNT(*) FROM orders GROUP BY status;
SELECT s.student_id,COUNT(e.enrollment_id) n FROM students s LEFT JOIN enrollments e USING(student_id) GROUP BY s.student_id ORDER BY n DESC;
WITH x AS (SELECT * FROM orders) SELECT status,COUNT(*) FROM x GROUP BY status;
CREATE INDEX IF NOT EXISTS idx_students_email ON students(email);
EXPLAIN QUERY PLAN SELECT * FROM students WHERE email='s001@example.edu';
BEGIN; UPDATE enrollments SET grade=grade WHERE enrollment_id=1; ROLLBACK;
SELECT student_id,ROW_NUMBER() OVER(ORDER BY student_id) AS rn FROM students;
