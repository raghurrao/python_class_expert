#!/usr/bin/env bash
# Day 4: awk and sed Scripting Practice

set -e

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DATA_DIR="${WORKSPACE_ROOT}/01_linux_basics/sample_data"
mkdir -p "${DATA_DIR}"

RAW_CSV="${DATA_DIR}/dirty_orders.csv"
CLEAN_CSV="${DATA_DIR}/clean_orders.csv"

echo "=================================================="
echo "    DAY 4: ADVANCED AWK & SED STREAM PROCESSING   "
echo "=================================================="

# Create dirty CSV dataset (contains double quotes, N/A strings, spaces)
cat <<EOF > "${RAW_CSV}"
"order_id","customer","region","amount"
"2001","Alice Smith","North","500.00"
"2002","Bob Jones","N/A","150.25"
"2003","Charlie Brown","South","N/A"
"2004","Diana Prince","West","750.80"
EOF

echo "[1] Raw Dirty CSV Data:"
cat "${RAW_CSV}"

echo ""
echo "[2] Cleaning CSV using sed (strip quotes, replace 'N/A' with 'NULL'):"
sed -e 's/"//g' -e 's/N\/A/NULL/g' "${RAW_CSV}" > "${CLEAN_CSV}"
cat "${CLEAN_CSV}"

echo ""
echo "[3] Performing Aggregations with awk (Sum & Avg of valid amount column):"
awk -F',' '
BEGIN { sum = 0; count = 0; }
NR > 1 && $4 != "NULL" {
    sum += $4;
    count++;
    print "    Item: " $2 " -> $" $4;
}
END {
    if (count > 0)
        printf "    -----------------------------------\n    Total Sales: $%.2f | Average Order: $%.2f\n", sum, (sum/count);
}
' "${CLEAN_CSV}"

echo "--------------------------------------------------"
echo "✅ DAY 4 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
