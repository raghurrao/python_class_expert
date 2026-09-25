# Day 19 — Find top rows within each group

**Today's goal:** Combine window functions and CTEs to find the top row or top few rows in each group.

**Suggested time:** 60–75 minutes

**Interactive routine:** State the grouping key and tie behavior, write your query in `queries/day-19.sql`, run it, and compare. Attempt the self-test before checking the answer key.

## 1. Why top-N per group is different

`ORDER BY price DESC LIMIT 1` finds one book overall. It does not find one book for every author. For one top row per author, rank the rows inside each author partition:

```sql
WITH ranked_books AS (
    SELECT author, title, price,
           ROW_NUMBER() OVER (
               PARTITION BY author
               ORDER BY price DESC, book_id
           ) AS row_num
    FROM books
)
SELECT author, title, price
FROM ranked_books
WHERE row_num = 1
ORDER BY author;
```

The CTE calculates the row number for each book. The outer query filters to the first row per author. `book_id` is a tie-breaker so `ROW_NUMBER` picks a predictable book if prices tie.

## 2. Why use an outer query or CTE?

Window functions are calculated after the `WHERE` clause at the same query level, so you cannot usually filter on the window result in that query's `WHERE`. Instead, calculate it in a CTE or subquery, then filter in the outer query.

## 3. Choose tie behavior deliberately

Use `ROW_NUMBER` when you want exactly N rows per group. Use `RANK` or `DENSE_RANK` when ties should share a rank. For example, return all books tied for the highest price per author:

```sql
WITH ranked_books AS (
    SELECT author, title, price,
           RANK() OVER (
               PARTITION BY author
               ORDER BY price DESC
           ) AS price_rank
    FROM books
)
SELECT author, title, price
FROM ranked_books
WHERE price_rank = 1;
```

There are no tied prices within an author in the current sample, but this query would return all ties if there were.

## 4. Top two orders per customer

```sql
WITH ranked_orders AS (
    SELECT customer, order_id, order_date, quantity,
           ROW_NUMBER() OVER (
               PARTITION BY customer
               ORDER BY order_date DESC, order_id DESC
           ) AS row_num
    FROM book_orders
)
SELECT customer, order_id, order_date, quantity
FROM ranked_orders
WHERE row_num <= 2
ORDER BY customer, row_num;
```

This returns up to two orders per customer, newest first. Customers with fewer than two orders still appear with all their orders.

## 5. Today's runnable practice

Edit `queries/day-19.sql`, save, and run from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-19.sql
```

## 6. Assignment — write these six queries

1. Return the most expensive book per author using `ROW_NUMBER`.
2. Return the two most expensive books overall (not per author).
3. Return the two most expensive books per author.
4. Return the highest-rated review per book using `ROW_NUMBER`. Exclude missing ratings; use `review_id` as a tie-breaker.
5. Return every book tied for the top price within its author using `RANK`.
6. Return the most recent order per customer, using `ROW_NUMBER` and a deterministic tie-breaker.

For each question, decide whether you need exactly N rows or want to retain ties.

## 7. Self-test — answer without notes

1. What does `PARTITION BY author` do to the row number?
2. Why does the top row per author query use a CTE?
3. Which function should you use for exactly one top row per group?
4. Which function can return multiple rows tied at rank 1?
5. Does `LIMIT 2` return two rows per author?
6. Why include a tie-breaker in a `ROW_NUMBER` ordering?

## 8. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Most expensive book per author
WITH ranked_books AS (
    SELECT book_id, author, title, price,
           ROW_NUMBER() OVER (
               PARTITION BY author
               ORDER BY price DESC, book_id
           ) AS row_num
    FROM books
)
SELECT author, title, price
FROM ranked_books
WHERE row_num = 1;
```

```sql
-- 2. Two most expensive books overall
SELECT title, price
FROM books
ORDER BY price DESC, book_id
LIMIT 2;
```

```sql
-- 3. Two most expensive books per author
WITH ranked_books AS (
    SELECT book_id, author, title, price,
           ROW_NUMBER() OVER (
               PARTITION BY author
               ORDER BY price DESC, book_id
           ) AS row_num
    FROM books
)
SELECT author, title, price
FROM ranked_books
WHERE row_num <= 2
ORDER BY author, row_num;
```

```sql
-- 4. Highest-rated review per book
WITH ranked_reviews AS (
    SELECT book_id, review_id, reviewer, rating,
           ROW_NUMBER() OVER (
               PARTITION BY book_id
               ORDER BY rating DESC, review_id
           ) AS row_num
    FROM book_reviews
    WHERE rating IS NOT NULL
)
SELECT book_id, reviewer, rating
FROM ranked_reviews
WHERE row_num = 1;
```

```sql
-- 5. All books tied at top price per author
WITH ranked_books AS (
    SELECT author, title, price,
           RANK() OVER (
               PARTITION BY author
               ORDER BY price DESC
           ) AS price_rank
    FROM books
)
SELECT author, title, price
FROM ranked_books
WHERE price_rank = 1;
```

```sql
-- 6. Most recent order per customer
WITH ranked_orders AS (
    SELECT customer, order_id, order_date,
           ROW_NUMBER() OVER (
               PARTITION BY customer
               ORDER BY order_date DESC, order_id DESC
           ) AS row_num
    FROM book_orders
)
SELECT customer, order_id, order_date
FROM ranked_orders
WHERE row_num = 1
ORDER BY customer;
```

Expected results: Assignment 1 returns **Arun Das — SQL for Curious Minds; Jo Lee — Small Worlds; Mira Sen — The Long Weekend**. Assignment 2 returns **SQL for Curious Minds and The Long Weekend**. Assignment 3 returns every book (Mira has two, the other authors one each). Assignment 4 returns **Kavita (5)** for book 1 and **Ava (4)** for book 3. Assignment 5 returns the same top book per author as Assignment 1. Assignment 6 returns order IDs **3, 5, 4, 6** for Asha, Ben, Chen, and Dina.

### Self-test solutions

1. It restarts numbering independently for each author.
2. The CTE lets the outer query filter on the calculated row number.
3. `ROW_NUMBER`.
4. `RANK`.
5. No. `LIMIT 2` returns two rows total; top two per author needs a partitioned ranking.
6. To make the row selection predictable when the main sort values tie.

## 9. Ready for Day 20?

You’re ready when you can explain the difference between top N overall and top N per group, and choose `ROW_NUMBER` or `RANK` based on tie requirements. Send me Assignment 3 and how many rows you expect.
