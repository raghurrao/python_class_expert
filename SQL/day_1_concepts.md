# Day 1: Interactive DDL (Data Definition Language)

Welcome to the interactive version of Day 1! Instead of reading everything at once, we will learn one small concept, immediately apply it in code, and test it before moving on.

---

## Step 1: The Basics of CREATE TABLE

**Concept:** The `CREATE TABLE` statement is used to define a new table and its columns. 

**Example:**
```sql
CREATE TABLE simple_users (
    id INTEGER,
    username VARCHAR(50)
);
```

**🎯 Your Turn (Task 1):** 
Open `day_1_answers.sql`. Under the `-- Task 1 & 2` heading, write a query to create a table called `authors` with three columns: `id` (INTEGER), `username` (VARCHAR(50)), and `email` (VARCHAR(100)).
Once written, save the file and run `python test_day_1.py` in your terminal to see if you pass Step 1!

---

## Step 2: Primary Keys and Constraints

**Concept:** To prevent bad data, we use rules called constraints.
*   `PRIMARY KEY`: Uniquely identifies the row.
*   `NOT NULL`: The column cannot be empty.
*   `UNIQUE`: No duplicates allowed.

**Example:**
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE
);
```

**🎯 Your Turn (Task 2):**
In `day_1_answers.sql`, update your `authors` table creation statement. 
Make `id` the `PRIMARY KEY`, and ensure `username` is both `NOT NULL` and `UNIQUE`. Make `email` `NOT NULL`.
Run `python test_day_1.py` again to pass Step 2!

---

## Step 3: Foreign Keys (Relationships)

**Concept:** A `FOREIGN KEY` links a column in one table to the `PRIMARY KEY` of another table. This is how tables relate to each other!

**Example:**
```sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

**🎯 Your Turn (Task 3):**
Under `-- Task 3` in your SQL file, create a `posts` table with:
*   `id` (INTEGER PRIMARY KEY)
*   `title` (VARCHAR(100) NOT NULL)
*   `author_id` (INTEGER)
Finally, add a foreign key linking `author_id` to the `id` column in the `authors` table.
Run the tests to pass Step 3!

---

## Step 4: The CHECK Constraint

**Concept:** The `CHECK` constraint ensures that values in a column meet a specific condition.

**Example:**
```sql
CREATE TABLE adult_users (
    id INTEGER PRIMARY KEY,
    age INTEGER CHECK (age >= 18)
);
```

**🎯 Your Turn (Task 4):**
Under `-- Task 4`, create a `comments` table with:
*   `id` (INTEGER PRIMARY KEY)
*   `post_id` (INTEGER with a Foreign Key referencing `posts(id)`)
*   `rating` (INTEGER)
Add a `CHECK` constraint to ensure the `rating` is between 1 and 5 (e.g., `rating >= 1 AND rating <= 5`).
Run the tests to finish Day 1!
