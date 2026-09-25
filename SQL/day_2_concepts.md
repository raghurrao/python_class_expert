# Day 2: Interactive DML (Data Manipulation Language)

Welcome to Day 2! Now that we have our tables set up, let's learn how to create, read, update, and delete (CRUD) data within them.

---

## Step 1: INSERT (Create)

**Concept:** The `INSERT INTO` statement adds new rows of data. Note that text values must be wrapped in single quotes (`'like this'`).

**Example:**
```sql
INSERT INTO simple_users (id, username) VALUES (1, 'john_doe');
```

**🎯 Your Turn (Task 1):** 
Open `day_2_answers.sql`. Write `INSERT` statements to add:
1. Two authors (with `id` 1 and 2, and unique usernames/emails).
2. Two posts (one written by `author_id = 1`, and the other by `author_id = 2`).

Run `python test_day_2.py` to see if you pass Step 1!

---

## Step 2: SELECT (Read)

**Concept:** `SELECT` retrieves data. You can filter rows using the `WHERE` clause.

**Example:**
```sql
-- Get all users
SELECT * FROM users;
-- Get just the username of a specific user
SELECT username FROM users WHERE id = 1;
```

**🎯 Your Turn (Task 2):**
In `day_2_answers.sql` under Task 2, write a `SELECT` query that returns just the `title` of all posts authored by the author with `id = 1`. 
Run the tests again!

---

## Step 3: UPDATE (Update)

**Concept:** `UPDATE` modifies existing data. Always use a `WHERE` clause, otherwise, you will update every single row in the table!

**Example:**
```sql
UPDATE users SET username = 'j_doe' WHERE id = 1;
```

**🎯 Your Turn (Task 3):**
Under Task 3, write an `UPDATE` statement that changes the `email` of the author with `id = 2` to `'new_email@example.com'`.
Run the tests to pass Step 3!

---

## Step 4: DELETE (Delete)

**Concept:** `DELETE` removes rows. Again, always use `WHERE` unless you want to empty the entire table!

**Example:**
```sql
DELETE FROM users WHERE id = 1;
```

**🎯 Your Turn (Task 4):**
Under Task 4, write a `DELETE` statement to remove the post with `id = 1`.
Run the tests to finish Day 2!
