-- Day 24 practice: inspect indexes, then inspect a query plan.
-- Run with: python run_sql.py queries/day-24.sql
PRAGMA index_list(book_orders);

EXPLAIN QUERY PLAN
SELECT order_id, order_date
FROM book_orders
WHERE book_id = 1;
