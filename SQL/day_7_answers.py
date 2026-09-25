# Interactive Day 7 Answers
from sqlalchemy import create_engine
engine = create_engine('sqlite:///blog.db')

# Task 1: Import MetaData and create an instance named `metadata`
from sqlalchemy import MetaData
metadata = MetaData()

# Task 2: Import Table, reflect the 'posts' table into a variable `posts_table`, and print its column keys
from sqlalchemy import Table
posts_table = Table('posts', metadata, autoload_with=engine)
print(posts_table.columns.keys())
