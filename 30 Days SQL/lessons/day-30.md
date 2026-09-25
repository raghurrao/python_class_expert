# Day 30 — Capstone: present your SQL findings

**Today's goal:** Run the finished capstone, explain the findings and assumptions, and assess what you can now do independently.

**Suggested time:** 75–90 minutes

**Interactive routine:** Run the final report before reading the answer key. Explain each result in plain language. Then answer the final test without looking at earlier lessons, and send me your findings and answers for review.

## 1. Run the finished report

The final capstone SQL is saved in `queries/day-30.sql`. From PowerShell in the course folder, run:

```powershell
python run_sql.py queries/day-30.sql
```

It produces monthly performance, customer ranking, book performance, review coverage, and revenue reconciliation.

## 2. Explain the results

Use the outputs to prepare a short report for the bookshop owner. Include:

1. Which month had the highest estimated revenue?
2. Which customer ordered the most units? Who tied for the next rank?
3. Which book generated the most estimated revenue?
4. Which books have no rated reviews?
5. Do the monthly, customer, book, and author revenue totals reconcile?
6. What assumptions and limitations should accompany the report?

Keep the explanation factual. Distinguish what the sample data shows from what the data cannot establish.

## 3. Final test — answer without notes

1. Write a query to list each title and price for books priced at least 20, most expensive first.
2. Explain the difference between `WHERE` and `HAVING`.
3. Write a query to count books per author.
4. Explain what `LEFT JOIN` preserves.
5. Why use `COUNT(r.rating)` instead of `COUNT(*)` to count rated reviews?
6. What does `ROW_NUMBER() OVER (PARTITION BY customer ORDER BY order_date, order_id)` calculate?
7. Write a condition for all orders in February 2026 using a half-open date range.
8. What is one reason to use a CTE?
9. What does `ROLLBACK` do?
10. Name one risk that can inflate an aggregate after a join, and how you would avoid it.

## 4. Final answer key — check after trying

### Capstone interpretation

1. March 2026 has the highest estimated revenue: **82.50**.
2. Asha Rao ordered **3 units**. Ben Cole and Dina Shah tie at the next rank with **2 units** each.
3. *SQL for Curious Minds* generated the most estimated revenue: **96**.
4. *SQL for Curious Minds* and *The Long Weekend* have reviews but no rated reviews, so their average ratings are `NULL`.
5. Yes. Each grouping reconciles to **182.50**.
6. Revenue is estimated as quantity times listed price; there is no information about discounts, refunds, shipping, tax, payments, or multiple lines per order.

### Final test solutions

1. One correct query:

   ```sql
   SELECT title, price
   FROM books
   WHERE price >= 20
   ORDER BY price DESC;
   ```

2. `WHERE` filters input rows before grouping; `HAVING` filters groups after aggregation.
3. `SELECT author, COUNT(*) FROM books GROUP BY author;`
4. It preserves every row from the left table, even without a matching right-table row.
5. `COUNT(r.rating)` skips `NULL` values; `COUNT(*)` counts every result row.
6. It assigns a sequential number to each customer's orders, starting over per customer and ordered by date then order ID.
7. `WHERE order_date >= '2026-02-01' AND order_date < '2026-03-01'`.
8. It names an intermediate query result, helping make a complex query readable and easier to reason about.
9. It undoes uncommitted changes in the transaction.
10. A one-to-many join can repeat rows and inflate sums. Join only necessary tables or aggregate to the correct grain before combining.

## 5. What you can do now

If you can write and explain the final report without copying the answers, you have a strong practical SQL foundation: querying, filtering, aggregation, joins, subqueries, CTEs, window functions, data changes, constraints, views, and basic query plans.

Expert-level work still comes from continued practice with larger, messier datasets, a specific production database, query tuning, and real business requirements. A good next step is to take a new dataset and repeat the same cycle: define the question and grain, write the SQL, check edge cases, and validate the results.

Send me your short report and final-test answers. I’ll review them and recommend the next topics based on where you feel least confident.
