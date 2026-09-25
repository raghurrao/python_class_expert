# Day 8: Executing Core Inserts and Selects (SQLAlchemy Core)

Now that SQLAlchemy knows the structure of your database via Table Reflection, let's use SQLAlchemy Core functions to insert and select data *without* writing raw SQL strings!

---

## Step 1: Core Inserts

**Concept:** You can use the `insert()` function to build an insert statement programmatically in pure Python.

**Example:**
```python
from sqlalchemy import insert

# Build the insert statement
stmt = insert(users_table).values(username='sarah', email='sarah@test.com')

# Execute it
with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit() # Important! You must commit when making changes in SQLAlchemy 2.0.
```

**🎯 Your Turn (Task 1):** 
Open `day_8_answers.py`. Import `insert`. I've already reflected the `authors` table for you. Build an `insert` statement to add a new author with `username='david'` and `email='david@test.com'`. Then execute and commit it using a connection!

---

## Step 2: Core Selects

**Concept:** You can use the `select()` function to build a select statement programmatically.

**Example:**
```python
from sqlalchemy import select

# Build the select statement
stmt = select(users_table)

# Execute and fetch
with engine.connect() as conn:
    result = conn.execute(stmt)
    for row in result.fetchall():
        print(row)
```

**🎯 Your Turn (Task 2):**
In `day_8_answers.py`, import `select`. Build a select statement for the `authors` table, execute it, fetch all the results, and print them! When you run the script, you should see 'david' in the printed list.

Run `python test_day_8.py` to test your logic!
