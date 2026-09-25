# Day 3 — Sort, limit, and remove duplicates

**Today's goal:** Control the order and size of a query result with `ORDER BY` and `LIMIT`, and use `DISTINCT` to return unique values.

**Suggested time:** 45–60 minutes

**Interactive routine:** Predict the output, write each assignment query in `queries/day-03.sql`, run it, and compare. Do the self-test before using the answer key. Send me your queries and answers for feedback.

## 1. The table we will query

We will keep using `books` in `books.db`:

| book_id | title | author | price | in_stock |
|---:|---|---|---:|---|
| 1 | The Quiet River | Mira Sen | 18.50 | true |
| 2 | SQL for Curious Minds | Arun Das | 32.00 | true |
| 3 | Small Worlds | Jo Lee | 12.75 | false |
| 4 | The Long Weekend | Mira Sen | 24.00 | true |

## 2. Sort with `ORDER BY`

Without `ORDER BY`, the database does not promise a particular row order. Even if rows seem to appear in insertion order, do not rely on it.

```sql
SELECT title, price
FROM books
ORDER BY price;
```

Ascending order is the default. You can make it explicit with `ASC`. Use `DESC` for descending order:

```sql
SELECT title, price
FROM books
ORDER BY price DESC;
```

Sort on more than one column by listing them in priority order. SQL sorts by the first column, then uses later columns to break ties:

```sql
SELECT title, author, price
FROM books
ORDER BY author ASC, price DESC;
```

That groups authors alphabetically and, within each author, sorts their books from more expensive to less expensive.

You can filter and sort together. Filtering comes before sorting in the query:

```sql
SELECT title, price
FROM books
WHERE in_stock = TRUE
ORDER BY price DESC;
```

## 3. Keep only the first rows with `LIMIT`

```sql
SELECT title, price
FROM books
ORDER BY price DESC
LIMIT 2;
```

This returns the two most expensive books. Use `ORDER BY` with `LIMIT` when you mean “top” or “bottom”; without sorting, the database can choose any qualifying rows.

`LIMIT` is applied after sorting. `LIMIT 0` returns no rows. SQLite also supports `LIMIT` without ordering, but that is useful mainly for quick inspection, not for a reliable “top results” answer.

## 4. Return unique values with `DISTINCT`

The `books` table has two books by Mira Sen. To list each author only once:

```sql
SELECT DISTINCT author
FROM books
ORDER BY author;
```

`DISTINCT` removes duplicate result rows. If you select multiple columns, uniqueness applies to the whole combination of selected values:

```sql
SELECT DISTINCT author, in_stock
FROM books;
```

This returns one row for each distinct author-and-stock-status pair, so one author can still appear more than once if the other selected value differs.

## 5. Today's runnable practice

Open PowerShell in the course folder. Edit `queries/day-03.sql`, save, then run:

```powershell
python run_sql.py queries/day-03.sql
```

The starter query shows the two most expensive books. Replace it with one assignment query at a time.

## 6. Assignment — write these six queries

Before running each query, write down which titles or values you expect to see.

1. Show all book titles and prices, from cheapest to most expensive.
2. Show all book titles and prices, from most expensive to cheapest.
3. Show the title and price of the cheapest in-stock book.
4. List all unique authors in alphabetical order.
5. Show all in-stock books, most expensive first, but return only the first two.
6. Show unique combinations of author and `in_stock` status, sorted by author and then stock status.

## 7. Self-test — answer without notes

1. What order does `ORDER BY price` use if you do not specify `ASC` or `DESC`?
2. Why should a query use `ORDER BY` before `LIMIT` when asking for the “top 3” rows?
3. What does `DISTINCT` remove?
4. If you select `DISTINCT author, in_stock`, what combination is considered for duplicates?
5. In `ORDER BY author, price DESC`, which column is the primary sort key?
6. Does a database guarantee row order when a query has no `ORDER BY`?

## 8. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Cheapest to most expensive
SELECT title, price
FROM books
ORDER BY price ASC;
```

```sql
-- 2. Most expensive to cheapest
SELECT title, price
FROM books
ORDER BY price DESC;
```

```sql
-- 3. Cheapest in-stock book
SELECT title, price
FROM books
WHERE in_stock = TRUE
ORDER BY price ASC
LIMIT 1;
```

```sql
-- 4. Unique authors, alphabetically
SELECT DISTINCT author
FROM books
ORDER BY author ASC;
```

```sql
-- 5. Two most expensive in-stock books
SELECT title, price
FROM books
WHERE in_stock = TRUE
ORDER BY price DESC
LIMIT 2;
```

```sql
-- 6. Unique author and stock-status pairs
SELECT DISTINCT author, in_stock
FROM books
ORDER BY author ASC, in_stock ASC;
```

### Self-test solutions

1. Ascending.
2. Sorting defines what “top” means; without it, the selected rows are not predictably the top rows.
3. Duplicate result rows, based on all selected columns together.
4. The pair of values (`author`, `in_stock`); identical pairs appear once.
5. `author`. `price DESC` sorts within equal author values.
6. No. Specify `ORDER BY` when result order matters.

## 9. Ready for Day 4?

You’re ready when you can explain why `LIMIT` needs a meaningful sort for a top-N question, and why selecting two columns with `DISTINCT` may still show an author more than once. Send your assignment queries or questions, and I’ll review them before we move on.
