#!/usr/bin/env bash
set -e

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DB_FILE="${WORKSPACE_ROOT}/02_sqlite/company.db"
SQL_FILE="${WORKSPACE_ROOT}/03_postgres/day18_indexes.sql"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

echo "=================================================="
echo "    DAY 18: QUERY OPTIMIZATION & INDEXING PRACTICE "
echo "=================================================="

echo "[1] Analyzing Query Plan Before vs After Indexing (${SQL_FILE}):"
"${SQLITE_BIN}" "${DB_FILE}" < "${SQL_FILE}"

echo "--------------------------------------------------"
echo "✅ DAY 18 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
