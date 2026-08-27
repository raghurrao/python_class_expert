# Day 17: Transactions, Concurrency & ACID Guarantees

A **Transaction** groups multiple database operations into a single atomic unit of work.

---

## 1. The ACID Guarantees

- **Atomicity**: All operations succeed, or all roll back ("all or nothing").
- **Consistency**: Database valid state constraints enforced before and after.
- **Isolation**: Concurrent transactions execute without interfering.
- **Durability**: Committed data survives system crashes.

---

## 2. Transaction Control Syntax

```sql
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 500 WHERE account_id = 101;
SAVEPOINT transferred;
UPDATE accounts SET balance = balance + 500 WHERE account_id = 102;

-- If an error occurs:
ROLLBACK TO SAVEPOINT transferred;

-- Otherwise:
COMMIT;
```

---

## 3. Hands-On Practical Exercise (Day 17)

Run `03_postgres/day17_run.sh` to test atomic rollback vs commit!
