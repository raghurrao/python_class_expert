# Day 5 — Search text and filter dates

**Today's goal:** Find text by exact value or pattern, and filter dates using ISO date values.

**Suggested time:** 45–60 minutes

**Interactive routine:** Predict the matching rows, write one assignment query at a time in `queries/day-05.sql`, and run it. Try the self-test before looking at the answers. Send me your work for feedback.

## 1. Two useful tables

We will use `books` and `book_orders`. The order table has six rows with dates stored as `YYYY-MM-DD` text:

| order_id | customer | order_date | book_id | quantity |
|---:|---|---|---:|---:|
| 1 | Asha Rao | 2026-01-05 | 1 | 1 |
| 2 | Ben Cole | 2026-01-17 | 2 | 1 |
| 3 | Asha Rao | 2026-02-02 | 3 | 2 |
| 4 | Chen Wu | 2026-02-14 | 4 | 1 |
| 5 | Ben Cole | 2026-03-01 | 1 | 1 |
| 6 | Dina Shah | 2026-03-12 | 2 | 2 |

To inspect the table, run this query from `queries/day-05.sql`:

```sql
SELECT *
FROM book_orders;
```

## 2. Exact text matches

Use `=` to find an exact text value. Put text in single quotes:

```sql
SELECT customer, order_date
FROM book_orders
WHERE customer = 'Asha Rao';
```

An empty string (`''`) is text with zero characters. It is not the same as `NULL`, which means missing or unknown. Use `= ''` to find empty text; use `IS NULL` to find missing values.

## 3. Text patterns with `LIKE`

`LIKE` uses two special pattern characters:

- `%` matches zero or more characters.
- `_` matches exactly one character.

```sql
-- Customer names that start with A
SELECT customer
FROM book_orders
WHERE customer LIKE 'A%';
```

```sql
-- Book titles containing the word SQL
SELECT title
FROM books
WHERE title LIKE '%SQL%';
```

`'A%'` means “starts with A”; `'%a'` means “ends with a”; `'%ha%'` means “contains ha”. In SQLite, `LIKE` is case-insensitive for basic English letters by default, so matching behavior can differ from some other databases. We will call out dialect differences as they arise.

## 4. Filter dates

The sample dates use the unambiguous `YYYY-MM-DD` format. In this format, text sorts in calendar order, so comparison operators work for these dates:

```sql
SELECT customer, order_date
FROM book_orders
WHERE order_date >= '2026-02-01';
```

To filter all dates in February, use a start-inclusive and end-exclusive range:

```sql
SELECT customer, order_date
FROM book_orders
WHERE order_date >= '2026-02-01'
  AND order_date <  '2026-03-01';
```

This pattern also works for timestamps that include a time, because it includes every time on February 28 and excludes March 1. `BETWEEN` is inclusive at both ends, which is often less convenient for date/time ranges.

## 5. Today's runnable practice

The database setup file now includes `book_orders`. If you haven’t recreated your local database since starting Day 5, run this once from PowerShell in the course folder:

```powershell
python setup_database.py
```

This rebuilds all sample tables and resets them to their course data. Then edit `queries/day-05.sql` and run it with:

```powershell
python run_sql.py queries/day-05.sql
```

## 6. Assignment — write these six queries

1. Show customers and dates for orders placed by Ben Cole.
2. Show the customer names that start with `A`.
3. Show book titles that contain `SQL`.
4. Show orders placed on or after February 1, 2026, but before March 1, 2026.
5. Show orders placed in January 2026 using `>=` and `<` boundaries.
6. Show orders placed on or before January 17, 2026.

For each query, predict which order IDs or titles it should return before running it.

## 7. Self-test — answer without notes

1. What does `%` match in a `LIKE` pattern?
2. What does `_` match in a `LIKE` pattern?
3. What is the difference between `''` and `NULL`?
4. Which date format is used in the sample database?
5. Why is `order_date < '2026-03-01'` a useful upper boundary for all of February?
6. Are both endpoints included in `BETWEEN`?

## 8. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Orders by Ben Cole
SELECT customer, order_date
FROM book_orders
WHERE customer = 'Ben Cole';
```

```sql
-- 2. Customer names starting with A
SELECT customer
FROM book_orders
WHERE customer LIKE 'A%';
```

```sql
-- 3. Book titles containing SQL
SELECT title
FROM books
WHERE title LIKE '%SQL%';
```

```sql
-- 4. February 2026
SELECT order_id, customer, order_date
FROM book_orders
WHERE order_date >= '2026-02-01'
  AND order_date <  '2026-03-01';
```

```sql
-- 5. January 2026
SELECT order_id, customer, order_date
FROM book_orders
WHERE order_date >= '2026-01-01'
  AND order_date <  '2026-02-01';
```

```sql
-- 6. On or before January 17, 2026
SELECT order_id, customer, order_date
FROM book_orders
WHERE order_date <= '2026-01-17';
```

Expected order IDs for questions 1, 4, 5, and 6: **2 and 5**; **3 and 4**; **1 and 2**; **1 and 2**. Question 2 matches Asha Rao's two orders (IDs 1 and 3). Question 3 returns SQL for Curious Minds.

### Self-test solutions

1. Zero or more characters.
2. Exactly one character.
3. `''` is a known text value containing no characters; `NULL` is missing or unknown.
4. `YYYY-MM-DD`.
5. It excludes March 1 while including every date in February.
6. Yes, `BETWEEN` includes both endpoints.

## 9. Ready for Day 6?

You’re ready when you can use `%` and `_` deliberately and write a month filter with an inclusive start and exclusive next-month boundary. Send your assignment queries or one result you want me to explain.
