-- Day 29 capstone report and reconciliation.
-- Run with: python run_sql.py queries/day-29.sql

-- Monthly performance: one row per month.
SELECT SUBSTR(order_date, 1, 7) AS order_month,
       COUNT(*) AS order_count,
       SUM(estimated_line_total) AS estimated_revenue
FROM order_details
GROUP BY SUBSTR(order_date, 1, 7)
ORDER BY order_month;

-- Customer ranking: one row per customer.
WITH customer_totals AS (
    SELECT customer,
           COUNT(*) AS order_count,
           SUM(quantity) AS units_ordered,
           SUM(estimated_line_total) AS estimated_revenue
    FROM order_details
    GROUP BY customer
)
SELECT customer, order_count, units_ordered, estimated_revenue,
       RANK() OVER (ORDER BY units_ordered DESC) AS quantity_rank
FROM customer_totals
ORDER BY quantity_rank, customer;

-- Book performance: one row per book, retaining books without orders.
SELECT b.book_id, b.title,
       COUNT(o.order_id) AS order_count,
       COALESCE(SUM(o.quantity), 0) AS units_ordered,
       COALESCE(SUM(o.quantity * b.price), 0) AS estimated_revenue
FROM books AS b
LEFT JOIN book_orders AS o
    ON b.book_id = o.book_id
GROUP BY b.book_id, b.title
ORDER BY estimated_revenue DESC;

-- Review coverage: one row per book.
SELECT b.book_id, b.title,
       COUNT(r.review_id) AS review_count,
       COUNT(r.rating) AS rated_review_count,
       AVG(r.rating) AS average_rating
FROM books AS b
LEFT JOIN book_reviews AS r
    ON b.book_id = r.book_id
GROUP BY b.book_id, b.title
ORDER BY b.book_id;

-- Reconcile estimated revenue across different groupings.
WITH monthly AS (
    SELECT SUBSTR(order_date, 1, 7) AS period,
           SUM(estimated_line_total) AS revenue
    FROM order_details GROUP BY SUBSTR(order_date, 1, 7)
), customer AS (
    SELECT customer AS period,
           SUM(estimated_line_total) AS revenue
    FROM order_details GROUP BY customer
), book AS (
    SELECT b.book_id AS period,
           SUM(o.quantity * b.price) AS revenue
    FROM books AS b INNER JOIN book_orders AS o ON b.book_id = o.book_id
    GROUP BY b.book_id
), author AS (
    SELECT b.author AS period,
           SUM(o.quantity * b.price) AS revenue
    FROM books AS b INNER JOIN book_orders AS o ON b.book_id = o.book_id
    GROUP BY b.author
)
SELECT (SELECT SUM(revenue) FROM monthly) AS monthly_total,
       (SELECT SUM(revenue) FROM customer) AS customer_total,
       (SELECT SUM(revenue) FROM book) AS book_total,
       (SELECT SUM(revenue) FROM author) AS author_total;
