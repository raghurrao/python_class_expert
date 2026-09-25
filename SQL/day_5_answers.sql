-- Interactive Day 5 Answers
-- Note: You are querying against blog.db

-- Task 1: Use a Subquery to find the titles of posts written by 'alice'
SELECT title 
FROM posts 
WHERE author_id = (SELECT id FROM authors WHERE username = 'alice');

-- Task 2: Rewrite Task 1 using a CTE (WITH clause)
WITH AliceAuthor AS (
    SELECT id FROM authors WHERE username = 'alice'
)
SELECT title 
FROM posts 
WHERE author_id IN (SELECT id FROM AliceAuthor);
