-- Day 18: Index Performance Optimization Script

-- Query Plan Before Index
EXPLAIN QUERY PLAN
SELECT * FROM employees WHERE email = 'alice@company.com';

-- Create B-Tree Index on email column
CREATE INDEX IF NOT EXISTS idx_emp_email ON employees(email);

-- Query Plan After Index
EXPLAIN QUERY PLAN
SELECT * FROM employees WHERE email = 'alice@company.com';
