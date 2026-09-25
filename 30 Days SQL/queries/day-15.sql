-- Day 15 practice area. Replace this query with one assignment query, save, and run:
-- python run_sql.py queries/day-15.sql
SELECT author AS person_name
FROM books
UNION
SELECT reviewer AS person_name
FROM book_reviews
ORDER BY person_name;
