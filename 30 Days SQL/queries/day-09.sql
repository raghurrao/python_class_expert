-- Day 9 practice area. Replace this query with one assignment query, save, and run:
-- python run_sql.py queries/day-09.sql
SELECT o.order_id, o.order_date, o.customer, b.title
FROM book_orders AS o
INNER JOIN books AS b
    ON o.book_id = b.book_id
ORDER BY o.order_id;
