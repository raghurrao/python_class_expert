# Day 10 — Join multiple tables without losing track

**Today's goal:** Join three related tables and reason about the grain of the result so that row counts and totals are not accidentally inflated.

**Suggested time:** 60–75 minutes

**Interactive routine:** Before writing the SQL, state what one output row should represent. Run your query from `queries/day-10.sql`, compare its row count with your prediction, and explain any repetition. Try the self-test before checking the key.

## 1. Follow the keys through a join chain

An order has a `book_id`, and a review also has a `book_id`. You can join both child tables to the book table:

```sql
SELECT b.title, o.order_id, r.reviewer, r.rating
FROM books AS b
INNER JOIN book_orders AS o
    ON b.book_id = o.book_id
INNER JOIN book_reviews AS r
    ON b.book_id = r.book_id
ORDER BY b.book_id, o.order_id, r.review_id;
```

Read the joins one at a time: match books to orders, then match each book to its reviews.

## 2. Understand the grain: what is one row?

The query above does **not** return one row per book or one row per order. It returns one row per matching **order-and-review pair for a book**.

For The Quiet River, there are 2 orders and 2 reviews. Every order matches both reviews, so that book produces 2 × 2 = 4 rows. SQL does exactly what the join conditions requested; this multiplication is not a database error.

Expected result rows by book:

| Book | Orders | Reviews | Joined rows |
|---|---:|---:|---:|
| The Quiet River | 2 | 2 | 4 |
| SQL for Curious Minds | 2 | 1 | 2 |
| Small Worlds | 1 | 1 | 1 |
| The Long Weekend | 1 | 1 | 1 |

So the full result has 8 rows. Before aggregating a join, write down its grain. If you need one row per order, joining reviews may repeat each order and duplicate its quantity.

## 3. A common aggregate trap

This query appears to calculate books ordered per title, but it joins reviews too:

```sql
SELECT b.title, SUM(o.quantity) AS quantity_ordered
FROM books AS b
INNER JOIN book_orders AS o
    ON b.book_id = o.book_id
INNER JOIN book_reviews AS r
    ON b.book_id = r.book_id
GROUP BY b.book_id, b.title;
```

For The Quiet River, its order quantities are 1 and 1. Because each matches 2 reviews, the joined rows contain 1, 1, 1, 1 and the sum is incorrectly doubled to 4.

If the question is only about order quantity, join only the tables needed:

```sql
SELECT b.title, SUM(o.quantity) AS quantity_ordered
FROM books AS b
INNER JOIN book_orders AS o
    ON b.book_id = o.book_id
GROUP BY b.book_id, b.title;
```

This returns the actual quantity by title: The Quiet River 2, SQL for Curious Minds 3, Small Worlds 2, and The Long Weekend 1.

`COUNT(DISTINCT ...)` can correct some duplicated counts, but it does not generally fix duplicated sums. The safest approach is to join only what the question needs or aggregate each one-to-many table separately before combining summaries.

## 4. Make the join path explicit

Use clear table aliases and qualify columns. This query walks from orders to books, then to reviews:

```sql
SELECT o.order_id, b.title, r.reviewer
FROM book_orders AS o
INNER JOIN books AS b
    ON o.book_id = b.book_id
INNER JOIN book_reviews AS r
    ON b.book_id = r.book_id;
```

The order of table names can vary, but each `ON` clause must express the intended relationship. Joining unrelated tables without the right condition can create a huge result where every row is paired with every other row.

## 5. Today's runnable practice

Edit `queries/day-10.sql` and run it from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-10.sql
```

## 6. Assignment — write these six queries

For each query, first write “one row per ___” and predict its row count.

1. Show each order ID, its customer, and the book title. (One row per order.)
2. Show each review ID, reviewer, and its book title. (One row per review.)
3. Show each book title with its number of orders. (One row per book that has orders.)
4. Show each book title, order ID, and reviewer by joining all three tables. How many rows appear, and why?
5. Calculate total ordered quantity per book title by joining only books and orders. (One row per book.)
6. Write the tempting three-table quantity sum, then explain why its total for The Quiet River is wrong. Do not treat the inflated result as correct.

## 7. Self-test — answer without notes

1. What does “grain” mean when describing a query result?
2. Why does a book with 2 orders and 2 reviews produce 4 rows when both child tables are joined through that book?
3. Which tables are needed to calculate order quantity per book title?
4. Why can adding a review join inflate `SUM(o.quantity)`?
5. Does `COUNT(DISTINCT book_id)` generally fix a duplicated sum?
6. Before writing a multi-table query, what should you decide about the desired output?

## 8. Answer key — check after trying

### Assignment solutions

```sql
-- 1. One row per order
SELECT o.order_id, o.customer, b.title
FROM book_orders AS o
INNER JOIN books AS b
    ON o.book_id = b.book_id
ORDER BY o.order_id;
```

```sql
-- 2. One row per review
SELECT r.review_id, r.reviewer, b.title
FROM book_reviews AS r
INNER JOIN books AS b
    ON r.book_id = b.book_id
ORDER BY r.review_id;
```

```sql
-- 3. One row per book with its order count
SELECT b.title, COUNT(o.order_id) AS order_count
FROM books AS b
INNER JOIN book_orders AS o
    ON b.book_id = o.book_id
GROUP BY b.book_id, b.title
ORDER BY b.book_id;
```

```sql
-- 4. One row per order-review combination for a book
SELECT b.title, o.order_id, r.reviewer
FROM books AS b
INNER JOIN book_orders AS o
    ON b.book_id = o.book_id
INNER JOIN book_reviews AS r
    ON b.book_id = r.book_id
ORDER BY b.book_id, o.order_id, r.review_id;
```

Expected row count is **8** because The Quiet River's 2 orders pair with its 2 reviews (4 rows); each other book contributes 2 × 1, 1 × 1, and 1 × 1 rows.

```sql
-- 5. Correct total ordered quantity: only join relevant tables
SELECT b.title, SUM(o.quantity) AS quantity_ordered
FROM books AS b
INNER JOIN book_orders AS o
    ON b.book_id = o.book_id
GROUP BY b.book_id, b.title
ORDER BY b.book_id;
```

Expected quantities in book order: **2, 3, 2, 1**.

```sql
-- 6. The tempting but incorrect fan-out sum
SELECT b.title, SUM(o.quantity) AS quantity_ordered
FROM books AS b
INNER JOIN book_orders AS o
    ON b.book_id = o.book_id
INNER JOIN book_reviews AS r
    ON b.book_id = r.book_id
GROUP BY b.book_id, b.title;
```

This returns 4 for The Quiet River instead of 2, because each of its two order rows repeats once for each of its two reviews.

### Self-test solutions

1. What one row in the result represents (for example, one order, one review, or one order-review pair).
2. Each of the two orders pairs with each of the two reviews: 2 × 2 = 4 combinations.
3. `books` and `book_orders`.
4. Each order row may repeat once per matching review, so its quantity is added multiple times.
5. No. It may fix a unique count, but sums operate on all repeated rows.
6. Decide what one result row should represent (the grain).

## 9. Ready for Day 11?

You’re ready when you can describe the grain of a join and explain why two one-to-many joins can multiply rows. Send me your query for Assignment 5 and tell me what the correct quantity is for The Quiet River.
