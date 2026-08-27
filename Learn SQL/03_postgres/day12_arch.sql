-- Day 12: Schema Architecture Script

-- Create Schemas for Staging and Data Warehouse
CREATE TABLE IF NOT EXISTS staging_raw_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    payload TEXT,
    ingested_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS dw_fact_sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    amount REAL,
    transaction_date DATE
);

INSERT INTO staging_raw_events (payload) VALUES
('{"user": "alice", "action": "login"}'),
('{"user": "bob", "action": "checkout"}');

INSERT INTO dw_fact_sales (customer_id, amount, transaction_date) VALUES
(101, 299.99, '2026-08-25'),
(102, 149.50, '2026-08-26');
