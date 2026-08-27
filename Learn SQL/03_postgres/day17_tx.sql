-- Day 17: Transaction Rollback and Commit Script

DROP TABLE IF EXISTS bank_accounts;

CREATE TABLE bank_accounts (
    acc_id INTEGER PRIMARY KEY,
    owner TEXT,
    balance REAL
);

INSERT INTO bank_accounts VALUES (1, 'Alice', 1000.0), (2, 'Bob', 500.0);

-- Transaction 1: Successful Transfer of $200 from Alice to Bob
BEGIN TRANSACTION;
UPDATE bank_accounts SET balance = balance - 200 WHERE acc_id = 1;
UPDATE bank_accounts SET balance = balance + 200 WHERE acc_id = 2;
COMMIT;

-- Transaction 2: Invalid Transfer with Rollback
BEGIN TRANSACTION;
UPDATE bank_accounts SET balance = balance - 99999 WHERE acc_id = 1;
ROLLBACK;
