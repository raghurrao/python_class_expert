# Day 2 — Filter rows with conditions

**Today's goal:** Select only the rows that meet one or more conditions, and predict exactly which rows your query will return.

**Suggested time:** 45–75 minutes

**Interactive routine:** Try the assignment and self-test without checking the answer key. Save each query into `queries/day-02.sql`, run it, and compare the results with your predictions. Send me your queries and self-test answers for feedback.

## 1. The table we will query

The `books` table in `books.db` has these columns:

| book_id | title | author | price | in_stock |
|---:|---|---|---:|---|
| 1 | The Quiet River | Mira Sen | 18.50 | true |
| 2 | SQL for Curious Minds | Arun Das | 32.00 | true |
| 3 | Small Worlds | Jo Lee | 12.75 | false |
| 4 | The Long Weekend | Mira Sen | 24.00 | true |

`WHERE` keeps rows only when its condition is true:

```sql
SELECT title, price
FROM books
WHERE price >= 20;
```

This returns SQL for Curious Minds and The Long Weekend. A condition can compare a column with a number, text, or another value.

## 2. Comparison operators

| Operator | Meaning | Example |
|---|---|---|
| `=` | equals | `author = 'Mira Sen'` |
| `<>` | not equal | `author <> 'Mira Sen'` |
| `>` | greater than | `price > 20` |
| `>=` | greater than or equal to | `price >= 20` |
| `<` | less than | `price < 20` |
| `<=` | less than or equal to | `price <= 20` |

Text must be in single quotes. The text match is exact here: `'Mira Sen'` is different from `'mira sen'` in some database configurations, so use the spelling and capitalization stored in the table.

## 3. Combine conditions with `AND` and `OR`

`AND` requires both conditions to be true:

```sql
SELECT title, price
FROM books
WHERE price < 25 AND in_stock = TRUE;
```

`OR` requires at least one condition to be true:

```sql
SELECT title, author
FROM books
WHERE author = 'Mira Sen' OR price < 15;
```

Use parentheses when a condition mixes `AND` and `OR`. Parentheses make the intended logic clear:

```sql
SELECT title, price, in_stock
FROM books
WHERE in_stock = TRUE AND (price < 20 OR price > 30);
```

This means: “in stock, and either cheaper than 20 or more expensive than 30.”

## 4. Shortcuts: `IN` and `BETWEEN`

Use `IN` when checking a column against a list of exact values:

```sql
SELECT title, author
FROM books
WHERE author IN ('Mira Sen', 'Jo Lee');
```

This is equivalent to checking `author = 'Mira Sen' OR author = 'Jo Lee'`.

Use `BETWEEN` for an inclusive range: both endpoints count.

```sql
SELECT title, price
FROM books
WHERE price BETWEEN 15 AND 25;
```

That includes prices equal to 15 or 25 as well as prices between them.

## 5. Pattern matching with `LIKE`

`LIKE` searches text patterns. In SQLite, `%` matches any number of characters and `_` matches one character.

```sql
SELECT title
FROM books
WHERE title LIKE 'SQL%';
```

`'SQL%'` means the title starts with `SQL`. `%River%` would match text with `River` anywhere in the value. Pattern matching behavior and case sensitivity can differ by database; for this SQLite course, use the capitalization shown in the sample data.

## 6. How to run today's work

Open PowerShell in the course folder. Edit `queries/day-02.sql` in a text editor, save a query, and run:

```powershell
python run_sql.py queries/day-02.sql
```

The runner reads SQL from that file and prints the result. Replace the starter query each time you want to try a different assignment question.

## 7. Assignment — write these six queries

For each query, first list the titles you expect. Then write and run SQL to check your prediction.

1. Show the title and price of books costing **at most 20**.
2. Show the title and author of books **not** written by Mira Sen.
3. Show the title and price of books that cost more than 15 **and** are in stock.
4. Show the title of books that are written by Jo Lee **or** cost more than 30.
5. Show the title and author of books written by Mira Sen or Jo Lee, using `IN`.
6. Show the title and price of books priced between 13 and 24, including both endpoints.

## 8. Self-test — answer without notes

1. What does `WHERE` do?
2. Does `BETWEEN 10 AND 20` include rows equal to 10 and 20?
3. In a `WHERE` condition, does `AND` mean both conditions must match, or either one?
4. Write a condition that matches a title starting with the word `The`.
5. Translate this into plain language: `WHERE in_stock = TRUE AND price < 25`.
6. What is the purpose of parentheses in a condition that mixes `AND` and `OR`?

## 9. Answer key — check after trying

### Assignment solutions

```sql
-- 1. At most 20
SELECT title, price
FROM books
WHERE price <= 20;
```

```sql
-- 2. Not written by Mira Sen
SELECT title, author
FROM books
WHERE author <> 'Mira Sen';
```

```sql
-- 3. More than 15 and in stock
SELECT title, price
FROM books
WHERE price > 15 AND in_stock = TRUE;
```

```sql
-- 4. Written by Jo Lee or costs more than 30
SELECT title
FROM books
WHERE author = 'Jo Lee' OR price > 30;
```

```sql
-- 5. Written by Mira Sen or Jo Lee
SELECT title, author
FROM books
WHERE author IN ('Mira Sen', 'Jo Lee');
```

```sql
-- 6. Price from 13 through 24, inclusive
SELECT title, price
FROM books
WHERE price BETWEEN 13 AND 24;
```

Expected matching titles for questions 1–6: **The Quiet River, Small Worlds**; **SQL for Curious Minds, Small Worlds**; **The Quiet River, SQL for Curious Minds, The Long Weekend**; **SQL for Curious Minds, Small Worlds**; **The Quiet River, Small Worlds, The Long Weekend**; **The Quiet River, The Long Weekend**.

### Self-test solutions

1. It filters rows, keeping those for which the condition is true.
2. Yes. `BETWEEN` includes both endpoints.
3. Both conditions must be true.
4. `title LIKE 'The%'`.
5. Return books that are in stock and cost less than 25.
6. They explicitly group logic so the query means what you intend and is easy to read.

## 10. Ready for Day 3?

You’re ready when you can explain the difference between `AND` and `OR`, predict the matching rows, and write all six assignment queries without copying the key. Send me your work or tell me which question felt confusing; I’ll respond to that before we move on.
