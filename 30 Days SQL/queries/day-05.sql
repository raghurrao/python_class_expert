-- Day 5 practice area. Replace this query with one assignment query, save, and run:
-- python run_sql.py queries/day-05.sql
SELECT customer, order_date
FROM book_orders
WHERE order_date >= '2026-02-01'
  AND order_date <  '2026-03-01';
