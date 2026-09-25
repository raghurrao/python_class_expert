# Day 22 — Design tables and constraints

**Today's goal:** Create a small relational schema and use primary keys, foreign keys, `NOT NULL`, `UNIQUE`, and `CHECK` constraints to protect data.

**Suggested time:** 60–75 minutes

**Interactive routine:** Read the schema before running it. Predict which example values are allowed by each constraint, run the practice file, then answer the assignment and self-test.

## 1. Design tables around entities

Suppose a tiny shop tracks authors and books. Store each author once, then let each book refer to its author ID:

```sql
CREATE TABLE day22_authors (
    author_id INTEGER PRIMARY KEY,
    name      TEXT NOT NULL UNIQUE
);

CREATE TABLE day22_books (
    book_id   INTEGER PRIMARY KEY,
    title     TEXT NOT NULL,
    author_id INTEGER NOT NULL REFERENCES day22_authors(author_id),
    price     NUMERIC NOT NULL CHECK (price >= 0)
);
```

The foreign key says `day22_books.author_id` must match an existing author. The `NOT NULL` constraint also requires every book to have an author.

## 2. What the constraints enforce

- `PRIMARY KEY`: uniquely identifies a row and cannot be `NULL`.
- `NOT NULL`: requires a value.
- `UNIQUE`: prevents duplicate values in that column (or combination of columns).
- `REFERENCES`: requires a matching row in another table when foreign-key enforcement is enabled.
- `CHECK`: requires a condition to be true, such as a nonnegative price.

Constraints are checked when rows are inserted or updated. They prevent invalid states instead of relying on every user of the database to remember the rules.

## 3. Choose a key

An integer ID is a common primary key. It stays stable even if a person's name or a book title changes. A natural value such as an email or ISBN can be constrained with `UNIQUE`, but it may change or may not be available for every row.

The database supports a one-to-many relation: one author can be referenced by many book rows. The foreign key belongs on the “many” side (`day22_books`).

## 4. SQLite type note

SQLite uses type affinity rather than rigid types by default. Declaring `price NUMERIC` communicates intent, but SQLite may still store values using different underlying storage classes. Constraints such as `NOT NULL`, `UNIQUE`, `CHECK`, and foreign keys remain important. Other database systems have stricter type rules.

## 5. Today's runnable practice

The practice file creates two temporary lesson tables, inserts valid sample data, displays it, and rolls back the transaction. The tables disappear when the script ends because the DDL is rolled back too.

Run it from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-22.sql
```

## 6. Assignment — design and reason

1. Add a `published_year` column to the sample design. It should be optional, but when provided it must be at least 1450. Write a `CHECK` that allows `NULL` or a year >= 1450.
2. Add an ISBN column that is optional but unique when present. Explain why SQLite's `UNIQUE` constraint allows multiple `NULL` values.
3. Explain why `author_id` belongs in the books table for a one-author-to-many-books relationship.
4. Write a `CREATE TABLE` for `day22_publishers` with an integer primary key and a required unique publisher name.
5. Write one valid and one invalid book insert for the schema. State which constraint rejects the invalid row.
6. Explain what foreign-key rule prevents an authorless or nonexistent-author book.

## 7. Self-test — answer without notes

1. Which constraint uniquely identifies a table row?
2. Which constraint prevents a missing required value?
3. Which constraint prevents duplicate names?
4. Where does a foreign key go in a one-to-many relationship?
5. What does `CHECK (price >= 0)` enforce?
6. In SQLite, is declaring `price NUMERIC` by itself a guarantee of strict numeric storage?

## 8. Answer key — check after trying

### Assignment examples

1. Example:

   ```sql
   published_year INTEGER CHECK (published_year IS NULL OR published_year >= 1450)
   ```

2. Example: `isbn TEXT UNIQUE`. SQLite allows multiple `NULL` values under a `UNIQUE` constraint because `NULL` values are treated as unknown rather than equal to each other.
3. A book row is on the many side and stores the ID of its one author. This avoids repeating author details for every book.
4. Example:

   ```sql
   CREATE TABLE day22_publishers (
       publisher_id INTEGER PRIMARY KEY,
       name TEXT NOT NULL UNIQUE
   );
   ```

5. Valid:

   ```sql
   INSERT INTO day22_books (book_id, title, author_id, price)
   VALUES (1, 'Learning SQL', 1, 10.00);
   ```

   Invalid examples include a negative price (rejected by `CHECK`), a missing title (rejected by `NOT NULL`), or an unknown author ID (rejected by the foreign key).

6. `author_id NOT NULL` prevents a missing link; `REFERENCES day22_authors(author_id)` rejects an ID that does not exist.

### Self-test solutions

1. `PRIMARY KEY`.
2. `NOT NULL`.
3. `UNIQUE`.
4. On the many-side table, pointing to the one-side table's key.
5. It rejects negative prices.
6. No. SQLite's default typing is flexible; the declaration gives type affinity, not strict enforcement.

## 9. Ready for Day 23?

You’re ready when you can explain what each constraint protects and where the foreign key belongs. Send me your proposed `published_year` column and ISBN constraint, and I’ll review them.
