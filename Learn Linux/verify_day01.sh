#!/bin/bash

echo "========================================="
echo "   Day 1 AWK Assignment Solutions & Test "
echo "========================================="
echo ""

echo "--- Task 1 Solution: High CPU Servers ($5 > 70) ---"
echo "Command: awk '\$5 > 70 { print \$1, \$2 }' data/servers.txt"
echo "Output:"
awk '$5 > 70 { print $1, $2 }' data/servers.txt
echo ""

echo "--- Task 2 Solution: Non-Active Servers ($4 != \"Active\") ---"
echo "Command: awk '\$4 != \"Active\" { print \$2, \$3 }' data/servers.txt"
echo "Output:"
awk '$4 != "Active" { print $2, $3 }' data/servers.txt
echo ""

echo "--- Task 3 Solution: Disk Usage (df -h | awk '{ print \$1, \$5 }') ---"
echo "Command: df -h | awk '{ print \$1, \$5 }' | head -n 6"
echo "Output:"
df -h | awk '{ print $1, $5 }' | head -n 6
echo ""

echo "--- Task 4 Solution: Hostname ($2) and Last Column ($NF) ---"
echo "Command: awk '{ print \$2, \$NF }' data/servers.txt"
echo "Output:"
awk '{ print $2, $NF }' data/servers.txt
echo ""
echo "========================================="
echo "Awesome job! If your outputs match, you passed Day 1!"
echo "========================================="
