#!/usr/bin/env bash
set -euo pipefail

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DB_FILE="${WORKSPACE_ROOT}/02_sqlite/company.db"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

MIN_SALARY=90000

echo "=================================================="
echo "    DAY 20: DYNAMIC PARAMETERIZED HEREDOC SQL     "
echo "=================================================="

echo "[1] Fetching Employees with Salary >= ${MIN_SALARY} using Heredoc:"

"${SQLITE_BIN}" "${DB_FILE}" <<EOF
SELECT first_name, last_name, salary
FROM employees
WHERE salary >= ${MIN_SALARY}
ORDER BY salary DESC;
EOF

echo "--------------------------------------------------"
echo "✅ DAY 20 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
