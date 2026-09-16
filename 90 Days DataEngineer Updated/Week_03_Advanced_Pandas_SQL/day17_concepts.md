# Day 17: SQLite in Python

Data engineers frequently pull data from relational databases. Today we learn how to connect to a SQLite database using Python's built-in `sqlite3` library and how to load that data directly into Pandas.

---

## 1. Why SQLite?
SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. It doesn't require a separate server process. The database is just a file on your disk, making it perfect for learning SQL and building lightweight applications.

---

## 2. Core Concepts & Operations

### Connecting to a Database
To interact with a database, you first need to establish a connection.

```python
import sqlite3
import pandas as pd

# Connect to a database file (creates it if it doesn't exist)
# Using ':memory:' creates a temporary database in RAM instead of a file
conn = sqlite3.connect('my_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()
```

### Executing SQL Commands
You use the cursor to execute raw SQL statements, like creating tables and inserting data.

```python
# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

# Commit the transaction (save changes)
conn.commit()
```

### Reading SQL into Pandas
While you can use `cursor.fetchall()` to get raw tuples, Pandas provides a much better way. `pd.read_sql_query()` executes a SQL query and immediately returns a DataFrame.

```python
# Read data directly into a DataFrame
query = "SELECT * FROM users"
df = pd.read_sql_query(query, conn)

print(df)
#    id   name  age
# 0   1  Alice   30
# 1   2    Bob   25

# You can also write a DataFrame directly to a SQL table
# df.to_sql('users_backup', conn, if_exists='replace', index=False)
```

### Closing the Connection
Always close the connection when you're done to free up resources and avoid database locks.

```python
conn.close()
```

---

## 3. Reference Documentation
* [Python sqlite3 documentation](https://docs.python.org/3/library/sqlite3.html)
* [Pandas read_sql_query](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html)
