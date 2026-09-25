-- Day 31 practice: recursive integer sequence from 1 through 10.
-- Run with: python run_sql.py queries/day-31.sql
WITH RECURSIVE numbers(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1
    FROM numbers
    WHERE n < 10
)
SELECT n
FROM numbers;
