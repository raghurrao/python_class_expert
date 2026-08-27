#!/usr/bin/env bash
set -e

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DB_FILE="${WORKSPACE_ROOT}/02_sqlite/company.db"
SQL_FILE="${WORKSPACE_ROOT}/02_sqlite/day11_subqueries.sql"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

echo "=================================================="
echo "    DAY 11: SUBQUERIES & SET OPERATIONS PRACTICE   "
echo "=================================================="

echo "[1] Executing Subqueries & Set Operations (${SQL_FILE}):"
"${SQLITE_BIN}" "${DB_FILE}" < "${SQL_FILE}"

echo "--------------------------------------------------"
echo "✅ DAY 11 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
