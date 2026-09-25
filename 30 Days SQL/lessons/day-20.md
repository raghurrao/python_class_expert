# Day 20 — Change data safely with transactions

**Today's goal:** Insert, update, and delete rows, and use a transaction to keep changes together or undo them.

**Suggested time:** 60–75 minutes

**Interactive routine:** Read each write statement before running it. Use a transaction and `ROLLBACK` for practice. Predict the result of each statement, run the starter file, and check that the original data remains unchanged.

## 1. Insert a row

`INSERT` adds a row. Name the columns so the values are clear:

```sql
INSERT INTO books (book_id, title, author, price, in_stock)
VALUES (5, 'A SQL Journey', 'Nia Park', 21.00, TRUE);
```

The column list and values must line up in the same order. This insert would fail if `book_id = 5` already existed or if a required value were missing.

## 2. Update rows

`UPDATE` changes existing rows. Use `WHERE` to specify which rows should change:

```sql
UPDATE books
SET price = 22.00
WHERE book_id = 5;
```

Without `WHERE`, the update changes every row in the table. Before running an update, run a `SELECT` with the same condition to confirm the target rows.

## 3. Delete rows

`DELETE` removes rows. Again, use `WHERE` to identify the intended row or rows:

```sql
DELETE FROM books
WHERE book_id = 5;
```

Without `WHERE`, every row in the table is removed. Confirm the target with a `SELECT` first.

## 4. Group changes in a transaction

A transaction groups statements into one unit. If something is wrong, `ROLLBACK` undoes the changes since the transaction began:

```sql
BEGIN;

UPDATE books
SET price = 22.00
WHERE book_id = 1;

SELECT book_id, title, price
FROM books
WHERE book_id = 1;

ROLLBACK;
```

The `SELECT` inside the transaction shows the temporary updated price. After `ROLLBACK`, the stored price is restored.

If the changes are correct and should be saved, `COMMIT` makes them permanent instead. Do not use `COMMIT` in a practice script unless you intend to keep the changes.

## 5. Today's safe runnable practice

The starter query deliberately demonstrates temporary changes and ends with `ROLLBACK`. Do not remove the rollback while practicing against the shared course database.

Run it from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-20.sql
```

You should see the temporary insert, update, and delete effects in intermediate results, then the original row count after rollback.

## 6. Assignment — reason through these statements

Do not run a permanent change against the course tables. Write each operation inside a transaction that ends with `ROLLBACK`.

1. Insert a practice book with `book_id = 5`, title `A SQL Journey`, author `Nia Park`, price `21.00`, and `in_stock = TRUE`. Select it to verify, then roll back.
2. Update that book's price to `22.00`. Select the row to verify, then roll back.
3. Delete that book. Select it to verify that it is gone inside the transaction, then roll back.
4. Write a `SELECT` that would identify the exact books before updating their prices.
5. Explain what happens if `WHERE book_id = 5` is omitted from an `UPDATE` or `DELETE`.
6. In your own words, explain the difference between `ROLLBACK` and `COMMIT`.

## 7. Self-test — answer without notes

1. What does `INSERT` do?
2. What does `UPDATE` do?
3. What happens if an `UPDATE` has no `WHERE` clause?
4. What does `ROLLBACK` do?
5. What does `COMMIT` do?
6. Why should you select the target rows before updating or deleting?

## 8. Answer key — check after trying

### Assignment examples

```sql
-- 1. Insert, inspect, then undo
BEGIN;
INSERT INTO books (book_id, title, author, price, in_stock)
VALUES (5, 'A SQL Journey', 'Nia Park', 21.00, TRUE);
SELECT * FROM books WHERE book_id = 5;
ROLLBACK;
```

```sql
-- 2. Update inside a transaction, inspect, then undo
BEGIN;
UPDATE books SET price = 22.00 WHERE book_id = 1;
SELECT book_id, title, price FROM books WHERE book_id = 1;
ROLLBACK;
```

```sql
-- 3. Delete inside a transaction, inspect, then undo
BEGIN;
DELETE FROM books WHERE book_id = 1;
SELECT * FROM books WHERE book_id = 1;
ROLLBACK;
```

4. For the price update above: `SELECT book_id, title, price FROM books WHERE book_id = 1;`
5. It would update or delete every row in the table.
6. `ROLLBACK` discards the transaction's changes; `COMMIT` saves them.

### Self-test solutions

1. Adds a new row.
2. Changes values in existing row(s).
3. Every row is updated.
4. Undoes uncommitted changes in the transaction.
5. Saves the transaction's changes permanently.
6. It confirms the `WHERE` condition selects exactly the rows you intend to change.

## 9. Ready for Day 21?

You’re ready when you can use a transaction to try a change, inspect it, and roll it back. Run the safe practice file and tell me what it shows before and after `ROLLBACK`.
