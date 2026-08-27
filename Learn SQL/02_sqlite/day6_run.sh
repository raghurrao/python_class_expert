#!/usr/bin/env bash
set -e

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DB_FILE="${WORKSPACE_ROOT}/02_sqlite/company.db"
SQL_FILE="${WORKSPACE_ROOT}/02_sqlite/day6_ddl.sql"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

echo "=================================================="
echo "      DAY 6: SQLITE DDL & SCHEMA CREATION         "
echo "=================================================="

echo "[1] Applying schema from ${SQL_FILE} to ${DB_FILE}..."
"${SQLITE_BIN}" "${DB_FILE}" < "${SQL_FILE}"

echo ""
echo "[2] Database Tables Created:"
"${SQLITE_BIN}" "${DB_FILE}" ".tables"

echo ""
echo "[3] Employee Table Schema:"
"${SQLITE_BIN}" "${DB_FILE}" ".schema employees"

echo "--------------------------------------------------"
echo "✅ DAY 6 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
