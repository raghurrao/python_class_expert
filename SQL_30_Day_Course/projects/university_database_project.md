# Day 29 capstone: university analytics

## Requirements

Use the shared schema to report student enrollment patterns for a department chair. Demonstrate schema understanding, safe data modification in a transaction, multi-table joins, aggregation, a subquery, a CTE, a window function, a constraint proposal, and an index proposal.

## Tasks

1. Document the primary and foreign keys in the student-course-enrollment path.
2. Add a test student inside a transaction and roll it back.
3. Report course enrollment count and average non-NULL grade limitation (grades are letters).
4. Find students with no enrollment using NOT EXISTS.
5. Use a CTE to compute course counts and rank courses per department.
6. Add a uniqueness or CHECK constraint proposal and justify it.
7. Propose an index for term/course lookup and inspect EXPLAIN QUERY PLAN.

## Test cases

- Include a student with no enrollments in the query logic.
- Preserve courses with zero enrollments using LEFT JOIN.
- Ensure a duplicate enrollment in the same term is rejected.
- Ensure rollback leaves no test student behind.

See `final_project.sql` for a worked solution.
