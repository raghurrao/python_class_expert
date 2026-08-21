#!/bin/bash
echo "=== Day 5 Assignment Test ==="
echo "--- Task 1: Formatted Servers ---"
awk 'NR > 1 { printf "%-18s %-12s %6.1f%%\n", $2, $4, $5 }' data/servers.txt
echo ""
echo "--- Task 2: Formatted Employees ---"
awk 'NR > 1 { printf "%-20s %-15s $%7d\n", $2" "$3, $4, $5 }' data/employees.txt
echo "============================="
