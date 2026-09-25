# Interactive Day 11 Answers
from sqlalchemy import create_engine, MetaData, Table, insert

engine = create_engine('sqlite:///blog.db')
metadata = MetaData()
authors = Table('authors', metadata, autoload_with=engine)
posts = Table('posts', metadata, autoload_with=engine)

# Task 1: Use `engine.begin()` to insert an author and a post in one transaction
with engine.begin() as conn:
    conn.execute(insert(authors).values(username='eve', email='eve@test.com'))
    conn.execute(insert(posts).values(title='Eve First Post', author_id=4))
