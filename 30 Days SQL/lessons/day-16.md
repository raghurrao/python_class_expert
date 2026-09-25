# Day 16 — Analyze dates with SQLite date functions

**Today's goal:** Extract calendar parts, group activity by month, and perform simple date calculations.

**Suggested time:** 60–75 minutes

**Dialect note:** This lesson uses SQLite's date functions. Other SQL systems have different date function names and syntax; ISO date filtering with comparisons is broadly useful.

**Interactive routine:** Predict the month for each order and the number of groups. Write queries in `queries/day-16.sql`, run them, and compare before opening the key.

## 1. Store dates in a consistent format

The `book_orders.order_date` values use ISO format: `YYYY-MM-DD`. This keeps dates unambiguous and allows reliable text comparison and sorting for these date-only values.

```sql
SELECT order_id, order_date
FROM book_orders
ORDER BY order_date;
```

Avoid mixing formats such as `02/03/2026` and `2026-03-02`; the first format is ambiguous and mixed formats do not sort consistently as text.

## 2. Extract year, month, or day with `strftime`

SQLite's `strftime` formats a date or timestamp. `%Y` means four-digit year, `%m` means two-digit month, `%d` means day of month:

```sql
SELECT order_date,
       strftime('%Y', order_date) AS order_year,
       strftime('%m', order_date) AS order_month,
       strftime('%d', order_date) AS order_day
FROM book_orders;
```

`strftime` returns text. Use a format string such as `%Y-%m` to build a year-month label.

## 3. Group by month

```sql
SELECT strftime('%Y-%m', order_date) AS order_month,
       COUNT(*) AS order_count
FROM book_orders
GROUP BY strftime('%Y-%m', order_date)
ORDER BY order_month;
```

The sample data has two orders in each of January, February, and March 2026. Including the year in the group key matters: grouping only by month number would combine January from different years if the table later included multiple years.

## 4. Add or subtract time with `date`

SQLite's `date` function can apply modifiers:

```sql
SELECT order_date,
       date(order_date, '+7 days') AS one_week_later,
       date(order_date, '-1 month') AS one_month_earlier
FROM book_orders;
```

The result is a date string. Month arithmetic can be surprising near the end of a month because months have different lengths. Check boundary behavior when calendar precision matters.

## 5. Filter a month with a half-open range

For filtering a known month, the start-inclusive, next-month-exclusive pattern is clear and works well with ISO dates:

```sql
SELECT order_id, order_date
FROM book_orders
WHERE order_date >= '2026-02-01'
  AND order_date <  '2026-03-01';
```

If the column contains timestamps, the exclusive upper boundary safely includes all times on the last day of the month.

## 6. Today's runnable practice

Edit `queries/day-16.sql`, save, and run from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-16.sql
```

## 7. Assignment — write these six queries

1. Show each order date with its year, month, and day as separate columns.
2. Count orders by year-month, sorted chronologically.
3. Sum ordered quantity by year-month.
4. Show each order date and the date 7 days later.
5. Show only orders placed in February 2026 using date boundaries.
6. Count orders per day of the month across all dates in the data using `strftime('%d', order_date)`. Sort by day.

## 8. Self-test — answer without notes

1. What does `strftime('%Y-%m', order_date)` return for `2026-02-14`?
2. Why include the year when grouping by month?
3. What is the result type of SQLite's `strftime`?
4. Why is `< '2026-03-01'` a good end boundary for February 2026?
5. What does `date(order_date, '+7 days')` calculate?
6. Why should you check month arithmetic near month ends?

## 9. Answer key — check after trying

### Assignment solutions

```sql
-- 1. Date parts
SELECT order_date,
       strftime('%Y', order_date) AS order_year,
       strftime('%m', order_date) AS order_month,
       strftime('%d', order_date) AS order_day
FROM book_orders;
```

```sql
-- 2. Number of orders by month
SELECT strftime('%Y-%m', order_date) AS order_month,
       COUNT(*) AS order_count
FROM book_orders
GROUP BY strftime('%Y-%m', order_date)
ORDER BY order_month;
```

```sql
-- 3. Quantity by month
SELECT strftime('%Y-%m', order_date) AS order_month,
       SUM(quantity) AS total_quantity
FROM book_orders
GROUP BY strftime('%Y-%m', order_date)
ORDER BY order_month;
```

```sql
-- 4. One week after each order
SELECT order_date,
       date(order_date, '+7 days') AS one_week_later
FROM book_orders;
```

```sql
-- 5. Orders during February 2026
SELECT order_id, order_date
FROM book_orders
WHERE order_date >= '2026-02-01'
  AND order_date <  '2026-03-01';
```

```sql
-- 6. Count by day of month
SELECT strftime('%d', order_date) AS day_of_month,
       COUNT(*) AS order_count
FROM book_orders
GROUP BY strftime('%d', order_date)
ORDER BY day_of_month;
```

Expected monthly order counts: **2026-01: 2, 2026-02: 2, 2026-03: 2**. Expected monthly quantities: **2026-01: 2, 2026-02: 3, 2026-03: 3**. Day-of-month counts: **01, 02, 05, 12, 14, 17 each have 1**.

### Self-test solutions

1. `2026-02`.
2. To keep January from different years in separate groups.
3. Text.
4. It includes all dates in February and excludes March 1 onward.
5. It returns the date one week after the order date.
6. Months have different lengths, so shifting a date by a month may not land on the same day number.

## 10. Ready for Day 17?

You’re ready when you can group by year-month and explain the half-open date range. Send me Assignment 3 and your expected totals for January, February, and March.
