# Interactive Day 6 Answers
from sqlalchemy import create_engine, text

# Task 1: Import create_engine and create an engine connected to 'sqlite:///blog.db'
engine = create_engine('sqlite:///blog.db')

# Task 2: Import text, open a connection, execute "SELECT * FROM authors", and print the results
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM authors"))
    for row in result.fetchall():
        print(row)
