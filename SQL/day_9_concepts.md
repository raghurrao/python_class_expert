# Day 9: Core Filtering, Ordering, and Updates/Deletes (SQLAlchemy Core)

Now that you can `insert` and `select`, let's learn how to filter results with `where()`, sort them with `order_by()`, and modify them with `update()` and `delete()`.

---

## Step 1: Filtering and Ordering (where & order_by)

**Concept:** You can chain `.where()` and `.order_by()` to your `select()` statement. 

**Example:**
```python
from sqlalchemy import select

# Select users where username is 'sarah', ordered by id descending
stmt = select(users_table).where(users_table.c.username == 'sarah').order_by(users_table.c.id.desc())
```
*(Notice the `.c.` which stands for 'columns' when accessing a column on a reflected table!)*

**🎯 Your Turn (Task 1):** 
Open `day_9_answers.py`. Write a `select` statement for the `authors_table` where the username is `'alice'`, ordered by `id` descending. Execute it, fetch all results, and print them!

---

## Step 2: Updates and Deletes

**Concept:** You build `update()` and `delete()` statements similarly, chaining `.where()` so you don't affect every row!

**Example:**
```python
from sqlalchemy import update, delete

# Update
update_stmt = update(users_table).where(users_table.c.id == 1).values(email='new@test.com')

# Delete
delete_stmt = delete(users_table).where(users_table.c.id == 2)
```

**🎯 Your Turn (Task 2):**
In `day_9_answers.py`, write an `update` statement to change the email of the author with `id = 3` (charlie) to `'charlie_new@test.com'`. 
Execute and `commit()` the connection! 

Run `python day_9_answers.py` to run your code, then run `python test_day_9.py` to verify!
