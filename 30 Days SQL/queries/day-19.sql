-- Day 19 practice area. Replace this query with one assignment query, save, and run:
-- python run_sql.py queries/day-19.sql
WITH ranked_books AS (
    SELECT book_id, author, title, price,
           ROW_NUMBER() OVER (
               PARTITION BY author
               ORDER BY price DESC, book_id
           ) AS row_num
    FROM books
)
SELECT author, title, price
FROM ranked_books
WHERE row_num = 1
ORDER BY author;
