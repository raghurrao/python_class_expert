-- Day 12 practice area. Replace this query with one assignment query, save, and run:
-- python run_sql.py queries/day-12.sql
SELECT title, price
FROM books
WHERE price > (
    SELECT AVG(price)
    FROM books
);
