-- Day 35 practice: calculate a label, then filter the named CTE result.
-- Run with: python run_sql.py queries/day-35.sql
WITH book_labels AS (
    SELECT title, price,
           CASE WHEN price >= 25 THEN 'Premium' ELSE 'Other' END AS price_band
    FROM books
)
SELECT title, price, price_band
FROM book_labels
WHERE price_band = 'Premium';
