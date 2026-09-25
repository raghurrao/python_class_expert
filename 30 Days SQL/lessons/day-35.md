# Day 35 — Understand SQL's logical processing order

**Today's goal:** Understand the conceptual order SQL uses to form a query result, and use that understanding to write clearer filters and aggregates.

**Suggested time:** 45–60 minutes

**Interactive routine:** Read the query, state which rows survive each stage, then run the practice file. Complete the assignments and test before checking the key.

## 1. Written order versus logical order

You write a query beginning with `SELECT`, but the database conceptually processes its parts in an order closer to:

1. `FROM` and `JOIN` — form the input rows.
2. `WHERE` — filter individual rows.
3. `GROUP BY` — form groups.
4. Aggregates — calculate summaries for each group.
5. `HAVING` — filter groups.
6. `SELECT` — calculate output expressions and aliases.
7. `DISTINCT` — remove duplicate output rows.
8. `ORDER BY` — sort the output.
9. `LIMIT` / `OFFSET` — keep a slice of the sorted output.

This is a logical model for understanding results. The optimizer may use a different physical execution plan as long as the result follows the query's meaning.

## 2. Why `WHERE` cannot usually use a `SELECT` alias

The alias is defined in the `SELECT` stage, after `WHERE` conceptually filters rows:

```sql
-- Clear standard SQL approach: repeat the expression
SELECT title,
       CASE WHEN price >= 25 THEN 'Premium' ELSE 'Other' END AS price_band
FROM books
WHERE price >= 25;
```

Some databases allow aliases in additional clauses as an extension, but standard SQL does not generally make a `SELECT` alias available in `WHERE`. Avoid depending on dialect-specific behavior.

If you need to filter by the computed label, use a CTE:

```sql
WITH book_labels AS (
    SELECT title,
           CASE WHEN price >= 25 THEN 'Premium' ELSE 'Other' END AS price_band
    FROM books
)
SELECT title, price_band
FROM book_labels
WHERE price_band = 'Premium';
```

In the outer query, `price_band` is now a column of the CTE result.

## 3. `WHERE` and `HAVING` act at different stages

```sql
SELECT author, COUNT(*) AS book_count
FROM books
WHERE in_stock = TRUE
GROUP BY author
HAVING COUNT(*) >= 2;
```

First, `WHERE` excludes out-of-stock rows. Then SQL groups the remaining books by author. Finally, `HAVING` keeps authors whose in-stock book count is at least two.

## 4. `DISTINCT`, sorting, and limiting

```sql
SELECT DISTINCT author
FROM books
ORDER BY author
LIMIT 2;
```

Conceptually, SQL selects the author values, removes duplicates, sorts the unique names, and then returns two. Without `ORDER BY`, the two returned values are not predictable.

## 5. Today's runnable practice

Edit `queries/day-35.sql`, save, and run from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-35.sql
```

The starter query uses a CTE to create a label and then filter on it in the outer query.

## 6. Assignment — trace the processing stages

1. For each query, state the clause that filters input rows and the clause that filters groups.
2. Write a CTE that labels books `Premium` when price >= 25 and `Other` otherwise, then select only `Premium` books.
3. Write a query for the two most expensive in-stock books. Explain why `ORDER BY` must come before `LIMIT` in the written query.
4. Write a query that counts in-stock books per author and keeps only authors with at least two such books.
5. Explain why `HAVING` can refer to an aggregate but `WHERE` cannot filter an aggregate result at the same query level.
6. Name the difference between logical processing order and physical execution order.

## 7. Self-test — answer without notes

1. Which clause forms the input rows?
2. Does `WHERE` filter rows before or after grouping?
3. Which clause filters groups after aggregation?
4. Why is a `SELECT` alias generally unavailable in `WHERE`?
5. When does `LIMIT` conceptually apply relative to `ORDER BY`?
6. Does logical query order require the engine to physically execute every clause in exactly that order?

## 8. Answer key — check after trying

### Assignment solutions

1. `WHERE` filters individual rows; `HAVING` filters groups.
2. Example:

   ```sql
   WITH book_labels AS (
       SELECT title,
              CASE WHEN price >= 25 THEN 'Premium' ELSE 'Other' END AS price_band
       FROM books
   )
   SELECT title, price_band
   FROM book_labels
   WHERE price_band = 'Premium';
   ```

3. Example:

   ```sql
   SELECT title, price
   FROM books
   WHERE in_stock = TRUE
   ORDER BY price DESC
   LIMIT 2;
   ```

   Sorting defines which rows count as the top two.

4. Example:

   ```sql
   SELECT author, COUNT(*) AS in_stock_count
   FROM books
   WHERE in_stock = TRUE
   GROUP BY author
   HAVING COUNT(*) >= 2;
   ```

5. `WHERE` filters rows before groups and aggregate values exist; `HAVING` runs after aggregation and can test aggregate results.
6. Logical order describes query meaning; physical order is the optimizer's chosen way to execute it.

### Self-test solutions

1. `FROM` and `JOIN`.
2. Before grouping.
3. `HAVING`.
4. The alias is produced in the `SELECT` stage, conceptually after `WHERE`.
5. After ordering.
6. No. The optimizer may rearrange physical operations while preserving the logical result.

## 9. Ready for Day 36?

You’re ready when you can trace a query from source rows through filtering, grouping, selection, ordering, and limiting. Send me your explanation of why the CTE makes `price_band` filterable.
