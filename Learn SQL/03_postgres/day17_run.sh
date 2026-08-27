#!/usr/bin/env bash
set -e

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DB_FILE="${WORKSPACE_ROOT}/03_postgres/postgres_sim.db"
SQL_FILE="${WORKSPACE_ROOT}/03_postgres/day17_tx.sql"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

echo "=================================================="
echo "    DAY 17: TRANSACTIONS & ACID ROLLBACK          "
echo "=================================================="

echo "[1] Executing Transactions (${SQL_FILE}):"
"${SQLITE_BIN}" "${DB_FILE}" < "${SQL_FILE}"

echo ""
echo "[2] Bank Accounts State After Transactions:"
"${SQLITE_BIN}" "${DB_FILE}" "SELECT * FROM bank_accounts;"

echo "--------------------------------------------------"
echo "✅ DAY 17 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
