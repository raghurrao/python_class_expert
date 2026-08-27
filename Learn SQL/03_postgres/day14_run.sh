#!/usr/bin/env bash
set -e

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DB_FILE="${WORKSPACE_ROOT}/02_sqlite/company.db"
SQL_FILE="${WORKSPACE_ROOT}/03_postgres/day14_window.sql"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

echo "=================================================="
echo "    DAY 14: WINDOW FUNCTIONS (RANKING) PRACTICE    "
echo "=================================================="

echo "[1] Executing Ranking Window Query (${SQL_FILE}):"
"${SQLITE_BIN}" "${DB_FILE}" < "${SQL_FILE}"

echo "--------------------------------------------------"
echo "✅ DAY 14 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
