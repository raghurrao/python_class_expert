-- Day 34: compare plans for equivalent month filters.
-- Run with: python run_sql.py queries/day-34.sql
EXPLAIN QUERY PLAN
SELECT order_id, order_date
FROM book_orders
WHERE order_date >= '2026-02-01'
  AND order_date <  '2026-03-01';

EXPLAIN QUERY PLAN
SELECT order_id, order_date
FROM book_orders
WHERE SUBSTR(order_date, 1, 7) = '2026-02';
