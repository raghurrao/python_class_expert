-- Day 20 safe practice: each change is rolled back before the script ends.
-- Run with: python run_sql.py queries/day-20.sql
BEGIN;

INSERT INTO books (book_id, title, author, price, in_stock)
VALUES (5, 'A SQL Journey', 'Nia Park', 21.00, TRUE);
SELECT book_id, title, author, price FROM books WHERE book_id = 5;

UPDATE books
SET price = 22.00
WHERE book_id = 5;
SELECT book_id, title, price FROM books WHERE book_id = 5;

DELETE FROM books
WHERE book_id = 5;
SELECT book_id, title FROM books WHERE book_id = 5;

ROLLBACK;

SELECT COUNT(*) AS books_after_rollback FROM books;
