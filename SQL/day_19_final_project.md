# 🏆 Day 19: The Grand Finale Mini-Project

Congratulations on reaching the end of the SQL & SQLAlchemy Mastery Plan! You've learned everything from raw SQL `JOIN`s, to SQLAlchemy Core queries, to ORM `joinedload` relationship loading, to Alembic Database Migrations.

For your final challenge, there is no test script. It's just you and a blank canvas.

## 🚀 The Challenge

Using everything you've learned, create a script called `final_project.py` in your SQL folder that does the following:

1. **Setup:** Create a new SQLite database connection (`sqlite:///final.db`) and map three ORM classes: `User`, `Category`, and `Product`. 
   *(Hint: Set up a One-to-Many relationship where a `Category` has many `Product`s. The `User` table can just be standalone).*
2. **Create:** Open a `Session` and add a few Users, Categories, and Products. `.commit()` them to the database.
3. **Read (Eager Loading):** Write a `select()` query using `joinedload` to fetch all Categories and their associated Products in a single query. Loop through and `print()` them out!

Once you complete this, you are officially an **Advanced SQLAlchemy Developer**! Feel free to refer back to any of the previous Day's concepts and answer files if you need a syntax reminder. 

Thank you for an incredible journey!
