# Day 14 — Organize queries with CTEs

**Today's goal:** Use a common table expression (CTE) to give a query result a temporary name and make multi-step SQL easier to read.

**Suggested time:** 60–75 minutes

**Interactive routine:** Read each query from the `WITH` section downward. Write today's assignments in `queries/day-14.sql`, run them, and compare your predicted output before checking the answer key.

## 1. What is a CTE?

A CTE is a named result set introduced by `WITH`. It exists only for the statement immediately following it. Think of it as a temporary, named step inside a query—not a permanent table.

```sql
WITH book_counts AS (
    SELECT author, COUNT(*) AS book_count
    FROM books
    GROUP BY author
)
SELECT author, book_count
FROM book_counts
WHERE book_count >= 2;
```

First, the CTE `book_counts` calculates a count per author. Then the main query selects from that result and keeps authors with at least two books.

## 2. Break a multi-step query into named steps

Suppose you want total quantity ordered by book, then only books whose total quantity is at least 2:

```sql
WITH quantity_by_book AS (
    SELECT b.book_id, b.title, SUM(o.quantity) AS total_quantity
    FROM books AS b
    INNER JOIN book_orders AS o
        ON b.book_id = o.book_id
    GROUP BY b.book_id, b.title
)
SELECT title, total_quantity
FROM quantity_by_book
WHERE total_quantity >= 2
ORDER BY total_quantity DESC;
```

The CTE performs the aggregation. The outer query filters and sorts the summary. The name `quantity_by_book` documents what each row represents: one summary per book.

## 3. Use more than one CTE

Separate independent calculations into named steps, then combine them:

```sql
WITH order_totals AS (
    SELECT customer, SUM(quantity) AS total_quantity
    FROM book_orders
    GROUP BY customer
),
customer_order_counts AS (
    SELECT customer, COUNT(*) AS order_count
    FROM book_orders
    GROUP BY customer
)
SELECT t.customer, t.total_quantity, c.order_count
FROM order_totals AS t
INNER JOIN customer_order_counts AS c
    ON t.customer = c.customer
ORDER BY t.customer;
```

Separate CTEs help keep each calculation focused. A CTE can refer to a CTE defined earlier in the same `WITH` clause.

## 4. CTEs and subqueries

CTEs and subqueries can often express the same logic. A CTE can be easier to read when:

- a query has several clear steps;
- an intermediate result deserves a descriptive name;
- you want to inspect or reason about a step separately.

For a short one-value comparison, a scalar subquery may be simpler. Choose the form that makes the logic easiest to follow.

## 5. Today's runnable practice

Edit `queries/day-14.sql`, save, and run from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-14.sql
```

## 6. Assignment — write these six queries

For each CTE, say what one row represents before writing the outer query.

1. Create a CTE called `book_counts` with one row per author and the author's book count. Select all rows from it, sorted by author.
2. Create a CTE called `rated_reviews` containing only reviews with a rating. From it, show each reviewer and rating.
3. Create a CTE with total ordered quantity per customer. Return only customers with totals above 1.
4. Create a CTE with total quantity per book, then show the title and total for books with totals of at least 2.
5. Use two CTEs: one for total quantity per customer and one for order count per customer. Join them and show both metrics.
6. Create a CTE with monthly order counts by selecting the first seven characters of each ISO date (`YYYY-MM`). Show the month and count in month order.

## 7. Self-test — answer without notes

1. What keyword begins a CTE?
2. Does a CTE create a permanent table?
3. How long is a CTE available?
4. In a CTE query, what does the CTE name represent?
5. Can a later CTE refer to an earlier CTE in the same `WITH` clause?
6. What is one reason to use a CTE instead of nesting every step in one large query?

## 8. Answer key — check after trying

### Assignment solutions

```sql
-- 1. One row per author
WITH book_counts AS (
    SELECT author, COUNT(*) AS book_count
    FROM books
    GROUP BY author
)
SELECT author, book_count
FROM book_counts
ORDER BY author;
```

```sql
-- 2. Only reviews with a rating
WITH rated_reviews AS (
    SELECT reviewer, rating
    FROM book_reviews
    WHERE rating IS NOT NULL
)
SELECT reviewer, rating
FROM rated_reviews
ORDER BY reviewer;
```

```sql
-- 3. Customers with total quantity above 1
WITH customer_totals AS (
    SELECT customer, SUM(quantity) AS total_quantity
    FROM book_orders
    GROUP BY customer
)
SELECT customer, total_quantity
FROM customer_totals
WHERE total_quantity > 1;
```

```sql
-- 4. Books with at least two total units ordered
WITH quantity_by_book AS (
    SELECT b.book_id, b.title, SUM(o.quantity) AS total_quantity
    FROM books AS b
    INNER JOIN book_orders AS o
        ON b.book_id = o.book_id
    GROUP BY b.book_id, b.title
)
SELECT title, total_quantity
FROM quantity_by_book
WHERE total_quantity >= 2;
```

```sql
-- 5. Two named per-customer calculations
WITH customer_totals AS (
    SELECT customer, SUM(quantity) AS total_quantity
    FROM book_orders
    GROUP BY customer
),
customer_counts AS (
    SELECT customer, COUNT(*) AS order_count
    FROM book_orders
    GROUP BY customer
)
SELECT t.customer, t.total_quantity, c.order_count
FROM customer_totals AS t
INNER JOIN customer_counts AS c
    ON t.customer = c.customer;
```

```sql
-- 6. Orders per calendar month
WITH monthly_orders AS (
    SELECT SUBSTR(order_date, 1, 7) AS order_month,
           COUNT(*) AS order_count
    FROM book_orders
    GROUP BY SUBSTR(order_date, 1, 7)
)
SELECT order_month, order_count
FROM monthly_orders
ORDER BY order_month;
```

Expected monthly counts: **2026-01: 2, 2026-02: 2, 2026-03: 2**.

### Self-test solutions

1. `WITH`.
2. No. It is a named query result, not a permanent table.
3. For the one statement immediately following its definition.
4. The named intermediate result set produced by its query.
5. Yes. Later CTEs can build on earlier ones.
6. It gives a complex step a readable name and makes the full query easier to reason about.

## 9. Ready for Day 15?

You’re ready when you can name an intermediate result, say what each row represents, and query it in the main statement. Send me Assignment 4 and describe the grain of its CTE.
