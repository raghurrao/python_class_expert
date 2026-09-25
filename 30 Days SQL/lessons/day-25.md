# Day 25 — Check query correctness and edge cases

**Today's goal:** Review a query for common correctness traps involving `NULL`, duplicates, outer joins, and boundaries.

**Suggested time:** 60–75 minutes

**Interactive routine:** For every prompt, state what one row represents, predict the result, then compare your query with the answer key. Try explaining why a plausible-looking wrong query is wrong.

## 1. Start with the question and the grain

Before writing SQL, clarify:

1. What does one result row represent?
2. Which rows should be included or excluded?
3. Can a join multiply rows?
4. How should missing values behave?
5. Are date boundaries inclusive or exclusive?

These questions catch many logic errors before you run the query.

## 2. `NULL` needs explicit handling

Wrong:

```sql
SELECT reviewer
FROM book_reviews
WHERE rating = NULL;
```

Correct:

```sql
SELECT reviewer
FROM book_reviews
WHERE rating IS NULL;
```

Also check how aggregates treat `NULL`: `COUNT(*)` counts all rows, while `COUNT(rating)` counts only non-`NULL` ratings. `AVG(rating)` also ignores missing ratings.

## 3. Joins can duplicate records

If you join orders to both books and reviews, an order may repeat once per matching review. `SUM(quantity)` can then be inflated. Include only the tables needed for the question or summarize one-to-many data before combining it.

When counting distinct entities after a join, consider `COUNT(DISTINCT key)`. For sums, `DISTINCT` is usually not a general fix: two legitimately different rows can have the same quantity.

## 4. `LEFT JOIN` conditions need care

To keep unmatched left rows, filter the right table in the `ON` clause:

```sql
SELECT b.title, o.order_id
FROM books AS b
LEFT JOIN book_orders AS o
    ON b.book_id = o.book_id
   AND o.order_date >= '2026-03-01'
   AND o.order_date <  '2026-04-01';
```

Putting the order date condition in `WHERE` removes rows with no March order because their `o.order_date` is `NULL`.

## 5. Use precise date boundaries

For all dates in February, use:

```sql
WHERE order_date >= '2026-02-01'
  AND order_date <  '2026-03-01'
```

This includes the first day and excludes the first day of the next month. It is safer for timestamps than using an inclusive end date at midnight.

## 6. Avoid ambiguous grouping

In a grouped query, each selected value should be a grouping column or an aggregate. This keeps the meaning of every output row clear and avoids database-specific behavior.

Also include deterministic sort keys when using `LIMIT` or `ROW_NUMBER` and ties are possible. If two rows have the same price, add a unique key such as `book_id` to decide which comes first.

## 7. Today's runnable practice

Edit `queries/day-25.sql`, save, and run from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-25.sql
```

## 8. Assignment — debug the query ideas

For each scenario, identify the bug and write a corrected query or rule.

1. A query uses `WHERE rating = NULL` but returns no unrated reviews.
2. A monthly revenue query joins orders, books, and reviews, then sums `quantity * price`.
3. A `LEFT JOIN` to March orders is followed by `WHERE order_date >= '2026-03-01'`, but the analyst expects every book to remain.
4. A February report uses `order_date BETWEEN '2026-02-01' AND '2026-02-28'`. Why can this be risky if the column later contains timestamps?
5. A report counts rows with `COUNT(rating)` and expects all review rows, including unrated ones.
6. A top-two query orders only by price, and two books tie at the second position. How can you make the result deterministic?

## 9. Self-test — answer without notes

1. What should you define before writing a multi-table aggregate query?
2. Why doesn't `COUNT(DISTINCT key)` fix an inflated sum?
3. Where should a right-table condition go to preserve unmatched left rows?
4. Why is the next-month-exclusive boundary useful for month filters?
5. What is the correct null test syntax?
6. What should you add to an ordering when ties could make a limited result unpredictable?

## 10. Answer key — check after trying

### Assignment guidance

1. `NULL` is not matched with equality. Use `WHERE rating IS NULL`.
2. Reviews can repeat each order. Remove the review join for revenue, or aggregate relevant data at the right grain before joining.
3. Move the date condition into `ON`:

   ```sql
   LEFT JOIN book_orders AS o
       ON b.book_id = o.book_id
      AND o.order_date >= '2026-03-01'
      AND o.order_date < '2026-04-01'
   ```

4. If the column contains timestamps, `2026-02-28` means midnight at the start of the day, so later times on Feb 28 are excluded. Use `>= '2026-02-01' AND < '2026-03-01'`.
5. Use `COUNT(*)` to count every review row. `COUNT(rating)` skips `NULL` ratings.
6. Add a unique tie-breaker, such as `ORDER BY price DESC, book_id`, to make the order deterministic.

### Self-test solutions

1. The result grain: what one output row represents.
2. It can fix a duplicated unique-entity count, but sum inputs still contain repeated values and may include legitimate equal values.
3. In the join's `ON` condition.
4. It includes all times on the final day and excludes the next month.
5. `IS NULL` (or `IS NOT NULL`).
6. A deterministic tie-breaker, ideally a unique key.

## 11. Ready for Day 26?

You’re ready when you can explain one way a query could silently return a plausible but wrong answer and how you would prevent it. Send me your correction for Assignment 3 and tell me why `WHERE` changes the outer join result.
