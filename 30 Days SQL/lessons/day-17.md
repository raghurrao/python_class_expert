# Day 17 — Rank rows with window functions

**Today's goal:** Use window functions to rank rows while keeping the detail rows in the result.

**Suggested time:** 60–75 minutes

**Interactive routine:** Predict the ranking and ties, write queries in `queries/day-17.sql`, run them, and explain the result. Complete the self-test before checking the key.

## 1. Aggregate versus window function

`GROUP BY` collapses many input rows into one row per group. A window function calculates across related rows but keeps each row in the result.

The `OVER (...)` clause defines the window of rows a function can consider:

```sql
SELECT order_id, customer, quantity,
       ROW_NUMBER() OVER (ORDER BY order_date) AS sequence_number
FROM book_orders;
```

Each order stays visible and receives a sequence number based on the date.

## 2. Rank rows with `ROW_NUMBER`, `RANK`, and `DENSE_RANK`

These functions assign positions according to the order inside `OVER`:

- `ROW_NUMBER()` gives every row a unique number.
- `RANK()` gives ties the same rank and leaves gaps after ties.
- `DENSE_RANK()` gives ties the same rank without gaps.

Compare the three functions for customer order counts:

```sql
WITH customer_orders AS (
    SELECT customer, COUNT(*) AS order_count
    FROM book_orders
    GROUP BY customer
)
SELECT customer, order_count,
       ROW_NUMBER() OVER (ORDER BY order_count DESC) AS row_number,
       RANK() OVER (ORDER BY order_count DESC) AS rank_number,
       DENSE_RANK() OVER (ORDER BY order_count DESC) AS dense_rank_number
FROM customer_orders
ORDER BY order_count DESC, customer;
```

Asha Rao and Ben Cole tie with two orders. Their `RANK()` values are both 1, then Chen Wu and Dina Shah share rank 3. `DENSE_RANK()` assigns Chen and Dina rank 2. `ROW_NUMBER()` still assigns a distinct position to every row; with a tie, its ordering between tied rows is not guaranteed unless you add another sort key in the window.

## 3. Partition rankings into groups

`PARTITION BY` restarts the function for each group. Rank the books by price within each author:

```sql
SELECT author, title, price,
       RANK() OVER (
           PARTITION BY author
           ORDER BY price DESC
       ) AS price_rank
FROM books
ORDER BY author, price_rank;
```

The rank starts again for each author. `PARTITION BY` does not collapse rows like `GROUP BY`; it just defines which rows are compared by the window function.

## 4. Window ordering is not output ordering

The `ORDER BY` inside `OVER` controls the calculation. The final `ORDER BY` controls the displayed row order. Use both when you need a ranked calculation and a particular output order.

```sql
SELECT title, price,
       ROW_NUMBER() OVER (ORDER BY price DESC) AS price_position
FROM books
ORDER BY title;
```

This assigns positions by price but displays the rows alphabetically by title.

## 5. Today's runnable practice

Edit `queries/day-17.sql`, save, and run from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-17.sql
```

## 6. Assignment — write these six queries

1. Number all orders from earliest to latest using `ROW_NUMBER`.
2. Rank customers by total quantity ordered, highest first.
3. Show both `RANK` and `DENSE_RANK` for customers ranked by number of orders.
4. Rank book prices within each author, highest price first.
5. Rank reviewers by rating, highest first, while excluding unrated reviews.
6. Number the orders separately for each customer, ordered by date. Add `order_id` as a tie-breaker.

For every query, identify the partition, if any, and the window ordering.

## 7. Self-test — answer without notes

1. Does a window function collapse a group to one row like `GROUP BY`?
2. What does `PARTITION BY` do?
3. How do `RANK` and `DENSE_RANK` differ after a tie?
4. Does `ORDER BY` inside `OVER` necessarily control the displayed row order?
5. Why should a `ROW_NUMBER` window use a tie-breaker when ordering values can tie?
6. How can you exclude unrated reviews from a ranking?

## 8. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Sequence orders by date
SELECT order_id, order_date, customer,
       ROW_NUMBER() OVER (ORDER BY order_date, order_id) AS order_number
FROM book_orders;
```

```sql
-- 2. Rank customers by total quantity
WITH customer_totals AS (
    SELECT customer, SUM(quantity) AS total_quantity
    FROM book_orders
    GROUP BY customer
)
SELECT customer, total_quantity,
       RANK() OVER (ORDER BY total_quantity DESC) AS quantity_rank
FROM customer_totals;
```

```sql
-- 3. Compare rank functions for order counts
WITH customer_orders AS (
    SELECT customer, COUNT(*) AS order_count
    FROM book_orders
    GROUP BY customer
)
SELECT customer, order_count,
       RANK() OVER (ORDER BY order_count DESC) AS rank_number,
       DENSE_RANK() OVER (ORDER BY order_count DESC) AS dense_rank_number
FROM customer_orders;
```

```sql
-- 4. Rank prices within each author
SELECT author, title, price,
       RANK() OVER (PARTITION BY author ORDER BY price DESC) AS price_rank
FROM books;
```

```sql
-- 5. Rank only rated reviews
SELECT reviewer, rating,
       RANK() OVER (ORDER BY rating DESC) AS rating_rank
FROM book_reviews
WHERE rating IS NOT NULL;
```

```sql
-- 6. Number orders per customer, ordered by date and unique tie-breaker
SELECT customer, order_id, order_date,
       ROW_NUMBER() OVER (
           PARTITION BY customer
           ORDER BY order_date, order_id
       ) AS customer_order_number
FROM book_orders;
```

Expected order-count ranking: Asha Rao and Ben Cole tie at rank 1; Chen Wu and Dina Shah tie at rank 3. Dense ranks are 1 and 2. Quantity ranking: Asha Rao rank 1, Ben Cole rank 2, Dina Shah rank 2, Chen Wu rank 4.

### Self-test solutions

1. No. It retains the input rows and adds a calculated value.
2. It divides rows into independent windows; the function restarts in each partition.
3. `RANK` leaves a gap after ties; `DENSE_RANK` does not.
4. No. Use the query's final `ORDER BY` to control display order.
5. A tie-breaker makes the row-number assignment predictable and repeatable.
6. Filter with `WHERE rating IS NOT NULL` before the window calculation.

## 9. Ready for Day 18?

You’re ready when you can describe the difference between the window order and the final output order, and explain how ties affect the three ranking functions. Send me your query for Assignment 6 and explain what the partition does.
