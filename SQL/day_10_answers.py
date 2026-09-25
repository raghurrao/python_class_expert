# Interactive Day 10 Answers
from sqlalchemy import create_engine, MetaData, Table, select

# Setup
engine = create_engine('sqlite:///blog.db')
metadata = MetaData()
authors_table = Table('authors', metadata, autoload_with=engine)
posts_table = Table('posts', metadata, autoload_with=engine)

# Task 1: Select from both tables using a join, execute, and print the results
stmt = select(authors_table, posts_table).select_from(authors_table.join(posts_table))

with engine.connect() as conn:
    result = conn.execute(stmt)
    for row in result.fetchall():
        print(row)
