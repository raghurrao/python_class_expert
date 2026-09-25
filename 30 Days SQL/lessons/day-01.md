# Day 1 — Meet SQL and read your first table

**Today's goal:** Understand what a database table is and write simple queries that choose, filter, and sort rows.

**Suggested time:** 45–75 minutes

**How to make this interactive:** Do the assignment and test first. Send me your SQL and your test answers before opening the answer key below. I’ll review them, explain any mistakes, and give you a small follow-up challenge.

## Open and use your practice database

Your database is the file `books.db` in the course folder. It contains a table called `books` with four example books. The setup file is `setup.sql`; the Python runner connects to the database and displays query results.

Open PowerShell in this course folder and run:

```powershell
python run_sql.py queries/day-01.sql
```

That runs the query saved in `queries/day-01.sql`. To practice, edit that file in a text editor, save your SQL, and run the command again. You can replace the starter query with an assignment query. To restore the starter table and sample data, run `python setup_database.py`.

The first query is already saved there:

```sql
SELECT title, author
FROM books;
```

`SELECT title, author` asks for just those two columns. `FROM books` tells the database which table to read. It returns four rows: one title and author for each book. Try running it now, then change the selected columns to `title, price` and run it again.

## 1. The basic idea

SQL (Structured Query Language) is a language for asking questions of relational databases. Data is organized into tables. A table has columns (fields) and rows (records), much like a spreadsheet, but tables can be linked together and queried reliably at scale.

Imagine a table named `books`:

| book_id | title | author | price | in_stock |
|---:|---|---|---:|---|
| 1 | The Quiet River | Mira Sen | 18.50 | true |
| 2 | SQL for Curious Minds | Arun Das | 32.00 | true |
| 3 | Small Worlds | Jo Lee | 12.75 | false |
| 4 | The Long Weekend | Mira Sen | 24.00 | true |

Each row describes one book. Each column describes one property of a book. `book_id` identifies a row; `price` is a number; `in_stock` is a true/false value.

## 2. Your first query: `SELECT` and `FROM`

```sql
SELECT title, author
FROM books;
```

Read it as: “Return the `title` and `author` columns from the `books` table.” SQL keywords are commonly written in uppercase for readability; the database does not require that capitalization.

To return every column, use `*`:

```sql
SELECT *
FROM books;
```

Use `*` when exploring a table. In queries you keep and reuse, name the columns you need so the result is easier to understand.

## 3. Filter rows with `WHERE`

```sql
SELECT title, price
FROM books
WHERE price < 20;
```

`WHERE` keeps rows that match a condition. Common comparison operators are `=`, `<>` (not equal), `>`, `>=`, `<`, and `<=`.

Text values use single quotes:

```sql
SELECT title
FROM books
WHERE author = 'Mira Sen';
```

Numbers are not quoted. For example, compare `price < 20`, not `price < '20'`.

## 4. Sort rows with `ORDER BY`

```sql
SELECT title, price
FROM books
ORDER BY price;
```

`ORDER BY` sorts ascending by default. Use `DESC` for descending order and `ASC` for ascending order:

```sql
SELECT title, price
FROM books
ORDER BY price DESC;
```

You can combine clauses. The usual order for today's queries is `SELECT`, `FROM`, `WHERE`, then `ORDER BY`:

```sql
SELECT title, price
FROM books
WHERE in_stock = true
ORDER BY price DESC;
```

The database filters first, then sorts the matching rows for the result.

## 5. Try the queries yourself

The database is already created for you. Here is the setup SQL, included as `setup.sql` so you can see how its table and sample data are defined. You do not need to run it to start practicing.

```sql
CREATE TABLE books (
    book_id   INTEGER PRIMARY KEY,
    title     TEXT NOT NULL,
    author    TEXT NOT NULL,
    price     NUMERIC(6, 2) NOT NULL,
    in_stock  BOOLEAN NOT NULL
);

INSERT INTO books (book_id, title, author, price, in_stock) VALUES
    (1, 'The Quiet River', 'Mira Sen', 18.50, TRUE),
    (2, 'SQL for Curious Minds', 'Arun Das', 32.00, TRUE),
    (3, 'Small Worlds', 'Jo Lee', 12.75, FALSE),
    (4, 'The Long Weekend', 'Mira Sen', 24.00, TRUE);
```

## 6. Assignment — 6 queries

Write one query for each task. Do not use `SELECT *` unless the task asks for all columns.

1. Show the title and author of every book.
2. Show every column for every book.
3. Show the title and price of books that cost less than 20.
4. Show the titles of books written by Mira Sen.
5. Show the title and price of books, ordered from most expensive to least expensive.
6. Show the title and price of books that are in stock, ordered from cheapest to most expensive.

For each query, predict how many rows it returns before running it. Then run it (or check against the sample table) and see whether your prediction was correct.

## 7. Self-test — answer without notes

1. In a table, what is the difference between a row and a column?
2. What does `FROM books` tell SQL?
3. Which clause filters rows?
4. Which clause sorts the result?
5. Does `ORDER BY price` sort from high to low or low to high by default?
6. Write a query that returns the title of books priced at least 20.
7. What is one reason to name columns instead of always using `SELECT *`?

## 8. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Titles and authors of all books
SELECT title, author
FROM books;
```

```sql
-- 2. Every column
SELECT *
FROM books;
```

```sql
-- 3. Books priced below 20
SELECT title, price
FROM books
WHERE price < 20;
```

```sql
-- 4. Books by Mira Sen
SELECT title
FROM books
WHERE author = 'Mira Sen';
```

```sql
-- 5. Most expensive first
SELECT title, price
FROM books
ORDER BY price DESC;
```

```sql
-- 6. In-stock books, cheapest first
SELECT title, price
FROM books
WHERE in_stock = TRUE
ORDER BY price ASC;
```

Expected row counts for tasks 1–6: **4, 4, 2, 2, 4, 3**.

### Self-test solutions

1. A row is one record; a column is one kind of information recorded for each record.
2. It names the table to read from.
3. `WHERE`.
4. `ORDER BY`.
5. Low to high (ascending).
6. One correct answer:

   ```sql
   SELECT title
   FROM books
   WHERE price >= 20;
   ```

7. Naming columns makes the result clearer and avoids returning data you do not need.

## 9. Ready to move on?

You’re ready for Day 2 when you can write the six assignment queries from a blank page and explain what `SELECT`, `FROM`, `WHERE`, and `ORDER BY` each do. Send me your six queries and self-test answers, even if you are unsure; I’ll give feedback before we continue.
