#!/bin/bash
echo "=== Day 13 Assignment Test ==="
awk -F',' 'NR > 1 { printf "Category: %-12s | Exact: $%7.2f | Int: $%d\n", $3, $6, int($6) }' data/sales_data.csv
echo "============================="
