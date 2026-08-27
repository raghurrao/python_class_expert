# Day 13: Advanced Data Types (JSON / JSONB & Timestamps)

Modern database applications store semi-structured JSON data alongside relational data.

---

## 1. Querying JSON Data

In PostgreSQL and SQLite 3.38+, JSON functions query attributes inside text/JSON fields directly.

- `json_extract(json_col, '$.key')` or `->>` operator in PostgreSQL.
- `json_each()`: Expands JSON arrays into rows.

```sql
SELECT 
    event_id,
    json_extract(payload, '$.user') AS username,
    json_extract(payload, '$.action') AS action_type
FROM staging_raw_events;
```

---

## 2. Hands-On Practical Exercise (Day 13)

Run `03_postgres/day13_run.sh` to extract JSON fields dynamically!
