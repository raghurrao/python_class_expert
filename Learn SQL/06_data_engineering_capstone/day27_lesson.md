# Day 27: Data Warehousing & Dimensional Modeling (Star Schema)

Welcome to **Module 6: SQL + Data Engineering Capstone Project**!

Data Warehouses store historical data optimized for analytical reporting (OLAP), distinct from transactional databases (OLTP).

---

## 1. OLTP vs. OLAP

| Feature | OLTP (Online Transaction Processing) | OLAP (Online Analytical Processing) |
| :--- | :--- | :--- |
| **Purpose** | Fast day-to-day operational transactions | Complex analytical queries & reporting |
| **Schema** | Highly Normalized (3NF) to avoid redundancy | Denormalized (Star / Snowflake Schema) |
| **Operations** | Frequent `INSERT`, `UPDATE`, single-row lookups | Bulk aggregations (`SUM`, `COUNT`), scans |

---

## 2. Dimensional Modeling (Star Schema)

```
       ┌────────────────────────┐
       │   dim_customers        │
       │────────────────────────│
       │ customer_key (PK)      │
       │ customer_id            │
       │ customer_name          │
       │ region                 │
       └───────────┬────────────┘
                   │ 1
                   │
                   │ N
       ┌───────────▼────────────┐           ┌────────────────────────┐
       │   fact_sales           │ 1       N │   dim_products         │
       │────────────────────────│───────────│────────────────────────│
       │ sale_id (PK)           │           │ product_key (PK)       │
       │ customer_key (FK)      │           │ product_id             │
       │ product_key (FK)       │           │ product_name           │
       │ date_key (FK)          │           │ category               │
       │ quantity               │           └────────────────────────┘
       │ total_amount           │
       └───────────▲────────────┘
                   │ N
                   │
                   │ 1
       ┌───────────┴────────────┐
       │   dim_date             │
       │────────────────────────│
       │ date_key (PK)          │
       │ full_date              │
       │ year, quarter, month   │
       └────────────────────────┘
```

---

## 3. Hands-On Practical Exercise (Day 27)

Run `06_data_engineering_capstone/day27_run.sh` to initialize the Star Schema tables!
