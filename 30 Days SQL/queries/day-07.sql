-- Day 7 practice area. Replace this query with one assignment query, save, and run:
-- python run_sql.py queries/day-07.sql
SELECT author, COUNT(*) AS book_count
FROM books
GROUP BY author;
