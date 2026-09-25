# Day 6: Intro to SQLAlchemy (Core)

Welcome to Week 2! We are now leaving raw `.sql` files behind and writing everything in Python using **SQLAlchemy**.
SQLAlchemy is a powerful library that allows you to connect to databases and execute SQL programmatically.

---

## Step 1: The Engine

**Concept:** The `Engine` is the starting point for any SQLAlchemy application. It handles the connection pool and dialect to the database. You create it using a "Connection String" (a URL that tells SQLAlchemy where the database is located and what type it is).

**Example:**
```python
from sqlalchemy import create_engine

# Create an engine connected to a local SQLite database named 'my_db.db'
engine = create_engine('sqlite:///my_db.db')
```

**🎯 Your Turn (Task 1):** 
Open `day_6_answers.py`. Import `create_engine` and create an engine connected to our `blog.db` file (`'sqlite:///blog.db'`). Assign it to a variable named `engine`.

---

## Step 2: Connections & Executing Raw SQL

**Concept:** Once you have an engine, you can open a `Connection` to the database and use it to execute raw SQL strings. You must wrap raw SQL strings in the `text()` function.

**Example:**
```python
from sqlalchemy import text

# Open a connection using a context manager (the 'with' block)
with engine.connect() as conn:
    # Execute a raw SQL string
    result = conn.execute(text("SELECT * FROM users"))
    
    # Fetch all the rows
    for row in result.fetchall():
        print(row)
```

**🎯 Your Turn (Task 2):**
In `day_6_answers.py`, import the `text` function. Then, open a connection using `with engine.connect() as conn:`. Inside that block, use `conn.execute(text(...))` to run a basic `SELECT * FROM authors` query. Fetch the results using `.fetchall()` and print them out!

Run `python test_day_6.py` to see if you successfully executed your first Python SQLAlchemy code!
