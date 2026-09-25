# Day 33 — Use savepoints and understand ACID

**Today's goal:** Use savepoints to undo part of a transaction and understand the ACID properties transactions aim to provide.

**Suggested time:** 45–60 minutes

**Interactive routine:** Run the safe demo and observe the price before the update, after the update, and after rolling back to the savepoint. Then answer the test.

## 1. Transaction refresher

A transaction groups changes so they can be committed together or undone together:

```sql
BEGIN;
-- one or more changes
COMMIT;
```

Use `ROLLBACK` instead of `COMMIT` to discard uncommitted changes. This is especially useful when multiple updates must succeed as one unit.

## 2. Use a savepoint

A savepoint creates a named point inside the current transaction. You can roll back only the work after that point:

```sql
BEGIN;

UPDATE books SET price = 20 WHERE book_id = 1;
SAVEPOINT after_first_change;

UPDATE books SET price = 99 WHERE book_id = 1;
SELECT price FROM books WHERE book_id = 1;

ROLLBACK TO after_first_change;
SELECT price FROM books WHERE book_id = 1;

ROLLBACK;
```

After `ROLLBACK TO`, the second update is undone, but the first update remains part of the still-open transaction. The final `ROLLBACK` undoes that first update too.

`RELEASE SAVEPOINT` removes a savepoint marker; it does not commit the whole transaction. Savepoint behavior and exact syntax can vary slightly by database.

## 3. ACID properties

Transactions are commonly described with four properties:

- **Atomicity:** The transaction's changes succeed together or are rolled back together.
- **Consistency:** Constraints and rules remain satisfied before and after a successful transaction.
- **Isolation:** Concurrent transactions are prevented from interfering in ways the database does not allow; exact isolation levels vary by database.
- **Durability:** Once committed, changes survive according to the database's durability guarantees.

These properties describe transaction guarantees, but details depend on the database engine and its configuration.

## 4. A practical pattern

When changing data:

1. Start a transaction.
2. Check which rows will change with a `SELECT`.
3. Apply the changes.
4. Check the result.
5. `COMMIT` if correct or `ROLLBACK` if not.

For a savepoint, use it when a longer transaction has a checkpoint that may need partial undo.

## 5. Today's safe runnable practice

The practice file temporarily updates a book price, saves a point, makes a second update, rolls back to the savepoint, checks the value, then rolls back the whole transaction. It leaves the original database unchanged.

Run from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-33.sql
```

## 6. Assignment — reason through the transaction

1. In the demo, what value should appear after the first update?
2. What value should appear after the second update?
3. What value should appear after `ROLLBACK TO` the savepoint?
4. What value remains stored after the final full `ROLLBACK`?
5. Explain what `RELEASE SAVEPOINT` does and what it does not do.
6. Name the ACID property that describes committed changes surviving a failure.

## 7. Self-test — answer without notes

1. What is a savepoint?
2. Does `ROLLBACK TO savepoint_name` necessarily end the whole transaction?
3. Which ACID property means all-or-nothing?
4. Which property concerns concurrent transactions?
5. What does `COMMIT` do?
6. Why check the rows before and after a data change?

## 8. Answer key — check after trying

### Assignment solutions

1. `20`.
2. `99`.
3. `20`, because the update after the savepoint is undone.
4. The original price, `18.50`, because the final rollback undoes the first update too.
5. It removes the savepoint marker; it does not commit the entire transaction.
6. Durability.

### Self-test solutions

1. A named checkpoint inside a transaction to which work can be rolled back.
2. No. It undoes changes after the savepoint while leaving the transaction active.
3. Atomicity.
4. Isolation.
5. It saves the transaction's changes.
6. To verify the target set and confirm that the intended effect occurred without unintended changes.

## 9. Ready for Day 34?

You’re ready when you can explain the difference between rolling back to a savepoint and rolling back the whole transaction. Send me the three price values you observed in the demo.
