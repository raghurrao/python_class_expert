# Day 34 — Write queries the index can use

**Today's goal:** Compare equivalent filters and use query plans to see when a query can use an ordinary index.

**Suggested time:** 45–60 minutes

**Interactive routine:** Run both query plans in the practice file, compare the plan details, then rewrite the assignment filters and explain the change.

## 1. Filter directly on an indexed column

The course database has an index on `book_orders(order_date)`. A date range written directly against that column can use the index:

```sql
EXPLAIN QUERY PLAN
SELECT order_id, order_date
FROM book_orders
WHERE order_date >= '2026-02-01'
  AND order_date <  '2026-03-01';
```

Look for a `SEARCH` using `idx_book_orders_order_date`. Query-plan wording can vary by SQLite version.

## 2. A function on the column can prevent a normal index lookup

This query asks the same general question but applies `SUBSTR` to each date:

```sql
EXPLAIN QUERY PLAN
SELECT order_id, order_date
FROM book_orders
WHERE SUBSTR(order_date, 1, 7) = '2026-02';
```

An ordinary index on `order_date` may not help SQLite search by `SUBSTR(order_date, 1, 7)`, so the planner may scan all rows (or scan all entries in a covering index). For a month filter, the half-open date range gives the planner a direct range predicate.

Some databases support expression indexes; SQLite does too, but the indexed expression must match the query expression appropriately. Prefer a direct filter when it expresses the requirement clearly and can use an existing index.

## 3. Composite indexes and column order

A composite index stores multiple columns together:

```sql
CREATE INDEX idx_orders_customer_date
    ON book_orders(customer, order_date);
```

This may help queries filtering by `customer`, or by `customer` plus `order_date`. It may not help as much for a query filtering only by `order_date`, because `customer` is the leading column. Index order should follow actual query patterns.

Do not create indexes by guesswork alone. Check important queries and measure on representative data.

## 4. Query plan versus benchmark

`EXPLAIN QUERY PLAN` shows a high-level plan choice, not elapsed time or actual row counts. A plan that uses an index is not automatically faster for every dataset. Use realistic data and repeatable measurements before changing production indexes.

Avoid changing a query merely to force index use if it makes the logic less clear or changes its result.

## 5. Today's runnable practice

Edit and run:

```powershell
python run_sql.py queries/day-34.sql
```

The starter file displays both query plans, side by side in sequence.

## 6. Assignment — inspect and rewrite

1. Compare the plan for a date range to the plan for `SUBSTR(order_date, 1, 7) = '2026-02'`.
2. Rewrite the month filter as an index-friendly half-open range.
3. Explain why an index on `(customer, order_date)` is useful for a customer-plus-date query.
4. Explain why that composite index may not be the best index for a query that filters only by date.
5. State one thing `EXPLAIN QUERY PLAN` tells you and one thing it does not tell you.
6. Give one reason not to add an index to every column.

## 7. Self-test — answer without notes

1. What does “sargable” mean in query optimization?
2. Why can wrapping an indexed column in a function make a regular index harder to use?
3. Which columns does a composite index on `(customer, order_date)` lead with?
4. What does SQLite's `SEARCH` plan detail generally indicate?
5. Does an index guarantee lower query time?
6. What should you do before making performance changes based on a tiny sample table?

## 8. Answer key — check after trying

### Assignment guidance

1. The date range should produce an indexed `SEARCH`; the `SUBSTR` predicate may scan the full table or a full index instead of seeking to a range.
2. `WHERE order_date >= '2026-02-01' AND order_date < '2026-03-01'`.
3. It narrows by customer first and can then constrain the date within that customer's range.
4. The leading index column is customer, so date-only filtering does not align with the leftmost part of the index.
5. It shows the chosen high-level plan; it does not show actual elapsed time or prove the query is faster.
6. Indexes use storage and add maintenance work to writes.

### Self-test solutions

1. A query predicate written so the database can efficiently search an index for matching rows.
2. The database may have to calculate the function for each row, rather than directly seek by the indexed stored value.
3. `customer` first, then `order_date`.
4. SQLite is doing a targeted lookup, often using an index; inspect the detail to see which index.
5. No. The optimizer estimates costs, and the table size and query shape matter.
6. Use representative data and measure; tiny datasets can produce misleading plan choices and timings.

## 9. Ready for Day 35?

You’re ready when you can read both plans and explain why the date-range predicate is a better match for the ordinary date index. Send me the plan details from Assignment 1.
