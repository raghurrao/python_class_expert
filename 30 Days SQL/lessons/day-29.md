# Day 29 — Capstone: validate and reconcile results

**Today's goal:** Check that the capstone reports are consistent, validate important counts and totals, and assemble the reports into one runnable SQL file.

**Suggested time:** 60–90 minutes

**Interactive routine:** Run the full report file, then compare your expected totals with the reconciliation output. If anything differs, trace the join and grouping grain before changing the query.

## 1. Why validate results?

A query can run without errors and still answer the wrong question. Validation checks whether separate views of the same data agree and whether row counts make sense.

For this sample, estimated revenue should reconcile across these groupings:

- monthly revenue;
- customer revenue;
- book revenue;
- author revenue.

Every grouping partitions the same order rows, so each overall revenue total should be the same.

## 2. Cross-check count and quantity

The source order table contains six rows and a total ordered quantity of eight. A useful first check is:

```sql
SELECT COUNT(*) AS order_rows,
       SUM(quantity) AS units_ordered
FROM book_orders;
```

If a grouped report produces a different total number of order rows or units, inspect whether joins duplicated or excluded orders.

## 3. Reconcile revenue in one statement

The capstone file includes a reconciliation query that calculates revenue from the order detail view and compares it with monthly, customer, book, and author totals. The totals should agree at **182.50**.

If one total differs, common causes include:

- joining in reviews and multiplying order rows;
- using an inner join where unmatched records should remain;
- grouping on the wrong key;
- filtering out rows unintentionally;
- applying a price or quantity calculation inconsistently.

## 4. Assemble the final report file

The file `queries/day-29.sql` contains multiple result sets:

1. monthly order count and estimated revenue;
2. customer unit totals and rank;
3. book sales summary;
4. review coverage;
5. cross-check totals.

The runner executes each semicolon-terminated statement and displays its result. This gives you a repeatable report file that can be rerun after sample data changes.

## 5. Today's runnable practice

From PowerShell in the course folder, run:

```powershell
python run_sql.py queries/day-29.sql
```

Read every result set. Check the row grain, count, and total for each section.

## 6. Assignment — validate the capstone

1. Run `queries/day-29.sql` and record the order row count, units, and revenue total.
2. Confirm monthly order counts add up to the total order rows.
3. Confirm customer units add up to total units ordered.
4. Confirm book and author estimated revenues each add up to the total revenue.
5. Confirm review coverage has one row per book and that unrated reviews are not counted in the average.
6. Write one sentence stating the main limitation of the revenue metric.

## 7. Self-test — answer without notes

1. If total revenue by customer differs from total revenue by month, what should you investigate first?
2. How many order rows are in the sample?
3. How many units are ordered in total?
4. What is the total estimated revenue?
5. Why should review rows not be joined directly into the sales aggregation?
6. What does a reconciliation check tell you—and what does it not prove?

## 8. Answer key — check after trying

### Assignment results

- Order row count: **6**.
- Total quantity: **8 units**.
- Monthly order counts: **2 + 2 + 2 = 6**.
- Customer units: **3 + 2 + 1 + 2 = 8**.
- Total estimated revenue: **182.50**.
- Monthly revenue: **50.50 + 49.50 + 82.50 = 182.50**.
- Book revenue: **37 + 96 + 25.50 + 24 = 182.50**.
- Author revenue: **61 + 96 + 25.50 = 182.50**.
- Review coverage: **four rows, one per book**; `COUNT(rating)` and `AVG(rating)` ignore missing ratings.
- Limitation: the estimate uses listed price and quantity only; it omits discounts, refunds, shipping, tax, and payment status.

### Self-test solutions

1. Check join fan-out, filters, grouping keys, and whether each report uses the same definition of revenue.
2. Six.
3. Eight.
4. 182.50.
5. One order can match several reviews, multiplying the order's quantity and revenue.
6. It can expose inconsistencies across aggregations, but matching totals do not prove every query or business assumption is correct.

## 9. Ready for Day 30?

You’re ready when the major totals reconcile and you can describe what they mean and what they leave out. Tomorrow we’ll finalize and explain the capstone as if presenting it to the bookshop owner.
