# Day 12 — Use subqueries

**Today's goal:** Put one query inside another to use its result as a value or list of values.

**Suggested time:** 60–75 minutes

**Interactive routine:** Predict what the inner query returns first, then predict the outer result. Write the assignment queries in `queries/day-12.sql`, run them, and compare. Try the self-test before the answer key.

## 1. What is a subquery?

A subquery is a query inside another SQL statement. Parentheses make the inner query a unit. Start by understanding the inner query, then see how the outer query uses its result.

This query finds books priced above the average book price:

```sql
SELECT title, price
FROM books
WHERE price > (
    SELECT AVG(price)
    FROM books
);
```

The inner query returns one value: the average price. The outer query compares each book's price with that value. The average here is 21.8125, so the books priced 24 and 32 are returned.

## 2. Scalar subqueries

A scalar subquery returns one value (one row and one column). It can be used anywhere a single value makes sense:

```sql
SELECT title,
       price,
       (SELECT AVG(price) FROM books) AS overall_average
FROM books;
```

The average is displayed next to each book. This is useful for comparisons, although the same value repeats on every row.

## 3. Subqueries that return a list with `IN`

An `IN` subquery returns a single column with zero or more values. For example, list books that have at least one review with a rating of 4 or higher:

```sql
SELECT title
FROM books
WHERE book_id IN (
    SELECT book_id
    FROM book_reviews
    WHERE rating >= 4
);
```

The inner query returns book IDs 1 and 3. The outer query finds the corresponding books. `IN` checks membership in the returned list.

## 4. Subquery result shape matters

- A scalar comparison such as `price > (...)` needs the inner query to return one value.
- `IN (...)` needs the inner query to return one column; it may return multiple rows.
- The inner query can read a different table from the outer query.

If a scalar subquery returns multiple rows, many databases report an error. Design the inner query so its result matches how the outer query will use it.

## 5. Today's runnable practice

Edit `queries/day-12.sql`, save, and run from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-12.sql
```

## 6. Assignment — write these six queries

For every assignment, write down what you expect the inner query to return before completing the outer query.

1. Show each book whose price is below the overall average price.
2. Show every book's title and price, and include the average book price in a column called `overall_average`.
3. Show the titles of books with a review rating of 4 or higher, using `IN` with a subquery.
4. Show order IDs for orders whose book has a review with a missing rating, using `IN` and a subquery on `book_reviews`.
5. Show the authors who have at least one book priced above the average book price. Use `DISTINCT` to avoid repeating an author.
6. Find the highest price and show the title(s) of book(s) at that price. Use a scalar subquery with `MAX`.

## 7. Self-test — answer without notes

1. What is a subquery?
2. What should a scalar subquery return?
3. How does `IN (subquery)` use the subquery result?
4. In the above-average-price example, which query runs conceptually to get the comparison value?
5. What shape does the subquery for `IN` need to return?
6. If an author has two expensive books, why might the result repeat their name?

## 8. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Books below the average price
SELECT title, price
FROM books
WHERE price < (
    SELECT AVG(price)
    FROM books
);
```

```sql
-- 2. Include the overall average on every row
SELECT title, price,
       (SELECT AVG(price) FROM books) AS overall_average
FROM books;
```

```sql
-- 3. Books with at least one rating of 4 or higher
SELECT title
FROM books
WHERE book_id IN (
    SELECT book_id
    FROM book_reviews
    WHERE rating >= 4
);
```

```sql
-- 4. Orders for books that have an unrated review
SELECT order_id
FROM book_orders
WHERE book_id IN (
    SELECT book_id
    FROM book_reviews
    WHERE rating IS NULL
);
```

```sql
-- 5. Authors with a book above the average price
SELECT DISTINCT author
FROM books
WHERE price > (
    SELECT AVG(price)
    FROM books
);
```

```sql
-- 6. Book or books with the maximum price
SELECT title, price
FROM books
WHERE price = (
    SELECT MAX(price)
    FROM books
);
```

Expected results: **Small Worlds** below average; overall average **21.8125**; books with rating >= 4 are **The Quiet River, Small Worlds**; orders for books with an unrated review are **2 and 6**; authors above average are **Arun Das and Mira Sen**; maximum-priced title is **SQL for Curious Minds (32)**.

### Self-test solutions

1. A query nested inside another query.
2. One row and one column (one value).
3. It checks whether the outer value matches any value returned by the inner query.
4. `SELECT AVG(price) FROM books` returns one average value.
5. One column; it can contain multiple rows.
6. The outer query has one row per qualifying book, so an author with two such books appears twice unless you use `DISTINCT` or group the result.

## 9. Ready for Day 13?

You’re ready when you can tell whether a subquery returns one value or a list, and explain how the outer query uses it. Send me Assignment 3 and the book IDs you expect the inner query to return.
