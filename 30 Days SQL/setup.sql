-- Rebuild all practice tables and their sample data.
PRAGMA foreign_keys = ON;
DROP VIEW IF EXISTS order_details;
DROP TABLE IF EXISTS book_reviews;
DROP TABLE IF EXISTS book_orders;
DROP TABLE IF EXISTS books;

CREATE TABLE books (
    book_id   INTEGER PRIMARY KEY,
    title     TEXT NOT NULL,
    author    TEXT NOT NULL,
    price     NUMERIC NOT NULL,
    in_stock  BOOLEAN NOT NULL
);

INSERT INTO books (book_id, title, author, price, in_stock) VALUES
    (1, 'The Quiet River', 'Mira Sen', 18.50, TRUE),
    (2, 'SQL for Curious Minds', 'Arun Das', 32.00, TRUE),
    (3, 'Small Worlds', 'Jo Lee', 12.75, FALSE),
    (4, 'The Long Weekend', 'Mira Sen', 24.00, TRUE);

DROP TABLE IF EXISTS book_reviews;

CREATE TABLE book_reviews (
    review_id   INTEGER PRIMARY KEY,
    book_id     INTEGER NOT NULL REFERENCES books(book_id),
    reviewer    TEXT NOT NULL,
    rating      INTEGER,
    review_text TEXT
);

INSERT INTO book_reviews (review_id, book_id, reviewer, rating, review_text) VALUES
    (1, 1, 'Kavita', 5, 'A lovely story.'),
    (2, 2, 'Ravi', NULL, 'A clear introduction.'),
    (3, 3, 'Ava', 4, NULL),
    (4, 4, 'Liam', NULL, NULL),
    (5, 1, 'Omar', 3, 'Good, but slow at first.');

CREATE TABLE book_orders (
    order_id   INTEGER PRIMARY KEY,
    customer   TEXT NOT NULL,
    order_date TEXT NOT NULL,
    book_id    INTEGER NOT NULL REFERENCES books(book_id),
    quantity   INTEGER NOT NULL
);

INSERT INTO book_orders (order_id, customer, order_date, book_id, quantity) VALUES
    (1, 'Asha Rao', '2026-01-05', 1, 1),
    (2, 'Ben Cole', '2026-01-17', 2, 1),
    (3, 'Asha Rao', '2026-02-02', 3, 2),
    (4, 'Chen Wu',  '2026-02-14', 4, 1),
    (5, 'Ben Cole', '2026-03-01', 1, 1),
    (6, 'Dina Shah','2026-03-12', 2, 2);

CREATE VIEW order_details AS
SELECT o.order_id,
       o.order_date,
       o.customer,
       b.title,
       b.author,
       o.quantity,
       b.price,
       o.quantity * b.price AS estimated_line_total
FROM book_orders AS o
INNER JOIN books AS b
    ON o.book_id = b.book_id;

CREATE INDEX idx_book_orders_book_id ON book_orders(book_id);
CREATE INDEX idx_book_orders_order_date ON book_orders(order_date);
CREATE INDEX idx_book_reviews_book_id ON book_reviews(book_id);
