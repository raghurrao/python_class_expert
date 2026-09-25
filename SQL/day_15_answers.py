# Interactive Day 15 Answers
from sqlalchemy import create_engine, String, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship, joinedload

engine = create_engine('sqlite:///blog.db')

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = 'authors'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    posts: Mapped[list["Post"]] = relationship(back_populates="author")

class Post(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id'))
    author: Mapped["Author"] = relationship(back_populates="posts")

with Session(engine) as session:
    # Task 1: Create a select statement for Author with joinedload(Author.posts)
    stmt = select(Author).options(joinedload(Author.posts))
    
    # Task 2: Execute using .scalars().unique().all(), then loop and print
    authors = session.execute(stmt).scalars().unique().all()
    for author in authors:
        for post in author.posts:
            print(f"{author.username}: {post.title}")
