-- Day 14 practice area. Replace this query with one assignment query, save, and run:
-- python run_sql.py queries/day-14.sql
WITH book_counts AS (
    SELECT author, COUNT(*) AS book_count
    FROM books
    GROUP BY author
)
SELECT author, book_count
FROM book_counts
ORDER BY author;
