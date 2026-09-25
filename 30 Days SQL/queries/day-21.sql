-- Day 21 practice area. Replace this query with one mini-project query, save, and run:
-- python run_sql.py queries/day-21.sql
SELECT strftime('%Y-%m', o.order_date) AS order_month,
       SUM(o.quantity * b.price) AS estimated_revenue
FROM book_orders AS o
INNER JOIN books AS b
    ON o.book_id = b.book_id
GROUP BY strftime('%Y-%m', o.order_date)
ORDER BY order_month;
