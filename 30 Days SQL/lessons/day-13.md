# Day 13 — Test related rows with `EXISTS`

**Today's goal:** Use `EXISTS` and `NOT EXISTS` to check whether a related row exists, including with a correlated subquery.

**Suggested time:** 60–75 minutes

**Interactive routine:** Identify the outer row and the matching inner rows. Write the assignment queries in `queries/day-13.sql`, predict results, run them, and then check the answer key.

## 1. What `EXISTS` answers

`EXISTS` asks a yes/no question: “Does this subquery return at least one row?” It does not return the subquery's columns; it returns true or false for each outer row.

Find books that have at least one review:

```sql
SELECT b.title
FROM books AS b
WHERE EXISTS (
    SELECT 1
    FROM book_reviews AS r
    WHERE r.book_id = b.book_id
);
```

All four books appear because each has a review. `SELECT 1` is a conventional choice: the value selected does not matter; `EXISTS` only cares whether a row exists.

## 2. Correlated subqueries

The condition `r.book_id = b.book_id` refers to `b`, an alias from the outer query. That makes this a correlated subquery. Conceptually, the database checks the inner query for each book in the outer query.

Find books that have a rating of 5:

```sql
SELECT b.title
FROM books AS b
WHERE EXISTS (
    SELECT 1
    FROM book_reviews AS r
    WHERE r.book_id = b.book_id
      AND r.rating = 5
);
```

Unlike a normal join, this returns each qualifying book once even if it has several matching reviews. It tests existence; it does not add one output row per review.

## 3. Use `NOT EXISTS` for missing related rows

`NOT EXISTS` keeps outer rows for which the subquery finds no match:

```sql
SELECT b.title
FROM books AS b
WHERE NOT EXISTS (
    SELECT 1
    FROM book_reviews AS r
    WHERE r.book_id = b.book_id
      AND r.rating = 5
);
```

This returns books without any rating-5 review. This pattern is often useful for “find records that have no related record” questions.

## 4. `EXISTS` compared with a join

If you need columns from both tables, use a join. If you only need to test whether a related row exists, `EXISTS` often describes the intention more directly and avoids duplicates from multiple matches.

For example, a join to reviews may return the same book more than once when several reviews match. `EXISTS` returns one outer book row if at least one match exists.

## 5. Today's runnable practice

Edit `queries/day-13.sql`, save, then run from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-13.sql
```

## 6. Assignment — write these six queries

For each, state which outer table supplies the rows and what matching condition the inner query checks.

1. Show books that have at least one order, using `EXISTS`.
2. Show books that have at least one unrated review, using `EXISTS` and `rating IS NULL`.
3. Show books that do not have any rating-5 review, using `NOT EXISTS`.
4. Show orders for which the referenced book has at least one review with a rating of 4 or higher. Use `EXISTS` correlated to the order's `book_id`.
5. Show authors who have at least one book priced over 20, using `EXISTS` correlated to the outer author.
6. Count the books with at least one rating-5 review. Use `EXISTS` so a book is counted once even if it has multiple rating-5 reviews.

## 7. Self-test — answer without notes

1. What does `EXISTS` check?
2. Does `EXISTS` return columns from its subquery?
3. What makes a subquery correlated?
4. Why can `EXISTS` avoid duplicate outer rows that a join could create?
5. What does `NOT EXISTS` mean?
6. In the sample database, which book has a rating-5 review?

## 8. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Books with at least one order
SELECT b.title
FROM books AS b
WHERE EXISTS (
    SELECT 1
    FROM book_orders AS o
    WHERE o.book_id = b.book_id
);
```

```sql
-- 2. Books with an unrated review
SELECT b.title
FROM books AS b
WHERE EXISTS (
    SELECT 1
    FROM book_reviews AS r
    WHERE r.book_id = b.book_id
      AND r.rating IS NULL
);
```

```sql
-- 3. Books with no rating-5 review
SELECT b.title
FROM books AS b
WHERE NOT EXISTS (
    SELECT 1
    FROM book_reviews AS r
    WHERE r.book_id = b.book_id
      AND r.rating = 5
);
```

```sql
-- 4. Orders whose book has a review rated 4 or higher
SELECT o.order_id, o.customer
FROM book_orders AS o
WHERE EXISTS (
    SELECT 1
    FROM book_reviews AS r
    WHERE r.book_id = o.book_id
      AND r.rating >= 4
);
```

```sql
-- 5. Authors with at least one book over 20
SELECT DISTINCT b.author
FROM books AS b
WHERE EXISTS (
    SELECT 1
    FROM books AS b2
    WHERE b2.author = b.author
      AND b2.price > 20
);
```

```sql
-- 6. Count books with a rating-5 review
SELECT COUNT(*) AS book_count
FROM books AS b
WHERE EXISTS (
    SELECT 1
    FROM book_reviews AS r
    WHERE r.book_id = b.book_id
      AND r.rating = 5
);
```

Expected results: books with orders: **all four**; books with an unrated review: **SQL for Curious Minds, The Long Weekend**; no 5-star review: **SQL for Curious Minds, Small Worlds, The Long Weekend**; matching order IDs: **1 and 5**; author result: **Arun Das, Mira Sen**; book count: **1**.

### Self-test solutions

1. Whether its subquery returns at least one row.
2. No. It returns a true/false existence result for the current outer row.
3. It refers to a value from the outer query, such as `b.book_id` inside the review subquery.
4. It only answers whether a match exists, so multiple matching child rows do not create more outer result rows.
5. The subquery returns no rows for that outer row.
6. The Quiet River.

## 9. Ready for Day 14?

You’re ready when you can write a correlated condition and explain which outer row it checks against. Send me Assignment 3 and tell me why it returns each book only once.
