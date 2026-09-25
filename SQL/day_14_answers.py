# Interactive Day 14 Answers
from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

engine = create_engine('sqlite:///blog.db')

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = 'authors'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    
    # Task 1a: Add 'posts' relationship
    posts: Mapped[list["Post"]] = relationship(back_populates="author")


class Post(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    
    # Task 1b: Add 'author_id' ForeignKey column
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id'))
    
    
    # Task 1c: Add 'author' relationship
    author: Mapped["Author"] = relationship(back_populates="posts")
    

with Session(engine) as session:
    # Task 2: Get author id=1, loop through her posts, and print the titles
    alice = session.get(Author, 1)
    if alice:
        for post in alice.posts:
            print(post.title)
