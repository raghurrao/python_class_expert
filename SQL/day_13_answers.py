# Interactive Day 13 Answers
from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine('sqlite:///blog.db')

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = 'authors'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))

with Session(engine) as session:
    # Task 1: Select 'alice' and print her username
    stmt = select(Author).where(Author.username == 'alice')
    alices = session.execute(stmt).scalars().all()
    for alice in alices:
        print(alice.username)

    # Task 2: Get author id=2, change username to 'bob_the_builder', and commit
    bob = session.get(Author, 2)
    if bob:
        bob.username = 'bob_the_builder'
    session.commit()
