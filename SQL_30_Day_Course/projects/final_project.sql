PRAGMA foreign_keys=ON;
-- Course counts, retaining zero-enrollment courses
WITH course_counts AS (
 SELECT c.course_id,c.title,c.department_id,COUNT(e.enrollment_id) AS enrollment_count
 FROM courses c LEFT JOIN enrollments e ON e.course_id=c.course_id
 GROUP BY c.course_id,c.title,c.department_id
)
SELECT d.name AS department,cc.title,cc.enrollment_count,
 DENSE_RANK() OVER(PARTITION BY cc.department_id ORDER BY cc.enrollment_count DESC) AS popularity_rank
FROM course_counts cc JOIN departments d ON d.department_id=cc.department_id
ORDER BY department,popularity_rank,cc.title;
-- Students without enrollments
SELECT s.student_id,s.first_name,s.last_name FROM students s
WHERE NOT EXISTS(SELECT 1 FROM enrollments e WHERE e.student_id=s.student_id);
-- Safe write demonstration; no lasting mutation
BEGIN; INSERT INTO students(first_name,last_name,email,enrollment_date,department_id) VALUES('Demo','Learner','demo.rollback@example.edu','2026-09-01',1); ROLLBACK;
CREATE INDEX IF NOT EXISTS idx_enrollments_term_course ON enrollments(term,course_id);
EXPLAIN QUERY PLAN SELECT * FROM enrollments WHERE term='2026-Fall' AND course_id=1;
