#!/usr/bin/env bash
set -e

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DB_FILE="${WORKSPACE_ROOT}/03_postgres/postgres_sim.db"
SQL_FILE="${WORKSPACE_ROOT}/03_postgres/day13_json.sql"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

echo "=================================================="
echo "    DAY 13: ADVANCED JSON & TIMESTAMP QUERYING    "
echo "=================================================="

echo "[1] Executing JSON Parsing Query (${SQL_FILE}):"
"${SQLITE_BIN}" "${DB_FILE}" < "${SQL_FILE}"

echo "--------------------------------------------------"
echo "✅ DAY 13 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
