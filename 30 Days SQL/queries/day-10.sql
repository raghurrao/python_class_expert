-- Day 10 practice area. Replace this query with one assignment query, save, and run:
-- python run_sql.py queries/day-10.sql
SELECT b.title, o.order_id, r.reviewer
FROM books AS b
INNER JOIN book_orders AS o
    ON b.book_id = o.book_id
INNER JOIN book_reviews AS r
    ON b.book_id = r.book_id
ORDER BY b.book_id, o.order_id, r.review_id;
