#!/usr/bin/env bash
set -e

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DB_FILE="${WORKSPACE_ROOT}/02_sqlite/company.db"
SQL_FILE="${WORKSPACE_ROOT}/03_postgres/day15_lead_lag.sql"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

echo "=================================================="
echo "    DAY 15: LAG/LEAD & CUMULATIVE RUNNING TOTALS  "
echo "=================================================="

echo "[1] Executing Cumulative Payroll Query (${SQL_FILE}):"
"${SQLITE_BIN}" "${DB_FILE}" < "${SQL_FILE}"

echo "--------------------------------------------------"
echo "✅ DAY 15 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
