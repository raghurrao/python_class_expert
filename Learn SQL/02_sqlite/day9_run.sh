#!/usr/bin/env bash
set -e

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DB_FILE="${WORKSPACE_ROOT}/02_sqlite/company.db"
SQL_FILE="${WORKSPACE_ROOT}/02_sqlite/day9_group.sql"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

echo "=================================================="
echo "      DAY 9: GROUP BY & AGGREGATIONS PRACTICE     "
echo "=================================================="

echo "[1] Running Aggregations (${SQL_FILE}):"
"${SQLITE_BIN}" "${DB_FILE}" < "${SQL_FILE}"

echo "--------------------------------------------------"
echo "✅ DAY 9 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
