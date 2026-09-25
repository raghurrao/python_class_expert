# Day 11: Transactions (SQLAlchemy Core)

You've successfully queried and updated data! However, in a real database, you want to make sure a series of operations either *all* succeed or *all* fail (rollback). This is called a Transaction.

---

## Step 1: The `engine.begin()` Context Manager

**Concept:** Earlier we used `engine.connect()` and called `conn.commit()` manually. 
If an error happens in your code before you reach `.commit()`, the database might be left in a weird state (like creating a user but failing to create their default settings). 

Instead, we should use `engine.begin()`. This creates a transaction block. 
*   If the block finishes without errors, it **automatically commits**! 
*   If Python crashes inside the block, it **automatically rolls back** everything!

**Example:**
```python
# Automatically commits on success, rolls back on error!
with engine.begin() as conn:
    conn.execute(stmt1)
    conn.execute(stmt2)
```

**🎯 Your Turn (Task 1):** 
Open `day_11_answers.py`. Write a block using `with engine.begin() as conn:`. 
Inside, execute an `insert` for a new author, and then an `insert` for a new post belonging to that author. 
Because you are using `engine.begin()`, you **should not** manually call `.commit()`!

Run `python test_day_11.py` to verify!
