-- Day 18 practice area. Replace this query with one assignment query, save, and run:
-- python run_sql.py queries/day-18.sql
SELECT order_id, order_date, customer, quantity,
       SUM(quantity) OVER (
           ORDER BY order_date, order_id
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_quantity
FROM book_orders
ORDER BY order_date, order_id;
