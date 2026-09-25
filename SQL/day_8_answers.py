# Interactive Day 8 Answers
from sqlalchemy import create_engine, MetaData, Table, insert, select

# Setup
engine = create_engine('sqlite:///blog.db')
metadata = MetaData()
authors_table = Table('authors', metadata, autoload_with=engine)

# Task 1: Import insert, build an insert statement for 'david', execute and commit
stmt_insert = insert(authors_table).values(username='david', email='david@test.com')
with engine.connect() as conn:
    conn.execute(stmt_insert)
    conn.commit()

# Task 2: Import select, build a select statement for all authors, execute and print
stmt_select = select(authors_table)
with engine.connect() as conn:
    result = conn.execute(stmt_select)
    for row in result.fetchall():
        print(row)
