-- Day 28 practice. Replace this query with a customer ranking query, save, and run:
-- python run_sql.py queries/day-28.sql
SELECT b.book_id,
       b.title,
       COUNT(r.review_id) AS review_count,
       COUNT(r.rating) AS rated_review_count,
       AVG(r.rating) AS average_rating
FROM books AS b
LEFT JOIN book_reviews AS r
    ON b.book_id = r.book_id
GROUP BY b.book_id, b.title
ORDER BY b.book_id;
