#!/usr/bin/env bash
set -euo pipefail

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DB_FILE="${WORKSPACE_ROOT}/02_sqlite/company.db"
EXPORT_DIR="${WORKSPACE_ROOT}/04_bash_sql/exports"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

mkdir -p "${EXPORT_DIR}"

REPORT_FILE="${EXPORT_DIR}/department_summary_$(date '+%Y%m%d').csv"

echo "=================================================="
echo "    DAY 19: AUTOMATED BATCH EXPORT SCRIPT         "
echo "=================================================="

echo "[1] Executing Batch Export to ${REPORT_FILE}..."

"${SQLITE_BIN}" "${DB_FILE}" "SELECT d.dept_name, COUNT(e.emp_id) AS total_staff, COALESCE(SUM(e.salary), 0) AS total_payroll FROM departments d LEFT JOIN employees e ON d.dept_id = e.dept_id GROUP BY d.dept_name;" > "${REPORT_FILE}"

echo "[2] Generated CSV Export Output:"
cat "${REPORT_FILE}"

echo "--------------------------------------------------"
echo "✅ DAY 19 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
