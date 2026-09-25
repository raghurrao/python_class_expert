-- Interactive Day 4 Answers
-- Note: You are practicing against the real blog.db file we just generated!

-- Task 1: INNER JOIN to get post title and author username
SELECT posts.title, authors.username
FROM posts
INNER JOIN authors ON posts.author_id = authors.id;

-- Task 2: LEFT JOIN to get all authors (even those with no posts) and their post titles
SELECT authors.username, posts.title
FROM authors
LEFT JOIN posts ON authors.id = posts.author_id;
