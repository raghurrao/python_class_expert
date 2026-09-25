-- Interactive Day 3 Answers

-- Task 1: Find the total number of posts in the posts table
SELECT COUNT(*) FROM posts;

-- Task 2: Count how many posts each author has written (Group by author_id)
SELECT author_id, COUNT(*) FROM posts GROUP BY author_id;

-- Task 3: Find authors who have written more than 1 post (Use HAVING)
SELECT author_id, COUNT(*) FROM posts GROUP BY author_id HAVING COUNT(*) > 1;
