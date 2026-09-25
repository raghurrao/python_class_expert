-- Day 16 practice area. Replace this query with one assignment query, save, and run:
-- python run_sql.py queries/day-16.sql
SELECT strftime('%Y-%m', order_date) AS order_month,
       COUNT(*) AS order_count
FROM book_orders
GROUP BY strftime('%Y-%m', order_date)
ORDER BY order_month;
