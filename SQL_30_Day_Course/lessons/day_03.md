# Day 03: INSERT, UPDATE, DELETE

## Learning objectives

- Explain Data modification in your own words and identify when to use it.
- Write, read, and debug queries using the day’s clauses.
- Verify query results against the shared university schema.

## Prerequisites and connection

Review the previous lesson’s vocabulary. Day 1 assumes no SQL experience. Each later day reuses the same `university.db`; earlier topics remain building blocks for this lesson.

## Concepts and syntax

Change data safely and understand affected rows. Think of a database as a well-organized filing system: tables are collections of consistently shaped records, columns describe attributes, and keys let records refer to one another. SQL states the result you want; SQLite’s query planner chooses how to produce it.

Core syntax to keep in mind:

```sql
SELECT expression [AS output_name]
FROM table_name
[JOIN other_table ON matching_key]
[WHERE row_condition]
[GROUP BY grouping_expression]
[HAVING group_condition]
[ORDER BY output_expression [ASC|DESC]]
[LIMIT row_count];
```

`SELECT` chooses output expressions; `FROM` identifies source rows; `JOIN ... ON` defines a relationship; `WHERE` filters individual rows; `GROUP BY` forms groups; `HAVING` filters groups; `ORDER BY` sorts the final result; `LIMIT` caps its size. Not every query uses every clause. SQLite uses dynamic typing with affinity; `INTEGER`, `REAL`, `TEXT`, `BLOB`, and `NUMERIC` are affinities rather than rigid server-style types.

## Schema used today

The core relations are `students(student_id, first_name, last_name, email, enrollment_date, department_id)`, `departments(department_id, name)`, `courses(course_id, course_code, title, department_id, credits, level)`, and `enrollments(enrollment_id, student_id, course_id, term, grade, enrolled_on)`. Business tables include `customers`, `orders`, `products`, `order_items`, and `payments`. Foreign keys connect records; nullable grades and emails provide realistic missing-value cases.

## Worked examples

### Worked example 1: List students

```sql
SELECT student_id, first_name, last_name FROM students ORDER BY student_id LIMIT 5;
```

Reasoning: choose the source relation, state the condition or relationship explicitly, and inspect the named output columns. This pattern can be adapted to the day’s focus by changing the relevant clause.

Expected output (first rows where applicable):

| Result |
|---|
| Query returns rows from the shared database; exact values depend on the listed predicates and ordering. |
### Worked example 2: Filter the relevant relation

```sql
SELECT * FROM courses WHERE credits >= 3 LIMIT 5;
```

Reasoning: choose the source relation, state the condition or relationship explicitly, and inspect the named output columns. This pattern can be adapted to the day’s focus by changing the relevant clause.

Expected output (first rows where applicable):

| Result |
|---|
| Query returns rows from the shared database; exact values depend on the listed predicates and ordering. |
### Worked example 3: Connect a related table

```sql
SELECT s.first_name, c.title FROM students AS s JOIN enrollments AS e ON e.student_id=s.student_id JOIN courses AS c ON c.course_id=e.course_id LIMIT 5;
```

Reasoning: choose the source relation, state the condition or relationship explicitly, and inspect the named output columns. This pattern can be adapted to the day’s focus by changing the relevant clause.

Expected output (first rows where applicable):

| Result |
|---|
| Query returns rows from the shared database; exact values depend on the listed predicates and ordering. |
### Worked example 4: Summarize a useful measure

```sql
SELECT department_id, COUNT(*) AS row_count FROM courses GROUP BY department_id ORDER BY row_count DESC;
```

Reasoning: choose the source relation, state the condition or relationship explicitly, and inspect the named output columns. This pattern can be adapted to the day’s focus by changing the relevant clause.

Expected output (first rows where applicable):

| Result |
|---|
| Query returns rows from the shared database; exact values depend on the listed predicates and ordering. |
### Worked example 5: Inspect business activity

```sql
SELECT o.status, COUNT(*) AS orders FROM orders AS o GROUP BY o.status ORDER BY o.status;
```

Reasoning: choose the source relation, state the condition or relationship explicitly, and inspect the named output columns. This pattern can be adapted to the day’s focus by changing the relevant clause.

Expected output (first rows where applicable):

| Result |
|---|
| Query returns rows from the shared database; exact values depend on the listed predicates and ordering. |

## Independent practice

Complete the 15 numbered tasks in [Day 03 exercises](../exercises/day_03_exercises.sql). Keep the file separate from the answer key. Run read-only exercises first; reset a disposable copy before modification practice.

### Real-world query challenges

1. Find a question an academic registrar could answer with this topic.
2. Adapt a query to identify students needing follow-up.
3. Produce a concise measure useful to a department chair.
4. Identify an edge case involving NULL or duplicate-looking data.
5. Explain how you would verify a result before sharing it.

### Debugging clinic

Each query below intentionally contains an error. Identify it, repair it, and explain the fix.

```sql
SELECT first_name last_name FROM students;
SELECT * FROM enrollments WHERE grade = NULL;
SELECT department_id, COUNT(*) FROM courses;
```

## Daily quiz

1. Explain the role of `Data` in a query. (Answer in your own words.)
2. Explain the role of `Data` in a query. (Answer in your own words.)
3. Explain the role of `Data` in a query. (Answer in your own words.)
4. Explain the role of `Data` in a query. (Answer in your own words.)
5. Explain the role of `Data` in a query. (Answer in your own words.)
6. Explain the role of `Data` in a query. (Answer in your own words.)
7. Explain the role of `Data` in a query. (Answer in your own words.)
8. Explain the role of `Data` in a query. (Answer in your own words.)
9. Explain the role of `Data` in a query. (Answer in your own words.)
10. Explain the role of `Data` in a query. (Answer in your own words.)

## Practical assessment

Write one query combining today’s idea with at least one earlier concept. State the intended result, run it, and explain how you checked its row count and edge cases.

## Revision summary and cheat sheet

- Write the query in small steps and execute after each clause.
- Use explicit column names and explicit join keys.
- Check NULL values with `IS NULL`; sort explicitly when output order matters.
- Save a working version before changing data.

## Common mistakes and troubleshooting

- A misspelled identifier produces “no such column/table”; compare against the schema.
- NULL is not equal to any value, including another NULL; use `IS NULL`.
- Joins can multiply rows; inspect key uniqueness and count before aggregating.
- Result order is not guaranteed without `ORDER BY`.
- Enable foreign keys on each SQLite connection when testing relationships.

## Mastery checklist

- [ ] I can explain the topic without reading the lesson.
- [ ] I can write a query from a plain-language request.
- [ ] I can predict and explain NULL, duplicate, and empty-result behavior.
- [ ] I can debug a malformed query and verify the corrected output.
- [ ] I scored at least 8/10 on the quiz.

## Answer key

Full solutions and reasoning are kept in [Day 03 solutions](../solutions/day_03_solutions.sql).
