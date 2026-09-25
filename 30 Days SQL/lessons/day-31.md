# Day 31 — Build sequences with recursive CTEs

**Today's goal:** Use a recursive CTE to generate a sequence and fill dates that have no matching activity.

**Suggested time:** 60–75 minutes

**Interactive routine:** First run the sequence query in `queries/day-31.sql`. Then try the date-calendar assignment and predict how many rows it will return before looking at the answer key.

## 1. What makes a CTE recursive?

A recursive CTE refers to itself. It has two parts:

1. An **anchor query** that produces the first row or rows.
2. A **recursive query** that uses the previous result to produce the next row or rows.

`UNION ALL` combines each generated step. A stopping condition prevents the recursion from continuing forever.

```sql
WITH RECURSIVE numbers(n) AS (
    SELECT 1                 -- anchor
    UNION ALL
    SELECT n + 1             -- recursive step
    FROM numbers
    WHERE n < 10              -- stop after 10
)
SELECT n
FROM numbers;
```

The output is the sequence 1 through 10.

## 2. Generate a calendar

The orders occur on six dates, but many days in the period have no orders. A recursive CTE can generate every date between the earliest and latest order:

```sql
WITH RECURSIVE calendar(day) AS (
    SELECT MIN(order_date) FROM book_orders
    UNION ALL
    SELECT date(day, '+1 day')
    FROM calendar
    WHERE day < (SELECT MAX(order_date) FROM book_orders)
)
SELECT day
FROM calendar
ORDER BY day;
```

The first query provides the earliest date. Each recursive step adds one day until it reaches the latest order date.

## 3. Fill missing dates with zero activity

Aggregate daily order activity first, then left join it to the generated calendar:

```sql
WITH RECURSIVE calendar(day) AS (
    SELECT MIN(order_date) FROM book_orders
    UNION ALL
    SELECT date(day, '+1 day')
    FROM calendar
    WHERE day < (SELECT MAX(order_date) FROM book_orders)
), daily_orders AS (
    SELECT order_date,
           COUNT(*) AS order_count,
           SUM(quantity) AS units_ordered
    FROM book_orders
    GROUP BY order_date
)
SELECT c.day,
       COALESCE(d.order_count, 0) AS order_count,
       COALESCE(d.units_ordered, 0) AS units_ordered
FROM calendar AS c
LEFT JOIN daily_orders AS d
    ON c.day = d.order_date
ORDER BY c.day;
```

The `LEFT JOIN` keeps calendar days without orders, and `COALESCE` displays zero for the missing daily summary.

## 4. Keep recursion bounded

Always make the recursive step and stop condition clear. An unbounded recursive CTE can generate a very large result or hit a database recursion limit. For a fixed date period, explicit start and end values can be safer than relying on table data.

SQLite supports recursive CTEs. Other SQL databases support them too, but syntax and recursion limits can differ.

## 5. Today's runnable practice

Run the number sequence starter query with:

```powershell
python run_sql.py queries/day-31.sql
```

Then replace it with the date-calendar query from section 3.

## 6. Assignment — recursive CTE practice

1. Generate integers from 1 to 20.
2. Generate all dates from the earliest to latest `book_orders.order_date`.
3. Fill dates without orders with zero, showing daily order count and units ordered.
4. Add estimated daily revenue to the calendar result. Use `order_details` to calculate daily revenue.
5. Explain what the anchor query returns and what the recursive step adds.
6. State the stopping condition and why it guarantees the sequence ends for the sample data.

## 7. Self-test — answer without notes

1. What are the two parts of a recursive CTE?
2. Why is a stopping condition necessary?
3. Why does the calendar query use `LEFT JOIN`?
4. Why is `COALESCE` used for days without activity?
5. What does `UNION ALL` do in the recursive query?
6. What risk comes from an unbounded recursive step?

## 8. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Integers 1 through 20
WITH RECURSIVE numbers(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM numbers WHERE n < 20
)
SELECT n FROM numbers;
```

```sql
-- 2. Calendar dates between first and last order
WITH RECURSIVE calendar(day) AS (
    SELECT MIN(order_date) FROM book_orders
    UNION ALL
    SELECT date(day, '+1 day')
    FROM calendar
    WHERE day < (SELECT MAX(order_date) FROM book_orders)
)
SELECT day FROM calendar ORDER BY day;
```

```sql
-- 3 and 4. Daily order count, units, and estimated revenue
WITH RECURSIVE calendar(day) AS (
    SELECT MIN(order_date) FROM book_orders
    UNION ALL
    SELECT date(day, '+1 day')
    FROM calendar
    WHERE day < (SELECT MAX(order_date) FROM book_orders)
), daily_orders AS (
    SELECT order_date,
           COUNT(*) AS order_count,
           SUM(quantity) AS units_ordered,
           SUM(estimated_line_total) AS estimated_revenue
    FROM order_details
    GROUP BY order_date
)
SELECT c.day,
       COALESCE(d.order_count, 0) AS order_count,
       COALESCE(d.units_ordered, 0) AS units_ordered,
       COALESCE(d.estimated_revenue, 0) AS estimated_revenue
FROM calendar AS c
LEFT JOIN daily_orders AS d
    ON c.day = d.order_date
ORDER BY c.day;
```

For this sample, the calendar returns **67 dates**, from 2026-01-05 through 2026-03-12. Six days have orders; the other dates display zero activity.

5. The anchor provides the starting date (the earliest order date). The recursive step adds one day to the previous date.
6. Stop when the current day reaches the latest order date; then no further row is generated.

### Self-test solutions

1. The anchor query and the recursive query/step.
2. To ensure recursion ends instead of generating rows indefinitely.
3. To retain every generated calendar date, including dates without a matching daily summary.
4. The joined summary is `NULL` on dates with no activity; zero is a useful display value for counts and sums.
5. It appends recursive rows while retaining duplicates; each date or number step is preserved.
6. The query can generate an unbounded or unexpectedly large number of rows and may hit a recursion limit.

## 9. Ready for Day 32?

You’re ready when you can identify the anchor, recursive step, and stopping condition in a recursive CTE. Send me your calendar query and the number of dates you expect.
