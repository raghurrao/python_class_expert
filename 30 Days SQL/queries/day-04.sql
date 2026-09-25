-- Day 4 practice area. Replace this query with one assignment query, save, and run:
-- python run_sql.py queries/day-04.sql
SELECT reviewer, rating
FROM book_reviews
WHERE rating IS NULL;
