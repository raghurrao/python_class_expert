#!/usr/bin/env bash
set -e

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DB_FILE="${WORKSPACE_ROOT}/02_sqlite/company.db"
SQL_FILE="${WORKSPACE_ROOT}/02_sqlite/day8_dql.sql"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

echo "=================================================="
echo "    DAY 8: DQL QUERYING & FILTERING PRACTICE      "
echo "=================================================="

echo "[1] Executing Query Suite (${SQL_FILE}):"
"${SQLITE_BIN}" "${DB_FILE}" < "${SQL_FILE}"

echo "--------------------------------------------------"
echo "✅ DAY 8 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
