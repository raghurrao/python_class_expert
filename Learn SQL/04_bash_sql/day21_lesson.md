# Day 21: Automated Database Backups & Backup Rotation

Regular database backups protect critical business data from hardware failure or accidental data deletion.

---

## 1. Backup Strategies

1. **Logical Dump (`.dump` / `pg_dump`)**: Exports database schema & data as portable SQL statements.
2. **Physical Backup**: Direct binary snapshot of `.db` file or data directory.
3. **Automated Compression & Rotation**: Compress dumps with `gzip` and purge backups older than $N$ days.

---

## 2. Hands-On Practical Exercise (Day 21)

Run `04_bash_sql/day21_backup.sh` to generate compressed backups and test restore validation!
