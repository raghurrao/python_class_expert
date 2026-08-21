#!/bin/bash
echo "=== Day 6 Assignment Test ==="
echo "--- Task 1: User Account Report ---"
awk -F':' '
BEGIN { print "=== SYSTEM USERS ===" }
$3 >= 1000 { print $1, $3 }
END { print "=== END OF LIST ===" }
' data/sample_passwd.txt
echo ""
echo "--- Task 2: Count Active Web Servers ---"
awk '
BEGIN { c=0 }
$2 ~ /^web/ && $4 == "Active" { c++ }
END { print "Active Web Servers:", c }
' data/servers.txt
echo "============================="
