#!/bin/bash
echo "=== Day 4 Assignment Test ==="
echo "--- Task 1: Web or DB Servers ---"
awk '$2 ~ /web|db/ { print $1, $2 }' data/servers.txt
echo ""
echo "--- Task 2: Active High RAM ---"
awk '$4 == "Active" && $6 > 8 { print $2, "RAM:", $6 }' data/servers.txt
echo ""
echo "--- Task 3: HTTP Errors (>= 400) ---"
awk '$9 >= 400 { print $1, "Status:", $9 }' data/web_access.log
echo "============================="
