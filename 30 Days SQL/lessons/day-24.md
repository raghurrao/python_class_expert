# Day 24 — Improve lookups with indexes

**Today's goal:** Understand what an index does, create an index, and inspect a query plan with SQLite.

**Suggested time:** 45–60 minutes

**Interactive routine:** Run the `EXPLAIN QUERY PLAN` command in the starter file, inspect the index list, then try the assignment. Tell me what the planner reports and what you think that means.

## 1. What an index does

An index is a data structure the database can use to find rows without scanning every row in a table. It is similar to a book index: instead of reading every page, you look up a value and go to the matching location.

The course setup creates these indexes:

```sql
CREATE INDEX idx_book_orders_book_id
    ON book_orders(book_id);

CREATE INDEX idx_book_orders_order_date
    ON book_orders(order_date);

CREATE INDEX idx_book_reviews_book_id
    ON book_reviews(book_id);
```

They can help lookups or joins that use those columns. Primary-key columns are indexed automatically by SQLite.

## 2. Inspect indexes

Use SQLite's `PRAGMA index_list(table_name)` to list a table's indexes:

```sql
PRAGMA index_list(book_orders);
```

You can inspect which columns are in an index with `PRAGMA index_info(index_name)`:

```sql
PRAGMA index_info(idx_book_orders_book_id);
```

## 3. Read a query plan

Prefix a query with `EXPLAIN QUERY PLAN` to see how SQLite intends to run it:

```sql
EXPLAIN QUERY PLAN
SELECT order_id, order_date
FROM book_orders
WHERE book_id = 1;
```

The output is a plan description, not the query result. Look for terms like `SEARCH` (SQLite uses an index or targeted lookup) and `SCAN` (it reads rows in a table or index). Exact wording can differ by SQLite version.

The sample table has only six rows. SQLite may choose a table scan because scanning six rows can be cheaper than using an index. That does not mean an index is useless on a larger table; the planner chooses based on estimated cost.

## 4. Index tradeoffs

Indexes can speed up filtering, joins, and some sorts, but they take storage and need maintenance when rows are inserted, updated, or deleted. Too many or poorly chosen indexes can make writes slower without helping important queries.

Good candidates are often columns used frequently in `WHERE`, join conditions, or ordering. Index design depends on actual query patterns and table size. An index on `(customer, order_date)` is a composite index; column order matters because it affects which lookups can use its leftmost columns.

## 5. Today's runnable practice

The course database has the listed indexes. If your database was created before Day 24, recreate it with `python setup_database.py` from PowerShell in the course folder. Then run:

```powershell
python run_sql.py queries/day-24.sql
```

## 6. Assignment — inspect and reason

1. List the indexes on `book_orders`.
2. Inspect the columns in `idx_book_orders_book_id`.
3. Show SQLite's plan for finding orders by `book_id`.
4. Show the plan for finding February orders by `order_date`.
5. In your own words, explain why the planner might choose a scan on this small sample table even though an index exists.
6. Give one cost of adding an index.

## 7. Self-test — answer without notes

1. What problem does an index help solve?
2. Does creating an index guarantee that the query planner will use it?
3. What does a `SCAN` in a query plan generally mean?
4. Name two query operations that might benefit from an index.
5. Name one tradeoff of indexes.
6. Why are the course tables too small for meaningful performance benchmarks?

## 8. Answer key — check after trying

### Assignment guidance

1. `PRAGMA index_list(book_orders);` shows the two course-created indexes and any primary-key autoindex.
2. `PRAGMA index_info(idx_book_orders_book_id);` shows `book_id`.
3. Use `EXPLAIN QUERY PLAN SELECT order_id, order_date FROM book_orders WHERE book_id = 1;`. The planner may show a scan or an indexed search depending on its cost estimate and SQLite version.
4. Use `EXPLAIN QUERY PLAN SELECT order_id FROM book_orders WHERE order_date >= '2026-02-01' AND order_date < '2026-03-01';`. A scan is possible because the table is tiny.
5. For six rows, reading the whole table can cost less than navigating an index, so SQLite may prefer a scan.
6. Indexes use storage and add work to inserts, updates, and deletes.

### Self-test solutions

1. Finding matching rows without having to read every row.
2. No. The optimizer chooses a plan based on estimated cost.
3. The plan reads the table or index rows rather than directly searching a narrow range; exact wording depends on the plan.
4. Filtering and joins (sorting may also benefit in suitable cases).
5. They use storage and slow down writes because they must be maintained.
6. Their tiny size makes elapsed times and planner decisions unrepresentative of large real datasets.

## 9. Ready for Day 25?

You’re ready when you can inspect an index and explain why an index is a tradeoff rather than an automatic speed button. Send me the planner output for Assignment 3 and your interpretation.
