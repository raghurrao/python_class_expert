# Day 20: Heredocs & Dynamic Parameterization in Bash SQL

Heredocs (`<<EOF`) allow embedding multi-line SQL queries directly inside shell scripts while dynamically substituting bash variables.

---

## 1. Heredoc Pattern

```bash
MIN_SALARY=80000
TARGET_DEPT=1

sqlite3 company.db <<EOF
SELECT first_name, salary 
FROM employees 
WHERE salary >= ${MIN_SALARY} AND dept_id = ${TARGET_DEPT};
EOF
```

---

## 2. Hands-On Practical Exercise (Day 20)

Run `04_bash_sql/day20_heredoc.sh` to run parameterized SQL heredocs!
