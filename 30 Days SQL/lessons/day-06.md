# Day 6 — Summarize data with aggregate functions

**Today's goal:** Use `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX` to turn many rows into useful summary values.

**Suggested time:** 45–60 minutes

**Interactive routine:** Predict each result before running it. Write the assignment query in `queries/day-06.sql`, run it, then compare. Try the self-test before checking the answer key and send me your work for feedback.

## 1. What is an aggregate?

An aggregate function takes values from multiple rows and returns a summary. Unlike a regular query that returns one result row for each matching record, an aggregate query usually returns one summary row.

We’ll use `book_orders` (six orders) and `book_reviews` (five reviews, two without ratings).

## 2. Count rows and values

`COUNT(*)` counts rows:

```sql
SELECT COUNT(*) AS order_count
FROM book_orders;
```

`AS order_count` gives the output column a readable name. `COUNT(column)` counts only rows where that column is not `NULL`:

```sql
SELECT COUNT(rating) AS rated_review_count
FROM book_reviews;
```

There are five review rows, but only three have a rating. `COUNT(DISTINCT column)` counts unique non-`NULL` values:

```sql
SELECT COUNT(DISTINCT customer) AS customer_count
FROM book_orders;
```

## 3. Sum and average

`SUM` adds numeric values. `AVG` returns their average:

```sql
SELECT SUM(quantity) AS books_ordered,
       AVG(quantity) AS average_quantity_per_order
FROM book_orders;
```

These calculations use all rows in `book_orders`. `AVG(rating)` ignores missing ratings, just like `COUNT(rating)`:

```sql
SELECT AVG(rating) AS average_rating
FROM book_reviews;
```

SQLite may display an average with a decimal result. Formatting and numeric precision vary by database.

## 4. Minimum and maximum

`MIN` and `MAX` find the smallest and largest values:

```sql
SELECT MIN(price) AS lowest_price,
       MAX(price) AS highest_price
FROM books;
```

They also work with text, where they use the database’s sort order, and with dates stored in ISO format.

## 5. Filter rows before aggregating

`WHERE` determines which rows go into the aggregate:

```sql
SELECT COUNT(*) AS february_orders
FROM book_orders
WHERE order_date >= '2026-02-01'
  AND order_date <  '2026-03-01';
```

This counts the February orders only. At this point, we are producing a single summary for all the rows that passed the filter. Grouping results into one summary per category comes next.

## 6. Today's runnable practice

Edit `queries/day-06.sql` and run it from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-06.sql
```

If your database is missing a table, recreate all course tables with `python setup_database.py`.

## 7. Assignment — write these six queries

For each query, predict the result before running it.

1. Count all rows in `book_orders` and name the result `order_count`.
2. Count the number of distinct customers in `book_orders`.
3. Find the total quantity ordered across all orders.
4. Find the average quantity per order.
5. Find the minimum and maximum book prices.
6. Count how many reviews have a rating and calculate their average rating.

## 8. Self-test — answer without notes

1. What does `COUNT(*)` count?
2. How is `COUNT(rating)` different from `COUNT(*)` when some ratings are `NULL`?
3. Does `AVG(rating)` include missing (`NULL`) ratings in the average?
4. What does `AS average_rating` do?
5. In an aggregate query with a `WHERE` clause, does filtering happen before or after calculating the aggregate?
6. Which aggregate finds the largest value?

## 9. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Count all orders
SELECT COUNT(*) AS order_count
FROM book_orders;
```

```sql
-- 2. Count distinct customers
SELECT COUNT(DISTINCT customer) AS customer_count
FROM book_orders;
```

```sql
-- 3. Total books ordered
SELECT SUM(quantity) AS total_quantity
FROM book_orders;
```

```sql
-- 4. Average quantity per order
SELECT AVG(quantity) AS average_quantity
FROM book_orders;
```

```sql
-- 5. Minimum and maximum book prices
SELECT MIN(price) AS lowest_price,
       MAX(price) AS highest_price
FROM books;
```

```sql
-- 6. Number of rated reviews and their average
SELECT COUNT(rating) AS rated_review_count,
       AVG(rating) AS average_rating
FROM book_reviews;
```

Expected values: **6 orders**; **4 customers**; **8 books total**; **1.3333... books per order**; **12.75 minimum and 32 maximum**; **3 rated reviews with an average rating of 4**.

### Self-test solutions

1. Every row in the filtered input table.
2. `COUNT(rating)` excludes rows where `rating` is `NULL`; `COUNT(*)` does not.
3. No. `AVG` ignores `NULL` values.
4. It gives the result column a name (alias).
5. Filtering happens first; the aggregate summarizes the remaining rows.
6. `MAX`.

## 10. Ready for Day 7?

You’re ready when you can explain the difference between `COUNT(*)` and `COUNT(column)`, and can use an aggregate to summarize the whole filtered table. Send your assignment queries or your predicted results and I’ll review them.
