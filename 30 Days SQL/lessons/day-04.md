# Day 4 — Understand and handle `NULL`

**Today's goal:** Find missing values correctly, understand why `NULL` is not an ordinary value, and show a fallback with `COALESCE`.

**Suggested time:** 45–60 minutes

**Interactive routine:** Predict which reviews match each condition, write the assignment queries in `queries/day-04.sql`, run them, and compare. Try the test before checking the answer key. Send me your work for feedback.

## 1. A table with missing values

The database now also includes `book_reviews`. A rating or review text can be missing, represented as `NULL`.

| review_id | book_id | reviewer | rating | review_text |
|---:|---:|---|---:|---|
| 1 | 1 | Kavita | 5 | A lovely story. |
| 2 | 2 | Ravi | `NULL` | A clear introduction. |
| 3 | 3 | Ava | 4 | `NULL` |
| 4 | 4 | Liam | `NULL` | `NULL` |
| 5 | 1 | Omar | 3 | Good, but slow at first. |

`NULL` means a value is missing or unknown. It is not the same thing as zero, an empty string (`''`), or the text `'NULL'`.

## 2. Test missing values with `IS NULL`

Do not use `rating = NULL`. `NULL` means unknown, so ordinary equality comparisons do not evaluate to true for it. Use `IS NULL`:

```sql
SELECT reviewer, rating
FROM book_reviews
WHERE rating IS NULL;
```

To find values that are present, use `IS NOT NULL`:

```sql
SELECT reviewer, rating
FROM book_reviews
WHERE rating IS NOT NULL;
```

This works for text columns too:

```sql
SELECT reviewer
FROM book_reviews
WHERE review_text IS NULL;
```

## 3. Why `= NULL` does not work

Comparisons involving `NULL` produce an unknown result rather than true or false. A `WHERE` clause keeps only rows where its condition is true, so this query returns no rows:

```sql
SELECT reviewer
FROM book_reviews
WHERE rating = NULL;
```

Use `IS NULL` instead. Similarly, to test whether something is missing, do not use `<> NULL`; write `IS NOT NULL`.

## 4. Replace missing values in the output with `COALESCE`

`COALESCE` returns the first non-`NULL` argument. It can show a helpful fallback in query results:

```sql
SELECT reviewer, COALESCE(rating, 0) AS rating_display
FROM book_reviews;
```

Here, a missing rating is displayed as `0`. That changes only the result shown by this query; it does not update the stored rating. Be thoughtful about the fallback: showing `0` could misleadingly imply that a reviewer gave a zero rating. A label can be clearer:

```sql
SELECT reviewer, COALESCE(CAST(rating AS TEXT), 'not rated') AS rating_display
FROM book_reviews;
```

The cast turns the numeric rating into text so the fallback label has the same type.

## 5. Recreate the practice database if needed

The setup file now creates both `books` and `book_reviews`. If your database predates today's lesson, run this from PowerShell in the course folder:

```powershell
python setup_database.py
```

This resets the sample tables to their original lesson data. Run a query saved in `queries/day-04.sql` with:

```powershell
python run_sql.py queries/day-04.sql
```

## 6. Assignment — write these six queries

1. Show the reviewer and rating for reviews that have no rating.
2. Show the reviewer and rating for reviews that do have a rating.
3. Show the reviewer for reviews with no review text.
4. Show each reviewer and a `rating_display` value that says `not rated` when the rating is missing. Keep actual ratings numeric if possible; if you choose text, cast the rating as shown above.
5. Find reviews where either the rating or the review text is missing.
6. Find reviews where both the rating and the review text are present.

Before running each query, write down the reviewer names you expect to see.

## 7. Self-test — answer without notes

1. Is `NULL` the same as zero?
2. What condition finds a missing `review_text`?
3. Why does `rating = NULL` not find rows with missing ratings?
4. What does `COALESCE(rating, 0)` return when `rating` is `NULL`?
5. Does `COALESCE` permanently change the value stored in the database?
6. Which condition means “the rating and review text are both present”?

## 8. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Missing ratings
SELECT reviewer, rating
FROM book_reviews
WHERE rating IS NULL;
```

```sql
-- 2. Present ratings
SELECT reviewer, rating
FROM book_reviews
WHERE rating IS NOT NULL;
```

```sql
-- 3. Missing review text
SELECT reviewer
FROM book_reviews
WHERE review_text IS NULL;
```

```sql
-- 4. Show a friendly label for missing ratings
SELECT reviewer,
       COALESCE(CAST(rating AS TEXT), 'not rated') AS rating_display
FROM book_reviews;
```

```sql
-- 5. Either field is missing
SELECT reviewer
FROM book_reviews
WHERE rating IS NULL OR review_text IS NULL;
```

```sql
-- 6. Both fields are present
SELECT reviewer
FROM book_reviews
WHERE rating IS NOT NULL AND review_text IS NOT NULL;
```

Expected reviewers for questions 1–6: **Ravi, Liam**; **Kavita, Ava, Omar**; **Ava, Liam**; all five reviewers with `not rated` for Ravi and Liam; **Ravi, Ava, Liam**; **Kavita, Omar**.

### Self-test solutions

1. No. Zero is a known numeric value; `NULL` means missing or unknown.
2. `review_text IS NULL`.
3. Equality with an unknown value evaluates to unknown, not true. Use `IS NULL`.
4. It returns `0` for that row.
5. No. It only changes the value displayed by that query.
6. `rating IS NOT NULL AND review_text IS NOT NULL`.

## 9. Ready for Day 5?

You’re ready when you can explain why `IS NULL` is necessary and distinguish missing data from zero or empty text. Send me your assignment queries or any output that surprised you, and I’ll help you reason through it.
