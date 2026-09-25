# Day 11 — Create conditional values with `CASE`

**Today's goal:** Use `CASE` to create labels or calculated values based on conditions in each row.

**Suggested time:** 45–60 minutes

**Interactive routine:** Predict the label for each row, write one assignment query at a time in `queries/day-11.sql`, run it, and compare. Try the self-test before opening the answer key.

## 1. `CASE` is SQL's if/then expression

`CASE` checks conditions in order and returns the result for the first condition that is true:

```sql
SELECT title,
       price,
       CASE
           WHEN price >= 25 THEN 'Premium'
           WHEN price >= 15 THEN 'Standard'
           ELSE 'Budget'
       END AS price_band
FROM books;
```

Read it as: if the price is at least 25, call it Premium; otherwise, if it is at least 15, call it Standard; if neither condition matches, call it Budget.

The order matters. Put the most specific or highest threshold first. If `price >= 15` came before `price >= 25`, every premium-priced book would match Standard first and never reach Premium.

## 2. Use `CASE` to label states

```sql
SELECT title,
       CASE
           WHEN in_stock = TRUE THEN 'Available'
           ELSE 'Out of stock'
       END AS stock_status
FROM books;
```

`CASE` returns a value for each input row. It does not filter out rows; for filtering, use `WHERE`.

## 3. Multiple conditions and `NULL`

Conditions inside `CASE` follow the same SQL logic as `WHERE`. A missing rating does not match `rating >= 4`, so it reaches a later `WHEN` or `ELSE`:

```sql
SELECT reviewer,
       CASE
           WHEN rating >= 4 THEN 'Positive'
           WHEN rating IS NULL THEN 'Not rated'
           ELSE 'Below 4'
       END AS review_category
FROM book_reviews;
```

An explicit `WHEN rating IS NULL` makes the missing-value behavior easy to understand. If no `WHEN` matches and there is no `ELSE`, `CASE` returns `NULL`.

## 4. `CASE` can produce numeric values

The results do not have to be text labels. For example, calculate a 10% sale price only for books costing at least 25:

```sql
SELECT title,
       CASE
           WHEN price >= 25 THEN price * 0.90
           ELSE price
       END AS sale_price
FROM books;
```

This changes only the value calculated in the result; it does not update the stored price.

## 5. Use a `CASE` inside an aggregate

Conditional aggregation lets you count selected rows in one grouped result:

```sql
SELECT author,
       SUM(CASE WHEN in_stock = TRUE THEN 1 ELSE 0 END) AS in_stock_count
FROM books
GROUP BY author;
```

For each book, the expression contributes 1 if it is in stock and 0 otherwise. `SUM` adds those values for each author.

## 6. Today's runnable practice

Edit `queries/day-11.sql`, save, and run from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-11.sql
```

## 7. Assignment — write these six queries

1. Show each title, price, and price band: `Premium` for price >= 25, `Standard` for price >= 15, otherwise `Budget`.
2. Show each title and stock label: `Available` or `Out of stock`.
3. Show each reviewer and rating category: `Positive` for rating >= 4, `Not rated` for missing rating, otherwise `Below 4`.
4. Calculate a sale price that gives 10% off books priced at least 25 and leaves other prices unchanged.
5. Count in-stock books per author using conditional aggregation.
6. Count out-of-stock books per author using conditional aggregation.

For each `CASE`, check boundary values carefully. A price exactly 25 should be Premium; a price exactly 15 should be Standard.

## 8. Self-test — answer without notes

1. What does SQL return from a `CASE` expression?
2. Which `WHEN` clause is used if more than one condition is true?
3. What is the purpose of `ELSE`?
4. Does `CASE` remove rows from the result?
5. What does a `CASE` expression without a matching `WHEN` or `ELSE` return?
6. Why does the order of price thresholds matter?

## 9. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Price bands
SELECT title, price,
       CASE
           WHEN price >= 25 THEN 'Premium'
           WHEN price >= 15 THEN 'Standard'
           ELSE 'Budget'
       END AS price_band
FROM books;
```

```sql
-- 2. Stock labels
SELECT title,
       CASE
           WHEN in_stock = TRUE THEN 'Available'
           ELSE 'Out of stock'
       END AS stock_status
FROM books;
```

```sql
-- 3. Review categories
SELECT reviewer, rating,
       CASE
           WHEN rating >= 4 THEN 'Positive'
           WHEN rating IS NULL THEN 'Not rated'
           ELSE 'Below 4'
       END AS review_category
FROM book_reviews;
```

```sql
-- 4. Sale price
SELECT title, price,
       CASE
           WHEN price >= 25 THEN price * 0.90
           ELSE price
       END AS sale_price
FROM books;
```

```sql
-- 5. Count in-stock books per author
SELECT author,
       SUM(CASE WHEN in_stock = TRUE THEN 1 ELSE 0 END) AS in_stock_count
FROM books
GROUP BY author;
```

```sql
-- 6. Count out-of-stock books per author
SELECT author,
       SUM(CASE WHEN in_stock = FALSE THEN 1 ELSE 0 END) AS out_of_stock_count
FROM books
GROUP BY author;
```

Expected price bands: The Quiet River Standard, SQL for Curious Minds Premium, Small Worlds Budget, The Long Weekend Standard. In-stock counts: Mira Sen 2, Arun Das 1, Jo Lee 0. Out-of-stock counts: Mira Sen 0, Arun Das 0, Jo Lee 1.

### Self-test solutions

1. The result value of the first true `WHEN` branch, or the `ELSE` result.
2. The first matching `WHEN` clause.
3. It provides a fallback for rows that match no `WHEN` condition.
4. No. It calculates a value for each row; `WHERE` filters rows.
5. `NULL`.
6. SQL checks the branches in order and stops at the first match.

## 10. Ready for Day 12?

You’re ready when you can write a `CASE` with correctly ordered thresholds and explain how its `ELSE` handles remaining rows. Send your query for Assignment 1 and tell me the price band for each book.
