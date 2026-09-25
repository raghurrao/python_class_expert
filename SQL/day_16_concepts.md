# Day 16: Database Migrations (Alembic Setup)

Welcome to Week 4! So far, we created `blog.db` manually and assumed the table structures never changed. But what happens when you want to add a new column to a database that already has live data? You can't just drop the table and recreate it!

You need a **Migration Tool**. SQLAlchemy's official migration tool is called **Alembic**.

---

## Step 1: Initializing Alembic

**Concept:** Before you can write migrations, you have to initialize Alembic. This creates a folder structure to hold your migration scripts.
Normally, you would run this in your terminal:
```bash
alembic init alembic
```

*(For this Interactive Day, I have already run `alembic init` for you! You will see a new `alembic/` folder and an `alembic.ini` file in your directory).*

---

## Step 2: Configuring Alembic to find your Database

**Concept:** Alembic needs to know where your database is! You configure this inside the `alembic.ini` file. 

**Example:**
Inside `alembic.ini`, there is a line that looks like this:
```ini
sqlalchemy.url = driver://user:pass@localhost/dbname
```
You need to change it to point to your actual database.

**🎯 Your Turn (Task 1):** 
Open the newly created **`alembic.ini`** file (it's in your SQL folder). 
Find the line that starts with `sqlalchemy.url` (around line 63) and change it to point to our local sqlite database:
`sqlalchemy.url = sqlite:///blog.db`

Run `python test_day_16.py` to see if you successfully configured Alembic!
