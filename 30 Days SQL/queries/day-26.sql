-- Day 26 capstone planning. Inspect the available analysis view and its grain.
-- Run with: python run_sql.py queries/day-26.sql
SELECT order_id, customer, order_date, title, quantity, estimated_line_total
FROM order_details
ORDER BY order_id;
