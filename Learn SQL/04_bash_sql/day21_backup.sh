#!/usr/bin/env bash
set -euo pipefail

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DB_FILE="${WORKSPACE_ROOT}/02_sqlite/company.db"
BACKUP_DIR="${WORKSPACE_ROOT}/04_bash_sql/backups"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

mkdir -p "${BACKUP_DIR}"

TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
BACKUP_SQL="${BACKUP_DIR}/company_backup_${TIMESTAMP}.sql"
BACKUP_GZ="${BACKUP_SQL}.gz"

echo "=================================================="
echo "    DAY 21: AUTOMATED DATABASE BACKUP & ROTATION  "
echo "=================================================="

echo "[1] Creating Logical SQL Dump: ${BACKUP_SQL}"
"${SQLITE_BIN}" "${DB_FILE}" ".dump" > "${BACKUP_SQL}"

echo "[2] Compressing Dump File with gzip..."
gzip -f "${BACKUP_SQL}"

echo "[3] Backup Generated: ${BACKUP_GZ}"
ls -lh "${BACKUP_GZ}"

echo "[4] Testing Restore in Temp Database..."
RESTORE_DB="${BACKUP_DIR}/restore_test.db"
rm -f "${RESTORE_DB}"
gunzip -c "${BACKUP_GZ}" | "${SQLITE_BIN}" "${RESTORE_DB}"

ROW_COUNT=$("${SQLITE_BIN}" "${RESTORE_DB}" "SELECT COUNT(*) FROM employees;")
echo "    Restored database successfully! Employee record count: ${ROW_COUNT}"
rm -f "${RESTORE_DB}"

echo "--------------------------------------------------"
echo "✅ DAY 21 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
