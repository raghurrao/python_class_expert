-- Interactive Day 1 Answers
-- Follow the steps in day_1_concepts.md and write your SQL here.

-- Task 1 & 2: Create the `authors` table (Apply constraints for Task 2 here as well)
CREATE TABLE authors (
    id INTEGER PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL
);

-- Task 3: Create the `posts` table with a Foreign Key
CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

-- Task 4: Create the `comments` table with a Foreign Key and CHECK constraint
CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    post_id INTEGER,
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    FOREIGN KEY (post_id) REFERENCES posts(id)
);
