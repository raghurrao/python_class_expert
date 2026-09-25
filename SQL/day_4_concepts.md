# Day 4: Joins (The Heart of Relational Databases)

Welcome to Day 4! Today we learn how to combine data from multiple tables.
I have generated a real SQLite database file for you named **`blog.db`** right in your folder. It contains the `authors`, `posts`, and `comments` tables with some pre-populated data so you can actually practice on real data!

---

## Step 1: INNER JOIN

**Concept:** `INNER JOIN` returns rows that have matching values in *both* tables.

**Example:**
```sql
-- Get orders along with the username of the person who made them
SELECT orders.order_id, users.username
FROM orders
INNER JOIN users ON orders.user_id = users.id;
```

**🎯 Your Turn (Task 1):** 
Open `day_4_answers.sql`. Write a query to get every `post.title` along with its `author.username`. 
You need to `INNER JOIN` the `posts` table with the `authors` table.

---

## Step 2: LEFT JOIN

**Concept:** `LEFT JOIN` returns *all* rows from the left table, and the matched rows from the right table. If there is no match, the right side will contain `NULL`.

**Example:**
```sql
-- Get all users, and any orders they might have (even if they have 0 orders)
SELECT users.username, orders.order_id
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```
*(Notice that `users` is the left table here).*

**🎯 Your Turn (Task 2):**
Write a query to get *all* authors (`authors.username`) and the `title` of their posts. 
*Hint: Use `LEFT JOIN` starting with the `authors` table so that an author like 'charlie' (who has 0 posts) still shows up in your results with a `NULL` title!*

Run `python test_day_4.py` to test your syntax!
