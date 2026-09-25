# Day 9 — Combine tables with `JOIN`

**Today's goal:** Combine related rows from two tables using their keys, and choose between `INNER JOIN` and `LEFT JOIN`.

**Suggested time:** 60–75 minutes

**Interactive routine:** Predict which rows should appear, write each query in `queries/day-09.sql`, run it, and compare. Attempt the test before consulting the answer key. Send me your SQL and questions for feedback.

## 1. The relationship we will use

Day 8 established that `book_orders.book_id` refers to `books.book_id`. A join uses this relationship to return book information alongside order information.

```sql
SELECT books.title, book_orders.order_date, book_orders.quantity
FROM books
INNER JOIN book_orders
    ON books.book_id = book_orders.book_id;
```

The `ON` condition says which rows are related. Here, a book row matches an order row when their `book_id` values are equal.

## 2. Use aliases to make joins easier to read

Aliases give tables shorter names for one query. `AS` is optional for table aliases:

```sql
SELECT b.title, o.order_date, o.quantity
FROM books AS b
INNER JOIN book_orders AS o
    ON b.book_id = o.book_id;
```

Once you assign an alias, use it to refer to that table in the query. Qualify column names such as `book_id` with a table alias when both tables have that column.

## 3. `INNER JOIN`: keep matching pairs

An `INNER JOIN` returns a row for every matching pair. A book with two orders appears twice because it has two matching order rows. This is expected: joins combine rows, so one-to-many relationships can increase the number of result rows.

```sql
SELECT b.title, o.order_id
FROM books AS b
INNER JOIN book_orders AS o
    ON b.book_id = o.book_id
ORDER BY o.order_id;
```

There are six orders, so this returns six rows.

## 4. `LEFT JOIN`: keep all rows from the left table

A `LEFT JOIN` returns every row from the table on the left, plus matching rows from the right. If a left-side row has no match, right-table columns show `NULL`.

All four books currently have orders, so use an `ON` condition that matches only March orders to see the unmatched behavior:

```sql
SELECT b.title, o.order_id, o.order_date
FROM books AS b
LEFT JOIN book_orders AS o
    ON b.book_id = o.book_id
   AND o.order_date >= '2026-03-01'
   AND o.order_date <  '2026-04-01'
ORDER BY b.book_id;
```

Every book stays in the output. Books without a March order have `NULL` for `order_id` and `order_date`.

### Important: a filter in `ON` differs from `WHERE`

For a `LEFT JOIN`, placing a right-table filter in `WHERE` can remove the unmatched rows and make the result behave like an inner join:

```sql
-- This excludes books without a March order
SELECT b.title, o.order_id
FROM books AS b
LEFT JOIN book_orders AS o
    ON b.book_id = o.book_id
WHERE o.order_date >= '2026-03-01';
```

If you want to keep every left-side row and only match qualifying right-side rows, put the condition in `ON`.

## 5. Count after joining: watch out for duplicates

A join may repeat a book once per order. If you count joined rows, you count order matches, not unique books. For unique book count, use `COUNT(DISTINCT b.book_id)`:

```sql
SELECT COUNT(DISTINCT b.book_id) AS books_with_orders
FROM books AS b
INNER JOIN book_orders AS o
    ON b.book_id = o.book_id;
```

This is a common source of incorrect totals. Always ask: “What does one result row represent?”

## 6. Today's runnable practice

Edit `queries/day-09.sql`, save, and run from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-09.sql
```

## 7. Assignment — write these six queries

Before running each one, predict the number of rows and what one row represents.

1. List each order ID, date, customer, and book title by joining `books` and `book_orders`.
2. Show the title and order ID for every matching pair, sorted by order ID.
3. Count order rows per book title. Show each title and its order count.
4. List every book and any March order ID. Keep books even when they have no March order by placing the date range in the `ON` condition.
5. Show every book and its rating-5 review, if one exists. Keep books without a rating-5 review by putting `r.rating = 5` in `ON`.
6. Count the number of distinct books that have orders.

## 8. Self-test — answer without notes

1. What columns connect `books` and `book_orders`?
2. What does an `INNER JOIN` keep?
3. What does a `LEFT JOIN` preserve?
4. Why can a book appear more than once after joining orders?
5. Where should a right-table condition go when you want unmatched left rows to remain in a `LEFT JOIN` result?
6. What does `COUNT(DISTINCT b.book_id)` count after a join?

## 9. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Order details with book titles
SELECT o.order_id, o.order_date, o.customer, b.title
FROM book_orders AS o
INNER JOIN books AS b
    ON o.book_id = b.book_id
ORDER BY o.order_id;
```

```sql
-- 2. Matching title and order ID
SELECT b.title, o.order_id
FROM books AS b
INNER JOIN book_orders AS o
    ON b.book_id = o.book_id
ORDER BY o.order_id;
```

```sql
-- 3. Order count per book
SELECT b.title, COUNT(o.order_id) AS order_count
FROM books AS b
INNER JOIN book_orders AS o
    ON b.book_id = o.book_id
GROUP BY b.book_id, b.title
ORDER BY b.book_id;
```

```sql
-- 4. Every book plus any March order
SELECT b.title, o.order_id
FROM books AS b
LEFT JOIN book_orders AS o
    ON b.book_id = o.book_id
   AND o.order_date >= '2026-03-01'
   AND o.order_date <  '2026-04-01'
ORDER BY b.book_id;
```

```sql
-- 5. Every book plus any 5-star review
SELECT b.title, r.reviewer, r.rating
FROM books AS b
LEFT JOIN book_reviews AS r
    ON b.book_id = r.book_id
   AND r.rating = 5
ORDER BY b.book_id;
```

```sql
-- 6. Unique books that have orders
SELECT COUNT(DISTINCT b.book_id) AS books_with_orders
FROM books AS b
INNER JOIN book_orders AS o
    ON b.book_id = o.book_id;
```

Expected row counts: **6, 6, 4, 4, 4, 1**. Assignment 4 returns March order IDs 5 and 6 for two books, and `NULL` for the other two. Assignment 5 returns the rating-5 review for The Quiet River and `NULL` reviews for the other books.

### Self-test solutions

1. `books.book_id` and `book_orders.book_id`.
2. Rows where both tables have a match according to the `ON` condition.
3. Every row from the left table, with matching right-side data when it exists.
4. A book can match multiple orders; each matching pair becomes a result row.
5. Put the condition in `ON` to keep unmatched left rows.
6. The number of different book IDs represented in the joined result.

## 10. Ready for Day 10?

You’re ready when you can explain why one book may produce multiple joined rows and when to use `LEFT JOIN` instead of `INNER JOIN`. Send me your query for Assignment 4 and explain why the March condition belongs in `ON`.
