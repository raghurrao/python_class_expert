-- Day 23 practice: create a reusable view, then query it.
-- Run with: python run_sql.py queries/day-23.sql
CREATE VIEW IF NOT EXISTS in_stock_books AS
SELECT book_id, title, author, price
FROM books
WHERE in_stock = TRUE;

SELECT title, price
FROM in_stock_books
ORDER BY price DESC;
