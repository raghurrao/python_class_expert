#!/bin/bash
echo "=== Day 8 Assignment Test ==="
echo "--- Task 1: Total Revenue ---"
awk -F',' 'NR > 1 { total += $6 } END { printf "Total Sales Revenue: $%.2f\n", total }' data/sales_data.csv
echo ""
echo "--- Task 2: Avg RAM Active Servers ---"
awk '$4 == "Active" { sum += $6; count++ } END { printf "Avg RAM: %.2f GB across %d active servers\n", sum/count, count }' data/servers.txt
echo "============================="
