# Day 7: Metadata and Table Reflection (SQLAlchemy Core)

Now that you know how to connect to a database, let's learn how SQLAlchemy understands the structure of your tables using `MetaData`.

---

## Step 1: The MetaData Object

**Concept:** `MetaData` is a catalog that stores the structure of your database (the tables, columns, constraints, etc.) in memory inside Python.

**Example:**
```python
from sqlalchemy import MetaData

# Create a MetaData instance
metadata = MetaData()
```

**🎯 Your Turn (Task 1):** 
Open `day_7_answers.py`. Import `MetaData` and create an instance of it named `metadata`.

---

## Step 2: Table Reflection

**Concept:** Instead of manually telling SQLAlchemy what your tables look like by typing out every column, you can have it "reflect" the tables directly from the database schema!

**Example:**
```python
from sqlalchemy import Table

# Connect the engine to the metadata and reflect a specific table
users_table = Table('users', metadata, autoload_with=engine)

# Print the columns SQLAlchemy discovered
print(users_table.columns.keys())
```

**🎯 Your Turn (Task 2):**
In `day_7_answers.py`, I've already included the `engine` code for you. 
Import `Table`. Create a variable `posts_table` that reflects the `posts` table from `blog.db` using `Table('posts', metadata, autoload_with=engine)`.
Then, print `posts_table.columns.keys()` to see the column names SQLAlchemy found!

Run `python test_day_7.py` to see table reflection in action!
