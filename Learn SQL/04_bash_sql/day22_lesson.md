# Day 22: Command Line Data Ingestion Pipelines

Command-line ETL pipelines stream data directly from external APIs or raw files, format JSON into CSV/TSV, and insert rows into relational database tables.

---

## 1. Streaming JSON to SQL Pipeline Architecture

```
Raw API Payload / JSON File
            │
            ▼ (jq parser)
Formatted CSV Records
            │
            ▼ (sqlite3 .import)
Database Table
```

---

## 2. Hands-On Practical Exercise (Day 22)

Run `04_bash_sql/day22_ingest.sh` to ingest JSON server logs directly into SQLite!
