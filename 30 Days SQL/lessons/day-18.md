# Day 18 — Calculate running totals and compare rows

**Today's goal:** Use window frames for running totals and moving averages, and use `LAG` / `LEAD` to compare a row with its neighbor.

**Suggested time:** 60–75 minutes

**Interactive routine:** For each query, say how rows are ordered and which rows are included in the calculation. Try the assignments in `queries/day-18.sql`, run them, and compare with the answer key.

## 1. Running totals with a window frame

A running total adds the current row to all earlier rows in the ordered window:

```sql
SELECT order_id, order_date, customer, quantity,
       SUM(quantity) OVER (
           ORDER BY order_date, order_id
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_quantity
FROM book_orders
ORDER BY order_date, order_id;
```

The frame `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` means “from the first row in the window through this row.” Including `order_id` gives a stable order if two orders share a date.

## 2. Running totals per customer

Add `PARTITION BY customer` to restart the running total for each customer:

```sql
SELECT customer, order_id, order_date, quantity,
       SUM(quantity) OVER (
           PARTITION BY customer
           ORDER BY order_date, order_id
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS customer_running_quantity
FROM book_orders
ORDER BY customer, order_date, order_id;
```

Each customer's first order starts a new cumulative total.

## 3. Moving averages with a limited frame

A moving average uses only a fixed number of nearby rows. This example averages the current order and the immediately previous order for each customer:

```sql
SELECT customer, order_id, order_date, quantity,
       AVG(quantity) OVER (
           PARTITION BY customer
           ORDER BY order_date, order_id
           ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
       ) AS recent_two_order_average
FROM book_orders;
```

For the first order in each customer's partition, only one row is available, so the result is that order's quantity. For later rows, the frame includes up to two rows.

## 4. Compare with the previous or next row

`LAG(column)` reads a value from an earlier row in the window. `LEAD(column)` reads a value from a later row:

```sql
SELECT customer, order_id, order_date, quantity,
       LAG(quantity) OVER (
           PARTITION BY customer
           ORDER BY order_date, order_id
       ) AS previous_quantity,
       LEAD(quantity) OVER (
           PARTITION BY customer
           ORDER BY order_date, order_id
       ) AS next_quantity
FROM book_orders
ORDER BY customer, order_date, order_id;
```

The first row in a customer's partition has no previous row, so `LAG` returns `NULL`. The last has no next row, so `LEAD` returns `NULL`. You can provide a default value as the second argument, such as `LAG(quantity, 1, 0)`.

## 5. Calculate changes between rows

You can subtract a lagged value from the current value:

```sql
SELECT customer, order_id, quantity,
       quantity - LAG(quantity) OVER (
           PARTITION BY customer
           ORDER BY order_date, order_id
       ) AS change_from_previous_order
FROM book_orders;
```

The first order per customer has a `NULL` change because there is no previous quantity to compare.

## 6. Today's runnable practice

Edit `queries/day-18.sql`, save, and run from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-18.sql
```

## 7. Assignment — write these six queries

1. Calculate a running total of quantity across all orders in date order.
2. Calculate a separate running total of quantity for each customer.
3. Calculate the moving average of the current and previous order quantities per customer.
4. Show each order and the quantity of the customer's previous order.
5. Calculate the change in quantity from each customer's previous order.
6. Show the next order date for each customer with `LEAD`.

For all order-sequence calculations, use `order_date, order_id` as the window ordering to make ties deterministic.

## 8. Self-test — answer without notes

1. What does `UNBOUNDED PRECEDING` mean in a running total frame?
2. What does `PARTITION BY customer` do to a running total?
3. How many rows does `ROWS BETWEEN 1 PRECEDING AND CURRENT ROW` include at most?
4. What does `LAG` return for the first row in a partition by default?
5. What does the second argument to `LAG(quantity, 1, 0)` mean?
6. Why include a unique tie-breaker in the window ordering?

## 9. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Running quantity across all orders
SELECT order_id, order_date, quantity,
       SUM(quantity) OVER (
           ORDER BY order_date, order_id
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_quantity
FROM book_orders;
```

```sql
-- 2. Running quantity per customer
SELECT customer, order_id, order_date, quantity,
       SUM(quantity) OVER (
           PARTITION BY customer
           ORDER BY order_date, order_id
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS customer_running_quantity
FROM book_orders;
```

```sql
-- 3. Average of up to the current and previous order
SELECT customer, order_id, quantity,
       AVG(quantity) OVER (
           PARTITION BY customer
           ORDER BY order_date, order_id
           ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
       ) AS recent_two_order_average
FROM book_orders;
```

```sql
-- 4. Previous order quantity
SELECT customer, order_id, quantity,
       LAG(quantity) OVER (
           PARTITION BY customer
           ORDER BY order_date, order_id
       ) AS previous_quantity
FROM book_orders;
```

```sql
-- 5. Change since the prior order
SELECT customer, order_id, quantity,
       quantity - LAG(quantity) OVER (
           PARTITION BY customer
           ORDER BY order_date, order_id
       ) AS change_from_previous_order
FROM book_orders;
```

```sql
-- 6. Next order date for each customer
SELECT customer, order_id, order_date,
       LEAD(order_date) OVER (
           PARTITION BY customer
           ORDER BY order_date, order_id
       ) AS next_order_date
FROM book_orders;
```

Expected running total across all orders: **1, 2, 4, 5, 6, 8**. Per-customer final totals: **Asha 3, Ben 2, Chen 1, Dina 2**. `LAG` and `LEAD` return `NULL` where there is no prior or next row in that customer's sequence.

### Self-test solutions

1. Start at the first row of the partition/window.
2. It restarts the running total for each customer.
3. At most two rows: the previous row and the current row.
4. `NULL`, because there is no earlier row.
5. The default value to use if the requested earlier row does not exist.
6. It makes the row sequence and calculations deterministic when primary sort values tie.

## 10. Ready for Day 19?

You’re ready when you can explain the window frame and why `LAG` returns `NULL` at a partition boundary. Send me your Assignment 2 query and the final running quantity for each customer.
