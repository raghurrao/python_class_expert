#!/usr/bin/env bash
# Day 2: Hands-on I/O Redirection and Piping Script

set -e

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DATA_DIR="${WORKSPACE_ROOT}/01_linux_basics/sample_data"
mkdir -p "${DATA_DIR}"

CSV_FILE="${DATA_DIR}/raw_users.csv"
LOG_FILE="${DATA_DIR}/process.log"

echo "=================================================="
echo "    DAY 2: I/O REDIRECTION & PIPES PRACTICE       "
echo "=================================================="

# 1. Overwrite (>) header line
echo "id,name,role,salary" > "${CSV_FILE}"

# 2. Append (>>) data rows
echo "101,Alice,Data Engineer,95000" >> "${CSV_FILE}"
echo "102,Bob,Database Admin,88000" >> "${CSV_FILE}"
echo "103,Charlie,Data Analyst,72000" >> "${CSV_FILE}"
echo "104,Diana,Software Engineer,105000" >> "${CSV_FILE}"
echo "105,Evan,Data Architect,120000" >> "${CSV_FILE}"

echo "[1] Created dataset '${CSV_FILE}':"
cat "${CSV_FILE}"

# 3. Piping (|) & filtering: Extract data engineers and architects
echo ""
echo "[2] Filtered 'Data' roles using Pipe (cat | grep):"
cat "${CSV_FILE}" | grep "Data" > "${DATA_DIR}/data_team.csv"
cat "${DATA_DIR}/data_team.csv"

# 4. Redirection of stderr (2>)
echo ""
echo "[3] Testing error redirection (2>):"
ls "${DATA_DIR}/non_existent_file.csv" 2> "${LOG_FILE}" || true
echo "    Error captured in log file:"
cat "${LOG_FILE}"

echo "--------------------------------------------------"
echo "✅ DAY 2 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
