# Day 15: Window Functions (Part 2: Value & Frame Clauses)

Value window functions access previous or subsequent rows without self-joins.

---

## 1. Key Value Functions & Frames

- `LAG(col, offset, default)`: Access previous row value.
- `LEAD(col, offset, default)`: Access subsequent row value.
- `SUM(col) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)`: Cumulative running total.

---

## 2. Hands-On Practical Exercise (Day 15)

Run `03_postgres/day15_run.sh` to calculate running totals and row comparisons!
