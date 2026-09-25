-- Day 13 practice area. Replace this query with one assignment query, save, and run:
-- python run_sql.py queries/day-13.sql
SELECT b.title
FROM books AS b
WHERE EXISTS (
    SELECT 1
    FROM book_reviews AS r
    WHERE r.book_id = b.book_id
      AND r.rating = 5
);
