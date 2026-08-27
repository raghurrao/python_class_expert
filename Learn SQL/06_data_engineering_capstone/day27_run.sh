#!/usr/bin/env bash
set -e

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DB_FILE="${WORKSPACE_ROOT}/06_data_engineering_capstone/warehouse.db"
SQL_FILE="${WORKSPACE_ROOT}/06_data_engineering_capstone/star_schema.sql"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

echo "=================================================="
echo "    DAY 27: DATA WAREHOUSE STAR SCHEMA CREATION   "
echo "=================================================="

echo "[1] Applying Star Schema to Data Warehouse (${DB_FILE})..."
"${SQLITE_BIN}" "${DB_FILE}" < "${SQL_FILE}"

echo ""
echo "[2] Warehouse Tables:"
"${SQLITE_BIN}" "${DB_FILE}" ".tables"

echo "--------------------------------------------------"
echo "✅ DAY 27 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
