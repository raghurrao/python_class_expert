# Day 8 — Understand keys and table relationships

**Today's goal:** Recognize primary keys and foreign keys, understand how tables relate, and inspect a database schema.

**Suggested time:** 45–60 minutes

**Interactive routine:** Inspect the schema using the queries below, sketch the relationships, complete the assignment, and send me your answers. No joins yet; we’ll use these relationships in Day 9.

## 1. Why split information into tables?

The course database stores books, orders, and reviews separately. An order refers to a book by its ID instead of copying the title and author into every order row. This reduces repeated data and gives each fact a clear place to live.

The relationships are:

```text
books.book_id  1 ─── many  book_orders.book_id
books.book_id  1 ─── many  book_reviews.book_id
```

One book can appear in many orders and can have many reviews. Each individual order row and review row points to one book.

## 2. Primary keys identify rows

A primary key is a column (or set of columns) that uniquely identifies each row in a table. In this database:

- `books.book_id` identifies a book.
- `book_orders.order_id` identifies an order.
- `book_reviews.review_id` identifies a review.

Primary keys must be unique and cannot be `NULL`. The primary key helps the database distinguish rows even when other values repeat. Two books could share a title, but they would still have different IDs.

Inspect the books table definition with:

```sql
PRAGMA table_info(books);
```

The `pk` column in the output marks the primary key column.

## 3. Foreign keys connect rows

A foreign key is a column whose values refer to a key in another table. Here, `book_orders.book_id` and `book_reviews.book_id` refer to `books.book_id`.

This rule prevents an order or review from referring to a book that does not exist. For example, an order with `book_id = 999` would be rejected because there is no book 999.

Inspect the foreign keys with:

```sql
PRAGMA foreign_key_list(book_orders);
```

And inspect reviews with:

```sql
PRAGMA foreign_key_list(book_reviews);
```

The local runner enables foreign key enforcement for each connection. The setup file also enables it while rebuilding the database.

## 4. One-to-many relationships

“One-to-many” describes how rows relate, not a special SQL command:

- One book can have many order rows.
- One book can have many review rows.
- Each order row points to one book ID.
- Each review row points to one book ID.

The `NOT NULL` constraint on a child table’s foreign key means every order and review must point to a book. Some database designs allow optional relationships; those foreign-key columns may allow `NULL` when a link is optional.

## 5. What the constraints protect

Constraints are rules stored in the database:

- `PRIMARY KEY` enforces a unique row identifier.
- `NOT NULL` requires a value.
- `REFERENCES` declares a foreign-key relationship.

Constraints protect data even when it is inserted by a different script or application. They are useful because correctness is enforced at the data layer, not just by convention.

## 6. Today's runnable practice

Edit `queries/day-08.sql` and run it from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-08.sql
```

To rebuild the current sample database with the new foreign-key constraints, run:

```powershell
python setup_database.py
```

## 7. Assignment — inspect and explain

Write and run the following queries. Then answer the questions in your own words.

1. Inspect the columns and primary key of `books` with `PRAGMA table_info`.
2. Inspect the foreign key of `book_orders`.
3. Inspect the foreign key of `book_reviews`.
4. Count how many order rows refer to each `book_id`. (You already know `GROUP BY`.)
5. Which table should contain a new book’s title and author: `books` or `book_orders`? Explain why.
6. If a new order row refers to a `book_id` that is not in `books`, what should the database do?

## 8. Self-test — answer without notes

1. What problem does a primary key solve?
2. What does a foreign key refer to?
3. Is a foreign key in `book_orders` or `books` for the relationship between orders and books?
4. Can many orders point to the same book?
5. What does `NOT NULL` on the foreign-key column require?
6. In the course schema, which column uniquely identifies each review?

## 9. Answer key — check after trying

### Assignment guidance

1. `book_id` is the primary key (`pk = 1`); the other fields describe each book.
2. `book_orders.book_id` references `books.book_id`.
3. `book_reviews.book_id` references `books.book_id`.
4. One correct query:

   ```sql
   SELECT book_id, COUNT(*) AS order_count
   FROM book_orders
   GROUP BY book_id;
   ```

   Expected counts: book 1 has 2 orders; book 2 has 2; book 3 has 1; book 4 has 1.

5. `books`, because title and author describe the book itself. Repeating them in every order would duplicate data.
6. The database rejects the row because the referenced book does not exist.

### Self-test solutions

1. It gives every row a unique, non-missing identifier.
2. It refers to a key in another table, connecting the rows and enforcing that the referenced row exists.
3. `book_orders` contains the foreign key `book_id`.
4. Yes. That is the one-to-many relationship.
5. Every order row must have a book ID; the link cannot be missing.
6. `review_id`.

## 10. Ready for Day 9?

You’re ready when you can point out the primary and foreign keys and explain which table holds the “many” side of a one-to-many relationship. Next we’ll use these keys to join rows across tables.
