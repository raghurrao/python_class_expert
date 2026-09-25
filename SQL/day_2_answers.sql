-- Interactive Day 2 Answers
-- Note: Do NOT rewrite your CREATE TABLE statements here. 
-- The test script will automatically run day_1_answers.sql before running this file.

-- Task 1: INSERT two authors and two posts
INSERT INTO authors (id, username, email) VALUES (1, 'author_one', 'one@test.com');
INSERT INTO authors (id, username, email) VALUES (2, 'author_two', 'two@test.com');
INSERT INTO posts (id, title, author_id) VALUES (1, 'First Post', 1);
INSERT INTO posts (id, title, author_id) VALUES (2, 'Second Post', 2);

-- Task 2: SELECT post titles where author_id = 1
SELECT title FROM posts WHERE author_id = 1;

-- Task 3: UPDATE the email of author_id 2 to 'new_email@example.com'
UPDATE authors SET email = 'new_email@example.com' WHERE id = 2;

-- Task 4: DELETE the post with id = 1
DELETE FROM posts WHERE id = 1;
