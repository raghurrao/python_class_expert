#!/usr/bin/env bash
set -e

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DB_FILE="${WORKSPACE_ROOT}/02_sqlite/company.db"
SQL_FILE="${WORKSPACE_ROOT}/02_sqlite/day7_dml.sql"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

echo "=================================================="
echo "    DAY 7: DML OPERATIONS & UPSERT PRACTICE       "
echo "=================================================="

# Ensure Day 6 schema is applied
"${SQLITE_BIN}" "${DB_FILE}" < "${WORKSPACE_ROOT}/02_sqlite/day6_ddl.sql"

echo "[1] Applying DML operations..."
"${SQLITE_BIN}" "${DB_FILE}" < "${SQL_FILE}"

echo ""
echo "[2] Departments Table Contents:"
"${SQLITE_BIN}" "${DB_FILE}" "SELECT * FROM departments;"

echo ""
echo "[3] Employees Table Contents:"
"${SQLITE_BIN}" "${DB_FILE}" "SELECT emp_id, first_name, last_name, salary, dept_id FROM employees;"

echo "--------------------------------------------------"
echo "✅ DAY 7 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
