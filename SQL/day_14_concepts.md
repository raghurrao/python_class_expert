# Day 14: ORM Relationships (One-to-Many)

Welcome to Day 14! One of the most powerful features of the SQLAlchemy ORM is how it handles relationships between tables. Instead of writing manual `JOIN` statements every time, you can set up Python attributes that automatically fetch related objects!

---

## Step 1: `relationship()` and `ForeignKey`

**Concept:** To link two classes, you use `ForeignKey` on the child table, and `relationship()` on the parent (and often child) classes to create a bidirectional link.

**Example:**
```python
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # One user has MANY orders
    orders: Mapped[list["Order"]] = relationship(back_populates="user")

class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    
    # One order belongs to ONE user
    user: Mapped["User"] = relationship(back_populates="orders")
```
*(Notice how `back_populates` links the two attributes together!)*

**🎯 Your Turn (Task 1):** 
Open `day_14_answers.py`. I have provided the `Author` and `Post` classes.
1. In `Author`, add a `posts` attribute using `relationship(back_populates="author")`. Use the type hint `Mapped[list["Post"]]`.
2. In `Post`, add an `author_id` column using `ForeignKey('authors.id')`. 
3. Also in `Post`, add an `author` attribute using `relationship(back_populates="posts")`. Use the type hint `Mapped["Author"]`.

---

## Step 2: Accessing the Relationship

**Concept:** Once relationships are set up, you can simply access the attribute in Python to get the related objects! SQLAlchemy will do the `JOIN` behind the scenes for you.

**Example:**
```python
with Session(engine) as session:
    user = session.get(User, 1)
    
    # Automatically fetches all their orders from the database!
    for order in user.orders:
        print(order.id)
```

**🎯 Your Turn (Task 2):**
In `day_14_answers.py`, inside the `Session` block, use `session.get()` to grab the author with `id=1` (`alice`). 
Then, loop through her `.posts` attribute and print out the `title` of each post!

Run `python test_day_14.py` to test your ORM Relationship logic!
