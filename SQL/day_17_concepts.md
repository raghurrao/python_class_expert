# Day 17: Generating Migrations (Alembic)

Now that Alembic knows *where* your database is, you need to tell it *what* your database should look like. It does this by reading your SQLAlchemy Classes!

---

## Step 1: Linking your MetaData

**Concept:** To automatically generate migrations, Alembic needs to read your SQLAlchemy `Base.metadata`. 
You do this by editing `alembic/env.py`.

**Example:**
Inside `alembic/env.py`, you import your `Base` class and point `target_metadata` to it:
```python
from my_models import Base
target_metadata = Base.metadata
```

**🎯 Your Turn (Task 1):** 
I have extracted your `Author` and `Post` classes into a new file called **`models.py`** in your SQL folder.
Open **`alembic/env.py`** (it's inside the alembic folder). 
Around line 21, change `target_metadata = None` to the following:
```python
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from models import Base

target_metadata = Base.metadata
```
*(The sys.path lines just ensure Alembic can find the `models.py` file in the folder above it).*

---

## Step 2: The Migration Commands

**Concept:** Once Alembic knows about your classes and your database, you run two terminal commands:
1. `alembic revision --autogenerate -m "Initial"` (Creates the migration script)
2. `alembic upgrade head` (Applies the script to the database)

**🎯 Your Turn (Task 2):**
Let's see if your configuration in `env.py` is correct first! 
Run `python test_day_17.py` to verify your `env.py` file!
*(If it passes, we will actually run the migration commands in the next lesson).*
