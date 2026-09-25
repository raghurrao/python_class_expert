-- Day 27 practice. Replace this query with another capstone summary, save, and run:
-- python run_sql.py queries/day-27.sql
SELECT SUBSTR(order_date, 1, 7) AS order_month,
       COUNT(*) AS order_count,
       SUM(estimated_line_total) AS estimated_revenue
FROM order_details
GROUP BY SUBSTR(order_date, 1, 7)
ORDER BY order_month;
