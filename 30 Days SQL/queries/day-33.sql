-- Day 33 safe transaction demo: all changes are rolled back.
-- Run with: python run_sql.py queries/day-33.sql
BEGIN;

UPDATE books
SET price = 20.00
WHERE book_id = 1;
SELECT price AS after_first_update FROM books WHERE book_id = 1;

SAVEPOINT after_first_change;

UPDATE books
SET price = 99.00
WHERE book_id = 1;
SELECT price AS after_second_update FROM books WHERE book_id = 1;

ROLLBACK TO after_first_change;
SELECT price AS after_rollback_to_savepoint FROM books WHERE book_id = 1;

ROLLBACK;
SELECT price AS original_price_restored FROM books WHERE book_id = 1;
