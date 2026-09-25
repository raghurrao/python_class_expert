# Day 21 — Week 3 review: analyze a bookshop

**Today's goal:** Combine joins, filters, aggregates, CTEs, and window functions in a small end-to-end analysis.

**Suggested time:** 75–90 minutes

**Interactive routine:** Attempt the mini-project before reading the answer key. For each query, define what one output row represents, write your SQL in `queries/day-21.sql`, and predict the key totals.

## 1. Business questions

The sample database contains books, orders, and reviews. Today, answer questions a bookseller might ask:

1. How much revenue did each month generate?
2. Which customers ordered the most units?
3. How many books did each author sell, and what was the revenue per author?
4. Which books have a rating of at least 4?
5. Which customer ranks first by total quantity, and who ties with them?

For this lesson, define estimated revenue as `quantity * price`. The data does not include discounts, shipping, refunds, or actual payment records, so this is a simplified calculation.

## 2. Suggested approach

Break the questions into steps:

1. Join `book_orders` to `books` using `book_id` to get the book price.
2. Calculate row-level extended value as `quantity * price`.
3. Group by month, customer, or author depending on the question.
4. Use a CTE to name a summary when you need another step, such as ranking customers.
5. Use `EXISTS` when you only need to check for a related review.

Be careful not to join reviews into the order revenue query: multiple reviews could repeat an order and inflate revenue.

## 3. Assignment — mini-project

Write and run each query. Before running, state the grain and predict the result.

1. Calculate estimated revenue per month. Show month and revenue in date order.
2. Calculate total quantity ordered per customer, highest first.
3. Calculate total quantity ordered and estimated revenue per author. Show one row per author.
4. List books that have at least one review rated 4 or higher, using `EXISTS`.
5. Rank customers by total quantity ordered. Use `RANK` so ties share a rank.
6. Bonus: show each customer’s total quantity and the overall average customer quantity on every row. Use a CTE plus a scalar subquery or window average.

## 4. Self-test — answer without notes

1. Which columns connect orders and books?
2. Why should the revenue query avoid joining `book_reviews`?
3. What should one row represent in the monthly revenue query?
4. What is the estimated revenue formula used here?
5. Which ranking function gives tied customers the same rank?
6. What limitation should you mention when reporting this estimated revenue?

## 5. Answer key — check after trying

### Mini-project solutions

```sql
-- 1. Estimated revenue per month
SELECT strftime('%Y-%m', o.order_date) AS order_month,
       SUM(o.quantity * b.price) AS estimated_revenue
FROM book_orders AS o
INNER JOIN books AS b
    ON o.book_id = b.book_id
GROUP BY strftime('%Y-%m', o.order_date)
ORDER BY order_month;
```

Expected: **2026-01 = 50.50, 2026-02 = 49.50, 2026-03 = 82.50**.

```sql
-- 2. Total quantity by customer
SELECT customer, SUM(quantity) AS total_quantity
FROM book_orders
GROUP BY customer
ORDER BY total_quantity DESC, customer;
```

Expected: **Asha Rao 3, Ben Cole 2, Dina Shah 2, Chen Wu 1**.

```sql
-- 3. Quantity and estimated revenue per author
SELECT b.author,
       SUM(o.quantity) AS total_quantity,
       SUM(o.quantity * b.price) AS estimated_revenue
FROM book_orders AS o
INNER JOIN books AS b
    ON o.book_id = b.book_id
GROUP BY b.author
ORDER BY b.author;
```

Expected: **Arun Das: quantity 3, revenue 96; Jo Lee: quantity 2, revenue 25.50; Mira Sen: quantity 3, revenue 61**.

```sql
-- 4. Books with a review rated 4 or higher
SELECT b.title
FROM books AS b
WHERE EXISTS (
    SELECT 1
    FROM book_reviews AS r
    WHERE r.book_id = b.book_id
      AND r.rating >= 4
);
```

Expected: **The Quiet River, Small Worlds**.

```sql
-- 5. Rank customers by total quantity, preserving ties
WITH customer_totals AS (
    SELECT customer, SUM(quantity) AS total_quantity
    FROM book_orders
    GROUP BY customer
)
SELECT customer, total_quantity,
       RANK() OVER (ORDER BY total_quantity DESC) AS quantity_rank
FROM customer_totals
ORDER BY quantity_rank, customer;
```

Expected: **Asha Rao rank 1; Ben Cole and Dina Shah rank 2; Chen Wu rank 4**.

```sql
-- 6. Customer totals with the overall average on every row
WITH customer_totals AS (
    SELECT customer, SUM(quantity) AS total_quantity
    FROM book_orders
    GROUP BY customer
)
SELECT customer, total_quantity,
       AVG(total_quantity) OVER () AS average_customer_quantity
FROM customer_totals;
```

Expected average customer quantity: **2**.

### Self-test solutions

1. `book_orders.book_id = books.book_id`.
2. Each order can match multiple reviews, multiplying order rows and inflating revenue.
3. One row per calendar month.
4. `quantity * price`.
5. `RANK` (and `DENSE_RANK` also shares ranks, with different numbering after ties).
6. It is an estimate based only on quantity and listed price, without discounts, shipping, refunds, or confirmed payment information.

## 6. Week 3 checkpoint

You’re ready to move on when you can explain the join path, the grain of each result, and why the revenue query must avoid review fan-out. Send me your Assignment 1 query and the monthly totals you expect.
