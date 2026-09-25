# Day 5: Subqueries & CTEs

Welcome to Day 5! Sometimes, you need to use the result of one query as the input for another query. 

---

## Step 1: Subqueries

**Concept:** A subquery is a query nested inside another query (often inside a `WHERE` clause).

**Example:**
```sql
-- Find all orders placed by users who live in 'New York'
SELECT order_id 
FROM orders 
WHERE user_id IN (
    SELECT id FROM users WHERE city = 'New York'
);
```

**🎯 Your Turn (Task 1):** 
Using the `blog.db`, open `day_5_answers.sql`. Write a query to select the `title` of all posts written by the author whose `username` is exactly `'alice'`. 
*Do this using a Subquery in the WHERE clause, not a JOIN!*

---

## Step 2: Common Table Expressions (CTEs)

**Concept:** A CTE (using the `WITH` clause) acts like a temporary table that exists just for one query. It makes complex queries much easier to read than deeply nested subqueries.

**Example:**
```sql
WITH NewYorkUsers AS (
    SELECT id FROM users WHERE city = 'New York'
)
SELECT order_id 
FROM orders 
WHERE user_id IN (SELECT id FROM NewYorkUsers);
```

**🎯 Your Turn (Task 2):**
Rewrite the query from Task 1 using a CTE. Create a CTE called `AliceAuthor` that selects the `id` of the author named `'alice'`. Then, on the next line, select the `title` from `posts` where the `author_id` is in that CTE.

Run `python test_day_5.py` to see if you mastered subqueries and CTEs!
