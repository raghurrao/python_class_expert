-- Day 32 demo: normalized order tables exist only inside this transaction.
-- Run with: python run_sql.py queries/day-32.sql
BEGIN;

CREATE TABLE day32_customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL
);

CREATE TABLE day32_orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES day32_customers(customer_id),
    order_date TEXT NOT NULL
);

CREATE TABLE day32_order_items (
    order_id INTEGER NOT NULL REFERENCES day32_orders(order_id),
    line_number INTEGER NOT NULL,
    book_id INTEGER NOT NULL REFERENCES books(book_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    PRIMARY KEY (order_id, line_number)
);

INSERT INTO day32_customers VALUES (1, 'Asha Rao');
INSERT INTO day32_orders VALUES (1001, 1, '2026-03-15');
INSERT INTO day32_order_items VALUES
    (1001, 1, 1, 1),
    (1001, 2, 3, 2);

SELECT o.order_id, c.customer_name, o.order_date,
       b.title, i.quantity, b.price,
       i.quantity * b.price AS estimated_line_total
FROM day32_orders AS o
INNER JOIN day32_customers AS c ON o.customer_id = c.customer_id
INNER JOIN day32_order_items AS i ON o.order_id = i.order_id
INNER JOIN books AS b ON i.book_id = b.book_id
ORDER BY o.order_id, i.line_number;

ROLLBACK;
