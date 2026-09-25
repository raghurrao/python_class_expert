# Day 13: CRUD with the ORM

Now that we have our `Author` class mapped, let's learn how to perform Create, Read, Update, and Delete operations seamlessly using the `Session`.

---

## Step 1: Querying (Read)

**Concept:** In SQLAlchemy 2.0, you query using `session.execute(select(...))` just like in Core, but you get back actual Python objects instead of basic rows! Use `.scalars().all()` to grab a clean list of the objects.

**Example:**
```python
from sqlalchemy import select

with Session(engine) as session:
    stmt = select(User).where(User.username == 'frank')
    # Use scalars() to get the actual User objects instead of Row tuples
    users = session.execute(stmt).scalars().all()
    
    for user in users:
        print(user.username)
```

**🎯 Your Turn (Task 1):** 
Open `day_13_answers.py`. Write a `select` statement for the `Author` class where `username == 'alice'`. 
Execute it using `session.execute(stmt).scalars().all()` and print out Alice's username!

---

## Step 2: Update and Delete

**Concept:** Updating is magically simple in the ORM! You just modify the Python object's attribute, and call `session.commit()`. SQLAlchemy automatically figures out the SQL `UPDATE` behind the scenes! To delete, you pass the object to `session.delete()`.

**Example:**
```python
with Session(engine) as session:
    # Get a user (using session.get is a fast shortcut for primary key lookups!)
    user = session.get(User, 1) 
    
    # Update is just changing a Python property!
    user.username = 'new_name'
    
    # Delete
    session.delete(user)
    
    session.commit()
```

**🎯 Your Turn (Task 2):**
In `day_13_answers.py`, use `session.get(Author, 2)` to grab the author with `id=2` (bob). 
Change his username to `'bob_the_builder'` by updating the object's attribute. Then `commit()` the session!

Run `python test_day_13.py` to verify your ORM CRUD skills!
