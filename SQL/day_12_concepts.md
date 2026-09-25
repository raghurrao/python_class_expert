# Day 12: ORM Basics (Declarative Mapping & Sessions)

Welcome to Week 3! We are finally moving to the **Object-Relational Mapper (ORM)**. 
Instead of thinking about "tables" and "rows", you will map your tables directly to Python **Classes**, and your rows will become **Objects**.

---

## Step 1: Declarative Mapping

**Concept:** You create a base class, and all your tables inherit from it. You define the table name and columns inside the class using Python type hints (`Mapped`).

**Example:**
```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String

# 1. Create the Base class
class Base(DeclarativeBase):
    pass

# 2. Map a table to a Python class
class User(Base):
    __tablename__ = 'users'
    
    # Define columns
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
```

**🎯 Your Turn (Task 1):** 
Open `day_12_answers.py`. I have already provided the `Base` class. 
Create an `Author` class that inherits from `Base` and maps to the `authors` table. 
Add two columns: `id` (int, primary key) and `username` (string 50).

---

## Step 2: The Session

**Concept:** In Core, you used `Connection` and `engine.connect()`. In the ORM, you use a `Session`. The session manages your objects and talks to the database for you.

**Example:**
```python
from sqlalchemy.orm import Session

# Create an object (just like a normal Python class!)
new_user = User(username='frank')

# Add to session and commit
with Session(engine) as session:
    session.add(new_user)
    session.commit()
```

**🎯 Your Turn (Task 2):**
In `day_12_answers.py`, I've set up the engine. 
Open a block with `with Session(engine) as session:`. Create a new `Author` object with `username='frank'`. Add it to the session, and commit it!

Run `python test_day_12.py` to see if you have successfully entered the world of ORM!
