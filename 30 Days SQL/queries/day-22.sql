-- Day 22 demo: schema and rows exist only inside this transaction and are rolled back.
-- Run with: python run_sql.py queries/day-22.sql
BEGIN;

CREATE TABLE day22_authors (
    author_id INTEGER PRIMARY KEY,
    name      TEXT NOT NULL UNIQUE
);

CREATE TABLE day22_books (
    book_id   INTEGER PRIMARY KEY,
    title     TEXT NOT NULL,
    author_id INTEGER NOT NULL REFERENCES day22_authors(author_id),
    price     NUMERIC NOT NULL CHECK (price >= 0)
);

INSERT INTO day22_authors (author_id, name) VALUES
    (1, 'Nia Park'),
    (2, 'Dev Rao');

INSERT INTO day22_books (book_id, title, author_id, price) VALUES
    (1, 'A SQL Journey', 1, 21.00),
    (2, 'Relational Thinking', 2, 18.00);

SELECT b.title, a.name AS author, b.price
FROM day22_books AS b
INNER JOIN day22_authors AS a
    ON b.author_id = a.author_id
ORDER BY b.book_id;

ROLLBACK;
