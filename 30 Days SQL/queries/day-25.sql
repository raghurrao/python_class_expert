-- Day 25 practice: count all reviews, then compare with COUNT(rating).
-- Run with: python run_sql.py queries/day-25.sql
SELECT COUNT(*) AS all_reviews,
       COUNT(rating) AS rated_reviews
FROM book_reviews;
