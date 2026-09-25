# Day 7 — Group and filter summaries

**Today's goal:** Use `GROUP BY` to calculate one aggregate result per category, and `HAVING` to filter those grouped results.

**Suggested time:** 60–75 minutes

**Interactive routine:** Predict each summary, write and run the query in `queries/day-07.sql`, and compare. Complete the test before reading the answer key. Send me your queries and predictions for feedback.

## 1. One summary per group

On Day 6, `COUNT(*)` returned one count for the entire table. `GROUP BY` divides the rows into groups and calculates an aggregate for each group.

```sql
SELECT author, COUNT(*) AS book_count
FROM books
GROUP BY author;
```

This returns one row per author. Mira Sen has two books, while Arun Das and Jo Lee each have one.

## 2. Group by more than one column

You can group on multiple columns. Each unique combination becomes its own group:

```sql
SELECT author, in_stock, COUNT(*) AS book_count
FROM books
GROUP BY author, in_stock
ORDER BY author, in_stock;
```

Mira Sen appears twice here because one group is for her in-stock books and another for her out-of-stock books.

## 3. Filter rows before grouping with `WHERE`

`WHERE` filters individual rows before the groups are calculated:

```sql
SELECT author, COUNT(*) AS in_stock_book_count
FROM books
WHERE in_stock = TRUE
GROUP BY author;
```

Only books in stock are included in each author's count.

## 4. Filter groups after aggregation with `HAVING`

`HAVING` filters groups based on an aggregate result:

```sql
SELECT author, COUNT(*) AS book_count
FROM books
GROUP BY author
HAVING COUNT(*) >= 2;
```

This returns only authors with at least two books. The difference is:

- `WHERE` decides which rows go into the groups.
- `HAVING` decides which completed groups appear in the result.

You can use both:

```sql
SELECT author, COUNT(*) AS in_stock_book_count
FROM books
WHERE in_stock = TRUE
GROUP BY author
HAVING COUNT(*) >= 2;
```

## 5. A useful query shape

For this week's queries, clauses generally appear in this order:

```sql
SELECT grouping_column, aggregate_function(...)
FROM table_name
WHERE row_condition
GROUP BY grouping_column
HAVING aggregate_condition
ORDER BY grouping_column;
```

Each selected value should either be included in the `GROUP BY` or be inside an aggregate such as `COUNT`, `SUM`, or `AVG`. Otherwise, SQL cannot determine which value to show for the whole group, and many databases will reject the query.

## 6. Today's runnable practice

Edit `queries/day-07.sql`, save, and run from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-07.sql
```

## 7. Assignment — write these six queries

For each query, predict the groups and results before running it.

1. Count books per author. Show the author and count.
2. Calculate the average book price per author. Show the author and average price.
3. Count orders per customer. Sort from the customer with the most orders to the fewest.
4. Calculate total quantity ordered per customer. Show only customers whose total quantity is greater than 1.
5. Count reviews with a rating per `book_id`. Exclude reviews where the rating is missing. (There is one review per book in the current data except book 1, which has two.)
6. Count books in stock per author, but show only authors with at least two in-stock books.

## 8. Self-test — answer without notes

1. What does `GROUP BY author` do?
2. Which clause filters individual input rows before grouping?
3. Which clause filters groups after calculating aggregates?
4. Can you select a plain column in a grouped query if it is neither grouped nor aggregated?
5. In a query with `WHERE` and `HAVING`, which one is applied first conceptually?
6. What does this query return?

   ```sql
   SELECT customer, SUM(quantity) AS total_quantity
   FROM book_orders
   GROUP BY customer
   HAVING SUM(quantity) > 1;
   ```

## 9. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Number of books per author
SELECT author, COUNT(*) AS book_count
FROM books
GROUP BY author;
```

```sql
-- 2. Average price per author
SELECT author, AVG(price) AS average_price
FROM books
GROUP BY author;
```

```sql
-- 3. Orders per customer, most to fewest
SELECT customer, COUNT(*) AS order_count
FROM book_orders
GROUP BY customer
ORDER BY order_count DESC;
```

```sql
-- 4. Customers with total quantity greater than 1
SELECT customer, SUM(quantity) AS total_quantity
FROM book_orders
GROUP BY customer
HAVING SUM(quantity) > 1;
```

```sql
-- 5. Count rated reviews per book
SELECT book_id, COUNT(rating) AS rated_review_count
FROM book_reviews
WHERE rating IS NOT NULL
GROUP BY book_id;
```

```sql
-- 6. Authors with at least two in-stock books
SELECT author, COUNT(*) AS in_stock_book_count
FROM books
WHERE in_stock = TRUE
GROUP BY author
HAVING COUNT(*) >= 2;
```

Expected summaries: **Mira Sen 2, Arun Das 1, Jo Lee 1**; average prices **Mira Sen 21.25, Arun Das 32, Jo Lee 12.75**; order counts **Asha Rao 2, Ben Cole 2, Chen Wu 1, Dina Shah 1**; quantity totals over 1 **Asha Rao 3, Dina Shah 2**; rated-review counts **book 1: 2, book 3: 1**; query 6 returns **Mira Sen: 2**.

### Self-test solutions

1. It puts rows with the same author into a group, so aggregates can be computed per author.
2. `WHERE`.
3. `HAVING`.
4. No. Include it in `GROUP BY` or aggregate it.
5. `WHERE` is applied first, then grouping and aggregate calculations, then `HAVING` filters the groups.
6. One row per customer whose total ordered quantity is greater than 1: Asha Rao (3) and Dina Shah (2).

## 10. Ready for Week 2?

You’re ready when you can choose between `WHERE` and `HAVING` and explain why every selected non-aggregate column belongs in `GROUP BY`. Send me your assignment queries or explain one result in your own words; next we’ll begin combining tables with joins.
