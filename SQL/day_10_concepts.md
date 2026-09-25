# Day 10: Core Joins (SQLAlchemy Core)

You've learned to query single tables in Python. Now let's learn how to `JOIN` tables in SQLAlchemy Core, just like we did in pure SQL!

---

## Step 1: Using .join()

**Concept:** You can join two reflected tables using the `.join()` method. The amazing part is that SQLAlchemy is smart enough to figure out the `ON` clause automatically if it detects a Foreign Key between the tables!

**Example:**
```python
from sqlalchemy import select

# Select from users joined with orders
# SQLAlchemy sees the ForeignKey and automatically writes: ON users.id = orders.user_id
stmt = select(users_table, orders_table).select_from(
    users_table.join(orders_table)
)
```

**🎯 Your Turn (Task 1):** 
Open `day_10_answers.py`. I've reflected both the `authors` and `posts` tables for you.
Write a `select()` statement that selects all columns from both `authors_table` and `posts_table`. 
Use `.select_from(authors_table.join(posts_table))` to chain the join.
Execute the query, fetch all results, and print them!

Run `python day_10_answers.py` to see your joined data print out, and then `python test_day_10.py` to verify your syntax!
