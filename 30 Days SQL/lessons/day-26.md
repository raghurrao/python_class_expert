# Day 26 — Capstone: define the analysis

**Today's goal:** Turn a broad business question into clear analysis questions, metric definitions, and expected result grains before writing the final SQL.

**Suggested time:** 45–60 minutes

**Interactive routine:** Write your answers to the assignment in your own words first. Then compare with the suggested project brief below and send me your plan for feedback.

## 1. Capstone scenario

You are helping a small bookshop understand its sample sales and reviews. The database has:

- `books`: one row per book;
- `book_orders`: one row per order line, with customer, date, book ID, and quantity;
- `book_reviews`: one row per review, with an optional rating and text;
- `order_details`: a view with one row per order and an estimated line total.

This is a teaching dataset, not a complete accounting system. Estimated revenue is quantity times listed book price; we do not have discounts, refunds, shipping, taxes, or payment status.

## 2. Define the questions and result grains

The capstone will answer:

1. **Monthly performance:** What estimated revenue and order count does each month have? One row per month.
2. **Customer activity:** How many orders and units did each customer place? One row per customer.
3. **Book performance:** How many units and how much estimated revenue did each book generate? One row per book.
4. **Author performance:** How many units and how much estimated revenue did each author generate? One row per author.
5. **Review coverage:** Which books have reviews, and how many rated reviews and average rating does each have? One row per book, including books with no rated reviews.
6. **Top customers:** How do customers rank by units ordered? One row per customer, with ties preserved.

Defining the grain up front prevents unexpected duplicates and makes the output easy to interpret.

## 3. Define metric formulas

Write down what each metric means before using it:

- `order_count`: number of rows in `book_orders` (the sample treats each row as one order line/order).
- `units_ordered`: sum of `quantity`.
- `estimated_revenue`: sum of `quantity * price` after joining each order to its book.
- `rated_review_count`: count of non-`NULL` ratings.
- `average_rating`: average of non-`NULL` ratings; it should remain `NULL` when a book has no rated reviews.
- `customer_rank`: rank by total units, with equal totals sharing a rank.

One important assumption: this sample has one book per order row, so row count is being used as order count. A real multi-line order system would need a separate order header ID to count distinct orders.

## 4. Plan the query techniques

| Question | Useful SQL concepts |
|---|---|
| Monthly performance | `order_details`, `strftime`, `GROUP BY` |
| Customer activity | `GROUP BY`, `SUM`, `COUNT` |
| Book performance | `LEFT JOIN`, `GROUP BY`, `COALESCE` if display needs it |
| Author performance | joins, `GROUP BY`, sums |
| Review coverage | `LEFT JOIN`, `COUNT(rating)`, `AVG(rating)` |
| Top customers | CTE, aggregate, `RANK()` |

Avoid joining reviews into sales totals unless you aggregate review rows first. Otherwise the join may duplicate orders.

## 5. Today's assignment — write the project brief

In your own words, write a short plan with:

1. The audience for the analysis and the decision it should support.
2. The six questions above, or a revised set of questions you prefer.
3. The row grain for each output.
4. The definition of estimated revenue and order count.
5. One limitation of the dataset.
6. One query correctness risk you will check for.

Save your SQL work in `queries/day-26.sql` as comments or a small query that inspects the available data. Today is planning; the capstone queries come next.

## 6. Self-test — answer without notes

1. What does “one row per month” describe?
2. Why define estimated revenue before writing the query?
3. Why is `COUNT(*)` only an approximate order count for a real multi-line order database?
4. Why could joining reviews to orders inflate revenue?
5. What should `AVG(rating)` return for a book with no rated reviews?
6. Which ranking function preserves tied customer ranks?

## 7. Suggested plan — compare after trying

1. Audience: a shop owner deciding which books, customers, and months need attention.
2. Questions: monthly revenue and order volume, customer activity, book and author performance, review coverage, and customer ranking.
3. Grains: one row per month, customer, book, author, book, and customer, respectively.
4. Estimated revenue is `SUM(quantity * listed price)`; order count is the number of order rows in this simplified data.
5. Revenue excludes discounts, refunds, shipping, and payment confirmation; order rows are simplified to one order line each.
6. Check for row multiplication when joining tables with multiple child rows, especially reviews and orders.

### Self-test solutions

1. The grain or level of detail of the result.
2. It makes the calculation explicit and prevents people from interpreting the metric differently.
3. One real order can have several line rows, so row count may count lines rather than orders.
4. Each order may repeat once for every matching review, duplicating its revenue contribution.
5. `NULL`, because there are no non-`NULL` values to average.
6. `RANK()`.

## 8. Capstone sequence

- Day 26: define scope, metrics, grains, and assumptions.
- Day 27: build monthly, customer, book, and author summaries.
- Day 28: add review coverage and customer ranking.
- Day 29: validate results, inspect edge cases, and prepare the final report query.
- Day 30: complete and explain the final capstone.

Send me your project brief before moving on, or say “continue” and we’ll proceed with the working assumption above.
