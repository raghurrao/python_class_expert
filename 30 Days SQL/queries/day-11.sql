-- Day 11 practice area. Replace this query with one assignment query, save, and run:
-- python run_sql.py queries/day-11.sql
SELECT title, price,
       CASE
           WHEN price >= 25 THEN 'Premium'
           WHEN price >= 15 THEN 'Standard'
           ELSE 'Budget'
       END AS price_band
FROM books;
