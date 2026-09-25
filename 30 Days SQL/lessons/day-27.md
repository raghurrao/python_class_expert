# Day 27 — Capstone: build sales summaries

**Today's goal:** Build monthly, customer, book, and author sales summaries with joins and aggregates.

**Suggested time:** 60–90 minutes

**Interactive routine:** For each summary, state its grain (one row per what?), predict the totals, then write and run the query in `queries/day-27.sql`. Compare with the answer key afterward.

## 1. Monthly performance

The `order_details` view has one row per order row and already includes `estimated_line_total`. Group it by month:

```sql
SELECT SUBSTR(order_date, 1, 7) AS order_month,
       COUNT(*) AS order_count,
       SUM(estimated_line_total) AS estimated_revenue
FROM order_details
GROUP BY SUBSTR(order_date, 1, 7)
ORDER BY order_month;
```

`SUBSTR(order_date, 1, 7)` extracts `YYYY-MM` from the ISO date. This uses the same estimated revenue definition from the project brief.

## 2. Customer activity

Group the detail rows by customer to count order rows, sum units, and sum estimated revenue:

```sql
SELECT customer,
       COUNT(*) AS order_count,
       SUM(quantity) AS units_ordered,
       SUM(estimated_line_total) AS estimated_revenue
FROM order_details
GROUP BY customer
ORDER BY estimated_revenue DESC;
```

The grain is one row per customer. `order_count` counts order rows in this teaching dataset; a production system may need `COUNT(DISTINCT order_id)` if there are multiple lines per order.

## 3. Book performance

Start from `books` and left join orders so every book can appear, even if it has no orders:

```sql
SELECT b.book_id, b.title,
       COUNT(o.order_id) AS order_count,
       COALESCE(SUM(o.quantity), 0) AS units_ordered,
       COALESCE(SUM(o.quantity * b.price), 0) AS estimated_revenue
FROM books AS b
LEFT JOIN book_orders AS o
    ON b.book_id = o.book_id
GROUP BY b.book_id, b.title
ORDER BY estimated_revenue DESC;
```

Use `COUNT(o.order_id)`, not `COUNT(*)`: an unmatched book still produces one left-join result row, so `COUNT(*)` would incorrectly count an order. `COALESCE` displays zero when there are no matching order rows.

## 4. Author performance

Join books to their order rows, then group by author:

```sql
SELECT b.author,
       SUM(o.quantity) AS units_ordered,
       SUM(o.quantity * b.price) AS estimated_revenue
FROM books AS b
INNER JOIN book_orders AS o
    ON b.book_id = o.book_id
GROUP BY b.author
ORDER BY estimated_revenue DESC;
```

Do not join reviews into this sales summary; reviews are not needed for the metric and could duplicate sales rows.

## 5. Today's runnable practice

Edit `queries/day-27.sql`, save, and run from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-27.sql
```

The starter file calculates the monthly summary. Replace it with another capstone query to practice.

## 6. Assignment — build four summaries

1. One row per month: `order_count` and `estimated_revenue`.
2. One row per customer: `order_count`, `units_ordered`, and `estimated_revenue`, sorted by revenue descending.
3. One row per book, including books without orders: order count, units, and estimated revenue.
4. One row per author: units and estimated revenue, sorted by revenue descending.

For each result, write the grain before the SQL. Compare its expected values with the answer key.

## 7. Self-test — answer without notes

1. What does the `order_details` view contribute to the monthly summary?
2. Why does the book summary use `LEFT JOIN`?
3. Why use `COUNT(o.order_id)` instead of `COUNT(*)` in that left-join summary?
4. Why is `COALESCE` used for book units and revenue?
5. Why should reviews be excluded from the sales aggregation join?
6. What assumption does `COUNT(*) AS order_count` make in the customer summary?

## 8. Answer key — check after trying

### Assignment solutions

```sql
-- 1. One row per month
SELECT SUBSTR(order_date, 1, 7) AS order_month,
       COUNT(*) AS order_count,
       SUM(estimated_line_total) AS estimated_revenue
FROM order_details
GROUP BY SUBSTR(order_date, 1, 7)
ORDER BY order_month;
```

```sql
-- 2. One row per customer
SELECT customer,
       COUNT(*) AS order_count,
       SUM(quantity) AS units_ordered,
       SUM(estimated_line_total) AS estimated_revenue
FROM order_details
GROUP BY customer
ORDER BY estimated_revenue DESC;
```

```sql
-- 3. One row per book, including those without orders
SELECT b.book_id, b.title,
       COUNT(o.order_id) AS order_count,
       COALESCE(SUM(o.quantity), 0) AS units_ordered,
       COALESCE(SUM(o.quantity * b.price), 0) AS estimated_revenue
FROM books AS b
LEFT JOIN book_orders AS o
    ON b.book_id = o.book_id
GROUP BY b.book_id, b.title
ORDER BY estimated_revenue DESC;
```

```sql
-- 4. One row per author
SELECT b.author,
       SUM(o.quantity) AS units_ordered,
       SUM(o.quantity * b.price) AS estimated_revenue
FROM books AS b
INNER JOIN book_orders AS o
    ON b.book_id = o.book_id
GROUP BY b.author
ORDER BY estimated_revenue DESC;
```

Expected monthly summary: **Jan: 2 orders / 50.50; Feb: 2 / 49.50; Mar: 2 / 82.50**. Customer summary: **Asha: 2 / 3 units / 44; Ben: 2 / 2 / 50.50; Chen: 1 / 1 / 24; Dina: 1 / 2 / 64**. Book summary: **SQL for Curious Minds: 2 / 3 / 96; The Quiet River: 2 / 2 / 37; Small Worlds: 1 / 2 / 25.50; The Long Weekend: 1 / 1 / 24**. Author summary: **Arun Das: 3 / 96; Mira Sen: 3 / 61; Jo Lee: 2 / 25.50**.

### Self-test solutions

1. It joins orders to books and calculates an estimated line total for each order row.
2. To keep books that have no matching order rows.
3. The unmatched row has a `NULL` order ID; `COUNT(order_id)` ignores it, while `COUNT(*)` would count it.
4. `SUM` returns `NULL` when there are no non-`NULL` values; `COALESCE` displays zero for no orders.
5. Multiple reviews can duplicate order rows and inflate sums.
6. It assumes one row in this dataset corresponds to one order. A multi-line order schema would require a distinct order ID or a separate order header table.

## 9. Ready for Day 28?

You’re ready when your four summary grains are clear and the totals match. Send me your monthly summary query and tell me how you handled books with no orders.
