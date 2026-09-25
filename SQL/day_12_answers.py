# Interactive Day 12 Answers
from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine('sqlite:///blog.db')

class Base(DeclarativeBase):
    pass

# Task 1: Create an Author class mapping to the 'authors' table
class Author(Base):
    __tablename__ = 'authors'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))

# Task 2: Open a Session, create a new Author named 'frank', add and commit
with Session(engine) as session:
    frank = Author(username='frank')
    session.add(frank)
    session.commit()
