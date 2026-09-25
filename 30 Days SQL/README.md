# 30 Days of SQL

A hands-on, day-by-day SQL learning course. Lessons and practice data live together in this folder.

## Your local practice database

The course database is `books.db` in this folder. It is a real SQLite database file containing the `books` table used in Day 1. To recreate it from scratch, run `python setup_database.py`. To run the starter query, run `python run_sql.py queries/day-01.sql`. Python includes SQLite support, so no separate database server or install is needed.

The SQL concepts in the first lessons work in both SQLite and PostgreSQL. We use SQLite locally to keep practice simple; dialect-specific differences will be called out when they matter.

## Lessons

- [Day 1 — Meet SQL and read your first table](lessons/day-01.md)
- [Day 2 — Filter rows with conditions](lessons/day-02.md)
- [Day 3 — Sort, limit, and remove duplicates](lessons/day-03.md)
- [Day 4 — Understand and handle `NULL`](lessons/day-04.md)
- [Day 5 — Search text and filter dates](lessons/day-05.md)
- [Day 6 — Summarize data with aggregate functions](lessons/day-06.md)
- [Day 7 — Group and filter summaries](lessons/day-07.md)
- [Day 8 — Understand keys and table relationships](lessons/day-08.md)
- [Day 9 — Combine tables with `JOIN`](lessons/day-09.md)
- [Day 10 — Join multiple tables without losing track](lessons/day-10.md)
- [Day 11 — Create conditional values with `CASE`](lessons/day-11.md)
- [Day 12 — Use subqueries](lessons/day-12.md)
- [Day 13 — Test related rows with `EXISTS`](lessons/day-13.md)
- [Day 14 — Organize queries with CTEs](lessons/day-14.md)
- [Day 15 — Combine query results with set operations](lessons/day-15.md)
- [Day 16 — Analyze dates with SQLite date functions](lessons/day-16.md)
- [Day 17 — Rank rows with window functions](lessons/day-17.md)
- [Day 18 — Calculate running totals and compare rows](lessons/day-18.md)
- [Day 19 — Find top rows within each group](lessons/day-19.md)
- [Day 20 — Change data safely with transactions](lessons/day-20.md)
- [Day 21 — Week 3 review: analyze a bookshop](lessons/day-21.md)
- [Day 22 — Design tables and constraints](lessons/day-22.md)
- [Day 23 — Reuse queries with views](lessons/day-23.md)
- [Day 24 — Improve lookups with indexes](lessons/day-24.md)
- [Day 25 — Check query correctness and edge cases](lessons/day-25.md)
- [Day 26 — Capstone: define the analysis](lessons/day-26.md)
- [Day 27 — Capstone: build sales summaries](lessons/day-27.md)
- [Day 28 — Capstone: review coverage and customer ranks](lessons/day-28.md)
- [Day 29 — Capstone: validate and reconcile results](lessons/day-29.md)
- [Day 30 — Capstone: present your SQL findings](lessons/day-30.md)

## How to use each lesson

1. Read the concept and study the examples.
2. Try the assignment and test without looking at the answer key.
3. Compare your work with the solutions and explain any differences.
4. Send your answers back for feedback before moving on.

The course uses SQLite for local hands-on practice. Most early concepts are also standard SQL; lessons will call out dialect differences when they matter.

The finished capstone report is [queries/day-30.sql](queries/day-30.sql).

## Beyond the first 30 days

- [Day 31 — Build sequences with recursive CTEs](lessons/day-31.md)
- [Day 32 — Normalize a sales schema](lessons/day-32.md)
- [Day 33 — Use savepoints and understand ACID](lessons/day-33.md)
- [Day 34 — Write queries the index can use](lessons/day-34.md)
- [Day 35 — Understand SQL's logical processing order](lessons/day-35.md)
