#!/usr/bin/env bash
set -e

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DB_FILE="${WORKSPACE_ROOT}/03_postgres/postgres_sim.db"
SQL_FILE="${WORKSPACE_ROOT}/03_postgres/day12_arch.sql"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

echo "=================================================="
echo "    DAY 12: POSTGRES ARCHITECTURE & SCHEMAS       "
echo "=================================================="

echo "[1] Creating Database Objects (${SQL_FILE}):"
"${SQLITE_BIN}" "${DB_FILE}" < "${SQL_FILE}"

echo ""
echo "[2] Staging Raw Events Table:"
"${SQLITE_BIN}" "${DB_FILE}" "SELECT * FROM staging_raw_events;"

echo ""
echo "[3] Data Warehouse Fact Sales Table:"
"${SQLITE_BIN}" "${DB_FILE}" "SELECT * FROM dw_fact_sales;"

echo "--------------------------------------------------"
echo "✅ DAY 12 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
