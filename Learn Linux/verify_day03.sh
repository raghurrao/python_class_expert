#!/bin/bash
echo "=== Day 3 Assignment Test ==="
echo "--- Task 1: Skip Header ---"
awk -F',' 'NR > 1 { print NR, $2, $6 }' data/sales_data.csv
echo ""
echo "--- Task 2: NF per line ---"
awk '{ print $1, "Fields:", NF }' data/servers.txt
echo ""
echo "--- Task 3: First 3 Rows ---"
awk -F':' 'NR <= 3 { print NR, $1 }' data/sample_passwd.txt
echo "============================="
