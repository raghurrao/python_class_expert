-- Day 17 practice area. Replace this query with one assignment query, save, and run:
-- python run_sql.py queries/day-17.sql
WITH customer_orders AS (
    SELECT customer, COUNT(*) AS order_count
    FROM book_orders
    GROUP BY customer
)
SELECT customer, order_count,
       ROW_NUMBER() OVER (ORDER BY order_count DESC, customer) AS row_number,
       RANK() OVER (ORDER BY order_count DESC) AS rank_number,
       DENSE_RANK() OVER (ORDER BY order_count DESC) AS dense_rank_number
FROM customer_orders
ORDER BY order_count DESC, customer;
