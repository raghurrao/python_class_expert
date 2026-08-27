#!/usr/bin/env bash
set -e

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
CAPSTONE_DIR="${WORKSPACE_ROOT}/06_data_engineering_capstone"
DB_FILE="${CAPSTONE_DIR}/warehouse.db"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

echo "=================================================================="
echo "   DAY 30: 30-DAY SQL & DATA ENGINEERING CAPSTONE EXECUTION       "
echo "=================================================================="

echo "[1] Triggering Raw Landing Zone Generation (Day 28)..."
"${CAPSTONE_DIR}/day28_arch.sh" > /dev/null

echo "[2] Triggering End-to-End Python ETL Pipeline (Day 29)..."
python3 "${CAPSTONE_DIR}/etl_pipeline.py"

echo ""
echo "[3] Running Data Warehouse Analytics & BI Reports (Day 30)..."
"${SQLITE_BIN}" "${DB_FILE}" < "${CAPSTONE_DIR}/day30_analytics.sql"

echo "=================================================================="
echo "🎉 CONGRATULATIONS! 30-DAY SQL & DATA ENGINEERING MASTERCLASS DONE!"
echo "=================================================================="
