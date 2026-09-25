# Day 15: ORM Querying (Eager vs Lazy Loading)

When you access a relationship (like you did on Day 14 with `alice.posts`), SQLAlchemy automatically pauses your code and runs a *second* SQL query behind the scenes to fetch those posts. This is called **Lazy Loading**. 

While this is convenient, if you write a `for` loop over 100 authors and ask for their posts inside the loop, SQLAlchemy will run 100 separate queries! This makes your app extremely slow and is known as the **N+1 query problem**.

---

## Step 1: Eager Loading with `joinedload`

**Concept:** To fix the N+1 problem, you can tell SQLAlchemy to fetch the parent *and* the children in a single, efficient query using a SQL `JOIN`. You do this using `.options()` and `joinedload`.

**Example:**
```python
from sqlalchemy.orm import joinedload
from sqlalchemy import select

with Session(engine) as session:
    # Tell SQLAlchemy to fetch the User AND their orders in the same query!
    stmt = select(User).options(joinedload(User.orders))
    
    users = session.execute(stmt).scalars().unique().all()
```
*(Note: We use `.unique()` because the SQL JOIN technically returns duplicate user rows for each order they have, and `.unique()` cleans those duplicates out for us).*

**🎯 Your Turn (Task 1):** 
Open `day_15_answers.py`. I have imported `joinedload` for you. 
Write a `select(Author)` statement, but add `.options(joinedload(Author.posts))` to it so that all posts are fetched instantly!

---

## Step 2: Executing and Verifying

**Concept:** Once you've eager-loaded the relationship, accessing `author.posts` will *not* trigger any extra database queries!

**🎯 Your Turn (Task 2):**
In `day_15_answers.py`, execute your statement using `session.execute(stmt).scalars().unique().all()`.
Loop through the authors, and inside that loop, loop through their posts and print the titles. 
Everything is happening efficiently from a single SQL query!

Run `python test_day_15.py` to verify!
