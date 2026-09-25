# Day 3: Aggregations & Grouping

Welcome to Day 3! Now we will learn how to analyze our data using aggregate functions and grouping.

---

## Step 1: Aggregate Functions

**Concept:** Aggregate functions perform a calculation on a set of values and return a single value.
*   `COUNT()`: Returns the number of rows.
*   `SUM()`: Returns the total sum of a numeric column.
*   `AVG()`: Returns the average value.
*   `MAX()` / `MIN()`: Returns the highest/lowest value.

**Example:**
```sql
-- Count how many total users exist
SELECT COUNT(*) FROM users;
```

**🎯 Your Turn (Task 1):** 
Open `day_3_answers.sql`. Write a query to find the total number of posts (using `COUNT`) in the database.

---

## Step 2: The GROUP BY Clause

**Concept:** `GROUP BY` groups rows that have the same values into summary rows. It is almost always used in conjunction with aggregate functions.

**Example:**
```sql
-- Count how many orders each user has made
SELECT user_id, COUNT(*) 
FROM orders 
GROUP BY user_id;
```

**🎯 Your Turn (Task 2):**
Write a query to count how many posts *each* author has written. Select the `author_id` and the `COUNT` of posts, grouped by `author_id`.

---

## Step 3: The HAVING Clause

**Concept:** `HAVING` was added to SQL because the `WHERE` keyword cannot be used with aggregate functions. It filters the data *after* the grouping has occurred.

**Example:**
```sql
-- Find users who have made MORE than 5 orders
SELECT user_id, COUNT(*) 
FROM orders 
GROUP BY user_id 
HAVING COUNT(*) > 5;
```

**🎯 Your Turn (Task 3):**
Write a query to find authors who have written *more than 1* post. Select the `author_id` and the `COUNT` of posts, grouping by `author_id`, and using `HAVING` to filter.

Run `python test_day_3.py` to see your results!
