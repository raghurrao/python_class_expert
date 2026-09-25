# Day 15 — Combine query results with set operations

**Today's goal:** Combine or compare compatible query results using `UNION`, `UNION ALL`, `INTERSECT`, and `EXCEPT`.

**Suggested time:** 60–75 minutes

**Interactive routine:** Predict how many distinct values or rows each query should return. Write and run assignment queries in `queries/day-15.sql`; explain what happens to duplicates before checking the answer key.

## 1. Combine results with `UNION`

`UNION` stacks the rows from two queries and removes duplicate result rows:

```sql
SELECT author AS person_name
FROM books
UNION
SELECT reviewer AS person_name
FROM book_reviews
ORDER BY person_name;
```

The two sides must return the same number of columns in the same order, with compatible data types. The output column names come from the first `SELECT`.

`UNION` removes duplicates across the combined results. It also removes duplicates that were already repeated within either input. In this data, Mira Sen appears on two books but only once in the `UNION` result.

## 2. Keep duplicates with `UNION ALL`

`UNION ALL` combines the rows but keeps every duplicate:

```sql
SELECT author AS person_name
FROM books
UNION ALL
SELECT reviewer AS person_name
FROM book_reviews
ORDER BY person_name;
```

Use `UNION ALL` when repeated rows matter or when you know the inputs do not overlap and want to retain all rows. It avoids the duplicate-removal step.

## 3. Find common rows with `INTERSECT`

`INTERSECT` returns rows found in both query results:

```sql
SELECT author
FROM books
INTERSECT
SELECT author
FROM books
WHERE price > 20;
```

This returns authors who appear in the full author list and among books priced over 20. Like `UNION`, `INTERSECT` removes duplicates.

## 4. Find rows in one result but not the other with `EXCEPT`

`EXCEPT` returns rows from the first query that do not appear in the second:

```sql
SELECT author
FROM books
EXCEPT
SELECT author
FROM books
WHERE price <= 15;
```

This returns authors that appear among all books but do not appear among books priced 15 or less. The order matters: `A EXCEPT B` is not the same as `B EXCEPT A`.

## 5. Sorting the combined result

Put one `ORDER BY` at the end to sort the combined output. The output column names come from the first `SELECT`. Do not put an `ORDER BY` between the two queries unless using a parenthesized subquery for a specific reason.

```sql
SELECT author AS name
FROM books
UNION
SELECT customer AS name
FROM book_orders
ORDER BY name;
```

SQLite supports all four set operators used in this lesson. Other databases may support additional variations or have slightly different rules.

## 6. Today's runnable practice

Edit `queries/day-15.sql`, save, and run from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-15.sql
```

## 7. Assignment — write these six queries

1. Combine all authors and reviewers into one sorted list with duplicates removed.
2. Combine all authors and reviewers into one sorted list keeping duplicates.
3. Find authors who have at least one book priced over 20 using `INTERSECT` between all authors and authors of books over 20.
4. Find authors who have books but do not have any book priced 15 or less, using `EXCEPT`.
5. Combine customer names from orders with reviewer names, keeping duplicates, and count the output rows by wrapping the combined query in a CTE.
6. Combine book titles priced under 20 with book titles priced at least 20 using `UNION`, then sort the result alphabetically.

## 8. Self-test — answer without notes

1. How many columns must each side of a `UNION` return?
2. What does `UNION` do with duplicate rows?
3. What is the difference between `UNION` and `UNION ALL`?
4. What does `INTERSECT` return?
5. What does `A EXCEPT B` return?
6. Where does the `ORDER BY` go when sorting a union result?

## 9. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Authors and reviewers, duplicates removed
SELECT author AS person_name FROM books
UNION
SELECT reviewer AS person_name FROM book_reviews
ORDER BY person_name;
```

```sql
-- 2. Authors and reviewers, duplicates kept
SELECT author AS person_name FROM books
UNION ALL
SELECT reviewer AS person_name FROM book_reviews
ORDER BY person_name;
```

```sql
-- 3. Authors appearing among books priced over 20
SELECT author FROM books
INTERSECT
SELECT author FROM books WHERE price > 20;
```

```sql
-- 4. Authors with no book priced 15 or less
SELECT author FROM books
EXCEPT
SELECT author FROM books WHERE price <= 15;
```

```sql
-- 5. Count combined customer and reviewer rows, retaining duplicates
WITH people AS (
    SELECT customer AS person_name FROM book_orders
    UNION ALL
    SELECT reviewer AS person_name FROM book_reviews
)
SELECT COUNT(*) AS row_count
FROM people;
```

```sql
-- 6. All titles, combined and sorted
SELECT title FROM books WHERE price < 20
UNION
SELECT title FROM books WHERE price >= 20
ORDER BY title;
```

Expected counts: query 1 has **8 unique names** (three distinct authors and five reviewers); query 2 has **9 rows** because Mira Sen appears twice among authors. Query 3 returns **Arun Das, Mira Sen**. Query 4 returns **Arun Das, Mira Sen**. Query 5 returns **11 rows** (six order customer rows plus five review rows). Query 6 returns all **4** titles.

### Self-test solutions

1. The same number of columns on both sides.
2. Removes duplicate result rows from the combined set.
3. `UNION` removes duplicates; `UNION ALL` keeps all rows.
4. Rows that appear in both query results.
5. Rows from A that do not appear in B.
6. At the end of the combined query, after the last `SELECT`.

## 10. Ready for Day 16?

You’re ready when you can choose between `UNION` and `UNION ALL`, and explain the direction of `EXCEPT`. Send me Assignment 1 and tell me how many unique names you expect.
