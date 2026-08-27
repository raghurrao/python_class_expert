#!/usr/bin/env bash
set -e

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DB_FILE="${WORKSPACE_ROOT}/02_sqlite/company.db"
SQL_FILE="${WORKSPACE_ROOT}/03_postgres/day16_cte.sql"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

echo "=================================================="
echo "      DAY 16: COMMON TABLE EXPRESSIONS (CTEs)     "
echo "=================================================="

echo "[1] Executing CTE Queries (${SQL_FILE}):"
"${SQLITE_BIN}" "${DB_FILE}" < "${SQL_FILE}"

echo "--------------------------------------------------"
echo "✅ DAY 16 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
