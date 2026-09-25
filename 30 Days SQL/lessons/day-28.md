# Day 28 — Capstone: review coverage and customer ranks

**Today's goal:** Complete two capstone analyses: review coverage per book and a ranking of customers by units ordered.

**Suggested time:** 60–75 minutes

**Interactive routine:** Predict which books have missing average ratings, and which customers tie in the ranking. Write each query in `queries/day-28.sql`, run it, then compare with the answer key.

## 1. Review coverage per book

Start from `books` and use a `LEFT JOIN` so every book remains in the output:

```sql
SELECT b.book_id,
       b.title,
       COUNT(r.review_id) AS review_count,
       COUNT(r.rating) AS rated_review_count,
       AVG(r.rating) AS average_rating
FROM books AS b
LEFT JOIN book_reviews AS r
    ON b.book_id = r.book_id
GROUP BY b.book_id, b.title
ORDER BY b.book_id;
```

The counts answer different questions:

- `COUNT(r.review_id)` counts review rows, even if the rating is missing.
- `COUNT(r.rating)` counts only reviews with a rating.
- `AVG(r.rating)` averages non-`NULL` ratings and remains `NULL` if none exist.

`COUNT(*)` would count the null-extended left-join row for a book without reviews. Counting the right-side primary key avoids that problem.

## 2. Rank customers by units ordered

First calculate one total per customer, then rank those summary rows:

```sql
WITH customer_totals AS (
    SELECT customer, SUM(quantity) AS units_ordered
    FROM book_orders
    GROUP BY customer
)
SELECT customer,
       units_ordered,
       RANK() OVER (ORDER BY units_ordered DESC) AS customer_rank
FROM customer_totals
ORDER BY customer_rank, customer;
```

`RANK()` gives tied customers the same rank and leaves a gap after a tie. If you want a gapless ranking, use `DENSE_RANK()` instead.

## 3. Add a top-customer label with `CASE`

You can combine concepts to label the top rank:

```sql
WITH customer_totals AS (
    SELECT customer, SUM(quantity) AS units_ordered
    FROM book_orders
    GROUP BY customer
), ranked_customers AS (
    SELECT customer, units_ordered,
           RANK() OVER (ORDER BY units_ordered DESC) AS customer_rank
    FROM customer_totals
)
SELECT customer, units_ordered, customer_rank,
       CASE WHEN customer_rank = 1 THEN 'Top customer' ELSE 'Other' END AS segment
FROM ranked_customers
ORDER BY customer_rank, customer;
```

Because rank 1 can be shared, this labels every customer tied for the most units.

## 4. Today's runnable practice

Edit `queries/day-28.sql`, save, and run from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-28.sql
```

The starter query calculates review coverage. Replace it with your customer ranking query to practice the second part.

## 5. Assignment — complete both capstone sections

1. For each book, show total review count, rated review count, and average rating. Include books with no reviews.
2. Explain why a book's review count can differ from its rated-review count, using a book from the sample data.
3. Rank customers by units ordered using `RANK`, preserving ties.
4. Add `DENSE_RANK` next to `RANK` and compare the ranks.
5. Use a CTE and `CASE` to label all rank-1 customers as `Top customer` and everyone else as `Other`.
6. Imagine a book has no reviews at all. What should your query show for review count, rated count, and average rating?

## 6. Self-test — answer without notes

1. Why does review coverage start from `books`?
2. What does `COUNT(r.review_id)` count after a left join?
3. What does `COUNT(r.rating)` exclude?
4. What does `AVG(r.rating)` return if every rating for the book is `NULL`?
5. Why can rank 1 belong to more than one customer?
6. How does `DENSE_RANK` differ from `RANK` after ties?

## 7. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Review coverage per book
SELECT b.book_id,
       b.title,
       COUNT(r.review_id) AS review_count,
       COUNT(r.rating) AS rated_review_count,
       AVG(r.rating) AS average_rating
FROM books AS b
LEFT JOIN book_reviews AS r
    ON b.book_id = r.book_id
GROUP BY b.book_id, b.title
ORDER BY b.book_id;
```

2. A review may exist without a rating. For example, SQL for Curious Minds has one review but zero rated reviews because its rating is `NULL`.

```sql
-- 3. Rank customers by quantity
WITH customer_totals AS (
    SELECT customer, SUM(quantity) AS units_ordered
    FROM book_orders
    GROUP BY customer
)
SELECT customer, units_ordered,
       RANK() OVER (ORDER BY units_ordered DESC) AS customer_rank
FROM customer_totals
ORDER BY customer_rank, customer;
```

```sql
-- 4. Compare rank types
WITH customer_totals AS (
    SELECT customer, SUM(quantity) AS units_ordered
    FROM book_orders
    GROUP BY customer
)
SELECT customer, units_ordered,
       RANK() OVER (ORDER BY units_ordered DESC) AS rank_number,
       DENSE_RANK() OVER (ORDER BY units_ordered DESC) AS dense_rank_number
FROM customer_totals;
```

```sql
-- 5. Label the top rank (including ties)
WITH customer_totals AS (
    SELECT customer, SUM(quantity) AS units_ordered
    FROM book_orders
    GROUP BY customer
), ranked_customers AS (
    SELECT customer, units_ordered,
           RANK() OVER (ORDER BY units_ordered DESC) AS customer_rank
    FROM customer_totals
)
SELECT customer, units_ordered, customer_rank,
       CASE WHEN customer_rank = 1 THEN 'Top customer' ELSE 'Other' END AS segment
FROM ranked_customers;
```

6. With the left join and key counts, a no-review book would show `review_count = 0`, `rated_review_count = 0`, and `average_rating = NULL`.

Expected review coverage: **The Quiet River 2 reviews / 2 rated / average 4; SQL for Curious Minds 1 / 0 / NULL; Small Worlds 1 / 1 / 4; The Long Weekend 1 / 0 / NULL**. Customer units: **Asha 3 rank 1; Ben 2 rank 2; Dina 2 rank 2; Chen 1 rank 4**. Dense ranks are **1, 2, 2, 3**.

### Self-test solutions

1. To keep every book, including those without matching reviews.
2. It counts only actual matching review rows, because an unmatched row has `NULL` in `r.review_id`.
3. Rows where the rating is `NULL`.
4. `NULL`.
5. Multiple customers can tie for the greatest total quantity.
6. `RANK` leaves a gap after ties; `DENSE_RANK` does not.

## 8. Ready for Day 29?

You’re ready when you can distinguish review count from rated-review count and explain customer ties. Send me your review-coverage output and tell me why two average ratings are `NULL`.
