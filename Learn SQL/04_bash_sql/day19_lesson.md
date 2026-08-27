# Day 19: Batch Automation with SQLite & Bash

Data pipelines automate batch SQL execution from shell scripts without human intervention.

---

## 1. Key Non-Interactive Execution Patterns

```bash
# Execute inline SQL query via bash
sqlite3 company.db "SELECT COUNT(*) FROM employees;"

# Run external SQL script file
sqlite3 company.db < analytics.sql

# Format output directly to CSV file
sqlite3 -csv company.db "SELECT * FROM employees;" > export.csv
```

---

## 2. Hands-On Practical Exercise (Day 19)

Run `04_bash_sql/day19_batch.sh` to generate automated CSV report exports!
