# Day 23 — Reuse queries with views

**Today's goal:** Create and query a view, and understand how a view makes a complex query reusable.

**Suggested time:** 45–60 minutes

**Interactive routine:** Run the starter file, inspect the output, then change its `SELECT` to answer the assignments. Explain what query logic the view hides before checking the answer key.

## 1. What is a view?

A view is a named query saved in the database. Querying a view feels like reading a table, but the database runs its underlying `SELECT` to produce the rows. A regular view stores the query definition, not a separate copy of its result data.

The course database includes a view called `order_details`. Its definition joins orders to books and calculates an estimated line total:

```sql
CREATE VIEW order_details AS
SELECT o.order_id,
       o.order_date,
       o.customer,
       b.title,
       b.author,
       o.quantity,
       b.price,
       o.quantity * b.price AS estimated_line_total
FROM book_orders AS o
INNER JOIN books AS b
    ON o.book_id = b.book_id;
```

It was added to `setup.sql`, so it is recreated whenever you rebuild the sample database.

## 2. Query a view like a table

```sql
SELECT order_id, customer, title, estimated_line_total
FROM order_details
ORDER BY order_id;
```

The query can use ordinary filters, sorting, and aggregation:

```sql
SELECT customer, SUM(estimated_line_total) AS estimated_spend
FROM order_details
GROUP BY customer
ORDER BY estimated_spend DESC;
```

The view makes the repeated join and calculation easier to reuse. It does not remove the need to understand the underlying tables and row grain.

## 3. Create your own view

For example, create a view for in-stock books:

```sql
CREATE VIEW in_stock_books AS
SELECT book_id, title, author, price
FROM books
WHERE in_stock = TRUE;
```

Then query it:

```sql
SELECT title, price
FROM in_stock_books
ORDER BY price DESC;
```

SQLite does not support `CREATE OR REPLACE VIEW`. To redefine a view in SQLite, use `DROP VIEW IF EXISTS name;` followed by `CREATE VIEW name AS ...`. Be careful: dropping a view removes its saved definition.

## 4. When views help

Views are useful to:

- give a long join a short, meaningful name;
- reuse a calculation or filter;
- expose a simpler set of columns to query users.

Views are not automatically faster. A standard view usually runs its underlying query when you select from it. Some database systems also offer materialized views, which store results, but SQLite does not support materialized views as a built-in feature.

## 5. Today's runnable practice

The starter file creates the `in_stock_books` view if it does not already exist, then queries it:

```powershell
python run_sql.py queries/day-23.sql
```

The view remains in your database until you drop it or recreate the database. `setup.sql` resets the database and removes views not defined there.

## 6. Assignment — write these six queries

1. Query `order_details` to show each order ID, title, quantity, and estimated line total.
2. Use `order_details` to calculate estimated revenue by month.
3. Use `order_details` to calculate estimated spend per customer.
4. Create a view called `rated_reviews` containing only reviews with a rating, then query it sorted from highest rating to lowest.
5. Create a view that lists the title, author, and price for out-of-stock books. Query the view.
6. Explain why `order_details` returns one row per order and why it does not include reviewers.

## 7. Self-test — answer without notes

1. Does a standard view normally store a separate copy of its result rows?
2. What does a view save?
3. Can you use `WHERE` and `ORDER BY` when querying a view?
4. Does creating a view automatically make a query faster?
5. Which file defines the course's `order_details` view so it can be recreated?
6. What row grain does `order_details` have?

## 8. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Inspect order details
SELECT order_id, title, quantity, estimated_line_total
FROM order_details
ORDER BY order_id;
```

```sql
-- 2. Estimated revenue by month
SELECT SUBSTR(order_date, 1, 7) AS order_month,
       SUM(estimated_line_total) AS estimated_revenue
FROM order_details
GROUP BY SUBSTR(order_date, 1, 7)
ORDER BY order_month;
```

```sql
-- 3. Estimated spend per customer
SELECT customer, SUM(estimated_line_total) AS estimated_spend
FROM order_details
GROUP BY customer
ORDER BY estimated_spend DESC;
```

```sql
-- 4. Create and query rated_reviews
CREATE VIEW IF NOT EXISTS rated_reviews AS
SELECT review_id, book_id, reviewer, rating, review_text
FROM book_reviews
WHERE rating IS NOT NULL;

SELECT reviewer, rating
FROM rated_reviews
ORDER BY rating DESC, reviewer;
```

```sql
-- 5. Create and query an out-of-stock book view
CREATE VIEW IF NOT EXISTS out_of_stock_books AS
SELECT title, author, price
FROM books
WHERE in_stock = FALSE;

SELECT title, author, price
FROM out_of_stock_books;
```

6. It joins one order row to its one referenced book, so the view has one row per order. Reviews are not part of the order-detail question and joining them could multiply order rows.

Expected monthly estimated revenues: **January 50.50, February 49.50, March 82.50**.

### Self-test solutions

1. No. A standard view stores the query definition and computes rows when queried.
2. The `SELECT` statement that defines its result.
3. Yes. Query it like a table and apply normal query clauses.
4. No. A regular view improves reuse and readability, not automatically performance.
5. `setup.sql`.
6. One row per order.

## 9. Ready for Day 24?

You’re ready when you can explain what query a view encapsulates and identify its row grain. Try Assignment 2 and compare its totals with Day 21.
