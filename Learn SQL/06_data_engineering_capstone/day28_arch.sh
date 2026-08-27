#!/usr/bin/env bash
set -euo pipefail

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
RAW_DIR="${WORKSPACE_ROOT}/06_data_engineering_capstone/raw_data"
DB_FILE="${WORKSPACE_ROOT}/06_data_engineering_capstone/warehouse.db"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

mkdir -p "${RAW_DIR}"

RAW_ORDERS="${RAW_DIR}/raw_orders_2026.csv"
RAW_CUSTOMERS="${RAW_DIR}/raw_customers.json"
RAW_PRODUCTS="${RAW_DIR}/raw_products.csv"

echo "=================================================="
echo "    DAY 28: RAW LANDING ZONE DATASET GENERATION   "
echo "=================================================="

# 1. Raw Customers JSON
cat <<EOF > "${RAW_CUSTOMERS}"
[
  {"id": 1, "name": "Alice Corp", "region": "North"},
  {"id": 2, "name": "Bob Enterprise", "region": "South"},
  {"id": 3, "name": "Charlie Inc", "region": "East"}
]
EOF

# 2. Raw Products CSV
cat <<EOF > "${RAW_PRODUCTS}"
id,product_name,category,unit_price
101,Cloud Server Pro,Infrastructure,199.99
102,SQL Database Enterprise,Database,499.00
103,Data Analytics Suite,Analytics,299.50
EOF

# 3. Raw Transactions CSV
cat <<EOF > "${RAW_ORDERS}"
order_id,customer_id,product_id,date,qty
9001,1,101,2026-08-25,2
9002,2,102,2026-08-26,1
9003,1,103,2026-08-26,5
9004,3,101,2026-08-27,3
EOF

echo "[1] Raw Landing Zone Files Generated in ${RAW_DIR}:"
ls -la "${RAW_DIR}"

echo "--------------------------------------------------"
echo "✅ DAY 28 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
