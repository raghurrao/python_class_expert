#!/bin/bash
echo "=== Day 2 Assignment Test ==="
echo ""
echo "--- Task 1: Bash Users ---"
awk -F':' '$7 == "/bin/bash" { print $1, $6 }' data/sample_passwd.txt
echo ""
echo "--- Task 2: CSV Electronics Sales ---"
awk -F',' '$3 == "Electronics" { print $1, $2, $6 }' data/sales_data.csv
echo ""
echo "--- Task 3: Custom Formatted Users ---"
awk -F':' 'BEGIN { OFS=" | " } { print "User: "$1, "UID: "$3 }' data/sample_passwd.txt | head -n 5
echo ""
echo "--- Task 4: UID < 10 ---"
awk -F':' '$3 < 10 { print $1, $3 }' data/sample_passwd.txt
awk -F':' 'BEGIN{ OFS=" | " } $4 < 10 { print "User:" $1, "UID:" $4 }' sample_passwd.txt 
echo "============================="
