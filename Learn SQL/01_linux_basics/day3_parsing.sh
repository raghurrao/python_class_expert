#!/usr/bin/env bash
# Day 3: Text Data Parsing Script

set -e

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DATA_DIR="${WORKSPACE_ROOT}/01_linux_basics/sample_data"
mkdir -p "${DATA_DIR}"

CSV_FILE="${DATA_DIR}/orders.csv"

echo "=================================================="
echo "      DAY 3: CLI DATA PARSING & PROFILING         "
echo "=================================================="

# Create order dataset
cat <<EOF > "${CSV_FILE}"
order_id,customer,region,amount
1001,Alice,North,250.50
1002,Bob,South,120.00
1003,Charlie,North,450.00
1004,Diana,East,80.00
1005,Evan,West,310.20
1006,Fiona,North,250.50
1007,George,South,95.00
1008,Hannah,East,520.00
EOF

echo "[1] Raw Orders Dataset (${CSV_FILE}):"
cat "${CSV_FILE}"

echo ""
echo "[2] Total Record Count (excluding header):"
TOTAL_RECORDS=$(tail -n +2 "${CSV_FILE}" | wc -l)
echo "    Total Orders: ${TOTAL_RECORDS}"

echo ""
echo "[3] Extracting Customer & Amount columns (cut -d',' -f2,4):"
tail -n +2 "${CSV_FILE}" | cut -d',' -f2,4

echo ""
echo "[4] Regional Order Frequencies (sort | uniq -c | sort -nr):"
tail -n +2 "${CSV_FILE}" | cut -d',' -f3 | sort | uniq -c | sort -nr

echo "--------------------------------------------------"
echo "✅ DAY 3 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
