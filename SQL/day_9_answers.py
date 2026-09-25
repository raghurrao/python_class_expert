# Interactive Day 9 Answers
from sqlalchemy import create_engine, MetaData, Table, select, update

# Setup
engine = create_engine('sqlite:///blog.db')
metadata = MetaData()
authors_table = Table('authors', metadata, autoload_with=engine)

# Task 1: Select authors where username is 'alice', ordered by id descending. Execute and print.
stmt_sel = select(authors_table).where(authors_table.c.username == 'alice').order_by(authors_table.c.id.desc())
with engine.connect() as conn:
    result = conn.execute(stmt_sel)
    for row in result.fetchall():
        print(row)

# Task 2: Update the email of author with id=3 to 'charlie_new@test.com'. Execute and commit.
stmt_upd = update(authors_table).where(authors_table.c.id == 3).values(email='charlie_new@test.com')
with engine.connect() as conn:
    conn.execute(stmt_upd)
    conn.commit()
