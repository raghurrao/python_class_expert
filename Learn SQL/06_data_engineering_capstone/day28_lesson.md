# Day 28: Data Pipeline Architecture & Raw Ingestion Zone

In production data engineering, data flows through three distinct storage layers:

```
┌────────────────────────────────────────────────────────┐
│ Layer 1: Raw Landing Zone                              │
│ Raw CSVs / JSON Payloads / API Dump                    │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ Layer 2: Staging Area (Postgres / SQLite)              │
│ Cleaned data types, stripped quotes, deduplicated rows │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ Layer 3: Data Warehouse (Star Schema)                  │
│ Fact & Dimension tables, analytics queries             │
└────────────────────────────────────────────────────────┘
```

---

## Hands-On Practical Exercise (Day 28)

Run `06_data_engineering_capstone/day28_arch.sh` to generate raw source files and staging table schemas!
