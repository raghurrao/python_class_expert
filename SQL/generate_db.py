import sqlite3

def generate():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.executescript("""
        DROP TABLE IF EXISTS comments;
        DROP TABLE IF EXISTS posts;
        DROP TABLE IF EXISTS authors;

        CREATE TABLE authors (
            id INTEGER PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL
        );
        CREATE TABLE posts (
            id INTEGER PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(id)
        );
        CREATE TABLE comments (
            id INTEGER PRIMARY KEY,
            comment_text TEXT NOT NULL,
            rating INTEGER CHECK(rating >= 1 AND rating <= 5),
            post_id INTEGER,
            FOREIGN KEY (post_id) REFERENCES posts(id)
        );

        INSERT INTO authors (id, username, email) VALUES (1, 'alice', 'alice@test.com');
        INSERT INTO authors (id, username, email) VALUES (2, 'bob', 'bob@test.com');
        INSERT INTO authors (id, username, email) VALUES (3, 'charlie', 'charlie@test.com'); -- Charlie has no posts!

        INSERT INTO posts (id, title, author_id) VALUES (1, 'Alice First Post', 1);
        INSERT INTO posts (id, title, author_id) VALUES (2, 'Alice Second Post', 1);
        INSERT INTO posts (id, title, author_id) VALUES (3, 'Bob First Post', 2);

        INSERT INTO comments (id, comment_text, rating, post_id) VALUES (1, 'Great post Alice!', 5, 1);
        INSERT INTO comments (id, comment_text, rating, post_id) VALUES (2, 'Nice', 4, 1);
        INSERT INTO comments (id, comment_text, rating, post_id) VALUES (3, 'Not bad', 3, 3);
    """)
    conn.commit()
    conn.close()
    print("blog.db generated successfully.")

if __name__ == '__main__':
    generate()
